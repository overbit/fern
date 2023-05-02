import { RawSchemas } from "@fern-api/yaml-schema";
import { Endpoint, Request, Schema, SchemaId } from "@fern-fern/openapi-ir-model/ir";
import { ROOT_PREFIX } from "../convertPackage";
import { Environment } from "../getEnvironment";
import { convertPathParameter } from "./convertPathParameter";
import { convertQueryParameter } from "./convertQueryParameter";
import { convertToHttpMethod } from "./convertToHttpMethod";
import { convertToTypeReference } from "./convertToTypeReference";
import { getTypeFromTypeReference } from "./utils/getTypeFromTypeReference";

export interface ConvertedEndpoint {
    value: RawSchemas.HttpEndpointSchema;
    schemaIdsToExclude: string[];
    additionalTypeDeclarations: Record<string, RawSchemas.TypeDeclarationSchema>;
}

export function convertEndpoint({
    endpoint,
    isPackageYml,
    schemas,
    environment,
    nonRequestReferencedSchemas,
}: {
    endpoint: Endpoint;
    isPackageYml: boolean;
    schemas: Record<SchemaId, Schema>;
    environment: Environment | undefined;
    nonRequestReferencedSchemas: SchemaId[];
}): ConvertedEndpoint {
    let additionalTypeDeclarations: Record<string, RawSchemas.TypeDeclarationSchema> = {};
    let schemaIdsToExclude: string[] = [];

    const pathParameters: Record<string, RawSchemas.HttpPathParameterSchema> = {};
    for (const pathParameter of endpoint.pathParameters) {
        const convertedPathParameter = convertPathParameter({ pathParameter, schemas, isPackageYml });
        pathParameters[pathParameter.name] = convertedPathParameter.value;
        additionalTypeDeclarations = {
            ...additionalTypeDeclarations,
            ...convertedPathParameter.additionalTypeDeclarations,
        };
    }

    const queryParameters: Record<string, RawSchemas.HttpQueryParameterSchema> = {};
    for (const queryParameter of endpoint.queryParameters) {
        const convertedQueryParameter = convertQueryParameter({ queryParameter, isPackageYml, schemas });
        queryParameters[queryParameter.name] = convertedQueryParameter.value;
        additionalTypeDeclarations = {
            ...additionalTypeDeclarations,
            ...convertedQueryParameter.additionalTypeDeclarations,
        };
    }

    const convertedEndpoint: RawSchemas.HttpEndpointSchema = {
        path: endpoint.path,
        method: convertToHttpMethod(endpoint.method),
    };

    if (Object.keys(pathParameters).length > 0) {
        convertedEndpoint["path-parameters"] = pathParameters;
    }

    if (endpoint.request != null) {
        const convertedRequest = getRequest({
            isPackageYml,
            request: endpoint.request,
            schemas,
            generatedRequestName: endpoint.generatedRequestName,
            requestNameOverride: endpoint.requestNameOverride ?? undefined,
            queryParameters: Object.keys(queryParameters).length > 0 ? queryParameters : undefined,
            nonRequestReferencedSchemas,
        });
        convertedEndpoint.request = convertedRequest.value;
        schemaIdsToExclude = [...schemaIdsToExclude, ...(convertedRequest.schemaIdsToExclude ?? [])];
        additionalTypeDeclarations = {
            ...additionalTypeDeclarations,
            ...convertedRequest.additionalTypeDeclarations,
        };
    } else if (Object.keys(queryParameters).length > 0) {
        convertedEndpoint.request = {
            name: endpoint.requestNameOverride ?? endpoint.generatedRequestName,
            "query-parameters": queryParameters,
        };
    }

    if (endpoint.response != null) {
        const responseTypeReference = convertToTypeReference({
            schema: endpoint.response.schema,
            prefix: isPackageYml ? undefined : ROOT_PREFIX,
            schemas,
        });
        additionalTypeDeclarations = {
            ...additionalTypeDeclarations,
            ...responseTypeReference.additionalTypeDeclarations,
        };
        if (endpoint.responseIsStreaming) {
            convertedEndpoint["response-stream"] = {
                type: getTypeFromTypeReference(responseTypeReference.typeReference),
            };
        } else {
            convertedEndpoint.response = {
                docs: endpoint.response.description ?? undefined,
                type: getTypeFromTypeReference(responseTypeReference.typeReference),
            };
        }
    }

    if (environment?.type === "multi") {
        const serverOverride = endpoint.server[0];
        if (endpoint.server.length === 0) {
            convertedEndpoint.url = environment.defaultUrl;
        } else if (serverOverride != null) {
            convertedEndpoint.url = serverOverride.name ?? undefined;
        } else {
            throw new Error(
                `${endpoint.method} ${endpoint.path} can only have a single server override, but has more.`
            );
        }
    }
    return {
        value: convertedEndpoint,
        schemaIdsToExclude,
        additionalTypeDeclarations,
    };
}

interface ConvertedRequest {
    value: RawSchemas.HttpRequestSchema;
    schemaIdsToExclude?: string[];
    additionalTypeDeclarations: Record<string, RawSchemas.TypeDeclarationSchema>;
}

function getRequest({
    isPackageYml,
    request,
    schemas,
    requestNameOverride,
    generatedRequestName,
    queryParameters,
    nonRequestReferencedSchemas,
}: {
    isPackageYml: boolean;
    request: Request;
    schemas: Record<SchemaId, Schema>;
    requestNameOverride?: string;
    generatedRequestName: string;
    queryParameters?: Record<string, RawSchemas.HttpQueryParameterSchema>;
    nonRequestReferencedSchemas: SchemaId[];
}): ConvertedRequest {
    let additionalTypeDeclarations: Record<string, RawSchemas.TypeDeclarationSchema> = {};
    if (request.type === "json") {
        const maybeSchemaId = request.schema.type === "reference" ? request.schema.schema : undefined;
        const resolvedSchema = request.schema.type === "reference" ? schemas[request.schema.schema] : request.schema;
        if (resolvedSchema == null) {
            throw Error(`Failed to resolve schema ${JSON.stringify(request.schema)}`);
        }

        // the request body is referenced if it is not an object or if other parts of the spec
        // refer to the same type
        if (
            resolvedSchema.type !== "object" ||
            (maybeSchemaId != null && nonRequestReferencedSchemas.includes(maybeSchemaId))
        ) {
            const requestTypeReference = convertToTypeReference({
                schema: resolvedSchema,
                prefix: isPackageYml ? undefined : ROOT_PREFIX,
                schemas,
            });
            const convertedRequest: ConvertedRequest = {
                schemaIdsToExclude: [],
                value: {
                    body:
                        typeof requestTypeReference === "string"
                            ? requestTypeReference
                            : requestTypeReference.typeReference,
                },
                additionalTypeDeclarations: {
                    ...additionalTypeDeclarations,
                    ...requestTypeReference.additionalTypeDeclarations,
                },
            };

            if (Object.keys(queryParameters ?? {}).length > 0) {
                convertedRequest.value.name = requestNameOverride ?? generatedRequestName;
                convertedRequest.value["query-parameters"] = queryParameters;
            }

            return convertedRequest;
        }
        const properties = Object.fromEntries(
            resolvedSchema.properties.map((property) => {
                const propertyTypeReference = convertToTypeReference({
                    schema: property.schema,
                    prefix: isPackageYml ? undefined : ROOT_PREFIX,
                    schemas,
                });
                additionalTypeDeclarations = {
                    ...additionalTypeDeclarations,
                    ...propertyTypeReference.additionalTypeDeclarations,
                };
                return [property.key, propertyTypeReference.typeReference];
            })
        );
        return {
            schemaIdsToExclude: maybeSchemaId != null ? [maybeSchemaId] : [],
            value: {
                name: requestNameOverride ?? resolvedSchema.nameOverride ?? resolvedSchema.generatedName,
                "query-parameters": queryParameters,
                body: {
                    properties,
                },
            },
            additionalTypeDeclarations,
        };
    } else {
        // multipart
        const properties = Object.fromEntries(
            request.properties.map((property) => {
                if (property.schema.type === "file") {
                    return [property.key, "file"];
                } else {
                    const propertyTypeReference = convertToTypeReference({
                        schema: property.schema.json,
                        prefix: isPackageYml ? undefined : ROOT_PREFIX,
                        schemas,
                    });
                    additionalTypeDeclarations = {
                        ...additionalTypeDeclarations,
                        ...propertyTypeReference.additionalTypeDeclarations,
                    };
                    return [property.key, propertyTypeReference.typeReference];
                }
            })
        );
        return {
            schemaIdsToExclude: request.name == null ? [] : [request.name],
            value: {
                name: requestNameOverride ?? request.name ?? generatedRequestName,
                "query-parameters": queryParameters,
                body: {
                    properties,
                },
            },
            additionalTypeDeclarations,
        };
    }
}