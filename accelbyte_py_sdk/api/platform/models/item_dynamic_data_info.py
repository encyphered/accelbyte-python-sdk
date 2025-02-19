# Auto-generated at 2021-09-27T17:12:36.234022+08:00
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

from ....core import Model


class ItemDynamicDataInfo(Model):
    """Item dynamic data info

    Properties:
        item_id: (itemId) REQUIRED str

        namespace: (namespace) REQUIRED str

        available_count: (availableCount) REQUIRED int

        user_available_count: (userAvailableCount) REQUIRED int

        user_purchase_limit: (userPurchaseLimit) REQUIRED int
    """

    # region fields

    item_id: str                                                                                   # REQUIRED
    namespace: str                                                                                 # REQUIRED
    available_count: int                                                                           # REQUIRED
    user_available_count: int                                                                      # REQUIRED
    user_purchase_limit: int                                                                       # REQUIRED

    # endregion fields

    # region with_x methods

    def with_item_id(self, value: str) -> ItemDynamicDataInfo:
        self.item_id = value
        return self

    def with_namespace(self, value: str) -> ItemDynamicDataInfo:
        self.namespace = value
        return self

    def with_available_count(self, value: int) -> ItemDynamicDataInfo:
        self.available_count = value
        return self

    def with_user_available_count(self, value: int) -> ItemDynamicDataInfo:
        self.user_available_count = value
        return self

    def with_user_purchase_limit(self, value: int) -> ItemDynamicDataInfo:
        self.user_purchase_limit = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "item_id") and self.item_id:
            result["itemId"] = str(self.item_id)
        elif include_empty:
            result["itemId"] = str()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "available_count") and self.available_count:
            result["availableCount"] = int(self.available_count)
        elif include_empty:
            result["availableCount"] = int()
        if hasattr(self, "user_available_count") and self.user_available_count:
            result["userAvailableCount"] = int(self.user_available_count)
        elif include_empty:
            result["userAvailableCount"] = int()
        if hasattr(self, "user_purchase_limit") and self.user_purchase_limit:
            result["userPurchaseLimit"] = int(self.user_purchase_limit)
        elif include_empty:
            result["userPurchaseLimit"] = int()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        item_id: str,
        namespace: str,
        available_count: int,
        user_available_count: int,
        user_purchase_limit: int,
    ) -> ItemDynamicDataInfo:
        instance = cls()
        instance.item_id = item_id
        instance.namespace = namespace
        instance.available_count = available_count
        instance.user_available_count = user_available_count
        instance.user_purchase_limit = user_purchase_limit
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ItemDynamicDataInfo:
        instance = cls()
        if not dict_:
            return instance
        if "itemId" in dict_ and dict_["itemId"] is not None:
            instance.item_id = str(dict_["itemId"])
        elif include_empty:
            instance.item_id = str()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "availableCount" in dict_ and dict_["availableCount"] is not None:
            instance.available_count = int(dict_["availableCount"])
        elif include_empty:
            instance.available_count = int()
        if "userAvailableCount" in dict_ and dict_["userAvailableCount"] is not None:
            instance.user_available_count = int(dict_["userAvailableCount"])
        elif include_empty:
            instance.user_available_count = int()
        if "userPurchaseLimit" in dict_ and dict_["userPurchaseLimit"] is not None:
            instance.user_purchase_limit = int(dict_["userPurchaseLimit"])
        elif include_empty:
            instance.user_purchase_limit = int()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "itemId": "item_id",
            "namespace": "namespace",
            "availableCount": "available_count",
            "userAvailableCount": "user_available_count",
            "userPurchaseLimit": "user_purchase_limit",
        }

    # endregion static methods
