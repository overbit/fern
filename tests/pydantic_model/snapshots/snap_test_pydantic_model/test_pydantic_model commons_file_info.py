# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ..core.datetime_utils import serialize_datetime


class FileInfo(pydantic.BaseModel):
    filename: str
    contents: str

    class Partial(typing_extensions.TypedDict):
        filename: typing_extensions.NotRequired[str]
        contents: typing_extensions.NotRequired[str]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @FileInfo.Validators.root()
            def validate(values: FileInfo.Partial) -> FileInfo.Partial:
                ...

            @FileInfo.Validators.field("filename")
            def validate_filename(filename: str, values: FileInfo.Partial) -> str:
                ...

            @FileInfo.Validators.field("contents")
            def validate_contents(contents: str, values: FileInfo.Partial) -> str:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[FileInfo.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[FileInfo.Validators._RootValidator]] = []
        _filename_pre_validators: typing.ClassVar[typing.List[FileInfo.Validators.PreFilenameValidator]] = []
        _filename_post_validators: typing.ClassVar[typing.List[FileInfo.Validators.FilenameValidator]] = []
        _contents_pre_validators: typing.ClassVar[typing.List[FileInfo.Validators.PreContentsValidator]] = []
        _contents_post_validators: typing.ClassVar[typing.List[FileInfo.Validators.ContentsValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[FileInfo.Validators._RootValidator], FileInfo.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[FileInfo.Validators._PreRootValidator], FileInfo.Validators._PreRootValidator]:
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
            cls, field_name: typing_extensions.Literal["filename"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[FileInfo.Validators.PreFilenameValidator], FileInfo.Validators.PreFilenameValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["filename"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[FileInfo.Validators.FilenameValidator], FileInfo.Validators.FilenameValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["contents"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[FileInfo.Validators.PreContentsValidator], FileInfo.Validators.PreContentsValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["contents"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[FileInfo.Validators.ContentsValidator], FileInfo.Validators.ContentsValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "filename":
                    if pre:
                        cls._filename_pre_validators.append(validator)
                    else:
                        cls._filename_post_validators.append(validator)
                if field_name == "contents":
                    if pre:
                        cls._contents_pre_validators.append(validator)
                    else:
                        cls._contents_post_validators.append(validator)
                return validator

            return decorator

        class PreFilenameValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: FileInfo.Partial) -> typing.Any:
                ...

        class FilenameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: FileInfo.Partial) -> str:
                ...

        class PreContentsValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: FileInfo.Partial) -> typing.Any:
                ...

        class ContentsValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: FileInfo.Partial) -> str:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: FileInfo.Partial) -> FileInfo.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: FileInfo.Partial) -> FileInfo.Partial:
        for validator in FileInfo.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: FileInfo.Partial) -> FileInfo.Partial:
        for validator in FileInfo.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("filename", pre=True)
    def _pre_validate_filename(cls, v: str, values: FileInfo.Partial) -> str:
        for validator in FileInfo.Validators._filename_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("filename", pre=False)
    def _post_validate_filename(cls, v: str, values: FileInfo.Partial) -> str:
        for validator in FileInfo.Validators._filename_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("contents", pre=True)
    def _pre_validate_contents(cls, v: str, values: FileInfo.Partial) -> str:
        for validator in FileInfo.Validators._contents_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("contents", pre=False)
    def _post_validate_contents(cls, v: str, values: FileInfo.Partial) -> str:
        for validator in FileInfo.Validators._contents_post_validators:
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
        json_encoders = {dt.datetime: serialize_datetime}
