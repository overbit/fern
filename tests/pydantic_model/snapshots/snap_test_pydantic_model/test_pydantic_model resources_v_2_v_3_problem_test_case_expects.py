# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from .....core.datetime_utils import serialize_datetime


class TestCaseExpects(pydantic.BaseModel):
    expected_stdout: typing.Optional[str] = pydantic.Field(alias="expectedStdout")

    class Partial(typing_extensions.TypedDict):
        expected_stdout: typing_extensions.NotRequired[typing.Optional[str]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestCaseExpects.Validators.root()
            def validate(values: TestCaseExpects.Partial) -> TestCaseExpects.Partial:
                ...

            @TestCaseExpects.Validators.field("expected_stdout")
            def validate_expected_stdout(expected_stdout: typing.Optional[str], values: TestCaseExpects.Partial) -> typing.Optional[str]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[TestCaseExpects.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[TestCaseExpects.Validators._RootValidator]] = []
        _expected_stdout_pre_validators: typing.ClassVar[
            typing.List[TestCaseExpects.Validators.PreExpectedStdoutValidator]
        ] = []
        _expected_stdout_post_validators: typing.ClassVar[
            typing.List[TestCaseExpects.Validators.ExpectedStdoutValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[TestCaseExpects.Validators._RootValidator], TestCaseExpects.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [TestCaseExpects.Validators._PreRootValidator], TestCaseExpects.Validators._PreRootValidator
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
            cls, field_name: typing_extensions.Literal["expected_stdout"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [TestCaseExpects.Validators.PreExpectedStdoutValidator],
            TestCaseExpects.Validators.PreExpectedStdoutValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["expected_stdout"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [TestCaseExpects.Validators.ExpectedStdoutValidator], TestCaseExpects.Validators.ExpectedStdoutValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "expected_stdout":
                    if pre:
                        cls._expected_stdout_pre_validators.append(validator)
                    else:
                        cls._expected_stdout_post_validators.append(validator)
                return validator

            return decorator

        class PreExpectedStdoutValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: TestCaseExpects.Partial) -> typing.Any:
                ...

        class ExpectedStdoutValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Optional[str], __values: TestCaseExpects.Partial) -> typing.Optional[str]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: TestCaseExpects.Partial) -> TestCaseExpects.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: TestCaseExpects.Partial) -> TestCaseExpects.Partial:
        for validator in TestCaseExpects.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: TestCaseExpects.Partial) -> TestCaseExpects.Partial:
        for validator in TestCaseExpects.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("expected_stdout", pre=True)
    def _pre_validate_expected_stdout(
        cls, v: typing.Optional[str], values: TestCaseExpects.Partial
    ) -> typing.Optional[str]:
        for validator in TestCaseExpects.Validators._expected_stdout_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("expected_stdout", pre=False)
    def _post_validate_expected_stdout(
        cls, v: typing.Optional[str], values: TestCaseExpects.Partial
    ) -> typing.Optional[str]:
        for validator in TestCaseExpects.Validators._expected_stdout_post_validators:
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
