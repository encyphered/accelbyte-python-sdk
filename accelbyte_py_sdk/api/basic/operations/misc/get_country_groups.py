# Auto-generated at 2021-09-27T17:01:31.720321+08:00
# from: Justice Basic Service (1.17.0)

# Copyright (c) 2018 - 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

# pylint: disable=duplicate-code
# pylint: disable=line-too-long
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-branches
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=too-many-public-methods
# pylint: disable=too-many-return-statements
# pylint: disable=too-many-statements
# pylint: disable=unused-import

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Union

from .....core import Operation
from .....core import HttpResponse

from ...models import ErrorEntity
from ...models import RetrieveCountryGroupResponse
from ...models import ValidationErrorEntity


class GetCountryGroups(Operation):
    """List country groups (getCountryGroups)

    Properties:
        url: /basic/v1/admin/namespaces/{namespace}/misc/countrygroups

        method: GET

        tags: Misc

        consumes: []

        produces: ["application/json"]

        security: bearer

        namespace: (namespace) REQUIRED str in path

        group_code: (groupCode) OPTIONAL str in query

    Responses:
        200: OK - List[RetrieveCountryGroupResponse] (successful operation)

        400: Bad Request - ValidationErrorEntity (errorCode: 20002 | errorMessage: validation error)

        401: Unauthorized - ErrorEntity (errorCode: 20001 | errorMessage: unauthorized)

        403: Forbidden - ErrorEntity (errorCode: 20013 | errorMessage: insufficient permission)

        404: Not Found - ErrorEntity (errorCode: 11233 | errorMessage: country group not found)
    """

    # region fields

    _url: str = "/basic/v1/admin/namespaces/{namespace}/misc/countrygroups"
    _method: str = "GET"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    namespace: str                                                                                 # REQUIRED in [path]
    group_code: str                                                                                # OPTIONAL in [query]

    # endregion fields

    # region properties

    @property
    def url(self) -> str:
        return self._url

    @property
    def method(self) -> str:
        return self._method

    @property
    def consumes(self) -> List[str]:
        return self._consumes

    @property
    def produces(self) -> List[str]:
        return self._produces

    @property
    def security(self) -> Optional[str]:
        return self._security

    @property
    def location_query(self) -> str:
        return self._location_query

    # endregion properties

    # region get methods

    def get_full_url(self, base_url: Union[None, str] = None) -> str:
        result = base_url if base_url is not None else ""

        # path params
        url = self.url
        for k, v in self.get_path_params().items():
            url = url.replace(f"{{{k}}}", v)
        result += url

        # query params
        result += "?" + "&".join([f"{k}={v}" for k, v in self.get_query_params().items()])

        return result

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
            "namespace",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "path": self.get_path_params(),
            "query": self.get_query_params(),
        }

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        return result

    def get_query_params(self) -> dict:
        result = {}
        if hasattr(self, "group_code"):
            result["groupCode"] = self.group_code
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_namespace(self, value: str) -> GetCountryGroups:
        self.namespace = value
        return self

    def with_group_code(self, value: str) -> GetCountryGroups:
        self.group_code = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "group_code") and self.group_code:
            result["groupCode"] = str(self.group_code)
        elif include_empty:
            result["groupCode"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, List[RetrieveCountryGroupResponse]], Union[None, ErrorEntity, ValidationErrorEntity]]:
        """Parse the given response.

        200: OK - List[RetrieveCountryGroupResponse] (successful operation)

        400: Bad Request - ValidationErrorEntity (errorCode: 20002 | errorMessage: validation error)

        401: Unauthorized - ErrorEntity (errorCode: 20001 | errorMessage: unauthorized)

        403: Forbidden - ErrorEntity (errorCode: 20013 | errorMessage: insufficient permission)

        404: Not Found - ErrorEntity (errorCode: 11233 | errorMessage: country group not found)
        """
        if code == 200:
            return [RetrieveCountryGroupResponse.create_from_dict(i) for i in content], None
        if code == 400:
            return None, ValidationErrorEntity.create_from_dict(content)
        if code == 401:
            return None, ErrorEntity.create_from_dict(content)
        if code == 403:
            return None, ErrorEntity.create_from_dict(content)
        if code == 404:
            return None, ErrorEntity.create_from_dict(content)
        was_handled, undocumented_response = HttpResponse.try_create_undocumented_response(code, content)
        if was_handled:
            return None, undocumented_response
        return None, HttpResponse.create_unhandled_error()

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        namespace: str,
        group_code: Optional[str] = None,
    ) -> GetCountryGroups:
        instance = cls()
        instance.namespace = namespace
        if group_code is not None:
            instance.group_code = group_code
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> GetCountryGroups:
        instance = cls()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "groupCode" in dict_ and dict_["groupCode"] is not None:
            instance.group_code = str(dict_["groupCode"])
        elif include_empty:
            instance.group_code = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "groupCode": "group_code",
        }

    # endregion static methods
