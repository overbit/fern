// This file was auto-generated by Fern from our API Definition.

package file

import (
	bytes "bytes"
	context "context"
	fmt "fmt"
	core "github.com/fern-api/fern-go/internal/testdata/sdk/download/fixtures/core"
	option "github.com/fern-api/fern-go/internal/testdata/sdk/download/fixtures/option"
	io "io"
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

func (c *Client) Download(
	ctx context.Context,
	filename string,
	opts ...option.RequestOption,
) (io.Reader, error) {
	options := core.NewRequestOptions(opts...)

	baseURL := ""
	if c.baseURL != "" {
		baseURL = c.baseURL
	}
	if options.BaseURL != "" {
		baseURL = options.BaseURL
	}
	endpointURL := fmt.Sprintf(baseURL+"/"+"file/%v/download", filename)

	headers := core.MergeHeaders(c.header.Clone(), options.ToHeader())

	response := bytes.NewBuffer(nil)
	if err := c.caller.Call(
		ctx,
		&core.CallParams{
			URL:      endpointURL,
			Method:   http.MethodGet,
			Headers:  headers,
			Client:   options.HTTPClient,
			Response: response,
		},
	); err != nil {
		return nil, err
	}
	return response, nil
}
