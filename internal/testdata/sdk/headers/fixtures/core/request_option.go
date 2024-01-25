// This file was auto-generated by Fern from our API Definition.

package core

import (
	base64 "encoding/base64"
	fmt "fmt"
	uuid "github.com/google/uuid"
	http "net/http"
	time "time"
)

// RequestOption adapts the behavior of the client or an individual request.
type RequestOption interface {
	applyRequestOptions(*RequestOptions)
}

// RequestOptions defines all of the possible request options.
//
// This type is primarily used by the generated code and is not meant
// to be used directly; use the option package instead.
type RequestOptions struct {
	BaseURL              string
	HTTPClient           HTTPClient
	HTTPHeader           http.Header
	Custom               *[]byte
	XApiName             string
	XApiId               uuid.UUID
	XApiDatetime         time.Time
	XApiDate             time.Time
	XApiBytes            []byte
	XApiOptionalName     *string
	XApiOptionalId       *uuid.UUID
	XApiOptionalDatetime *time.Time
	XApiOptionalDate     *time.Time
	XApiOptionalBytes    *[]byte
}

// NewRequestOptions returns a new *RequestOptions value.
//
// This function is primarily used by the generated code and is not meant
// to be used directly; use RequestOption instead.
func NewRequestOptions(opts ...RequestOption) *RequestOptions {
	options := &RequestOptions{
		HTTPHeader: make(http.Header),
	}
	for _, opt := range opts {
		opt.applyRequestOptions(options)
	}
	return options
}

// ToHeader maps the configured request options into a http.Header used
// for the request(s).
func (r *RequestOptions) ToHeader() http.Header {
	header := r.cloneHeader()
	if r.Custom != nil {
		header.Set("X-API-Custom-Key", fmt.Sprintf("%v", base64.StdEncoding.EncodeToString(*r.Custom)))
	}
	header.Set("X-API-Name", fmt.Sprintf("%v", r.XApiName))
	header.Set("X-API-ID", fmt.Sprintf("%v", r.XApiId))
	header.Set("X-API-Datetime", fmt.Sprintf("%v", r.XApiDatetime.Format(time.RFC3339)))
	header.Set("X-API-Date", fmt.Sprintf("%v", r.XApiDate.Format("2006-01-02")))
	header.Set("X-API-Bytes", fmt.Sprintf("%v", base64.StdEncoding.EncodeToString(r.XApiBytes)))
	if r.XApiOptionalName != nil {
		header.Set("X-API-Optional-Name", fmt.Sprintf("%v", *r.XApiOptionalName))
	}
	if r.XApiOptionalId != nil {
		header.Set("X-API-Optional-ID", fmt.Sprintf("%v", *r.XApiOptionalId))
	}
	if r.XApiOptionalDatetime != nil {
		header.Set("X-API-Optional-Datetime", fmt.Sprintf("%v", r.XApiOptionalDatetime.Format(time.RFC3339)))
	}
	if r.XApiOptionalDate != nil {
		header.Set("X-API-Optional-Date", fmt.Sprintf("%v", r.XApiOptionalDate.Format("2006-01-02")))
	}
	if r.XApiOptionalBytes != nil {
		header.Set("X-API-Optional-Bytes", fmt.Sprintf("%v", base64.StdEncoding.EncodeToString(*r.XApiOptionalBytes)))
	}
	header.Set("X-API-Fern-Header", fmt.Sprintf("%v", "fern"))
	return header
}

func (r *RequestOptions) cloneHeader() http.Header {
	return r.HTTPHeader.Clone()
}

// BaseURLOption implements the RequestOption interface.
type BaseURLOption struct {
	BaseURL string
}

func (b *BaseURLOption) applyRequestOptions(opts *RequestOptions) {
	opts.BaseURL = b.BaseURL
}

func (b *BaseURLOption) applyIdempotentRequestOptions(opts *IdempotentRequestOptions) {
	opts.BaseURL = b.BaseURL
}

// HTTPClientOption implements the RequestOption interface.
type HTTPClientOption struct {
	HTTPClient HTTPClient
}

func (h *HTTPClientOption) applyRequestOptions(opts *RequestOptions) {
	opts.HTTPClient = h.HTTPClient
}

func (h *HTTPClientOption) applyIdempotentRequestOptions(opts *IdempotentRequestOptions) {
	opts.HTTPClient = h.HTTPClient
}

// HTTPHeaderOption implements the RequestOption interface.
type HTTPHeaderOption struct {
	HTTPHeader http.Header
}

func (h *HTTPHeaderOption) applyRequestOptions(opts *RequestOptions) {
	opts.HTTPHeader = h.HTTPHeader
}

func (h *HTTPHeaderOption) applyIdempotentRequestOptions(opts *IdempotentRequestOptions) {
	opts.HTTPHeader = h.HTTPHeader
}

// CustomOption implements the RequestOption interface.
type CustomOption struct {
	Custom *[]byte
}

func (c *CustomOption) applyRequestOptions(opts *RequestOptions) {
	opts.Custom = c.Custom
}

func (c *CustomOption) applyIdempotentRequestOptions(opts *IdempotentRequestOptions) {
	opts.Custom = c.Custom
}

// XApiNameOption implements the RequestOption interface.
type XApiNameOption struct {
	XApiName string
}

func (x *XApiNameOption) applyRequestOptions(opts *RequestOptions) {
	opts.XApiName = x.XApiName
}

func (x *XApiNameOption) applyIdempotentRequestOptions(opts *IdempotentRequestOptions) {
	opts.XApiName = x.XApiName
}

// XApiIdOption implements the RequestOption interface.
type XApiIdOption struct {
	XApiId uuid.UUID
}

func (x *XApiIdOption) applyRequestOptions(opts *RequestOptions) {
	opts.XApiId = x.XApiId
}

func (x *XApiIdOption) applyIdempotentRequestOptions(opts *IdempotentRequestOptions) {
	opts.XApiId = x.XApiId
}

// XApiDatetimeOption implements the RequestOption interface.
type XApiDatetimeOption struct {
	XApiDatetime time.Time
}

func (x *XApiDatetimeOption) applyRequestOptions(opts *RequestOptions) {
	opts.XApiDatetime = x.XApiDatetime
}

func (x *XApiDatetimeOption) applyIdempotentRequestOptions(opts *IdempotentRequestOptions) {
	opts.XApiDatetime = x.XApiDatetime
}

// XApiDateOption implements the RequestOption interface.
type XApiDateOption struct {
	XApiDate time.Time
}

func (x *XApiDateOption) applyRequestOptions(opts *RequestOptions) {
	opts.XApiDate = x.XApiDate
}

func (x *XApiDateOption) applyIdempotentRequestOptions(opts *IdempotentRequestOptions) {
	opts.XApiDate = x.XApiDate
}

// XApiBytesOption implements the RequestOption interface.
type XApiBytesOption struct {
	XApiBytes []byte
}

func (x *XApiBytesOption) applyRequestOptions(opts *RequestOptions) {
	opts.XApiBytes = x.XApiBytes
}

func (x *XApiBytesOption) applyIdempotentRequestOptions(opts *IdempotentRequestOptions) {
	opts.XApiBytes = x.XApiBytes
}

// XApiOptionalNameOption implements the RequestOption interface.
type XApiOptionalNameOption struct {
	XApiOptionalName *string
}

func (x *XApiOptionalNameOption) applyRequestOptions(opts *RequestOptions) {
	opts.XApiOptionalName = x.XApiOptionalName
}

func (x *XApiOptionalNameOption) applyIdempotentRequestOptions(opts *IdempotentRequestOptions) {
	opts.XApiOptionalName = x.XApiOptionalName
}

// XApiOptionalIdOption implements the RequestOption interface.
type XApiOptionalIdOption struct {
	XApiOptionalId *uuid.UUID
}

func (x *XApiOptionalIdOption) applyRequestOptions(opts *RequestOptions) {
	opts.XApiOptionalId = x.XApiOptionalId
}

func (x *XApiOptionalIdOption) applyIdempotentRequestOptions(opts *IdempotentRequestOptions) {
	opts.XApiOptionalId = x.XApiOptionalId
}

// XApiOptionalDatetimeOption implements the RequestOption interface.
type XApiOptionalDatetimeOption struct {
	XApiOptionalDatetime *time.Time
}

func (x *XApiOptionalDatetimeOption) applyRequestOptions(opts *RequestOptions) {
	opts.XApiOptionalDatetime = x.XApiOptionalDatetime
}

func (x *XApiOptionalDatetimeOption) applyIdempotentRequestOptions(opts *IdempotentRequestOptions) {
	opts.XApiOptionalDatetime = x.XApiOptionalDatetime
}

// XApiOptionalDateOption implements the RequestOption interface.
type XApiOptionalDateOption struct {
	XApiOptionalDate *time.Time
}

func (x *XApiOptionalDateOption) applyRequestOptions(opts *RequestOptions) {
	opts.XApiOptionalDate = x.XApiOptionalDate
}

func (x *XApiOptionalDateOption) applyIdempotentRequestOptions(opts *IdempotentRequestOptions) {
	opts.XApiOptionalDate = x.XApiOptionalDate
}

// XApiOptionalBytesOption implements the RequestOption interface.
type XApiOptionalBytesOption struct {
	XApiOptionalBytes *[]byte
}

func (x *XApiOptionalBytesOption) applyRequestOptions(opts *RequestOptions) {
	opts.XApiOptionalBytes = x.XApiOptionalBytes
}

func (x *XApiOptionalBytesOption) applyIdempotentRequestOptions(opts *IdempotentRequestOptions) {
	opts.XApiOptionalBytes = x.XApiOptionalBytes
}
