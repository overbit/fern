import { AbsoluteFilePath } from "@fern-api/fs-utils";
import { TaskContext } from "@fern-api/task-context";
import { readFile, writeFile } from "fs/promises";
import YAML from "yaml";
import { Migration } from "../../../types/Migration";
import { getAllRootApiYamlFiles } from "./getAllRootApiYamlFiles";

export const migration: Migration = {
    name: "add-error-discrimination-config",
    summary: "Adds error discrimination configuration",
    run: async ({ context }) => {
        const rootApiFile = await getAllRootApiYamlFiles(context);
        for (const filepath of rootApiFile) {
            try {
                await migrateRootApiFile(filepath, context);
            } catch (error) {
                context.failWithoutThrowing(`Failed to migrate ${filepath}`, error);
            }
        }
    },
};

async function migrateRootApiFile(filepath: AbsoluteFilePath, _context: TaskContext): Promise<void> {
    const contents = await readFile(filepath);
    const parsedDocument = YAML.parseDocument(contents.toString());
    const errorDiscriminant = parsedDocument.get("error-discriminant", true);
    if (errorDiscriminant == null || !YAML.isScalar(errorDiscriminant) || typeof errorDiscriminant.value !== "string") {
        return;
    }
    parsedDocument.set("error-discrimination", {
        strategy: "property",
        "property-name": errorDiscriminant.value,
    });
    parsedDocument.delete("error-discriminant");
    await writeFile(filepath, parsedDocument.toString());
}
