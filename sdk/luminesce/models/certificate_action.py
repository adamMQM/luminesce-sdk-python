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





class CertificateAction(str, Enum):
    """
    The action to take with a certificate
    """

    """
    allowed enum values
    """
    CREATE = 'Create'
    CREATEANDALLOWMULTIPLEWHICHAREVALID = 'CreateAndAllowMultipleWhichAreValid'
    RENEW = 'Renew'
    REVOKE = 'Revoke'

    @classmethod
    def from_json(cls, json_str: str) -> CertificateAction:
        """Create an instance of CertificateAction from a JSON string"""
        return CertificateAction(json.loads(json_str))
