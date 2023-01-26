# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .scope import Scope


class StackFrame(pydantic.BaseModel):
    method_name: str = pydantic.Field(alias="methodName")
    line_number: int = pydantic.Field(alias="lineNumber")
    scopes: typing.List[Scope]

    class Partial(typing_extensions.TypedDict):
        method_name: typing_extensions.NotRequired[str]
        line_number: typing_extensions.NotRequired[int]
        scopes: typing_extensions.NotRequired[typing.List[Scope]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @StackFrame.Validators.root()
            def validate(values: StackFrame.Partial) -> StackFrame.Partial:
                ...

            @StackFrame.Validators.field("method_name")
            def validate_method_name(method_name: str, values: StackFrame.Partial) -> str:
                ...

            @StackFrame.Validators.field("line_number")
            def validate_line_number(line_number: int, values: StackFrame.Partial) -> int:
                ...

            @StackFrame.Validators.field("scopes")
            def validate_scopes(scopes: typing.List[Scope], values: StackFrame.Partial) -> typing.List[Scope]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[StackFrame.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[StackFrame.Validators._RootValidator]] = []
        _method_name_pre_validators: typing.ClassVar[typing.List[StackFrame.Validators.PreMethodNameValidator]] = []
        _method_name_post_validators: typing.ClassVar[typing.List[StackFrame.Validators.MethodNameValidator]] = []
        _line_number_pre_validators: typing.ClassVar[typing.List[StackFrame.Validators.PreLineNumberValidator]] = []
        _line_number_post_validators: typing.ClassVar[typing.List[StackFrame.Validators.LineNumberValidator]] = []
        _scopes_pre_validators: typing.ClassVar[typing.List[StackFrame.Validators.PreScopesValidator]] = []
        _scopes_post_validators: typing.ClassVar[typing.List[StackFrame.Validators.ScopesValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[StackFrame.Validators._RootValidator], StackFrame.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[StackFrame.Validators._PreRootValidator], StackFrame.Validators._PreRootValidator]:
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
            cls, field_name: typing_extensions.Literal["method_name"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [StackFrame.Validators.PreMethodNameValidator], StackFrame.Validators.PreMethodNameValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["method_name"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[StackFrame.Validators.MethodNameValidator], StackFrame.Validators.MethodNameValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["line_number"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [StackFrame.Validators.PreLineNumberValidator], StackFrame.Validators.PreLineNumberValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["line_number"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[StackFrame.Validators.LineNumberValidator], StackFrame.Validators.LineNumberValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["scopes"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[StackFrame.Validators.PreScopesValidator], StackFrame.Validators.PreScopesValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["scopes"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[StackFrame.Validators.ScopesValidator], StackFrame.Validators.ScopesValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "method_name":
                    if pre:
                        cls._method_name_pre_validators.append(validator)
                    else:
                        cls._method_name_post_validators.append(validator)
                if field_name == "line_number":
                    if pre:
                        cls._line_number_pre_validators.append(validator)
                    else:
                        cls._line_number_post_validators.append(validator)
                if field_name == "scopes":
                    if pre:
                        cls._scopes_pre_validators.append(validator)
                    else:
                        cls._scopes_post_validators.append(validator)
                return validator

            return decorator

        class PreMethodNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: StackFrame.Partial) -> typing.Any:
                ...

        class MethodNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: StackFrame.Partial) -> str:
                ...

        class PreLineNumberValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: StackFrame.Partial) -> typing.Any:
                ...

        class LineNumberValidator(typing_extensions.Protocol):
            def __call__(self, __v: int, __values: StackFrame.Partial) -> int:
                ...

        class PreScopesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: StackFrame.Partial) -> typing.Any:
                ...

        class ScopesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.List[Scope], __values: StackFrame.Partial) -> typing.List[Scope]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: StackFrame.Partial) -> StackFrame.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: StackFrame.Partial) -> StackFrame.Partial:
        for validator in StackFrame.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: StackFrame.Partial) -> StackFrame.Partial:
        for validator in StackFrame.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("method_name", pre=True)
    def _pre_validate_method_name(cls, v: str, values: StackFrame.Partial) -> str:
        for validator in StackFrame.Validators._method_name_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("method_name", pre=False)
    def _post_validate_method_name(cls, v: str, values: StackFrame.Partial) -> str:
        for validator in StackFrame.Validators._method_name_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("line_number", pre=True)
    def _pre_validate_line_number(cls, v: int, values: StackFrame.Partial) -> int:
        for validator in StackFrame.Validators._line_number_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("line_number", pre=False)
    def _post_validate_line_number(cls, v: int, values: StackFrame.Partial) -> int:
        for validator in StackFrame.Validators._line_number_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("scopes", pre=True)
    def _pre_validate_scopes(cls, v: typing.List[Scope], values: StackFrame.Partial) -> typing.List[Scope]:
        for validator in StackFrame.Validators._scopes_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("scopes", pre=False)
    def _post_validate_scopes(cls, v: typing.List[Scope], values: StackFrame.Partial) -> typing.List[Scope]:
        for validator in StackFrame.Validators._scopes_post_validators:
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
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
