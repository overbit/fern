// This file was auto-generated by Fern from our API Definition.

package dummy

import (
	context "context"
	v2 "github.com/fern-api/stream-go/v2"
	core "github.com/fern-api/stream-go/v2/core"
	option "github.com/fern-api/stream-go/v2/option"
	http "net/http"
)

type Client struct {
	baseURL string
	caller  *core.Caller
	header  http.Header
}

func NewClient(opts ...option.RequestOption) *Client {
	options := core.NewRequestOptions(opts...)
	return &Client{
		baseURL: options.BaseURL,
		caller:  core.NewCaller(options.HTTPClient),
		header:  options.ToHeader(),
	}
}

func (c *Client) GenerateStream(
	ctx context.Context,
	request *v2.GenerateStreamRequestzs,
	opts ...option.RequestOption,
) (*core.Stream[v2.StreamResponse], error) {
	options := core.NewRequestOptions(opts...)

	baseURL := ""
	if c.baseURL != "" {
		baseURL = c.baseURL
	}
	if options.BaseURL != "" {
		baseURL = options.BaseURL
	}
	endpointURL := baseURL + "/" + "generate-stream"

	headers := core.MergeHeaders(c.header.Clone(), options.ToHeader())

	streamer := core.NewStreamer[v2.StreamResponse](c.caller)
	return streamer.Stream(
		ctx,
		&core.StreamParams{
			URL:     endpointURL,
			Method:  http.MethodPost,
			Headers: headers,
			Client:  options.HTTPClient,
			Request: request,
		},
	)
}
