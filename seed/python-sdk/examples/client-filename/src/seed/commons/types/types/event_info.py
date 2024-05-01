# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import pydantic_v1
from .tag import Tag


class EventInfo_Metadata(pydantic_v1.BaseModel):
    """
    Examples
    --------
    from seed.commons import EventInfo_Metadata

    EventInfo_Metadata(
        id="metadata-alskjfg8",
        data={"one": "two"},
        json_string='{"one": "two"}',
    )
    """

    id: str
    data: typing.Optional[typing.Dict[str, str]] = None
    json_string: typing.Optional[str] = pydantic_v1.Field(alias="jsonString", default=None)
    type: typing.Literal["metadata"] = "metadata"

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}


class EventInfo_Tag(pydantic_v1.BaseModel):
    value: Tag
    type: typing.Literal["tag"] = "tag"

    class Config:
        frozen = True
        smart_union = True


"""
from seed.commons import EventInfo_Metadata

EventInfo_Metadata(
    id="metadata-alskjfg8",
    data={"one": "two"},
    json_string='{"one": "two"}',
)
"""
EventInfo = typing.Union[EventInfo_Metadata, EventInfo_Tag]
