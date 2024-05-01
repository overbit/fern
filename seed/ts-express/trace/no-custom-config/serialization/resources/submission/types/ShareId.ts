/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as SeedTrace from "../../../../api/index";
import * as core from "../../../../core";

export const ShareId: core.serialization.Schema<serializers.ShareId.Raw, SeedTrace.ShareId> =
    core.serialization.string();

export declare namespace ShareId {
    type Raw = string;
}