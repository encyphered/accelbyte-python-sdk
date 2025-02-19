# Auto-generated at 2021-09-27T17:01:25.069062+08:00
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

from ...models import ModelInviteAdminRequestV3
from ...models import ModelInviteAdminResponseV3
from ...models import RestErrorResponse


class AdminInviteUserV3(Operation):
    """Invite User Admin (AdminInviteUserV3)

    Properties:
        url: /iam/v3/admin/namespaces/{namespace}/users/invite

        method: POST

        tags: Users

        consumes: []

        produces: ["application/json"]

        security: bearer

        body: (body) REQUIRED ModelInviteAdminRequestV3 in body

        namespace: (namespace) REQUIRED str in path

    Responses:
        201: Created - ModelInviteAdminResponseV3 (Created)

        400: Bad Request - RestErrorResponse (errorCode: 20019 | errorMessage: unable to parse request body)

        404: Not Found - RestErrorResponse (errorCode: 10154 | errorMessage: country not found)

        409: Conflict - RestErrorResponse (errorCode: 10133 | errorMessage: email already used)

        422: Unprocessable Entity - RestErrorResponse (errorCode: 10183 | errorMessage: validation error)

        500: Internal Server Error - RestErrorResponse (errorCode: 20000 | errorMessage: internal server error)
    """

    # region fields

    _url: str = "/iam/v3/admin/namespaces/{namespace}/users/invite"
    _method: str = "POST"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    body: ModelInviteAdminRequestV3                                                                # REQUIRED in [body]
    namespace: str                                                                                 # REQUIRED in [path]

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
            "body",
            "namespace",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "body": self.get_body_params(),
            "path": self.get_path_params(),
        }

    def get_body_params(self) -> Any:
        return self.body.to_dict()

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "body") or self.body is None:
            return False
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_body(self, value: ModelInviteAdminRequestV3) -> AdminInviteUserV3:
        self.body = value
        return self

    def with_namespace(self, value: str) -> AdminInviteUserV3:
        self.namespace = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "body") and self.body:
            result["body"] = self.body.to_dict(include_empty=include_empty)
        elif include_empty:
            result["body"] = ModelInviteAdminRequestV3()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, ModelInviteAdminResponseV3], Union[None, RestErrorResponse]]:
        """Parse the given response.

        201: Created - ModelInviteAdminResponseV3 (Created)

        400: Bad Request - RestErrorResponse (errorCode: 20019 | errorMessage: unable to parse request body)

        404: Not Found - RestErrorResponse (errorCode: 10154 | errorMessage: country not found)

        409: Conflict - RestErrorResponse (errorCode: 10133 | errorMessage: email already used)

        422: Unprocessable Entity - RestErrorResponse (errorCode: 10183 | errorMessage: validation error)

        500: Internal Server Error - RestErrorResponse (errorCode: 20000 | errorMessage: internal server error)
        """
        if code == 201:
            return ModelInviteAdminResponseV3.create_from_dict(content), None
        if code == 400:
            return None, RestErrorResponse.create_from_dict(content)
        if code == 404:
            return None, RestErrorResponse.create_from_dict(content)
        if code == 409:
            return None, RestErrorResponse.create_from_dict(content)
        if code == 422:
            return None, RestErrorResponse.create_from_dict(content)
        if code == 500:
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
        body: ModelInviteAdminRequestV3,
        namespace: str,
    ) -> AdminInviteUserV3:
        instance = cls()
        instance.body = body
        instance.namespace = namespace
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AdminInviteUserV3:
        instance = cls()
        if "body" in dict_ and dict_["body"] is not None:
            instance.body = ModelInviteAdminRequestV3.create_from_dict(dict_["body"], include_empty=include_empty)
        elif include_empty:
            instance.body = ModelInviteAdminRequestV3()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "body": "body",
            "namespace": "namespace",
        }

    # endregion static methods
