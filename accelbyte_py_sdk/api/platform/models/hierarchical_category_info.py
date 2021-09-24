# Auto-generated at 2021-09-24T09:01:00.690426+08:00
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


class HierarchicalCategoryInfo(Model):
    """Hierarchical category info

    Properties:
        namespace: (namespace) REQUIRED str

        parent_category_path: (parentCategoryPath) REQUIRED str

        category_path: (categoryPath) REQUIRED str

        created_at: (createdAt) REQUIRED str

        updated_at: (updatedAt) REQUIRED str

        display_name: (displayName) REQUIRED str

        child_categories: (childCategories) REQUIRED List[HierarchicalCategoryInfo]

        root: (root) OPTIONAL bool
    """

    # region fields

    namespace: str                                                                                 # REQUIRED
    parent_category_path: str                                                                      # REQUIRED
    category_path: str                                                                             # REQUIRED
    created_at: str                                                                                # REQUIRED
    updated_at: str                                                                                # REQUIRED
    display_name: str                                                                              # REQUIRED
    child_categories: List[HierarchicalCategoryInfo]                                               # REQUIRED
    root: bool                                                                                     # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_namespace(self, value: str) -> HierarchicalCategoryInfo:
        self.namespace = value
        return self

    def with_parent_category_path(self, value: str) -> HierarchicalCategoryInfo:
        self.parent_category_path = value
        return self

    def with_category_path(self, value: str) -> HierarchicalCategoryInfo:
        self.category_path = value
        return self

    def with_created_at(self, value: str) -> HierarchicalCategoryInfo:
        self.created_at = value
        return self

    def with_updated_at(self, value: str) -> HierarchicalCategoryInfo:
        self.updated_at = value
        return self

    def with_display_name(self, value: str) -> HierarchicalCategoryInfo:
        self.display_name = value
        return self

    def with_child_categories(self, value: List[HierarchicalCategoryInfo]) -> HierarchicalCategoryInfo:
        self.child_categories = value
        return self

    def with_root(self, value: bool) -> HierarchicalCategoryInfo:
        self.root = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "parent_category_path") and self.parent_category_path:
            result["parentCategoryPath"] = str(self.parent_category_path)
        elif include_empty:
            result["parentCategoryPath"] = str()
        if hasattr(self, "category_path") and self.category_path:
            result["categoryPath"] = str(self.category_path)
        elif include_empty:
            result["categoryPath"] = str()
        if hasattr(self, "created_at") and self.created_at:
            result["createdAt"] = str(self.created_at)
        elif include_empty:
            result["createdAt"] = str()
        if hasattr(self, "updated_at") and self.updated_at:
            result["updatedAt"] = str(self.updated_at)
        elif include_empty:
            result["updatedAt"] = str()
        if hasattr(self, "display_name") and self.display_name:
            result["displayName"] = str(self.display_name)
        elif include_empty:
            result["displayName"] = str()
        if hasattr(self, "child_categories") and self.child_categories:
            result["childCategories"] = [i0.to_dict(include_empty=include_empty) for i0 in self.child_categories]
        elif include_empty:
            result["childCategories"] = []
        if hasattr(self, "root") and self.root:
            result["root"] = bool(self.root)
        elif include_empty:
            result["root"] = bool()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        namespace: str,
        parent_category_path: str,
        category_path: str,
        created_at: str,
        updated_at: str,
        display_name: str,
        child_categories: List[HierarchicalCategoryInfo],
        root: Optional[bool] = None,
    ) -> HierarchicalCategoryInfo:
        instance = cls()
        instance.namespace = namespace
        instance.parent_category_path = parent_category_path
        instance.category_path = category_path
        instance.created_at = created_at
        instance.updated_at = updated_at
        instance.display_name = display_name
        instance.child_categories = child_categories
        if root is not None:
            instance.root = root
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> HierarchicalCategoryInfo:
        instance = cls()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "parentCategoryPath" in dict_ and dict_["parentCategoryPath"] is not None:
            instance.parent_category_path = str(dict_["parentCategoryPath"])
        elif include_empty:
            instance.parent_category_path = str()
        if "categoryPath" in dict_ and dict_["categoryPath"] is not None:
            instance.category_path = str(dict_["categoryPath"])
        elif include_empty:
            instance.category_path = str()
        if "createdAt" in dict_ and dict_["createdAt"] is not None:
            instance.created_at = str(dict_["createdAt"])
        elif include_empty:
            instance.created_at = str()
        if "updatedAt" in dict_ and dict_["updatedAt"] is not None:
            instance.updated_at = str(dict_["updatedAt"])
        elif include_empty:
            instance.updated_at = str()
        if "displayName" in dict_ and dict_["displayName"] is not None:
            instance.display_name = str(dict_["displayName"])
        elif include_empty:
            instance.display_name = str()
        if "childCategories" in dict_ and dict_["childCategories"] is not None:
            instance.child_categories = [HierarchicalCategoryInfo.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["childCategories"]]
        elif include_empty:
            instance.child_categories = []
        if "root" in dict_ and dict_["root"] is not None:
            instance.root = bool(dict_["root"])
        elif include_empty:
            instance.root = bool()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "parentCategoryPath": "parent_category_path",
            "categoryPath": "category_path",
            "createdAt": "created_at",
            "updatedAt": "updated_at",
            "displayName": "display_name",
            "childCategories": "child_categories",
            "root": "root",
        }

    # endregion static methods
