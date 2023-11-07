# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict
from pydantic import BaseModel, Field, constr
from finbourne_luminesce.models.query_designer_binary_operator import QueryDesignerBinaryOperator

class FilterTermDesign(BaseModel):
    """
    A single filter clause  # noqa: E501
    """
    operator: QueryDesignerBinaryOperator = Field(...)
    value: constr(strict=True, max_length=2048, min_length=0) = Field(..., description="The value to compare against (always as a string, but will be formatted to the correct type)")
    __properties = ["operator", "value"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> FilterTermDesign:
        """Create an instance of FilterTermDesign from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FilterTermDesign:
        """Create an instance of FilterTermDesign from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FilterTermDesign.parse_obj(obj)

        _obj = FilterTermDesign.parse_obj({
            "operator": obj.get("operator"),
            "value": obj.get("value")
        })
        return _obj
