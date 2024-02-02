# frozen_string_literal: true

require_relative "seed_objects_with_imports_client/commons/metadata/types/metadata"
require_relative "seed_objects_with_imports_client/file/directory/types/directory"
require_relative "seed_objects_with_imports_client/file/types/file"
require_relative "seed_objects_with_imports_client/types/node"
require_relative "seed_objects_with_imports_client/types/tree"
require "async/http/faraday"
require "faraday"

module SeedObjectsWithImportsClient
  class Client
    # @param max_retries [Long] The number of times to retry a failed request, defaults to 2.
    # @param timeout_in_seconds [Long]
    # @return []
    def initialize(max_retries: nil, timeout_in_seconds: nil)
      RequestClient.initialize(headers: headers, base_url: base_url, conn: conn)
    end
  end

  class AsyncClient
    # @param max_retries [Long] The number of times to retry a failed request, defaults to 2.
    # @param timeout_in_seconds [Long]
    # @return []
    def initialize(max_retries: nil, timeout_in_seconds: nil)
      AsyncRequestClient.initialize(headers: headers, base_url: base_url, conn: conn)
    end
  end
end