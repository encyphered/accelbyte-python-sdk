# Auto-generated at 2021-09-27T17:01:27.429670+08:00
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

from ...models import ErrorEntity


class PublicCreateUserNamespaceSlot(Operation):
    """Creates a slot (publicCreateUserNamespaceSlot)

    Properties:
        url: /social/public/namespaces/{namespace}/users/{userId}/slots

        method: POST

        tags: Slot

        consumes: ["multipart/form-data"]

        produces: ["application/json"]

        security: bearer

        custom_attribute: (customAttribute) OPTIONAL str in form_data

        checksum: (checksum) OPTIONAL str in form_data

        file: (file) OPTIONAL Any in form_data

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

        label: (label) OPTIONAL str in query

        tags: (tags) OPTIONAL List[str] in query

    Responses:
        201: Created - (Successful create of a slot)

        400: Bad Request - ErrorEntity (ErrorCode: 12121 | ErrorMessage: Checksum mismatch for [{filename}])

        409: Conflict - ErrorEntity (ErrorCode: 12171 | ErrorMessage: User [{userId}] exceed max slot count [{maxCount}] in namespace [{namespace}])
    """

    # region fields

    _url: str = "/social/public/namespaces/{namespace}/users/{userId}/slots"
    _method: str = "POST"
    _consumes: List[str] = ["multipart/form-data"]
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    custom_attribute: str                                                                          # OPTIONAL in [form_data]
    checksum: str                                                                                  # OPTIONAL in [form_data]
    file: Any                                                                                      # OPTIONAL in [form_data]
    namespace: str                                                                                 # REQUIRED in [path]
    user_id: str                                                                                   # REQUIRED in [path]
    label: str                                                                                     # OPTIONAL in [query]
    tags: List[str]                                                                                # OPTIONAL in [query]

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
            "user_id",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "form_data": self.get_form_data_params(),
            "path": self.get_path_params(),
            "query": self.get_query_params(),
        }

    def get_form_data_params(self) -> dict:
        result = {}
        if hasattr(self, "custom_attribute"):
            result["customAttribute"] = self.custom_attribute
        if hasattr(self, "checksum"):
            result["checksum"] = self.checksum
        if hasattr(self, "file"):
            result["file"] = self.file
        return result

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        if hasattr(self, "user_id"):
            result["userId"] = self.user_id
        return result

    def get_query_params(self) -> dict:
        result = {}
        if hasattr(self, "label"):
            result["label"] = self.label
        if hasattr(self, "tags"):
            result["tags"] = self.tags
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "user_id") or self.user_id is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_custom_attribute(self, value: str) -> PublicCreateUserNamespaceSlot:
        self.custom_attribute = value
        return self

    def with_checksum(self, value: str) -> PublicCreateUserNamespaceSlot:
        self.checksum = value
        return self

    def with_file(self, value: Any) -> PublicCreateUserNamespaceSlot:
        self.file = value
        return self

    def with_namespace(self, value: str) -> PublicCreateUserNamespaceSlot:
        self.namespace = value
        return self

    def with_user_id(self, value: str) -> PublicCreateUserNamespaceSlot:
        self.user_id = value
        return self

    def with_label(self, value: str) -> PublicCreateUserNamespaceSlot:
        self.label = value
        return self

    def with_tags(self, value: List[str]) -> PublicCreateUserNamespaceSlot:
        self.tags = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "custom_attribute") and self.custom_attribute:
            result["customAttribute"] = str(self.custom_attribute)
        elif include_empty:
            result["customAttribute"] = str()
        if hasattr(self, "checksum") and self.checksum:
            result["checksum"] = str(self.checksum)
        elif include_empty:
            result["checksum"] = str()
        if hasattr(self, "file") and self.file:
            result["file"] = Any(self.file)
        elif include_empty:
            result["file"] = Any()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        if hasattr(self, "label") and self.label:
            result["label"] = str(self.label)
        elif include_empty:
            result["label"] = str()
        if hasattr(self, "tags") and self.tags:
            result["tags"] = [str(i0) for i0 in self.tags]
        elif include_empty:
            result["tags"] = []
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, HttpResponse], Union[None, ErrorEntity]]:
        """Parse the given response.

        201: Created - (Successful create of a slot)

        400: Bad Request - ErrorEntity (ErrorCode: 12121 | ErrorMessage: Checksum mismatch for [{filename}])

        409: Conflict - ErrorEntity (ErrorCode: 12171 | ErrorMessage: User [{userId}] exceed max slot count [{maxCount}] in namespace [{namespace}])
        """
        if code == 201:
            return HttpResponse.create(code, "Created"), None
        if code == 400:
            return None, ErrorEntity.create_from_dict(content)
        if code == 409:
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
        custom_attribute: Optional[str] = None,
        checksum: Optional[str] = None,
        file: Optional[Any] = None,
        label: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> PublicCreateUserNamespaceSlot:
        instance = cls()
        instance.namespace = namespace
        instance.user_id = user_id
        if custom_attribute is not None:
            instance.custom_attribute = custom_attribute
        if checksum is not None:
            instance.checksum = checksum
        if file is not None:
            instance.file = file
        if label is not None:
            instance.label = label
        if tags is not None:
            instance.tags = tags
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> PublicCreateUserNamespaceSlot:
        instance = cls()
        if "customAttribute" in dict_ and dict_["customAttribute"] is not None:
            instance.custom_attribute = str(dict_["customAttribute"])
        elif include_empty:
            instance.custom_attribute = str()
        if "checksum" in dict_ and dict_["checksum"] is not None:
            instance.checksum = str(dict_["checksum"])
        elif include_empty:
            instance.checksum = str()
        if "file" in dict_ and dict_["file"] is not None:
            instance.file = Any(dict_["file"])
        elif include_empty:
            instance.file = Any()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        if "label" in dict_ and dict_["label"] is not None:
            instance.label = str(dict_["label"])
        elif include_empty:
            instance.label = str()
        if "tags" in dict_ and dict_["tags"] is not None:
            instance.tags = [str(i0) for i0 in dict_["tags"]]
        elif include_empty:
            instance.tags = []
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "customAttribute": "custom_attribute",
            "checksum": "checksum",
            "file": "file",
            "namespace": "namespace",
            "userId": "user_id",
            "label": "label",
            "tags": "tags",
        }

    # endregion static methods
