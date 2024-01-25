// This file was auto-generated by Fern from our API Definition.

package user

import (
	context "context"
	fmt "fmt"
	fixtures "github.com/fern-api/fern-go/internal/testdata/sdk/optional-response/fixtures"
	core "github.com/fern-api/fern-go/internal/testdata/sdk/optional-response/fixtures/core"
	option "github.com/fern-api/fern-go/internal/testdata/sdk/optional-response/fixtures/option"
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

func (c *Client) GetName(
	ctx context.Context,
	userId string,
	opts ...option.RequestOption,
) (*string, error) {
	options := core.NewRequestOptions(opts...)

	baseURL := ""
	if c.baseURL != "" {
		baseURL = c.baseURL
	}
	if options.BaseURL != "" {
		baseURL = options.BaseURL
	}
	endpointURL := fmt.Sprintf(baseURL+"/"+"users/%v/name", userId)

	headers := core.MergeHeaders(c.header.Clone(), options.ToHeader())

	var response *string
	if err := c.caller.Call(
		ctx,
		&core.CallParams{
			URL:                endpointURL,
			Method:             http.MethodGet,
			Headers:            headers,
			Client:             options.HTTPClient,
			Response:           &response,
			ResponseIsOptional: true,
		},
	); err != nil {
		return nil, err
	}
	return response, nil
}

func (c *Client) GetUser(
	ctx context.Context,
	userId string,
	opts ...option.RequestOption,
) (*fixtures.User, error) {
	options := core.NewRequestOptions(opts...)

	baseURL := ""
	if c.baseURL != "" {
		baseURL = c.baseURL
	}
	if options.BaseURL != "" {
		baseURL = options.BaseURL
	}
	endpointURL := fmt.Sprintf(baseURL+"/"+"users/%v", userId)

	headers := core.MergeHeaders(c.header.Clone(), options.ToHeader())

	var response *fixtures.User
	if err := c.caller.Call(
		ctx,
		&core.CallParams{
			URL:                endpointURL,
			Method:             http.MethodGet,
			Headers:            headers,
			Client:             options.HTTPClient,
			Response:           &response,
			ResponseIsOptional: true,
		},
	); err != nil {
		return nil, err
	}
	return response, nil
}
