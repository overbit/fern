# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ...core.datetime_utils import serialize_datetime
from .trace_response_v_2 import TraceResponseV2


class TraceResponsesPageV2(pydantic.BaseModel):
    offset: typing.Optional[int] = pydantic.Field(
        description=(
            "If present, use this to load subseqent pages.\n"
            "The offset is the id of the next trace response to load.\n"
        )
    )
    trace_responses: typing.List[TraceResponseV2] = pydantic.Field(alias="traceResponses")

    class Partial(typing_extensions.TypedDict):
        offset: typing_extensions.NotRequired[typing.Optional[int]]
        trace_responses: typing_extensions.NotRequired[typing.List[TraceResponseV2]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TraceResponsesPageV2.Validators.root()
            def validate(values: TraceResponsesPageV2.Partial) -> TraceResponsesPageV2.Partial:
                ...

            @TraceResponsesPageV2.Validators.field("offset")
            def validate_offset(offset: typing.Optional[int], values: TraceResponsesPageV2.Partial) -> typing.Optional[int]:
                ...

            @TraceResponsesPageV2.Validators.field("trace_responses")
            def validate_trace_responses(trace_responses: typing.List[TraceResponseV2], values: TraceResponsesPageV2.Partial) -> typing.List[TraceResponseV2]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[TraceResponsesPageV2.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[TraceResponsesPageV2.Validators._RootValidator]] = []
        _offset_pre_validators: typing.ClassVar[typing.List[TraceResponsesPageV2.Validators.PreOffsetValidator]] = []
        _offset_post_validators: typing.ClassVar[typing.List[TraceResponsesPageV2.Validators.OffsetValidator]] = []
        _trace_responses_pre_validators: typing.ClassVar[
            typing.List[TraceResponsesPageV2.Validators.PreTraceResponsesValidator]
        ] = []
        _trace_responses_post_validators: typing.ClassVar[
            typing.List[TraceResponsesPageV2.Validators.TraceResponsesValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [TraceResponsesPageV2.Validators._RootValidator], TraceResponsesPageV2.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [TraceResponsesPageV2.Validators._PreRootValidator], TraceResponsesPageV2.Validators._PreRootValidator
        ]:
            ...

        @classmethod
        def root(cls, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["offset"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [TraceResponsesPageV2.Validators.PreOffsetValidator], TraceResponsesPageV2.Validators.PreOffsetValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["offset"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [TraceResponsesPageV2.Validators.OffsetValidator], TraceResponsesPageV2.Validators.OffsetValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["trace_responses"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [TraceResponsesPageV2.Validators.PreTraceResponsesValidator],
            TraceResponsesPageV2.Validators.PreTraceResponsesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["trace_responses"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [TraceResponsesPageV2.Validators.TraceResponsesValidator],
            TraceResponsesPageV2.Validators.TraceResponsesValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "offset":
                    if pre:
                        cls._offset_pre_validators.append(validator)
                    else:
                        cls._offset_post_validators.append(validator)
                if field_name == "trace_responses":
                    if pre:
                        cls._trace_responses_pre_validators.append(validator)
                    else:
                        cls._trace_responses_post_validators.append(validator)
                return validator

            return decorator

        class PreOffsetValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: TraceResponsesPageV2.Partial) -> typing.Any:
                ...

        class OffsetValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[int], __values: TraceResponsesPageV2.Partial
            ) -> typing.Optional[int]:
                ...

        class PreTraceResponsesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: TraceResponsesPageV2.Partial) -> typing.Any:
                ...

        class TraceResponsesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[TraceResponseV2], __values: TraceResponsesPageV2.Partial
            ) -> typing.List[TraceResponseV2]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: TraceResponsesPageV2.Partial) -> TraceResponsesPageV2.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: TraceResponsesPageV2.Partial) -> TraceResponsesPageV2.Partial:
        for validator in TraceResponsesPageV2.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: TraceResponsesPageV2.Partial) -> TraceResponsesPageV2.Partial:
        for validator in TraceResponsesPageV2.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("offset", pre=True)
    def _pre_validate_offset(
        cls, v: typing.Optional[int], values: TraceResponsesPageV2.Partial
    ) -> typing.Optional[int]:
        for validator in TraceResponsesPageV2.Validators._offset_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("offset", pre=False)
    def _post_validate_offset(
        cls, v: typing.Optional[int], values: TraceResponsesPageV2.Partial
    ) -> typing.Optional[int]:
        for validator in TraceResponsesPageV2.Validators._offset_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("trace_responses", pre=True)
    def _pre_validate_trace_responses(
        cls, v: typing.List[TraceResponseV2], values: TraceResponsesPageV2.Partial
    ) -> typing.List[TraceResponseV2]:
        for validator in TraceResponsesPageV2.Validators._trace_responses_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("trace_responses", pre=False)
    def _post_validate_trace_responses(
        cls, v: typing.List[TraceResponseV2], values: TraceResponsesPageV2.Partial
    ) -> typing.List[TraceResponseV2]:
        for validator in TraceResponsesPageV2.Validators._trace_responses_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
