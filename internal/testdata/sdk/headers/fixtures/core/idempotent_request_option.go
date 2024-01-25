// This file was auto-generated by Fern from our API Definition.

package core

import (
	fmt "fmt"
	http "net/http"
)

// IdempotentRequestOption adapts the behavior of an individual request.
type IdempotentRequestOption interface {
	applyIdempotentRequestOptions(*IdempotentRequestOptions)
}

// IdempotentRequestOptions defines all of the possible idempotent request options.
//
// This type is primarily used by the generated code and is not meant
// to be used directly; use the option package instead.
type IdempotentRequestOptions struct {
	*RequestOptions

	IdempotencyKey string
}

// NewIdempotentRequestOptions returns a new *IdempotentRequestOptions value.
//
// This function is primarily used by the generated code and is not meant
// to be used directly; use IdempotentRequestOption instead.
func NewIdempotentRequestOptions(opts ...IdempotentRequestOption) *IdempotentRequestOptions {
	options := &IdempotentRequestOptions{
		RequestOptions: NewRequestOptions(),
	}
	for _, opt := range opts {
		if requestOption, ok := opt.(RequestOption); ok {
			requestOption.applyRequestOptions(options.RequestOptions)
		}
		opt.applyIdempotentRequestOptions(options)
	}
	return options
}

// IdempotencyKeyOption implements the RequestOption interface.
type IdempotencyKeyOption struct {
	IdempotencyKey string
}

func (i *IdempotencyKeyOption) applyIdempotentRequestOptions(opts *IdempotentRequestOptions) {
	opts.IdempotencyKey = i.IdempotencyKey
}

// ToHeader maps the configured request options into a http.Header used
// for the request.
func (i *IdempotentRequestOptions) ToHeader() http.Header {
	header := i.RequestOptions.ToHeader()
	if i.IdempotencyKey != "" {
		header.Set("Idempotency-Key", fmt.Sprintf("%v", i.IdempotencyKey))
	}
	return header
}
