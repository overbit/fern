// Generated by Fern. Do not edit.

package api

import (
	context "context"
	core "github.com/fern-api/fern-go/internal/testdata/sdk/path-and-query-params/fixtures/core"
)

type Service interface {
	GetUser(ctx context.Context, userId string, request *GetUserRequest) (string, error)
}

func NewClient(baseURL string, httpClient core.HTTPClient, opts ...core.ClientOption) (Service, error) {
	options := new(core.ClientOptions)
	for _, opt := range opts {
		opt(options)
	}
	return &client{
		getUser: newGetUserEndpoint(baseURL, httpClient, options).Call,
	}, nil
}

type client struct {
	getUser func(ctx context.Context, userId string, request *GetUserRequest) (string, error)
}

func (g *client) GetUser(ctx context.Context, userId string, request *GetUserRequest) (string, error) {
	return g.getUser(ctx, userId, request)
}
