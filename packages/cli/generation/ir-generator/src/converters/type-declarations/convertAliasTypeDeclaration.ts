import { assertNever } from "@fern-api/core-utils";
import { isRawEnumDefinition, isRawObjectDefinition, isRawUnionDefinition, RawSchemas } from "@fern-api/yaml-schema";
import { ResolvedTypeReference, ShapeType, Type } from "@fern-fern/ir-model/types";
import { FernFileContext } from "../../FernFileContext";
import { TypeResolver } from "../../resolvers/TypeResolver";

export function convertAliasTypeDeclaration({
    alias,
    file,
    typeResolver,
}: {
    alias: string | RawSchemas.AliasSchema;
    file: FernFileContext;
    typeResolver: TypeResolver;
}): Type {
    const aliasOfStr = typeof alias === "string" ? alias : alias.alias;
    return Type.alias({
        aliasOf: file.parseTypeReference(aliasOfStr),
        resolvedType: constructResolvedTypeReference({ aliasOf: aliasOfStr, file, typeResolver }),
    });
}

function constructResolvedTypeReference({
    aliasOf,
    file,
    typeResolver,
}: {
    aliasOf: string;
    file: FernFileContext;
    typeResolver: TypeResolver;
}): ResolvedTypeReference {
    const resolvedType = typeResolver.resolveTypeOrThrow({ type: aliasOf, file });
    switch (resolvedType._type) {
        case "primitive":
        case "container":
        case "void":
        case "unknown":
            return resolvedType.originalTypeReference;
        case "named": {
            const shapeType = isRawObjectDefinition(resolvedType.declaration)
                ? ShapeType.Object
                : isRawUnionDefinition(resolvedType.declaration)
                ? ShapeType.Union
                : isRawEnumDefinition(resolvedType.declaration)
                ? ShapeType.Enum
                : assertNever(resolvedType.declaration);
            return ResolvedTypeReference.named({
                name: resolvedType.name,
                shape: shapeType,
            });
        }
    }
}