import { RawSchemas } from "@fern-api/yaml-schema";
import { Type } from "@fern-fern/ir-model/types";
import { FernFileContext } from "../../FernFileContext";
import { convertDeclaration } from "../convertDeclaration";

export function convertEnumTypeDeclaration({
    _enum,
    file,
}: {
    _enum: RawSchemas.EnumSchema;
    file: FernFileContext;
}): Type {
    return Type.enum({
        values: _enum.enum.map((value) => ({
            ...convertDeclaration(value),
            name: file.casingsGenerator.generateWireCasingsV1({
                wireValue: typeof value === "string" ? value : value.value,
                name: getEnumName(value).name,
            }),
            nameV2: file.casingsGenerator.generateNameAndWireValue({
                wireValue: typeof value === "string" ? value : value.value,
                name: getEnumName(value).name,
            }),
            value: typeof value === "string" ? value : value.value,
        })),
    });
}

export function getEnumName(enumValue: RawSchemas.EnumValueSchema): { name: string; wasExplicitlySet: boolean } {
    if (typeof enumValue === "string") {
        return {
            name: enumValue,
            wasExplicitlySet: false,
        };
    }

    if (enumValue.name == null) {
        return {
            name: enumValue.value,
            wasExplicitlySet: false,
        };
    }

    return {
        name: enumValue.name,
        wasExplicitlySet: true,
    };
}