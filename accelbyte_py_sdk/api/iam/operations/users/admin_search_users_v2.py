# Auto-generated at 2021-09-27T17:01:24.817666+08:00
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

from ...models import ModelSearchUsersByPlatformIDResponse


class AdminSearchUsersV2(Operation):
    """Search Users (AdminSearchUsersV2)

    Properties:
        url: /iam/v2/admin/namespaces/{namespace}/users

        method: GET

        tags: Users

        consumes: []

        produces: ["application/json"]

        security: bearer

        namespace: (namespace) REQUIRED str in path

        platform_id: (platformId) REQUIRED str in query

        role_id: (roleId) OPTIONAL str in query

        login_id: (loginId) OPTIONAL str in query

        user_id: (userId) OPTIONAL str in query

        platform_user_id: (platformUserId) OPTIONAL str in query

        display_name: (displayName) OPTIONAL str in query

        limit: (limit) OPTIONAL str in query

        before: (before) OPTIONAL str in query

        after: (after) OPTIONAL str in query

    Responses:
        200: OK - ModelSearchUsersByPlatformIDResponse (OK)

        400: Bad Request - (Invalid request)

        401: Unauthorized - (Unauthorized access)

        403: Forbidden - (Forbidden)
    """

    # region fields

    _url: str = "/iam/v2/admin/namespaces/{namespace}/users"
    _method: str = "GET"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    namespace: str                                                                                 # REQUIRED in [path]
    platform_id: str                                                                               # REQUIRED in [query]
    role_id: str                                                                                   # OPTIONAL in [query]
    login_id: str                                                                                  # OPTIONAL in [query]
    user_id: str                                                                                   # OPTIONAL in [query]
    platform_user_id: str                                                                          # OPTIONAL in [query]
    display_name: str                                                                              # OPTIONAL in [query]
    limit: str                                                                                     # OPTIONAL in [query]
    before: str                                                                                    # OPTIONAL in [query]
    after: str                                                                                     # OPTIONAL in [query]

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
            "platform_id",
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
        if hasattr(self, "platform_id"):
            result["platformId"] = self.platform_id
        if hasattr(self, "role_id"):
            result["roleId"] = self.role_id
        if hasattr(self, "login_id"):
            result["loginId"] = self.login_id
        if hasattr(self, "user_id"):
            result["userId"] = self.user_id
        if hasattr(self, "platform_user_id"):
            result["platformUserId"] = self.platform_user_id
        if hasattr(self, "display_name"):
            result["displayName"] = self.display_name
        if hasattr(self, "limit"):
            result["limit"] = self.limit
        if hasattr(self, "before"):
            result["before"] = self.before
        if hasattr(self, "after"):
            result["after"] = self.after
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "platform_id") or self.platform_id is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_namespace(self, value: str) -> AdminSearchUsersV2:
        self.namespace = value
        return self

    def with_platform_id(self, value: str) -> AdminSearchUsersV2:
        self.platform_id = value
        return self

    def with_role_id(self, value: str) -> AdminSearchUsersV2:
        self.role_id = value
        return self

    def with_login_id(self, value: str) -> AdminSearchUsersV2:
        self.login_id = value
        return self

    def with_user_id(self, value: str) -> AdminSearchUsersV2:
        self.user_id = value
        return self

    def with_platform_user_id(self, value: str) -> AdminSearchUsersV2:
        self.platform_user_id = value
        return self

    def with_display_name(self, value: str) -> AdminSearchUsersV2:
        self.display_name = value
        return self

    def with_limit(self, value: str) -> AdminSearchUsersV2:
        self.limit = value
        return self

    def with_before(self, value: str) -> AdminSearchUsersV2:
        self.before = value
        return self

    def with_after(self, value: str) -> AdminSearchUsersV2:
        self.after = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "platform_id") and self.platform_id:
            result["platformId"] = str(self.platform_id)
        elif include_empty:
            result["platformId"] = str()
        if hasattr(self, "role_id") and self.role_id:
            result["roleId"] = str(self.role_id)
        elif include_empty:
            result["roleId"] = str()
        if hasattr(self, "login_id") and self.login_id:
            result["loginId"] = str(self.login_id)
        elif include_empty:
            result["loginId"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        if hasattr(self, "platform_user_id") and self.platform_user_id:
            result["platformUserId"] = str(self.platform_user_id)
        elif include_empty:
            result["platformUserId"] = str()
        if hasattr(self, "display_name") and self.display_name:
            result["displayName"] = str(self.display_name)
        elif include_empty:
            result["displayName"] = str()
        if hasattr(self, "limit") and self.limit:
            result["limit"] = str(self.limit)
        elif include_empty:
            result["limit"] = str()
        if hasattr(self, "before") and self.before:
            result["before"] = str(self.before)
        elif include_empty:
            result["before"] = str()
        if hasattr(self, "after") and self.after:
            result["after"] = str(self.after)
        elif include_empty:
            result["after"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, ModelSearchUsersByPlatformIDResponse], Union[None, HttpResponse]]:
        """Parse the given response.

        200: OK - ModelSearchUsersByPlatformIDResponse (OK)

        400: Bad Request - (Invalid request)

        401: Unauthorized - (Unauthorized access)

        403: Forbidden - (Forbidden)
        """
        if code == 200:
            return ModelSearchUsersByPlatformIDResponse.create_from_dict(content), None
        if code == 400:
            return None, HttpResponse.create(code, "Bad Request")
        if code == 401:
            return None, HttpResponse.create(code, "Unauthorized")
        if code == 403:
            return None, HttpResponse.create(code, "Forbidden")
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
        platform_id: str,
        role_id: Optional[str] = None,
        login_id: Optional[str] = None,
        user_id: Optional[str] = None,
        platform_user_id: Optional[str] = None,
        display_name: Optional[str] = None,
        limit: Optional[str] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
    ) -> AdminSearchUsersV2:
        instance = cls()
        instance.namespace = namespace
        instance.platform_id = platform_id
        if role_id is not None:
            instance.role_id = role_id
        if login_id is not None:
            instance.login_id = login_id
        if user_id is not None:
            instance.user_id = user_id
        if platform_user_id is not None:
            instance.platform_user_id = platform_user_id
        if display_name is not None:
            instance.display_name = display_name
        if limit is not None:
            instance.limit = limit
        if before is not None:
            instance.before = before
        if after is not None:
            instance.after = after
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AdminSearchUsersV2:
        instance = cls()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "platformId" in dict_ and dict_["platformId"] is not None:
            instance.platform_id = str(dict_["platformId"])
        elif include_empty:
            instance.platform_id = str()
        if "roleId" in dict_ and dict_["roleId"] is not None:
            instance.role_id = str(dict_["roleId"])
        elif include_empty:
            instance.role_id = str()
        if "loginId" in dict_ and dict_["loginId"] is not None:
            instance.login_id = str(dict_["loginId"])
        elif include_empty:
            instance.login_id = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        if "platformUserId" in dict_ and dict_["platformUserId"] is not None:
            instance.platform_user_id = str(dict_["platformUserId"])
        elif include_empty:
            instance.platform_user_id = str()
        if "displayName" in dict_ and dict_["displayName"] is not None:
            instance.display_name = str(dict_["displayName"])
        elif include_empty:
            instance.display_name = str()
        if "limit" in dict_ and dict_["limit"] is not None:
            instance.limit = str(dict_["limit"])
        elif include_empty:
            instance.limit = str()
        if "before" in dict_ and dict_["before"] is not None:
            instance.before = str(dict_["before"])
        elif include_empty:
            instance.before = str()
        if "after" in dict_ and dict_["after"] is not None:
            instance.after = str(dict_["after"])
        elif include_empty:
            instance.after = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "platformId": "platform_id",
            "roleId": "role_id",
            "loginId": "login_id",
            "userId": "user_id",
            "platformUserId": "platform_user_id",
            "displayName": "display_name",
            "limit": "limit",
            "before": "before",
            "after": "after",
        }

    # endregion static methods
