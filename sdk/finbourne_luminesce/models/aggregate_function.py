# coding: utf-8

"""
    FINBOURNE Luminesce Web API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class AggregateFunction(str, Enum):
    """
    Aggregation function type
    """

    """
    allowed enum values
    """
    COUNT = 'count'
    COUNT_DISTINCT = 'count_distinct'
    SUM = 'sum'
    TOTAL = 'total'
    AVG = 'avg'
    MIN = 'min'
    MAX = 'max'
    GROUP_CONCAT = 'group_concat'

    @classmethod
    def from_json(cls, json_str: str) -> AggregateFunction:
        """Create an instance of AggregateFunction from a JSON string"""
        return AggregateFunction(json.loads(json_str))
