# Auto-generated at 2021-09-27T17:01:25.528273+08:00
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

from ...models import ModelWebLinkingResponse
from ...models import RestErrorResponse


class PublicWebLinkPlatform(Operation):
    """Create Public Web Linking (PublicWebLinkPlatform)

    Properties:
        url: /iam/v3/public/namespaces/{namespace}/users/me/platforms/{platformId}/web/link

        method: GET

        tags: Users

        consumes: []

        produces: ["application/json"]

        security: bearer

        namespace: (namespace) REQUIRED str in path

        platform_id: (platformId) REQUIRED str in path

        client_id: (clientId) OPTIONAL str in query

        redirect_uri: (redirectUri) OPTIONAL str in query

    Responses:
        200: OK - ModelWebLinkingResponse (OK)

        400: Bad Request - RestErrorResponse (errorCode: 20002 | errorMessage: validation error)

        401: Unauthorized - RestErrorResponse (errorCode: 20001 | errorMessage: unauthorized access)

        404: Not Found - RestErrorResponse (errorCode: 10365 | errorMessage: client not found)
    """

    # region fields

    _url: str = "/iam/v3/public/namespaces/{namespace}/users/me/platforms/{platformId}/web/link"
    _method: str = "GET"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    namespace: str                                                                                 # REQUIRED in [path]
    platform_id: str                                                                               # REQUIRED in [path]
    client_id: str                                                                                 # OPTIONAL in [query]
    redirect_uri: str                                                                              # OPTIONAL in [query]

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
        if hasattr(self, "platform_id"):
            result["platformId"] = self.platform_id
        return result

    def get_query_params(self) -> dict:
        result = {}
        if hasattr(self, "client_id"):
            result["clientId"] = self.client_id
        if hasattr(self, "redirect_uri"):
            result["redirectUri"] = self.redirect_uri
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

    def with_namespace(self, value: str) -> PublicWebLinkPlatform:
        self.namespace = value
        return self

    def with_platform_id(self, value: str) -> PublicWebLinkPlatform:
        self.platform_id = value
        return self

    def with_client_id(self, value: str) -> PublicWebLinkPlatform:
        self.client_id = value
        return self

    def with_redirect_uri(self, value: str) -> PublicWebLinkPlatform:
        self.redirect_uri = value
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
        if hasattr(self, "client_id") and self.client_id:
            result["clientId"] = str(self.client_id)
        elif include_empty:
            result["clientId"] = str()
        if hasattr(self, "redirect_uri") and self.redirect_uri:
            result["redirectUri"] = str(self.redirect_uri)
        elif include_empty:
            result["redirectUri"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, ModelWebLinkingResponse], Union[None, RestErrorResponse]]:
        """Parse the given response.

        200: OK - ModelWebLinkingResponse (OK)

        400: Bad Request - RestErrorResponse (errorCode: 20002 | errorMessage: validation error)

        401: Unauthorized - RestErrorResponse (errorCode: 20001 | errorMessage: unauthorized access)

        404: Not Found - RestErrorResponse (errorCode: 10365 | errorMessage: client not found)
        """
        if code == 200:
            return ModelWebLinkingResponse.create_from_dict(content), None
        if code == 400:
            return None, RestErrorResponse.create_from_dict(content)
        if code == 401:
            return None, RestErrorResponse.create_from_dict(content)
        if code == 404:
            return None, RestErrorResponse.create_from_dict(content)
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
        client_id: Optional[str] = None,
        redirect_uri: Optional[str] = None,
    ) -> PublicWebLinkPlatform:
        instance = cls()
        instance.namespace = namespace
        instance.platform_id = platform_id
        if client_id is not None:
            instance.client_id = client_id
        if redirect_uri is not None:
            instance.redirect_uri = redirect_uri
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> PublicWebLinkPlatform:
        instance = cls()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "platformId" in dict_ and dict_["platformId"] is not None:
            instance.platform_id = str(dict_["platformId"])
        elif include_empty:
            instance.platform_id = str()
        if "clientId" in dict_ and dict_["clientId"] is not None:
            instance.client_id = str(dict_["clientId"])
        elif include_empty:
            instance.client_id = str()
        if "redirectUri" in dict_ and dict_["redirectUri"] is not None:
            instance.redirect_uri = str(dict_["redirectUri"])
        elif include_empty:
            instance.redirect_uri = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "platformId": "platform_id",
            "clientId": "client_id",
            "redirectUri": "redirect_uri",
        }

    # endregion static methods
