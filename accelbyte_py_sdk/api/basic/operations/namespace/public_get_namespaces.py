# Auto-generated at 2021-09-27T17:01:31.778097+08:00
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
from ...models import NamespaceInfo


class PublicGetNamespaces(Operation):
    """Get all namespaces (publicGetNamespaces)

    Properties:
        url: /basic/v1/public/namespaces

        method: GET

        tags: Namespace

        consumes: []

        produces: ["application/json"]

        security: bearer

        active_only: (activeOnly) OPTIONAL bool in query

    Responses:
        200: OK - List[NamespaceInfo] (Successful operation)

        401: Unauthorized - ErrorEntity (errorCode: 20001 | errorMessage: unauthorized)
    """

    # region fields

    _url: str = "/basic/v1/public/namespaces"
    _method: str = "GET"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    active_only: bool                                                                              # OPTIONAL in [query]

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

        result += self.url

        # query params
        result += "?" + "&".join([f"{k}={v}" for k, v in self.get_query_params().items()])

        return result

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "query": self.get_query_params(),
        }

    def get_query_params(self) -> dict:
        result = {}
        if hasattr(self, "active_only"):
            result["activeOnly"] = self.active_only
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        return True

    # endregion is/has methods

    # region with_x methods

    def with_active_only(self, value: bool) -> PublicGetNamespaces:
        self.active_only = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "active_only") and self.active_only:
            result["activeOnly"] = bool(self.active_only)
        elif include_empty:
            result["activeOnly"] = bool()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, List[NamespaceInfo]], Union[None, ErrorEntity]]:
        """Parse the given response.

        200: OK - List[NamespaceInfo] (Successful operation)

        401: Unauthorized - ErrorEntity (errorCode: 20001 | errorMessage: unauthorized)
        """
        if code == 200:
            return [NamespaceInfo.create_from_dict(i) for i in content], None
        if code == 401:
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
        active_only: Optional[bool] = None,
    ) -> PublicGetNamespaces:
        instance = cls()
        if active_only is not None:
            instance.active_only = active_only
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> PublicGetNamespaces:
        instance = cls()
        if "activeOnly" in dict_ and dict_["activeOnly"] is not None:
            instance.active_only = bool(dict_["activeOnly"])
        elif include_empty:
            instance.active_only = bool()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "activeOnly": "active_only",
        }

    # endregion static methods
