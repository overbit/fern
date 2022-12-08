# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .node_id import NodeId


class DoublyLinkedListNodeValue(pydantic.BaseModel):
    node_id: NodeId = pydantic.Field(alias="nodeId")
    val: float
    next: typing.Optional[NodeId]
    prev: typing.Optional[NodeId]

    class Partial(typing_extensions.TypedDict):
        node_id: typing_extensions.NotRequired[NodeId]
        val: typing_extensions.NotRequired[float]
        next: typing_extensions.NotRequired[typing.Optional[NodeId]]
        prev: typing_extensions.NotRequired[typing.Optional[NodeId]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @DoublyLinkedListNodeValue.Validators.root
            def validate(values: DoublyLinkedListNodeValue.Partial) -> DoublyLinkedListNodeValue.Partial:
                ...

            @DoublyLinkedListNodeValue.Validators.field("node_id")
            def validate_node_id(node_id: NodeId, values: DoublyLinkedListNodeValue.Partial) -> NodeId:
                ...

            @DoublyLinkedListNodeValue.Validators.field("val")
            def validate_val(val: float, values: DoublyLinkedListNodeValue.Partial) -> float:
                ...

            @DoublyLinkedListNodeValue.Validators.field("next")
            def validate_next(next: typing.Optional[NodeId], values: DoublyLinkedListNodeValue.Partial) -> typing.Optional[NodeId]:
                ...

            @DoublyLinkedListNodeValue.Validators.field("prev")
            def validate_prev(prev: typing.Optional[NodeId], values: DoublyLinkedListNodeValue.Partial) -> typing.Optional[NodeId]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[DoublyLinkedListNodeValue.Validators._RootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[DoublyLinkedListNodeValue.Validators._RootValidator]] = []
        _node_id_pre_validators: typing.ClassVar[typing.List[DoublyLinkedListNodeValue.Validators.NodeIdValidator]] = []
        _node_id_post_validators: typing.ClassVar[
            typing.List[DoublyLinkedListNodeValue.Validators.NodeIdValidator]
        ] = []
        _val_pre_validators: typing.ClassVar[typing.List[DoublyLinkedListNodeValue.Validators.ValValidator]] = []
        _val_post_validators: typing.ClassVar[typing.List[DoublyLinkedListNodeValue.Validators.ValValidator]] = []
        _next_pre_validators: typing.ClassVar[typing.List[DoublyLinkedListNodeValue.Validators.NextValidator]] = []
        _next_post_validators: typing.ClassVar[typing.List[DoublyLinkedListNodeValue.Validators.NextValidator]] = []
        _prev_pre_validators: typing.ClassVar[typing.List[DoublyLinkedListNodeValue.Validators.PrevValidator]] = []
        _prev_post_validators: typing.ClassVar[typing.List[DoublyLinkedListNodeValue.Validators.PrevValidator]] = []

        @classmethod
        def root(cls, *, pre: bool = False) -> DoublyLinkedListNodeValue.Validators._RootValidator:
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
            cls, field_name: typing_extensions.Literal["node_id"], *, pre: bool = False
        ) -> typing.Callable[
            [DoublyLinkedListNodeValue.Validators.NodeIdValidator], DoublyLinkedListNodeValue.Validators.NodeIdValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["val"], *, pre: bool = False
        ) -> typing.Callable[
            [DoublyLinkedListNodeValue.Validators.ValValidator], DoublyLinkedListNodeValue.Validators.ValValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["next"], *, pre: bool = False
        ) -> typing.Callable[
            [DoublyLinkedListNodeValue.Validators.NextValidator], DoublyLinkedListNodeValue.Validators.NextValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["prev"], *, pre: bool = False
        ) -> typing.Callable[
            [DoublyLinkedListNodeValue.Validators.PrevValidator], DoublyLinkedListNodeValue.Validators.PrevValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "node_id":
                    if pre:
                        cls._node_id_pre_validators.append(validator)
                    else:
                        cls._node_id_post_validators.append(validator)
                if field_name == "val":
                    if pre:
                        cls._val_pre_validators.append(validator)
                    else:
                        cls._val_post_validators.append(validator)
                if field_name == "next":
                    if pre:
                        cls._next_pre_validators.append(validator)
                    else:
                        cls._next_post_validators.append(validator)
                if field_name == "prev":
                    if pre:
                        cls._prev_pre_validators.append(validator)
                    else:
                        cls._prev_post_validators.append(validator)
                return validator

            return decorator

        class NodeIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: NodeId, __values: DoublyLinkedListNodeValue.Partial) -> NodeId:
                ...

        class ValValidator(typing_extensions.Protocol):
            def __call__(self, __v: float, __values: DoublyLinkedListNodeValue.Partial) -> float:
                ...

        class NextValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[NodeId], __values: DoublyLinkedListNodeValue.Partial
            ) -> typing.Optional[NodeId]:
                ...

        class PrevValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[NodeId], __values: DoublyLinkedListNodeValue.Partial
            ) -> typing.Optional[NodeId]:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: DoublyLinkedListNodeValue.Partial) -> DoublyLinkedListNodeValue.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: DoublyLinkedListNodeValue.Partial) -> DoublyLinkedListNodeValue.Partial:
        for validator in DoublyLinkedListNodeValue.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: DoublyLinkedListNodeValue.Partial) -> DoublyLinkedListNodeValue.Partial:
        for validator in DoublyLinkedListNodeValue.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("node_id", pre=True)
    def _pre_validate_node_id(cls, v: NodeId, values: DoublyLinkedListNodeValue.Partial) -> NodeId:
        for validator in DoublyLinkedListNodeValue.Validators._node_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("node_id", pre=False)
    def _post_validate_node_id(cls, v: NodeId, values: DoublyLinkedListNodeValue.Partial) -> NodeId:
        for validator in DoublyLinkedListNodeValue.Validators._node_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("val", pre=True)
    def _pre_validate_val(cls, v: float, values: DoublyLinkedListNodeValue.Partial) -> float:
        for validator in DoublyLinkedListNodeValue.Validators._val_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("val", pre=False)
    def _post_validate_val(cls, v: float, values: DoublyLinkedListNodeValue.Partial) -> float:
        for validator in DoublyLinkedListNodeValue.Validators._val_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("next", pre=True)
    def _pre_validate_next(
        cls, v: typing.Optional[NodeId], values: DoublyLinkedListNodeValue.Partial
    ) -> typing.Optional[NodeId]:
        for validator in DoublyLinkedListNodeValue.Validators._next_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("next", pre=False)
    def _post_validate_next(
        cls, v: typing.Optional[NodeId], values: DoublyLinkedListNodeValue.Partial
    ) -> typing.Optional[NodeId]:
        for validator in DoublyLinkedListNodeValue.Validators._next_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("prev", pre=True)
    def _pre_validate_prev(
        cls, v: typing.Optional[NodeId], values: DoublyLinkedListNodeValue.Partial
    ) -> typing.Optional[NodeId]:
        for validator in DoublyLinkedListNodeValue.Validators._prev_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("prev", pre=False)
    def _post_validate_prev(
        cls, v: typing.Optional[NodeId], values: DoublyLinkedListNodeValue.Partial
    ) -> typing.Optional[NodeId]:
        for validator in DoublyLinkedListNodeValue.Validators._prev_post_validators:
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
