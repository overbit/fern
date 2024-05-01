/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as SeedTrace from "../../../../api/index";
import * as core from "../../../../core";

export const WorkspaceSubmitRequest: core.serialization.ObjectSchema<
    serializers.WorkspaceSubmitRequest.Raw,
    SeedTrace.WorkspaceSubmitRequest
> = core.serialization.object({
    submissionId: core.serialization.lazy(async () => (await import("../../..")).SubmissionId),
    language: core.serialization.lazy(async () => (await import("../../..")).Language),
    submissionFiles: core.serialization.list(
        core.serialization.lazyObject(async () => (await import("../../..")).SubmissionFileInfo)
    ),
    userId: core.serialization.string().optional(),
});

export declare namespace WorkspaceSubmitRequest {
    interface Raw {
        submissionId: serializers.SubmissionId.Raw;
        language: serializers.Language.Raw;
        submissionFiles: serializers.SubmissionFileInfo.Raw[];
        userId?: string | null;
    }
}