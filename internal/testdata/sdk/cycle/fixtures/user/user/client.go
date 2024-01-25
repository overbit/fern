// This file was auto-generated by Fern from our API Definition.

package user

import (
	context "context"
	core "github.com/fern-api/fern-go/internal/testdata/sdk/cycle/fixtures/core"
	option "github.com/fern-api/fern-go/internal/testdata/sdk/cycle/fixtures/option"
	user "github.com/fern-api/fern-go/internal/testdata/sdk/cycle/fixtures/user"
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

func (c *Client) List(
	ctx context.Context,
	opts ...option.RequestOption,
) ([]*user.User, error) {
	options := core.NewRequestOptions(opts...)

	baseURL := ""
	if c.baseURL != "" {
		baseURL = c.baseURL
	}
	if options.BaseURL != "" {
		baseURL = options.BaseURL
	}
	endpointURL := baseURL + "/" + "users"

	headers := core.MergeHeaders(c.header.Clone(), options.ToHeader())

	var response []*user.User
	if err := c.caller.Call(
		ctx,
		&core.CallParams{
			URL:      endpointURL,
			Method:   http.MethodGet,
			Headers:  headers,
			Client:   options.HTTPClient,
			Response: &response,
		},
	); err != nil {
		return nil, err
	}
	return response, nil
}
