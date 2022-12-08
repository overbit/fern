# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...commons.types.debug_variable_value import DebugVariableValue
from .expression_location import ExpressionLocation
from .stack_information import StackInformation
from .submission_id import SubmissionId


class TraceResponse(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")
    line_number: int = pydantic.Field(alias="lineNumber")
    return_value: typing.Optional[DebugVariableValue] = pydantic.Field(alias="returnValue")
    expression_location: typing.Optional[ExpressionLocation] = pydantic.Field(alias="expressionLocation")
    stack: StackInformation
    stdout: typing.Optional[str]

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]
        line_number: typing_extensions.NotRequired[int]
        return_value: typing_extensions.NotRequired[typing.Optional[DebugVariableValue]]
        expression_location: typing_extensions.NotRequired[typing.Optional[ExpressionLocation]]
        stack: typing_extensions.NotRequired[StackInformation]
        stdout: typing_extensions.NotRequired[typing.Optional[str]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TraceResponse.Validators.root
            def validate(values: TraceResponse.Partial) -> TraceResponse.Partial:
                ...

            @TraceResponse.Validators.field("submission_id")
            def validate_submission_id(submission_id: SubmissionId, values: TraceResponse.Partial) -> SubmissionId:
                ...

            @TraceResponse.Validators.field("line_number")
            def validate_line_number(line_number: int, values: TraceResponse.Partial) -> int:
                ...

            @TraceResponse.Validators.field("return_value")
            def validate_return_value(return_value: typing.Optional[DebugVariableValue], values: TraceResponse.Partial) -> typing.Optional[DebugVariableValue]:
                ...

            @TraceResponse.Validators.field("expression_location")
            def validate_expression_location(expression_location: typing.Optional[ExpressionLocation], values: TraceResponse.Partial) -> typing.Optional[ExpressionLocation]:
                ...

            @TraceResponse.Validators.field("stack")
            def validate_stack(stack: StackInformation, values: TraceResponse.Partial) -> StackInformation:
                ...

            @TraceResponse.Validators.field("stdout")
            def validate_stdout(stdout: typing.Optional[str], values: TraceResponse.Partial) -> typing.Optional[str]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[TraceResponse.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[TraceResponse.Validators._RootValidator]] = []
        _submission_id_pre_validators: typing.ClassVar[typing.List[TraceResponse.Validators.SubmissionIdValidator]] = []
        _submission_id_post_validators: typing.ClassVar[
            typing.List[TraceResponse.Validators.SubmissionIdValidator]
        ] = []
        _line_number_pre_validators: typing.ClassVar[typing.List[TraceResponse.Validators.LineNumberValidator]] = []
        _line_number_post_validators: typing.ClassVar[typing.List[TraceResponse.Validators.LineNumberValidator]] = []
        _return_value_pre_validators: typing.ClassVar[typing.List[TraceResponse.Validators.ReturnValueValidator]] = []
        _return_value_post_validators: typing.ClassVar[typing.List[TraceResponse.Validators.ReturnValueValidator]] = []
        _expression_location_pre_validators: typing.ClassVar[
            typing.List[TraceResponse.Validators.ExpressionLocationValidator]
        ] = []
        _expression_location_post_validators: typing.ClassVar[
            typing.List[TraceResponse.Validators.ExpressionLocationValidator]
        ] = []
        _stack_pre_validators: typing.ClassVar[typing.List[TraceResponse.Validators.StackValidator]] = []
        _stack_post_validators: typing.ClassVar[typing.List[TraceResponse.Validators.StackValidator]] = []
        _stdout_pre_validators: typing.ClassVar[typing.List[TraceResponse.Validators.StdoutValidator]] = []
        _stdout_post_validators: typing.ClassVar[typing.List[TraceResponse.Validators.StdoutValidator]] = []

        @classmethod
        def root(cls, *, pre: bool = False) -> TraceResponse.Validators._RootValidator:
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
            cls, field_name: typing_extensions.Literal["submission_id"], *, pre: bool = False
        ) -> typing.Callable[
            [TraceResponse.Validators.SubmissionIdValidator], TraceResponse.Validators.SubmissionIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["line_number"], *, pre: bool = False
        ) -> typing.Callable[
            [TraceResponse.Validators.LineNumberValidator], TraceResponse.Validators.LineNumberValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["return_value"], *, pre: bool = False
        ) -> typing.Callable[
            [TraceResponse.Validators.ReturnValueValidator], TraceResponse.Validators.ReturnValueValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["expression_location"], *, pre: bool = False
        ) -> typing.Callable[
            [TraceResponse.Validators.ExpressionLocationValidator], TraceResponse.Validators.ExpressionLocationValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["stack"], *, pre: bool = False
        ) -> typing.Callable[[TraceResponse.Validators.StackValidator], TraceResponse.Validators.StackValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["stdout"], *, pre: bool = False
        ) -> typing.Callable[[TraceResponse.Validators.StdoutValidator], TraceResponse.Validators.StdoutValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    if pre:
                        cls._submission_id_pre_validators.append(validator)
                    else:
                        cls._submission_id_post_validators.append(validator)
                if field_name == "line_number":
                    if pre:
                        cls._line_number_pre_validators.append(validator)
                    else:
                        cls._line_number_post_validators.append(validator)
                if field_name == "return_value":
                    if pre:
                        cls._return_value_pre_validators.append(validator)
                    else:
                        cls._return_value_post_validators.append(validator)
                if field_name == "expression_location":
                    if pre:
                        cls._expression_location_pre_validators.append(validator)
                    else:
                        cls._expression_location_post_validators.append(validator)
                if field_name == "stack":
                    if pre:
                        cls._stack_pre_validators.append(validator)
                    else:
                        cls._stack_post_validators.append(validator)
                if field_name == "stdout":
                    if pre:
                        cls._stdout_pre_validators.append(validator)
                    else:
                        cls._stdout_post_validators.append(validator)
                return validator

            return decorator

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: SubmissionId, __values: TraceResponse.Partial) -> SubmissionId:
                ...

        class LineNumberValidator(typing_extensions.Protocol):
            def __call__(self, __v: int, __values: TraceResponse.Partial) -> int:
                ...

        class ReturnValueValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[DebugVariableValue], __values: TraceResponse.Partial
            ) -> typing.Optional[DebugVariableValue]:
                ...

        class ExpressionLocationValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[ExpressionLocation], __values: TraceResponse.Partial
            ) -> typing.Optional[ExpressionLocation]:
                ...

        class StackValidator(typing_extensions.Protocol):
            def __call__(self, __v: StackInformation, __values: TraceResponse.Partial) -> StackInformation:
                ...

        class StdoutValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Optional[str], __values: TraceResponse.Partial) -> typing.Optional[str]:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: TraceResponse.Partial) -> TraceResponse.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: TraceResponse.Partial) -> TraceResponse.Partial:
        for validator in TraceResponse.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: TraceResponse.Partial) -> TraceResponse.Partial:
        for validator in TraceResponse.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id", pre=True)
    def _pre_validate_submission_id(cls, v: SubmissionId, values: TraceResponse.Partial) -> SubmissionId:
        for validator in TraceResponse.Validators._submission_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("submission_id", pre=False)
    def _post_validate_submission_id(cls, v: SubmissionId, values: TraceResponse.Partial) -> SubmissionId:
        for validator in TraceResponse.Validators._submission_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("line_number", pre=True)
    def _pre_validate_line_number(cls, v: int, values: TraceResponse.Partial) -> int:
        for validator in TraceResponse.Validators._line_number_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("line_number", pre=False)
    def _post_validate_line_number(cls, v: int, values: TraceResponse.Partial) -> int:
        for validator in TraceResponse.Validators._line_number_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("return_value", pre=True)
    def _pre_validate_return_value(
        cls, v: typing.Optional[DebugVariableValue], values: TraceResponse.Partial
    ) -> typing.Optional[DebugVariableValue]:
        for validator in TraceResponse.Validators._return_value_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("return_value", pre=False)
    def _post_validate_return_value(
        cls, v: typing.Optional[DebugVariableValue], values: TraceResponse.Partial
    ) -> typing.Optional[DebugVariableValue]:
        for validator in TraceResponse.Validators._return_value_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("expression_location", pre=True)
    def _pre_validate_expression_location(
        cls, v: typing.Optional[ExpressionLocation], values: TraceResponse.Partial
    ) -> typing.Optional[ExpressionLocation]:
        for validator in TraceResponse.Validators._expression_location_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("expression_location", pre=False)
    def _post_validate_expression_location(
        cls, v: typing.Optional[ExpressionLocation], values: TraceResponse.Partial
    ) -> typing.Optional[ExpressionLocation]:
        for validator in TraceResponse.Validators._expression_location_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("stack", pre=True)
    def _pre_validate_stack(cls, v: StackInformation, values: TraceResponse.Partial) -> StackInformation:
        for validator in TraceResponse.Validators._stack_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("stack", pre=False)
    def _post_validate_stack(cls, v: StackInformation, values: TraceResponse.Partial) -> StackInformation:
        for validator in TraceResponse.Validators._stack_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("stdout", pre=True)
    def _pre_validate_stdout(cls, v: typing.Optional[str], values: TraceResponse.Partial) -> typing.Optional[str]:
        for validator in TraceResponse.Validators._stdout_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("stdout", pre=False)
    def _post_validate_stdout(cls, v: typing.Optional[str], values: TraceResponse.Partial) -> typing.Optional[str]:
        for validator in TraceResponse.Validators._stdout_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        extra = pydantic.Extra.forbid
