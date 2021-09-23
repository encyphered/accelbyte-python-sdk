# Auto-generated at 2021-09-21T14:10:35.539883+08:00
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

from ...models import ModelRemoveUserRoleV4Request
from ...models import RestErrorResponse


class AdminRemoveUserRoleV4(Operation):
    """Admin Remove User Role v4 (AdminRemoveUserRoleV4)

    Properties:
        url: /iam/v4/admin/namespaces/{namespace}/users/{userId}/roles

        method: DELETE

        tags: Users V4

        consumes: []

        produces: ["application/json"]

        security: bearer

        body: (body) REQUIRED ModelRemoveUserRoleV4Request in body

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

    Responses:
        204: No Content - (Operation succeeded)

        400: Bad Request - RestErrorResponse (errorCode: 20019 | errorMessage: unable to parse request body)

        403: Forbidden - RestErrorResponse (errorCode: 20003 | errorMessage: forbidden access)

        404: Not Found - RestErrorResponse (errorCode: 20008 | errorMessage: user not found)

        422: Unprocessable Entity - RestErrorResponse (errorCode: 10183 | errorMessage: unprocessable entity)

        500: Internal Server Error - RestErrorResponse (errorCode: 20000 | errorMessage: internal server error)
    """

    # region fields

    _url: str = "/iam/v4/admin/namespaces/{namespace}/users/{userId}/roles"
    _method: str = "DELETE"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    body: ModelRemoveUserRoleV4Request                                                             # REQUIRED in [body]
    namespace: str                                                                                 # REQUIRED in [path]
    user_id: str                                                                                   # REQUIRED in [path]

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
            "user_id",
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
        if hasattr(self, "user_id"):
            result["userId"] = self.user_id
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "body") or self.body is None:
            return False
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "user_id") or self.user_id is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_body(self, value: ModelRemoveUserRoleV4Request) -> AdminRemoveUserRoleV4:
        self.body = value
        return self

    def with_namespace(self, value: str) -> AdminRemoveUserRoleV4:
        self.namespace = value
        return self

    def with_user_id(self, value: str) -> AdminRemoveUserRoleV4:
        self.user_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "body") and self.body:
            result["body"] = self.body.to_dict(include_empty=include_empty)
        elif include_empty:
            result["body"] = ModelRemoveUserRoleV4Request()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, HttpResponse], Union[None, RestErrorResponse]]:
        """Parse the given response.

        204: No Content - (Operation succeeded)

        400: Bad Request - RestErrorResponse (errorCode: 20019 | errorMessage: unable to parse request body)

        403: Forbidden - RestErrorResponse (errorCode: 20003 | errorMessage: forbidden access)

        404: Not Found - RestErrorResponse (errorCode: 20008 | errorMessage: user not found)

        422: Unprocessable Entity - RestErrorResponse (errorCode: 10183 | errorMessage: unprocessable entity)

        500: Internal Server Error - RestErrorResponse (errorCode: 20000 | errorMessage: internal server error)
        """
        if code == 204:
            return HttpResponse.create(code, "No Content"), None
        if code == 400:
            return None, RestErrorResponse.create_from_dict(content)
        if code == 403:
            return None, RestErrorResponse.create_from_dict(content)
        if code == 404:
            return None, RestErrorResponse.create_from_dict(content)
        if code == 422:
            return None, RestErrorResponse.create_from_dict(content)
        if code == 500:
            return None, RestErrorResponse.create_from_dict(content)
        return None, HttpResponse.create_unhandled_error()

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        body: ModelRemoveUserRoleV4Request,
        namespace: str,
        user_id: str,
    ) -> AdminRemoveUserRoleV4:
        instance = cls()
        instance.body = body
        instance.namespace = namespace
        instance.user_id = user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AdminRemoveUserRoleV4:
        instance = cls()
        if "body" in dict_ and dict_["body"] is not None:
            instance.body = ModelRemoveUserRoleV4Request.create_from_dict(dict_["body"], include_empty=include_empty)
        elif include_empty:
            instance.body = ModelRemoveUserRoleV4Request()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "body": "body",
            "namespace": "namespace",
            "userId": "user_id",
        }

    # endregion static methods