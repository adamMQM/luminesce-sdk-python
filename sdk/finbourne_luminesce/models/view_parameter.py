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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, constr
from finbourne_luminesce.models.data_type import DataType

class ViewParameter(BaseModel):
    """
    Parameters of view  # noqa: E501
    """
    name: constr(strict=True, max_length=256, min_length=0) = Field(..., description="Name of the provider")
    data_type: DataType = Field(..., alias="dataType")
    value: constr(strict=True, max_length=256, min_length=0) = Field(..., description="Value of the provider")
    is_table_data_mandatory: Optional[StrictBool] = Field(None, alias="isTableDataMandatory", description="Should this be selected? False would imply it is only being filtered on.  Ignored when Aggregations are present")
    description: Optional[constr(strict=True, max_length=256, min_length=0)] = Field(None, description="Description of the parameter")
    __properties = ["name", "dataType", "value", "isTableDataMandatory", "description"]

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
    def from_json(cls, json_str: str) -> ViewParameter:
        """Create an instance of ViewParameter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ViewParameter:
        """Create an instance of ViewParameter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ViewParameter.parse_obj(obj)

        _obj = ViewParameter.parse_obj({
            "name": obj.get("name"),
            "data_type": obj.get("dataType"),
            "value": obj.get("value"),
            "is_table_data_mandatory": obj.get("isTableDataMandatory"),
            "description": obj.get("description")
        })
        return _obj
