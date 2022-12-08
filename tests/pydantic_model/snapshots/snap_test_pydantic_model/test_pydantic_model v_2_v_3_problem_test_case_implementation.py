# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .test_case_function import TestCaseFunction
from .test_case_implementation_description import TestCaseImplementationDescription


class TestCaseImplementation(pydantic.BaseModel):
    description: TestCaseImplementationDescription
    function: TestCaseFunction

    class Partial(typing_extensions.TypedDict):
        description: typing_extensions.NotRequired[TestCaseImplementationDescription]
        function: typing_extensions.NotRequired[TestCaseFunction]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestCaseImplementation.Validators.root
            def validate(values: TestCaseImplementation.Partial) -> TestCaseImplementation.Partial:
                ...

            @TestCaseImplementation.Validators.field("description")
            def validate_description(description: TestCaseImplementationDescription, values: TestCaseImplementation.Partial) -> TestCaseImplementationDescription:
                ...

            @TestCaseImplementation.Validators.field("function")
            def validate_function(function: TestCaseFunction, values: TestCaseImplementation.Partial) -> TestCaseFunction:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[TestCaseImplementation.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[TestCaseImplementation.Validators._RootValidator]] = []
        _description_pre_validators: typing.ClassVar[
            typing.List[TestCaseImplementation.Validators.DescriptionValidator]
        ] = []
        _description_post_validators: typing.ClassVar[
            typing.List[TestCaseImplementation.Validators.DescriptionValidator]
        ] = []
        _function_pre_validators: typing.ClassVar[typing.List[TestCaseImplementation.Validators.FunctionValidator]] = []
        _function_post_validators: typing.ClassVar[
            typing.List[TestCaseImplementation.Validators.FunctionValidator]
        ] = []

        @classmethod
        def root(cls, *, pre: bool = False) -> TestCaseImplementation.Validators._RootValidator:
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
            cls, field_name: typing_extensions.Literal["description"], *, pre: bool = False
        ) -> typing.Callable[
            [TestCaseImplementation.Validators.DescriptionValidator],
            TestCaseImplementation.Validators.DescriptionValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["function"], *, pre: bool = False
        ) -> typing.Callable[
            [TestCaseImplementation.Validators.FunctionValidator], TestCaseImplementation.Validators.FunctionValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "description":
                    if pre:
                        cls._description_pre_validators.append(validator)
                    else:
                        cls._description_post_validators.append(validator)
                if field_name == "function":
                    if pre:
                        cls._function_pre_validators.append(validator)
                    else:
                        cls._function_post_validators.append(validator)
                return validator

            return decorator

        class DescriptionValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: TestCaseImplementationDescription, __values: TestCaseImplementation.Partial
            ) -> TestCaseImplementationDescription:
                ...

        class FunctionValidator(typing_extensions.Protocol):
            def __call__(self, __v: TestCaseFunction, __values: TestCaseImplementation.Partial) -> TestCaseFunction:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: TestCaseImplementation.Partial) -> TestCaseImplementation.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: TestCaseImplementation.Partial) -> TestCaseImplementation.Partial:
        for validator in TestCaseImplementation.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: TestCaseImplementation.Partial) -> TestCaseImplementation.Partial:
        for validator in TestCaseImplementation.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("description", pre=True)
    def _pre_validate_description(
        cls, v: TestCaseImplementationDescription, values: TestCaseImplementation.Partial
    ) -> TestCaseImplementationDescription:
        for validator in TestCaseImplementation.Validators._description_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("description", pre=False)
    def _post_validate_description(
        cls, v: TestCaseImplementationDescription, values: TestCaseImplementation.Partial
    ) -> TestCaseImplementationDescription:
        for validator in TestCaseImplementation.Validators._description_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("function", pre=True)
    def _pre_validate_function(cls, v: TestCaseFunction, values: TestCaseImplementation.Partial) -> TestCaseFunction:
        for validator in TestCaseImplementation.Validators._function_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("function", pre=False)
    def _post_validate_function(cls, v: TestCaseFunction, values: TestCaseImplementation.Partial) -> TestCaseFunction:
        for validator in TestCaseImplementation.Validators._function_post_validators:
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
