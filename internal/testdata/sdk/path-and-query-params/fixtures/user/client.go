// This file was auto-generated by Fern from our API Definition.

package user

import (
	context "context"
	fmt "fmt"
	fixtures "github.com/fern-api/fern-go/internal/testdata/sdk/path-and-query-params/fixtures"
	core "github.com/fern-api/fern-go/internal/testdata/sdk/path-and-query-params/fixtures/core"
	option "github.com/fern-api/fern-go/internal/testdata/sdk/path-and-query-params/fixtures/option"
	http "net/http"
	url "net/url"
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

func (c *Client) GetUser(
	ctx context.Context,
	userId string,
	request *fixtures.GetUserRequest,
	opts ...option.RequestOption,
) (string, error) {
	options := core.NewRequestOptions(opts...)

	baseURL := ""
	if c.baseURL != "" {
		baseURL = c.baseURL
	}
	if options.BaseURL != "" {
		baseURL = options.BaseURL
	}
	endpointURL := fmt.Sprintf(baseURL+"/"+"users/%v", userId)

	queryParams := make(url.Values)
	if request.Shallow != nil {
		queryParams.Add("shallow", fmt.Sprintf("%v", *request.Shallow))
	}
	if len(queryParams) > 0 {
		endpointURL += "?" + queryParams.Encode()
	}

	headers := core.MergeHeaders(c.header.Clone(), options.ToHeader())

	var response string
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
		return "", err
	}
	return response, nil
}
