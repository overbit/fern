// This file was auto-generated by Fern from our API Definition.

package api

import (
	uuid "github.com/google/uuid"
	time "time"
)

type SetNameRequest struct {
	XEndpointHeader                 string     `json:"-"`
	XEndpointIdHeader               uuid.UUID  `json:"-"`
	XEndpointDateHeader             time.Time  `json:"-"`
	XEndpointDatetimeHeader         time.Time  `json:"-"`
	XEndpointBytesHeader            []byte     `json:"-"`
	XEndpointOptionalHeader         *string    `json:"-"`
	XEndpointOptionalIdHeader       *uuid.UUID `json:"-"`
	XEndpointOptionalDateHeader     *time.Time `json:"-"`
	XEndpointOptionalDatetimeHeader *time.Time `json:"-"`
	XEndpointOptionalBytesHeader    *[]byte    `json:"-"`
	xEndpointFernHeader             string
}

func (s *SetNameRequest) XEndpointFernHeader() string {
	return s.xEndpointFernHeader
}

type UpdateNameRequest struct {
	XEndpointHeader string `json:"-"`
}
