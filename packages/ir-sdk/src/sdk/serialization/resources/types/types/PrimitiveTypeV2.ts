/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as FernIr from "../../../../api";
import * as core from "../../../../core";

export const PrimitiveTypeV2: core.serialization.Schema<serializers.PrimitiveTypeV2.Raw, FernIr.PrimitiveTypeV2> =
    core.serialization
        .union("type", {
            integer: core.serialization.lazyObject(async () => (await import("../../..")).IntegerType),
            double: core.serialization.lazyObject(async () => (await import("../../..")).DoubleType),
            string: core.serialization.lazyObject(async () => (await import("../../..")).StringType),
        })
        .transform<FernIr.PrimitiveTypeV2>({
            transform: (value) => {
                switch (value.type) {
                    case "integer":
                        return FernIr.PrimitiveTypeV2.integer(value);
                    case "double":
                        return FernIr.PrimitiveTypeV2.double(value);
                    case "string":
                        return FernIr.PrimitiveTypeV2.string(value);
                    default:
                        return value as FernIr.PrimitiveTypeV2;
                }
            },
            untransform: ({ _visit, ...value }) => value as any,
        });

export declare namespace PrimitiveTypeV2 {
    type Raw = PrimitiveTypeV2.Integer | PrimitiveTypeV2.Double | PrimitiveTypeV2.String;

    interface Integer extends serializers.IntegerType.Raw {
        type: "integer";
    }

    interface Double extends serializers.DoubleType.Raw {
        type: "double";
    }

    interface String extends serializers.StringType.Raw {
        type: "string";
    }
}
