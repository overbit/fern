// This file was auto-generated by Fern from our API Definition.

package literal

type SendLiteralsInQueryRequest struct {
	Query  string `query:"query"`
	prompt string
	stream bool
}

func (s *SendLiteralsInQueryRequest) Prompt() string {
	return s.prompt
}

func (s *SendLiteralsInQueryRequest) Stream() bool {
	return s.stream
}