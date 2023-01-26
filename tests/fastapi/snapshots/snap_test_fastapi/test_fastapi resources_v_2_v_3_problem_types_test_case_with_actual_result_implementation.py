# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ......core.datetime_utils import serialize_datetime
from .assert_correctness_check import AssertCorrectnessCheck
from .non_void_function_definition import NonVoidFunctionDefinition


class TestCaseWithActualResultImplementation(pydantic.BaseModel):
    get_actual_result: NonVoidFunctionDefinition = pydantic.Field(alias="getActualResult")
    assert_correctness_check: AssertCorrectnessCheck = pydantic.Field(alias="assertCorrectnessCheck")

    class Partial(typing_extensions.TypedDict):
        get_actual_result: typing_extensions.NotRequired[NonVoidFunctionDefinition]
        assert_correctness_check: typing_extensions.NotRequired[AssertCorrectnessCheck]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @TestCaseWithActualResultImplementation.Validators.root()
            def validate(values: TestCaseWithActualResultImplementation.Partial) -> TestCaseWithActualResultImplementation.Partial:
                ...

            @TestCaseWithActualResultImplementation.Validators.field("get_actual_result")
            def validate_get_actual_result(get_actual_result: NonVoidFunctionDefinition, values: TestCaseWithActualResultImplementation.Partial) -> NonVoidFunctionDefinition:
                ...

            @TestCaseWithActualResultImplementation.Validators.field("assert_correctness_check")
            def validate_assert_correctness_check(assert_correctness_check: AssertCorrectnessCheck, values: TestCaseWithActualResultImplementation.Partial) -> AssertCorrectnessCheck:
                ...
        """

        _pre_validators: typing.ClassVar[
            typing.List[TestCaseWithActualResultImplementation.Validators._PreRootValidator]
        ] = []
        _post_validators: typing.ClassVar[
            typing.List[TestCaseWithActualResultImplementation.Validators._RootValidator]
        ] = []
        _get_actual_result_pre_validators: typing.ClassVar[
            typing.List[TestCaseWithActualResultImplementation.Validators.PreGetActualResultValidator]
        ] = []
        _get_actual_result_post_validators: typing.ClassVar[
            typing.List[TestCaseWithActualResultImplementation.Validators.GetActualResultValidator]
        ] = []
        _assert_correctness_check_pre_validators: typing.ClassVar[
            typing.List[TestCaseWithActualResultImplementation.Validators.PreAssertCorrectnessCheckValidator]
        ] = []
        _assert_correctness_check_post_validators: typing.ClassVar[
            typing.List[TestCaseWithActualResultImplementation.Validators.AssertCorrectnessCheckValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [TestCaseWithActualResultImplementation.Validators._RootValidator],
            TestCaseWithActualResultImplementation.Validators._RootValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [TestCaseWithActualResultImplementation.Validators._PreRootValidator],
            TestCaseWithActualResultImplementation.Validators._PreRootValidator,
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
            cls, field_name: typing_extensions.Literal["get_actual_result"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [TestCaseWithActualResultImplementation.Validators.PreGetActualResultValidator],
            TestCaseWithActualResultImplementation.Validators.PreGetActualResultValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["get_actual_result"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [TestCaseWithActualResultImplementation.Validators.GetActualResultValidator],
            TestCaseWithActualResultImplementation.Validators.GetActualResultValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["assert_correctness_check"],
            *,
            pre: typing_extensions.Literal[True],
        ) -> typing.Callable[
            [TestCaseWithActualResultImplementation.Validators.PreAssertCorrectnessCheckValidator],
            TestCaseWithActualResultImplementation.Validators.PreAssertCorrectnessCheckValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["assert_correctness_check"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [TestCaseWithActualResultImplementation.Validators.AssertCorrectnessCheckValidator],
            TestCaseWithActualResultImplementation.Validators.AssertCorrectnessCheckValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "get_actual_result":
                    if pre:
                        cls._get_actual_result_pre_validators.append(validator)
                    else:
                        cls._get_actual_result_post_validators.append(validator)
                if field_name == "assert_correctness_check":
                    if pre:
                        cls._assert_correctness_check_pre_validators.append(validator)
                    else:
                        cls._assert_correctness_check_post_validators.append(validator)
                return validator

            return decorator

        class PreGetActualResultValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: TestCaseWithActualResultImplementation.Partial) -> typing.Any:
                ...

        class GetActualResultValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: NonVoidFunctionDefinition, __values: TestCaseWithActualResultImplementation.Partial
            ) -> NonVoidFunctionDefinition:
                ...

        class PreAssertCorrectnessCheckValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: TestCaseWithActualResultImplementation.Partial) -> typing.Any:
                ...

        class AssertCorrectnessCheckValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: AssertCorrectnessCheck, __values: TestCaseWithActualResultImplementation.Partial
            ) -> AssertCorrectnessCheck:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(
                self, __values: TestCaseWithActualResultImplementation.Partial
            ) -> TestCaseWithActualResultImplementation.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(
        cls, values: TestCaseWithActualResultImplementation.Partial
    ) -> TestCaseWithActualResultImplementation.Partial:
        for validator in TestCaseWithActualResultImplementation.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(
        cls, values: TestCaseWithActualResultImplementation.Partial
    ) -> TestCaseWithActualResultImplementation.Partial:
        for validator in TestCaseWithActualResultImplementation.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("get_actual_result", pre=True)
    def _pre_validate_get_actual_result(
        cls, v: NonVoidFunctionDefinition, values: TestCaseWithActualResultImplementation.Partial
    ) -> NonVoidFunctionDefinition:
        for validator in TestCaseWithActualResultImplementation.Validators._get_actual_result_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("get_actual_result", pre=False)
    def _post_validate_get_actual_result(
        cls, v: NonVoidFunctionDefinition, values: TestCaseWithActualResultImplementation.Partial
    ) -> NonVoidFunctionDefinition:
        for validator in TestCaseWithActualResultImplementation.Validators._get_actual_result_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("assert_correctness_check", pre=True)
    def _pre_validate_assert_correctness_check(
        cls, v: AssertCorrectnessCheck, values: TestCaseWithActualResultImplementation.Partial
    ) -> AssertCorrectnessCheck:
        for validator in TestCaseWithActualResultImplementation.Validators._assert_correctness_check_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("assert_correctness_check", pre=False)
    def _post_validate_assert_correctness_check(
        cls, v: AssertCorrectnessCheck, values: TestCaseWithActualResultImplementation.Partial
    ) -> AssertCorrectnessCheck:
        for validator in TestCaseWithActualResultImplementation.Validators._assert_correctness_check_post_validators:
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
