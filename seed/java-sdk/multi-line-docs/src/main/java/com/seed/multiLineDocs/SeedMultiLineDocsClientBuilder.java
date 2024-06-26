/**
 * This file was auto-generated by Fern from our API Definition.
 */
package com.seed.multiLineDocs;

import com.seed.multiLineDocs.core.ClientOptions;
import com.seed.multiLineDocs.core.Environment;

public final class SeedMultiLineDocsClientBuilder {
    private ClientOptions.Builder clientOptionsBuilder = ClientOptions.builder();

    private Environment environment;

    public SeedMultiLineDocsClientBuilder url(String url) {
        this.environment = Environment.custom(url);
        return this;
    }

    public SeedMultiLineDocsClient build() {
        clientOptionsBuilder.environment(this.environment);
        return new SeedMultiLineDocsClient(clientOptionsBuilder.build());
    }
}
