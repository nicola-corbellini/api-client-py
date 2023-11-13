# coding: utf-8

"""
    😸 Cheshire-Cat API

    Production ready AI assistant framework

    The version of the OpenAPI document: 1.3.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr
from cheshire_cat_api.models.location_inner import LocationInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ValidationError(BaseModel):
    """
    ValidationError
    """ # noqa: E501
    loc: List[LocationInner]
    msg: StrictStr
    type: StrictStr
    __properties: ClassVar[List[str]] = ["loc", "msg", "type"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ValidationError from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in loc (list)
        _items = []
        if self.loc:
            for _item in self.loc:
                if _item:
                    _items.append(_item.to_dict())
            _dict['loc'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ValidationError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "loc": [LocationInner.from_dict(_item) for _item in obj.get("loc")] if obj.get("loc") is not None else None,
            "msg": obj.get("msg"),
            "type": obj.get("type")
        })
        return _obj


