import { assertNever, assertNeverNoThrow } from "@fern-api/core-utils";
import { App, ResolvedUrlPath } from "@fern-api/ui";
import * as FernRegistryDocsReadV1 from "@fern-fern/registry-browser/api/resources/docs/resources/v1/resources/read";
import * as FernRegistryDocsReadV2 from "@fern-fern/registry-browser/api/resources/docs/resources/v2/resources/read";
import { GetStaticPaths, GetStaticProps } from "next";
import { Inter } from "next/font/google";
import Head from "next/head";
import { REGISTRY_SERVICE } from "../../service";
import { getSlugFromUrl } from "../../url-path-resolver/getSlugFromUrl";
import { UrlPathResolver } from "../../url-path-resolver/UrlPathResolver";

const inter = Inter({ subsets: ["latin"] });

export declare namespace Docs {
    export interface Props {
        docs: FernRegistryDocsReadV2.LoadDocsForUrlResponse;
        resolvedUrlPath: ResolvedUrlPath;
    }
}

export default function Docs({ docs, resolvedUrlPath }: Docs.Props): JSX.Element {
    return (
        <main className={inter.className}>
            <Head>
                {docs.definition.config.title != null && <title>{docs.definition.config.title}</title>}
                {docs.definition.config.favicon != null && (
                    <link rel="icon" id="favicon" href={docs.definition.files[docs.definition.config.favicon]}></link>
                )}
            </Head>
            <App docs={docs} resolvedUrlPath={resolvedUrlPath} />
        </main>
    );
}

export const getStaticProps: GetStaticProps<Docs.Props> = async ({ params = {} }) => {
    const { host, slug: slugArray } = params;

    if (host == null) {
        throw new Error("host is not defined");
    }

    const pathname = slugArray != null ? (slugArray as string[]).join("/") : "";
    const docs = await REGISTRY_SERVICE.docs.v2.read.getDocsForUrl({
        url: process.env.NEXT_PUBLIC_DOCS_DOMAIN ?? `${host}${pathname}`,
    });

    if (!docs.ok) {
        // eslint-disable-next-line no-console
        console.error("Failed to fetch docs", docs.error);
        return { notFound: true };
    }

    let slug = getSlugFromUrl({ pathname, basePath: docs.body.baseUrl.basePath });
    if (slug === "") {
        const firstNavigationItem = docs.body.definition.config.navigation.items[0];
        if (firstNavigationItem != null) {
            slug = firstNavigationItem.urlSlug;
        } else {
            return { notFound: true };
        }
    }

    const urlPathResolver = new UrlPathResolver(docs.body.definition);
    const resolvedUrlPath = await urlPathResolver.resolveSlug(slug);
    if (resolvedUrlPath == null) {
        return { notFound: true };
    }

    switch (resolvedUrlPath.type) {
        case "section": {
            const firstNavigatableItem = getFirstNavigatableItem(resolvedUrlPath.section);
            if (firstNavigatableItem != null) {
                return {
                    redirect: {
                        permanent: false,
                        destination: firstNavigatableItem,
                    },
                };
            } else {
                return {
                    notFound: true,
                };
            }
        }
        case "api":
        case "apiSubpackage":
        case "clientLibraries":
        case "endpoint":
        case "markdown-page":
        case "mdx-page":
        case "topLevelEndpoint":
            return {
                props: {
                    docs: docs.body,
                    resolvedUrlPath,
                },
            };
        default:
            assertNever(resolvedUrlPath);
    }
};

export const getStaticPaths: GetStaticPaths = () => {
    return { paths: [], fallback: "blocking" };
};

function getFirstNavigatableItem(section: FernRegistryDocsReadV1.DocsSection, slugPrefix?: string): string | undefined {
    for (const item of section.items) {
        switch (item.type) {
            case "api":
            case "page": {
                const parts = [];
                if (slugPrefix != null) {
                    parts.push(slugPrefix);
                }
                parts.push(section.urlSlug, item.urlSlug);
                return parts.join("/");
            }
            case "section":
                return getFirstNavigatableItem(item, section.urlSlug);
            default:
                assertNeverNoThrow(item);
        }
    }
    return undefined;
}