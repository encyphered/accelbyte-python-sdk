# Auto-generated at 2021-09-21T14:10:35.155567+08:00
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

from ...models import RestapiErrorResponse


class AdminDeleteClientPermissionV3(Operation):
    """Delete Client Permission (AdminDeleteClientPermissionV3)

    Properties:
        url: /iam/v3/admin/namespaces/{namespace}/clients/{clientId}/permissions/{resource}/{action}

        method: DELETE

        tags: Clients

        consumes: []

        produces: ["application/json"]

        security: bearer

        namespace: (namespace) REQUIRED str in path

        client_id: (clientId) REQUIRED str in path

        resource: (resource) REQUIRED str in path

        action: (action) REQUIRED int in path

    Responses:
        204: No Content - (Operation succeeded)

        400: Bad Request - RestapiErrorResponse (errorCode: 20002 | errorMessage: validation error)

        401: Unauthorized - RestapiErrorResponse (errorCode: 20001 | errorMessage: unauthorized access)

        403: Forbidden - RestapiErrorResponse (errorCode: 20013 | errorMessage: insufficient permissions)

        404: Not Found - RestapiErrorResponse (errorCode: 10365 | errorMessage: client not found)
    """

    # region fields

    _url: str = "/iam/v3/admin/namespaces/{namespace}/clients/{clientId}/permissions/{resource}/{action}"
    _method: str = "DELETE"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    namespace: str                                                                                 # REQUIRED in [path]
    client_id: str                                                                                 # REQUIRED in [path]
    resource: str                                                                                  # REQUIRED in [path]
    action: int                                                                                    # REQUIRED in [path]

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
            "client_id",
            "resource",
            "action",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "path": self.get_path_params(),
        }

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        if hasattr(self, "client_id"):
            result["clientId"] = self.client_id
        if hasattr(self, "resource"):
            result["resource"] = self.resource
        if hasattr(self, "action"):
            result["action"] = self.action
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "client_id") or self.client_id is None:
            return False
        if not hasattr(self, "resource") or self.resource is None:
            return False
        if not hasattr(self, "action") or self.action is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_namespace(self, value: str) -> AdminDeleteClientPermissionV3:
        self.namespace = value
        return self

    def with_client_id(self, value: str) -> AdminDeleteClientPermissionV3:
        self.client_id = value
        return self

    def with_resource(self, value: str) -> AdminDeleteClientPermissionV3:
        self.resource = value
        return self

    def with_action(self, value: int) -> AdminDeleteClientPermissionV3:
        self.action = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "client_id") and self.client_id:
            result["clientId"] = str(self.client_id)
        elif include_empty:
            result["clientId"] = str()
        if hasattr(self, "resource") and self.resource:
            result["resource"] = str(self.resource)
        elif include_empty:
            result["resource"] = str()
        if hasattr(self, "action") and self.action:
            result["action"] = int(self.action)
        elif include_empty:
            result["action"] = int()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, HttpResponse], Union[None, RestapiErrorResponse]]:
        """Parse the given response.

        204: No Content - (Operation succeeded)

        400: Bad Request - RestapiErrorResponse (errorCode: 20002 | errorMessage: validation error)

        401: Unauthorized - RestapiErrorResponse (errorCode: 20001 | errorMessage: unauthorized access)

        403: Forbidden - RestapiErrorResponse (errorCode: 20013 | errorMessage: insufficient permissions)

        404: Not Found - RestapiErrorResponse (errorCode: 10365 | errorMessage: client not found)
        """
        if code == 204:
            return HttpResponse.create(code, "No Content"), None
        if code == 400:
            return None, RestapiErrorResponse.create_from_dict(content)
        if code == 401:
            return None, RestapiErrorResponse.create_from_dict(content)
        if code == 403:
            return None, RestapiErrorResponse.create_from_dict(content)
        if code == 404:
            return None, RestapiErrorResponse.create_from_dict(content)
        return None, HttpResponse.create_unhandled_error()

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        namespace: str,
        client_id: str,
        resource: str,
        action: int,
    ) -> AdminDeleteClientPermissionV3:
        instance = cls()
        instance.namespace = namespace
        instance.client_id = client_id
        instance.resource = resource
        instance.action = action
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AdminDeleteClientPermissionV3:
        instance = cls()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "clientId" in dict_ and dict_["clientId"] is not None:
            instance.client_id = str(dict_["clientId"])
        elif include_empty:
            instance.client_id = str()
        if "resource" in dict_ and dict_["resource"] is not None:
            instance.resource = str(dict_["resource"])
        elif include_empty:
            instance.resource = str()
        if "action" in dict_ and dict_["action"] is not None:
            instance.action = int(dict_["action"])
        elif include_empty:
            instance.action = int()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "clientId": "client_id",
            "resource": "resource",
            "action": "action",
        }

    # endregion static methods