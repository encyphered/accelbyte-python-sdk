# Auto-generated at 2021-09-27T17:01:24.728407+08:00
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

from ...models import OauthmodelErrorResponse
from ...models import OauthmodelTokenResponse


class PlatformTokenRequestHandler(Operation):
    """OAuth2 access token generation specific to platform (PlatformTokenRequestHandler)

    Properties:
        url: /iam/oauth/namespaces/{namespace}/platforms/{platformId}/token

        method: POST

        tags: OAuth

        consumes: ["application/x-www-form-urlencoded"]

        produces: ["application/json"]

        security: bearer

        platform_token: (platform_token) OPTIONAL str in form_data

        device_id: (device_id) OPTIONAL str in form_data

        namespace: (namespace) REQUIRED str in path

        platform_id: (platformId) REQUIRED str in path

    Responses:
        200: OK - OauthmodelTokenResponse (Access Token returned)

        400: Bad Request - OauthmodelErrorResponse (General request error)

        401: Unauthorized - OauthmodelErrorResponse (Client authentication failed)
    """

    # region fields

    _url: str = "/iam/oauth/namespaces/{namespace}/platforms/{platformId}/token"
    _method: str = "POST"
    _consumes: List[str] = ["application/x-www-form-urlencoded"]
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    platform_token: str                                                                            # OPTIONAL in [form_data]
    device_id: str                                                                                 # OPTIONAL in [form_data]
    namespace: str                                                                                 # REQUIRED in [path]
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
            "namespace",
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
        if hasattr(self, "platform_token"):
            result["platform_token"] = self.platform_token
        if hasattr(self, "device_id"):
            result["device_id"] = self.device_id
        return result

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        if hasattr(self, "platform_id"):
            result["platformId"] = self.platform_id
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

    def with_platform_token(self, value: str) -> PlatformTokenRequestHandler:
        self.platform_token = value
        return self

    def with_device_id(self, value: str) -> PlatformTokenRequestHandler:
        self.device_id = value
        return self

    def with_namespace(self, value: str) -> PlatformTokenRequestHandler:
        self.namespace = value
        return self

    def with_platform_id(self, value: str) -> PlatformTokenRequestHandler:
        self.platform_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "platform_token") and self.platform_token:
            result["platform_token"] = str(self.platform_token)
        elif include_empty:
            result["platform_token"] = str()
        if hasattr(self, "device_id") and self.device_id:
            result["device_id"] = str(self.device_id)
        elif include_empty:
            result["device_id"] = str()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "platform_id") and self.platform_id:
            result["platformId"] = str(self.platform_id)
        elif include_empty:
            result["platformId"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, OauthmodelTokenResponse], Union[None, OauthmodelErrorResponse]]:
        """Parse the given response.

        200: OK - OauthmodelTokenResponse (Access Token returned)

        400: Bad Request - OauthmodelErrorResponse (General request error)

        401: Unauthorized - OauthmodelErrorResponse (Client authentication failed)
        """
        if code == 200:
            return OauthmodelTokenResponse.create_from_dict(content), None
        if code == 400:
            return None, OauthmodelErrorResponse.create_from_dict(content)
        if code == 401:
            return None, OauthmodelErrorResponse.create_from_dict(content)
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
        platform_token: Optional[str] = None,
        device_id: Optional[str] = None,
    ) -> PlatformTokenRequestHandler:
        instance = cls()
        instance.namespace = namespace
        instance.platform_id = platform_id
        if platform_token is not None:
            instance.platform_token = platform_token
        if device_id is not None:
            instance.device_id = device_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> PlatformTokenRequestHandler:
        instance = cls()
        if "platform_token" in dict_ and dict_["platform_token"] is not None:
            instance.platform_token = str(dict_["platform_token"])
        elif include_empty:
            instance.platform_token = str()
        if "device_id" in dict_ and dict_["device_id"] is not None:
            instance.device_id = str(dict_["device_id"])
        elif include_empty:
            instance.device_id = str()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "platformId" in dict_ and dict_["platformId"] is not None:
            instance.platform_id = str(dict_["platformId"])
        elif include_empty:
            instance.platform_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "platform_token": "platform_token",
            "device_id": "device_id",
            "namespace": "namespace",
            "platformId": "platform_id",
        }

    # endregion static methods
