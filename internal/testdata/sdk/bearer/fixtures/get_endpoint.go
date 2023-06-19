// Generated by Fern. Do not edit.

package api

import (
	context "context"
	errors "errors"
	core "github.com/fern-api/fern-go/internal/testdata/sdk/bearer/fixtures/core"
	io "io"
	http "net/http"
)

type getEndpoint struct {
	url        string
	httpClient core.HTTPClient
	header     http.Header
}

func newGetEndpoint(url string, httpClient core.HTTPClient, clientOptions *core.ClientOptions) *getEndpoint {
	return &getEndpoint{
		url:        url,
		httpClient: httpClient,
		header:     clientOptions.ToHeader(),
	}
}

func (g *getEndpoint) decodeError(statusCode int, body io.Reader) error {
	bytes, err := io.ReadAll(body)
	if err != nil {
		return err
	}
	return errors.New(string(bytes))
}

func (g *getEndpoint) Call(ctx context.Context) (string, error) {
	endpointURL := g.url
	var response string
	if err := core.DoRequest(
		ctx,
		g.httpClient,
		endpointURL,
		http.MethodGet,
		nil,
		response,
		g.header,
		g.decodeError,
	); err != nil {
		return response, err
	}
	return response, nil
}
