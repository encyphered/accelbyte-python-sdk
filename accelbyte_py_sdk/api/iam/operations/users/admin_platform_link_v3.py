# Auto-generated at 2021-09-27T17:01:25.220453+08:00
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


class AdminPlatformLinkV3(Operation):
    """Link user's account with platform (AdminPlatformLinkV3)

    Properties:
        url: /iam/v3/admin/namespaces/{namespace}/users/{userId}/platforms/{platformId}/link

        method: POST

        tags: Users

        consumes: ["application/x-www-form-urlencoded"]

        produces: ["application/json"]

        security: bearer

        ticket: (ticket) REQUIRED str in form_data

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

        platform_id: (platformId) REQUIRED str in path

    Responses:
        204: No Content - (Operation succeeded)

        400: Bad Request - (errorCode: 20019 | errorMessage: unable to parse request body)

        401: Unauthorized - (Unauthorized access)

        403: Forbidden - (Forbidden)

        404: Not Found - (errorCode: 20008 | errorMessage: user not found)

        409: Conflict - (errorCode: 10163 | errorMessage: platform is already linked with the user account)

        500: Internal Server Error - (errorCode: 20000 | errorMessage: internal server error)
    """

    # region fields

    _url: str = "/iam/v3/admin/namespaces/{namespace}/users/{userId}/platforms/{platformId}/link"
    _method: str = "POST"
    _consumes: List[str] = ["application/x-www-form-urlencoded"]
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    ticket: str                                                                                    # REQUIRED in [form_data]
    namespace: str                                                                                 # REQUIRED in [path]
    user_id: str                                                                                   # REQUIRED in [path]
    platform_id: str                                                                               # REQUIRED in [path]

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

        return result

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
            "ticket",
            "namespace",
            "user_id",
            "platform_id",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "form_data": self.get_form_data_params(),
            "path": self.get_path_params(),
        }

    def get_form_data_params(self) -> dict:
        result = {}
        if hasattr(self, "ticket"):
            result["ticket"] = self.ticket
        return result

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        if hasattr(self, "user_id"):
            result["userId"] = self.user_id
        if hasattr(self, "platform_id"):
            result["platformId"] = self.platform_id
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "ticket") or self.ticket is None:
            return False
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "user_id") or self.user_id is None:
            return False
        if not hasattr(self, "platform_id") or self.platform_id is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_ticket(self, value: str) -> AdminPlatformLinkV3:
        self.ticket = value
        return self

    def with_namespace(self, value: str) -> AdminPlatformLinkV3:
        self.namespace = value
        return self

    def with_user_id(self, value: str) -> AdminPlatformLinkV3:
        self.user_id = value
        return self

    def with_platform_id(self, value: str) -> AdminPlatformLinkV3:
        self.platform_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "ticket") and self.ticket:
            result["ticket"] = str(self.ticket)
        elif include_empty:
            result["ticket"] = str()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        if hasattr(self, "platform_id") and self.platform_id:
            result["platformId"] = str(self.platform_id)
        elif include_empty:
            result["platformId"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, HttpResponse], Union[None, HttpResponse]]:
        """Parse the given response.

        204: No Content - (Operation succeeded)

        400: Bad Request - (errorCode: 20019 | errorMessage: unable to parse request body)

        401: Unauthorized - (Unauthorized access)

        403: Forbidden - (Forbidden)

        404: Not Found - (errorCode: 20008 | errorMessage: user not found)

        409: Conflict - (errorCode: 10163 | errorMessage: platform is already linked with the user account)

        500: Internal Server Error - (errorCode: 20000 | errorMessage: internal server error)
        """
        if code == 204:
            return HttpResponse.create(code, "No Content"), None
        if code == 400:
            return None, HttpResponse.create(code, "Bad Request")
        if code == 401:
            return None, HttpResponse.create(code, "Unauthorized")
        if code == 403:
            return None, HttpResponse.create(code, "Forbidden")
        if code == 404:
            return None, HttpResponse.create(code, "Not Found")
        if code == 409:
            return None, HttpResponse.create(code, "Conflict")
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
        ticket: str,
        namespace: str,
        user_id: str,
        platform_id: str,
    ) -> AdminPlatformLinkV3:
        instance = cls()
        instance.ticket = ticket
        instance.namespace = namespace
        instance.user_id = user_id
        instance.platform_id = platform_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AdminPlatformLinkV3:
        instance = cls()
        if "ticket" in dict_ and dict_["ticket"] is not None:
            instance.ticket = str(dict_["ticket"])
        elif include_empty:
            instance.ticket = str()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        if "platformId" in dict_ and dict_["platformId"] is not None:
            instance.platform_id = str(dict_["platformId"])
        elif include_empty:
            instance.platform_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "ticket": "ticket",
            "namespace": "namespace",
            "userId": "user_id",
            "platformId": "platform_id",
        }

    # endregion static methods
