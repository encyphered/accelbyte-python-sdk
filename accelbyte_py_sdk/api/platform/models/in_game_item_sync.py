# Auto-generated at 2021-09-27T17:12:36.174867+08:00
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


class InGameItemSync(Model):
    """In game item sync

    Properties:
        target_namespace: (targetNamespace) REQUIRED str

        target_item_id: (targetItemId) REQUIRED str

        category_path: (categoryPath) REQUIRED str
    """

    # region fields

    target_namespace: str                                                                          # REQUIRED
    target_item_id: str                                                                            # REQUIRED
    category_path: str                                                                             # REQUIRED

    # endregion fields

    # region with_x methods

    def with_target_namespace(self, value: str) -> InGameItemSync:
        self.target_namespace = value
        return self

    def with_target_item_id(self, value: str) -> InGameItemSync:
        self.target_item_id = value
        return self

    def with_category_path(self, value: str) -> InGameItemSync:
        self.category_path = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "target_namespace") and self.target_namespace:
            result["targetNamespace"] = str(self.target_namespace)
        elif include_empty:
            result["targetNamespace"] = str()
        if hasattr(self, "target_item_id") and self.target_item_id:
            result["targetItemId"] = str(self.target_item_id)
        elif include_empty:
            result["targetItemId"] = str()
        if hasattr(self, "category_path") and self.category_path:
            result["categoryPath"] = str(self.category_path)
        elif include_empty:
            result["categoryPath"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        target_namespace: str,
        target_item_id: str,
        category_path: str,
    ) -> InGameItemSync:
        instance = cls()
        instance.target_namespace = target_namespace
        instance.target_item_id = target_item_id
        instance.category_path = category_path
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> InGameItemSync:
        instance = cls()
        if not dict_:
            return instance
        if "targetNamespace" in dict_ and dict_["targetNamespace"] is not None:
            instance.target_namespace = str(dict_["targetNamespace"])
        elif include_empty:
            instance.target_namespace = str()
        if "targetItemId" in dict_ and dict_["targetItemId"] is not None:
            instance.target_item_id = str(dict_["targetItemId"])
        elif include_empty:
            instance.target_item_id = str()
        if "categoryPath" in dict_ and dict_["categoryPath"] is not None:
            instance.category_path = str(dict_["categoryPath"])
        elif include_empty:
            instance.category_path = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "targetNamespace": "target_namespace",
            "targetItemId": "target_item_id",
            "categoryPath": "category_path",
        }

    # endregion static methods
