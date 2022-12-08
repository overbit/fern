# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .submission_id import SubmissionId


class SubmissionIdNotFound(pydantic.BaseModel):
    missing_submission_id: SubmissionId = pydantic.Field(alias="missingSubmissionId")

    class Partial(typing_extensions.TypedDict):
        missing_submission_id: typing_extensions.NotRequired[SubmissionId]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @SubmissionIdNotFound.Validators.root
            def validate(values: SubmissionIdNotFound.Partial) -> SubmissionIdNotFound.Partial:
                ...

            @SubmissionIdNotFound.Validators.field("missing_submission_id")
            def validate_missing_submission_id(missing_submission_id: SubmissionId, values: SubmissionIdNotFound.Partial) -> SubmissionId:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[SubmissionIdNotFound.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[SubmissionIdNotFound.Validators._RootValidator]] = []
        _missing_submission_id_pre_validators: typing.ClassVar[
            typing.List[SubmissionIdNotFound.Validators.MissingSubmissionIdValidator]
        ] = []
        _missing_submission_id_post_validators: typing.ClassVar[
            typing.List[SubmissionIdNotFound.Validators.MissingSubmissionIdValidator]
        ] = []

        @classmethod
        def root(cls, *, pre: bool = False) -> SubmissionIdNotFound.Validators._RootValidator:
            def decorator(validator: typing.Any) -> typing.Any:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload  # type: ignore
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["missing_submission_id"], *, pre: bool = False
        ) -> typing.Callable[
            [SubmissionIdNotFound.Validators.MissingSubmissionIdValidator],
            SubmissionIdNotFound.Validators.MissingSubmissionIdValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "missing_submission_id":
                    if pre:
                        cls._missing_submission_id_pre_validators.append(validator)
                    else:
                        cls._missing_submission_id_post_validators.append(validator)
                return validator

            return decorator

        class MissingSubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: SubmissionId, __values: SubmissionIdNotFound.Partial) -> SubmissionId:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: SubmissionIdNotFound.Partial) -> SubmissionIdNotFound.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: SubmissionIdNotFound.Partial) -> SubmissionIdNotFound.Partial:
        for validator in SubmissionIdNotFound.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: SubmissionIdNotFound.Partial) -> SubmissionIdNotFound.Partial:
        for validator in SubmissionIdNotFound.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("missing_submission_id", pre=True)
    def _pre_validate_missing_submission_id(cls, v: SubmissionId, values: SubmissionIdNotFound.Partial) -> SubmissionId:
        for validator in SubmissionIdNotFound.Validators._missing_submission_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("missing_submission_id", pre=False)
    def _post_validate_missing_submission_id(
        cls, v: SubmissionId, values: SubmissionIdNotFound.Partial
    ) -> SubmissionId:
        for validator in SubmissionIdNotFound.Validators._missing_submission_id_post_validators:
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
