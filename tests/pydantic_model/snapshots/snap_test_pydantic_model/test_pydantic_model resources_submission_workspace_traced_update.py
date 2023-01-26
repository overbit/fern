# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ...core.datetime_utils import serialize_datetime


class WorkspaceTracedUpdate(pydantic.BaseModel):
    trace_responses_size: int = pydantic.Field(alias="traceResponsesSize")

    class Partial(typing_extensions.TypedDict):
        trace_responses_size: typing_extensions.NotRequired[int]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @WorkspaceTracedUpdate.Validators.root()
            def validate(values: WorkspaceTracedUpdate.Partial) -> WorkspaceTracedUpdate.Partial:
                ...

            @WorkspaceTracedUpdate.Validators.field("trace_responses_size")
            def validate_trace_responses_size(trace_responses_size: int, values: WorkspaceTracedUpdate.Partial) -> int:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[WorkspaceTracedUpdate.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[WorkspaceTracedUpdate.Validators._RootValidator]] = []
        _trace_responses_size_pre_validators: typing.ClassVar[
            typing.List[WorkspaceTracedUpdate.Validators.PreTraceResponsesSizeValidator]
        ] = []
        _trace_responses_size_post_validators: typing.ClassVar[
            typing.List[WorkspaceTracedUpdate.Validators.TraceResponsesSizeValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [WorkspaceTracedUpdate.Validators._RootValidator], WorkspaceTracedUpdate.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [WorkspaceTracedUpdate.Validators._PreRootValidator], WorkspaceTracedUpdate.Validators._PreRootValidator
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
            cls, field_name: typing_extensions.Literal["trace_responses_size"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [WorkspaceTracedUpdate.Validators.PreTraceResponsesSizeValidator],
            WorkspaceTracedUpdate.Validators.PreTraceResponsesSizeValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["trace_responses_size"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [WorkspaceTracedUpdate.Validators.TraceResponsesSizeValidator],
            WorkspaceTracedUpdate.Validators.TraceResponsesSizeValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "trace_responses_size":
                    if pre:
                        cls._trace_responses_size_pre_validators.append(validator)
                    else:
                        cls._trace_responses_size_post_validators.append(validator)
                return validator

            return decorator

        class PreTraceResponsesSizeValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: WorkspaceTracedUpdate.Partial) -> typing.Any:
                ...

        class TraceResponsesSizeValidator(typing_extensions.Protocol):
            def __call__(self, __v: int, __values: WorkspaceTracedUpdate.Partial) -> int:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: WorkspaceTracedUpdate.Partial) -> WorkspaceTracedUpdate.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: WorkspaceTracedUpdate.Partial) -> WorkspaceTracedUpdate.Partial:
        for validator in WorkspaceTracedUpdate.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: WorkspaceTracedUpdate.Partial) -> WorkspaceTracedUpdate.Partial:
        for validator in WorkspaceTracedUpdate.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("trace_responses_size", pre=True)
    def _pre_validate_trace_responses_size(cls, v: int, values: WorkspaceTracedUpdate.Partial) -> int:
        for validator in WorkspaceTracedUpdate.Validators._trace_responses_size_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("trace_responses_size", pre=False)
    def _post_validate_trace_responses_size(cls, v: int, values: WorkspaceTracedUpdate.Partial) -> int:
        for validator in WorkspaceTracedUpdate.Validators._trace_responses_size_post_validators:
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
