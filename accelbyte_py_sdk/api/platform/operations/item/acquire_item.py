# Auto-generated at 2021-09-27T17:01:29.457219+08:00
# from: Justice Platform Service (3.24.0)

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
from ...models import ItemAcquireRequest
from ...models import ItemAcquireResult


class AcquireItem(Operation):
    """Acquire item (acquireItem)

    Properties:
        url: /platform/admin/namespaces/{namespace}/items/{itemId}/acquire

        method: PUT

        tags: Item

        consumes: []

        produces: ["application/json"]

        security: bearer

        body: (body) OPTIONAL ItemAcquireRequest in body

        namespace: (namespace) REQUIRED str in path

        item_id: (itemId) REQUIRED str in path

    Responses:
        200: OK - ItemAcquireResult (successful operation)

        404: Not Found - ErrorEntity (ErrorCode: 30341 | ErrorMessage: Item [{itemId}] does not exist in namespace [{namespace}])
    """

    # region fields

    _url: str = "/platform/admin/namespaces/{namespace}/items/{itemId}/acquire"
    _method: str = "PUT"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    body: ItemAcquireRequest                                                                       # OPTIONAL in [body]
    namespace: str                                                                                 # REQUIRED in [path]
    item_id: str                                                                                   # REQUIRED in [path]

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
            "item_id",
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
        if hasattr(self, "item_id"):
            result["itemId"] = self.item_id
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "item_id") or self.item_id is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_body(self, value: ItemAcquireRequest) -> AcquireItem:
        self.body = value
        return self

    def with_namespace(self, value: str) -> AcquireItem:
        self.namespace = value
        return self

    def with_item_id(self, value: str) -> AcquireItem:
        self.item_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "body") and self.body:
            result["body"] = self.body.to_dict(include_empty=include_empty)
        elif include_empty:
            result["body"] = ItemAcquireRequest()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "item_id") and self.item_id:
            result["itemId"] = str(self.item_id)
        elif include_empty:
            result["itemId"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, ItemAcquireResult], Union[None, ErrorEntity]]:
        """Parse the given response.

        200: OK - ItemAcquireResult (successful operation)

        404: Not Found - ErrorEntity (ErrorCode: 30341 | ErrorMessage: Item [{itemId}] does not exist in namespace [{namespace}])
        """
        if code == 200:
            return ItemAcquireResult.create_from_dict(content), None
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
        item_id: str,
        body: Optional[ItemAcquireRequest] = None,
    ) -> AcquireItem:
        instance = cls()
        instance.namespace = namespace
        instance.item_id = item_id
        if body is not None:
            instance.body = body
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AcquireItem:
        instance = cls()
        if "body" in dict_ and dict_["body"] is not None:
            instance.body = ItemAcquireRequest.create_from_dict(dict_["body"], include_empty=include_empty)
        elif include_empty:
            instance.body = ItemAcquireRequest()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "itemId" in dict_ and dict_["itemId"] is not None:
            instance.item_id = str(dict_["itemId"])
        elif include_empty:
            instance.item_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "body": "body",
            "namespace": "namespace",
            "itemId": "item_id",
        }

    # endregion static methods
