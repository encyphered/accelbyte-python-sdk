# Auto-generated at 2021-09-27T17:01:24.540198+08:00
# from: Justice Iam Service (4.1.0)

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

from ...models import ModelGetAdminUsersResponse
from ...models import RestErrorResponse


class GetAdminUsersByRoleID(Operation):
    """Get Admin Users By RoleId (GetAdminUsersByRoleID)

    Properties:
        url: /iam/namespaces/{namespace}/users/admin

        method: GET

        tags: Users

        consumes: ["application/json"]

        produces: ["application/json"]

        security: bearer

        namespace: (namespace) REQUIRED str in path

        role_id: (roleId) OPTIONAL str in query

        limit: (limit) OPTIONAL int in query

        after: (after) OPTIONAL int in query

        before: (before) OPTIONAL int in query

    Responses:
        200: OK - ModelGetAdminUsersResponse (OK)

        400: Bad Request - RestErrorResponse (errorCode: 20021 | errorMessage: invalid pagination parameter)

        401: Unauthorized - (Unauthorized access)

        403: Forbidden - (Forbidden)

        404: Not Found - (Data not found)

        500: Internal Server Error - (errorCode: 20000 | errorMessage: internal server error)
    """

    # region fields

    _url: str = "/iam/namespaces/{namespace}/users/admin"
    _method: str = "GET"
    _consumes: List[str] = ["application/json"]
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    namespace: str                                                                                 # REQUIRED in [path]
    role_id: str                                                                                   # OPTIONAL in [query]
    limit: int                                                                                     # OPTIONAL in [query]
    after: int                                                                                     # OPTIONAL in [query]
    before: int                                                                                    # OPTIONAL in [query]

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
        if hasattr(self, "role_id"):
            result["roleId"] = self.role_id
        if hasattr(self, "limit"):
            result["limit"] = self.limit
        if hasattr(self, "after"):
            result["after"] = self.after
        if hasattr(self, "before"):
            result["before"] = self.before
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_namespace(self, value: str) -> GetAdminUsersByRoleID:
        self.namespace = value
        return self

    def with_role_id(self, value: str) -> GetAdminUsersByRoleID:
        self.role_id = value
        return self

    def with_limit(self, value: int) -> GetAdminUsersByRoleID:
        self.limit = value
        return self

    def with_after(self, value: int) -> GetAdminUsersByRoleID:
        self.after = value
        return self

    def with_before(self, value: int) -> GetAdminUsersByRoleID:
        self.before = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "role_id") and self.role_id:
            result["roleId"] = str(self.role_id)
        elif include_empty:
            result["roleId"] = str()
        if hasattr(self, "limit") and self.limit:
            result["limit"] = int(self.limit)
        elif include_empty:
            result["limit"] = int()
        if hasattr(self, "after") and self.after:
            result["after"] = int(self.after)
        elif include_empty:
            result["after"] = int()
        if hasattr(self, "before") and self.before:
            result["before"] = int(self.before)
        elif include_empty:
            result["before"] = int()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, ModelGetAdminUsersResponse], Union[None, HttpResponse, RestErrorResponse]]:
        """Parse the given response.

        200: OK - ModelGetAdminUsersResponse (OK)

        400: Bad Request - RestErrorResponse (errorCode: 20021 | errorMessage: invalid pagination parameter)

        401: Unauthorized - (Unauthorized access)

        403: Forbidden - (Forbidden)

        404: Not Found - (Data not found)

        500: Internal Server Error - (errorCode: 20000 | errorMessage: internal server error)
        """
        if code == 200:
            return ModelGetAdminUsersResponse.create_from_dict(content), None
        if code == 400:
            return None, RestErrorResponse.create_from_dict(content)
        if code == 401:
            return None, HttpResponse.create(code, "Unauthorized")
        if code == 403:
            return None, HttpResponse.create(code, "Forbidden")
        if code == 404:
            return None, HttpResponse.create(code, "Not Found")
        if code == 500:
            return None, HttpResponse.create(code, "Internal Server Error")
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
        role_id: Optional[str] = None,
        limit: Optional[int] = None,
        after: Optional[int] = None,
        before: Optional[int] = None,
    ) -> GetAdminUsersByRoleID:
        instance = cls()
        instance.namespace = namespace
        if role_id is not None:
            instance.role_id = role_id
        if limit is not None:
            instance.limit = limit
        if after is not None:
            instance.after = after
        if before is not None:
            instance.before = before
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> GetAdminUsersByRoleID:
        instance = cls()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "roleId" in dict_ and dict_["roleId"] is not None:
            instance.role_id = str(dict_["roleId"])
        elif include_empty:
            instance.role_id = str()
        if "limit" in dict_ and dict_["limit"] is not None:
            instance.limit = int(dict_["limit"])
        elif include_empty:
            instance.limit = int()
        if "after" in dict_ and dict_["after"] is not None:
            instance.after = int(dict_["after"])
        elif include_empty:
            instance.after = int()
        if "before" in dict_ and dict_["before"] is not None:
            instance.before = int(dict_["before"])
        elif include_empty:
            instance.before = int()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "roleId": "role_id",
            "limit": "limit",
            "after": "after",
            "before": "before",
        }

    # endregion static methods
