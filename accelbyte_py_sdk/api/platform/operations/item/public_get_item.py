# Auto-generated at 2021-09-21T14:10:38.959181+08:00
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
from ...models import PopulatedItemInfo


class PublicGetItem(Operation):
    """Get an item in locale (publicGetItem)

    Properties:
        url: /platform/public/namespaces/{namespace}/items/{itemId}/locale

        method: GET

        tags: Item

        consumes: []

        produces: ["application/json"]

        security: bearer

        namespace: (namespace) REQUIRED str in path

        item_id: (itemId) REQUIRED str in path

        store_id: (storeId) OPTIONAL str in query

        region: (region) OPTIONAL str in query

        language: (language) OPTIONAL str in query

        populate_bundle: (populateBundle) OPTIONAL bool in query

    Responses:
        200: OK - PopulatedItemInfo (successful operation)

        404: Not Found - ErrorEntity (ErrorCode: 30341 | ErrorMessage: Item [{itemId}] does not exist in namespace [{namespace}])
    """

    # region fields

    _url: str = "/platform/public/namespaces/{namespace}/items/{itemId}/locale"
    _method: str = "GET"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    namespace: str                                                                                 # REQUIRED in [path]
    item_id: str                                                                                   # REQUIRED in [path]
    store_id: str                                                                                  # OPTIONAL in [query]
    region: str                                                                                    # OPTIONAL in [query]
    language: str                                                                                  # OPTIONAL in [query]
    populate_bundle: bool                                                                          # OPTIONAL in [query]

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
            "item_id",
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
        if hasattr(self, "item_id"):
            result["itemId"] = self.item_id
        return result

    def get_query_params(self) -> dict:
        result = {}
        if hasattr(self, "store_id"):
            result["storeId"] = self.store_id
        if hasattr(self, "region"):
            result["region"] = self.region
        if hasattr(self, "language"):
            result["language"] = self.language
        if hasattr(self, "populate_bundle"):
            result["populateBundle"] = self.populate_bundle
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

    def with_namespace(self, value: str) -> PublicGetItem:
        self.namespace = value
        return self

    def with_item_id(self, value: str) -> PublicGetItem:
        self.item_id = value
        return self

    def with_store_id(self, value: str) -> PublicGetItem:
        self.store_id = value
        return self

    def with_region(self, value: str) -> PublicGetItem:
        self.region = value
        return self

    def with_language(self, value: str) -> PublicGetItem:
        self.language = value
        return self

    def with_populate_bundle(self, value: bool) -> PublicGetItem:
        self.populate_bundle = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "item_id") and self.item_id:
            result["itemId"] = str(self.item_id)
        elif include_empty:
            result["itemId"] = str()
        if hasattr(self, "store_id") and self.store_id:
            result["storeId"] = str(self.store_id)
        elif include_empty:
            result["storeId"] = str()
        if hasattr(self, "region") and self.region:
            result["region"] = str(self.region)
        elif include_empty:
            result["region"] = str()
        if hasattr(self, "language") and self.language:
            result["language"] = str(self.language)
        elif include_empty:
            result["language"] = str()
        if hasattr(self, "populate_bundle") and self.populate_bundle:
            result["populateBundle"] = bool(self.populate_bundle)
        elif include_empty:
            result["populateBundle"] = bool()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, PopulatedItemInfo], Union[None, ErrorEntity]]:
        """Parse the given response.

        200: OK - PopulatedItemInfo (successful operation)

        404: Not Found - ErrorEntity (ErrorCode: 30341 | ErrorMessage: Item [{itemId}] does not exist in namespace [{namespace}])
        """
        if code == 200:
            return PopulatedItemInfo.create_from_dict(content), None
        if code == 404:
            return None, ErrorEntity.create_from_dict(content)
        return None, HttpResponse.create_unhandled_error()

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        namespace: str,
        item_id: str,
        store_id: Optional[str] = None,
        region: Optional[str] = None,
        language: Optional[str] = None,
        populate_bundle: Optional[bool] = None,
    ) -> PublicGetItem:
        instance = cls()
        instance.namespace = namespace
        instance.item_id = item_id
        if store_id is not None:
            instance.store_id = store_id
        if region is not None:
            instance.region = region
        if language is not None:
            instance.language = language
        if populate_bundle is not None:
            instance.populate_bundle = populate_bundle
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> PublicGetItem:
        instance = cls()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "itemId" in dict_ and dict_["itemId"] is not None:
            instance.item_id = str(dict_["itemId"])
        elif include_empty:
            instance.item_id = str()
        if "storeId" in dict_ and dict_["storeId"] is not None:
            instance.store_id = str(dict_["storeId"])
        elif include_empty:
            instance.store_id = str()
        if "region" in dict_ and dict_["region"] is not None:
            instance.region = str(dict_["region"])
        elif include_empty:
            instance.region = str()
        if "language" in dict_ and dict_["language"] is not None:
            instance.language = str(dict_["language"])
        elif include_empty:
            instance.language = str()
        if "populateBundle" in dict_ and dict_["populateBundle"] is not None:
            instance.populate_bundle = bool(dict_["populateBundle"])
        elif include_empty:
            instance.populate_bundle = bool()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "itemId": "item_id",
            "storeId": "store_id",
            "region": "region",
            "language": "language",
            "populateBundle": "populate_bundle",
        }

    # endregion static methods