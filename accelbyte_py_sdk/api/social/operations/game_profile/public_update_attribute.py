# Auto-generated at 2021-09-27T17:01:27.238347+08:00
# from: Justice Social Service (1.17.1)

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

from ...models import Attribute
from ...models import ErrorEntity
from ...models import GameProfileInfo


class PublicUpdateAttribute(Operation):
    """Updates game profile attribute (publicUpdateAttribute)

    Properties:
        url: /social/public/namespaces/{namespace}/users/{userId}/profiles/{profileId}/attributes/{attributeName}

        method: PUT

        tags: GameProfile

        consumes: ["application/json"]

        produces: ["application/json"]

        security: bearer

        body: (body) OPTIONAL Attribute in body

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

        profile_id: (profileId) REQUIRED str in path

        attribute_name: (attributeName) REQUIRED str in path

    Responses:
        200: OK - GameProfileInfo (successful operation)

        400: Bad Request - ErrorEntity (ErrorCode: 12022 | ErrorMessage: Game profile attribute name [{attrName1}] passed in request url mismatch the name [{attrName2}] in body)

        404: Not Found - ErrorEntity (ErrorCode: 12041 | ErrorMessage: Game profile with id [{profileId}] is not found)
    """

    # region fields

    _url: str = "/social/public/namespaces/{namespace}/users/{userId}/profiles/{profileId}/attributes/{attributeName}"
    _method: str = "PUT"
    _consumes: List[str] = ["application/json"]
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    body: Attribute                                                                                # OPTIONAL in [body]
    namespace: str                                                                                 # REQUIRED in [path]
    user_id: str                                                                                   # REQUIRED in [path]
    profile_id: str                                                                                # REQUIRED in [path]
    attribute_name: str                                                                            # REQUIRED in [path]

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
            "user_id",
            "profile_id",
            "attribute_name",
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
        if hasattr(self, "profile_id"):
            result["profileId"] = self.profile_id
        if hasattr(self, "attribute_name"):
            result["attributeName"] = self.attribute_name
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "user_id") or self.user_id is None:
            return False
        if not hasattr(self, "profile_id") or self.profile_id is None:
            return False
        if not hasattr(self, "attribute_name") or self.attribute_name is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_body(self, value: Attribute) -> PublicUpdateAttribute:
        self.body = value
        return self

    def with_namespace(self, value: str) -> PublicUpdateAttribute:
        self.namespace = value
        return self

    def with_user_id(self, value: str) -> PublicUpdateAttribute:
        self.user_id = value
        return self

    def with_profile_id(self, value: str) -> PublicUpdateAttribute:
        self.profile_id = value
        return self

    def with_attribute_name(self, value: str) -> PublicUpdateAttribute:
        self.attribute_name = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "body") and self.body:
            result["body"] = self.body.to_dict(include_empty=include_empty)
        elif include_empty:
            result["body"] = Attribute()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        if hasattr(self, "profile_id") and self.profile_id:
            result["profileId"] = str(self.profile_id)
        elif include_empty:
            result["profileId"] = str()
        if hasattr(self, "attribute_name") and self.attribute_name:
            result["attributeName"] = str(self.attribute_name)
        elif include_empty:
            result["attributeName"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, GameProfileInfo], Union[None, ErrorEntity]]:
        """Parse the given response.

        200: OK - GameProfileInfo (successful operation)

        400: Bad Request - ErrorEntity (ErrorCode: 12022 | ErrorMessage: Game profile attribute name [{attrName1}] passed in request url mismatch the name [{attrName2}] in body)

        404: Not Found - ErrorEntity (ErrorCode: 12041 | ErrorMessage: Game profile with id [{profileId}] is not found)
        """
        if code == 200:
            return GameProfileInfo.create_from_dict(content), None
        if code == 400:
            return None, ErrorEntity.create_from_dict(content)
        if code == 404:
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
        namespace: str,
        user_id: str,
        profile_id: str,
        attribute_name: str,
        body: Optional[Attribute] = None,
    ) -> PublicUpdateAttribute:
        instance = cls()
        instance.namespace = namespace
        instance.user_id = user_id
        instance.profile_id = profile_id
        instance.attribute_name = attribute_name
        if body is not None:
            instance.body = body
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> PublicUpdateAttribute:
        instance = cls()
        if "body" in dict_ and dict_["body"] is not None:
            instance.body = Attribute.create_from_dict(dict_["body"], include_empty=include_empty)
        elif include_empty:
            instance.body = Attribute()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        if "profileId" in dict_ and dict_["profileId"] is not None:
            instance.profile_id = str(dict_["profileId"])
        elif include_empty:
            instance.profile_id = str()
        if "attributeName" in dict_ and dict_["attributeName"] is not None:
            instance.attribute_name = str(dict_["attributeName"])
        elif include_empty:
            instance.attribute_name = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "body": "body",
            "namespace": "namespace",
            "userId": "user_id",
            "profileId": "profile_id",
            "attributeName": "attribute_name",
        }

    # endregion static methods
