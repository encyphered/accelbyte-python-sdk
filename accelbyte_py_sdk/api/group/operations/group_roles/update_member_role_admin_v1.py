# Auto-generated at 2021-09-27T17:01:30.876011+08:00
# from: Justice Group Service (2.4.0)

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

from ...models import ModelsUpdateMemberRoleRequestV1
from ...models import ModelsUpdateMemberRoleResponseV1
from ...models import ResponseErrorResponse


class UpdateMemberRoleAdminV1(Operation):
    """update member role (updateMemberRoleAdminV1)

    Properties:
        url: /group/v1/admin/namespaces/{namespace}/roles/{memberRoleId}

        method: PATCH

        tags: Group Roles

        consumes: ["application/json"]

        produces: ["application/json"]

        security: bearer

        body: (body) REQUIRED ModelsUpdateMemberRoleRequestV1 in body

        namespace: (namespace) REQUIRED str in path

        member_role_id: (memberRoleId) REQUIRED str in path

    Responses:
        200: OK - ModelsUpdateMemberRoleResponseV1 (OK)

        400: Bad Request - ResponseErrorResponse (errorCode: 20002 | errorMessage: validation error)

        401: Unauthorized - ResponseErrorResponse (errorCode: 20001 | errorMessage: unauthorized access)

        403: Forbidden - ResponseErrorResponse (errorCode: 20022 | errorMessage: token is not user token)

        404: Not Found - ResponseErrorResponse (errorCode: 73232 | errorMessage: member role not found)

        500: Internal Server Error - ResponseErrorResponse (Internal Server Error)
    """

    # region fields

    _url: str = "/group/v1/admin/namespaces/{namespace}/roles/{memberRoleId}"
    _method: str = "PATCH"
    _consumes: List[str] = ["application/json"]
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    body: ModelsUpdateMemberRoleRequestV1                                                          # REQUIRED in [body]
    namespace: str                                                                                 # REQUIRED in [path]
    member_role_id: str                                                                            # REQUIRED in [path]

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
            "member_role_id",
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
        if hasattr(self, "member_role_id"):
            result["memberRoleId"] = self.member_role_id
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "body") or self.body is None:
            return False
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "member_role_id") or self.member_role_id is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_body(self, value: ModelsUpdateMemberRoleRequestV1) -> UpdateMemberRoleAdminV1:
        self.body = value
        return self

    def with_namespace(self, value: str) -> UpdateMemberRoleAdminV1:
        self.namespace = value
        return self

    def with_member_role_id(self, value: str) -> UpdateMemberRoleAdminV1:
        self.member_role_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "body") and self.body:
            result["body"] = self.body.to_dict(include_empty=include_empty)
        elif include_empty:
            result["body"] = ModelsUpdateMemberRoleRequestV1()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "member_role_id") and self.member_role_id:
            result["memberRoleId"] = str(self.member_role_id)
        elif include_empty:
            result["memberRoleId"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, ModelsUpdateMemberRoleResponseV1], Union[None, ResponseErrorResponse]]:
        """Parse the given response.

        200: OK - ModelsUpdateMemberRoleResponseV1 (OK)

        400: Bad Request - ResponseErrorResponse (errorCode: 20002 | errorMessage: validation error)

        401: Unauthorized - ResponseErrorResponse (errorCode: 20001 | errorMessage: unauthorized access)

        403: Forbidden - ResponseErrorResponse (errorCode: 20022 | errorMessage: token is not user token)

        404: Not Found - ResponseErrorResponse (errorCode: 73232 | errorMessage: member role not found)

        500: Internal Server Error - ResponseErrorResponse (Internal Server Error)
        """
        if code == 200:
            return ModelsUpdateMemberRoleResponseV1.create_from_dict(content), None
        if code == 400:
            return None, ResponseErrorResponse.create_from_dict(content)
        if code == 401:
            return None, ResponseErrorResponse.create_from_dict(content)
        if code == 403:
            return None, ResponseErrorResponse.create_from_dict(content)
        if code == 404:
            return None, ResponseErrorResponse.create_from_dict(content)
        if code == 500:
            return None, ResponseErrorResponse.create_from_dict(content)
        was_handled, undocumented_response = HttpResponse.try_create_undocumented_response(code, content)
        if was_handled:
            return None, undocumented_response
        return None, HttpResponse.create_unhandled_error()

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        body: ModelsUpdateMemberRoleRequestV1,
        namespace: str,
        member_role_id: str,
    ) -> UpdateMemberRoleAdminV1:
        instance = cls()
        instance.body = body
        instance.namespace = namespace
        instance.member_role_id = member_role_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> UpdateMemberRoleAdminV1:
        instance = cls()
        if "body" in dict_ and dict_["body"] is not None:
            instance.body = ModelsUpdateMemberRoleRequestV1.create_from_dict(dict_["body"], include_empty=include_empty)
        elif include_empty:
            instance.body = ModelsUpdateMemberRoleRequestV1()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "memberRoleId" in dict_ and dict_["memberRoleId"] is not None:
            instance.member_role_id = str(dict_["memberRoleId"])
        elif include_empty:
            instance.member_role_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "body": "body",
            "namespace": "namespace",
            "memberRoleId": "member_role_id",
        }

    # endregion static methods
