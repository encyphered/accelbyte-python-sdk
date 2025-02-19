# Auto-generated at 2021-09-27T17:12:36.169984+08:00
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


class BasicItem(Model):
    """Basic item

    Properties:
        item_id: (itemId) REQUIRED str

        app_id: (appId) OPTIONAL str

        app_type: (appType) OPTIONAL str

        base_app_id: (baseAppId) OPTIONAL str

        sku: (sku) OPTIONAL str

        namespace: (namespace) REQUIRED str

        name: (name) REQUIRED str

        entitlement_type: (entitlementType) REQUIRED str

        use_count: (useCount) OPTIONAL int

        status: (status) REQUIRED str

        item_type: (itemType) REQUIRED str

        tags: (tags) OPTIONAL List[str]

        features: (features) OPTIONAL List[str]

        created_at: (createdAt) REQUIRED str

        updated_at: (updatedAt) REQUIRED str
    """

    # region fields

    item_id: str                                                                                   # REQUIRED
    app_id: str                                                                                    # OPTIONAL
    app_type: str                                                                                  # OPTIONAL
    base_app_id: str                                                                               # OPTIONAL
    sku: str                                                                                       # OPTIONAL
    namespace: str                                                                                 # REQUIRED
    name: str                                                                                      # REQUIRED
    entitlement_type: str                                                                          # REQUIRED
    use_count: int                                                                                 # OPTIONAL
    status: str                                                                                    # REQUIRED
    item_type: str                                                                                 # REQUIRED
    tags: List[str]                                                                                # OPTIONAL
    features: List[str]                                                                            # OPTIONAL
    created_at: str                                                                                # REQUIRED
    updated_at: str                                                                                # REQUIRED

    # endregion fields

    # region with_x methods

    def with_item_id(self, value: str) -> BasicItem:
        self.item_id = value
        return self

    def with_app_id(self, value: str) -> BasicItem:
        self.app_id = value
        return self

    def with_app_type(self, value: str) -> BasicItem:
        self.app_type = value
        return self

    def with_base_app_id(self, value: str) -> BasicItem:
        self.base_app_id = value
        return self

    def with_sku(self, value: str) -> BasicItem:
        self.sku = value
        return self

    def with_namespace(self, value: str) -> BasicItem:
        self.namespace = value
        return self

    def with_name(self, value: str) -> BasicItem:
        self.name = value
        return self

    def with_entitlement_type(self, value: str) -> BasicItem:
        self.entitlement_type = value
        return self

    def with_use_count(self, value: int) -> BasicItem:
        self.use_count = value
        return self

    def with_status(self, value: str) -> BasicItem:
        self.status = value
        return self

    def with_item_type(self, value: str) -> BasicItem:
        self.item_type = value
        return self

    def with_tags(self, value: List[str]) -> BasicItem:
        self.tags = value
        return self

    def with_features(self, value: List[str]) -> BasicItem:
        self.features = value
        return self

    def with_created_at(self, value: str) -> BasicItem:
        self.created_at = value
        return self

    def with_updated_at(self, value: str) -> BasicItem:
        self.updated_at = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "item_id") and self.item_id:
            result["itemId"] = str(self.item_id)
        elif include_empty:
            result["itemId"] = str()
        if hasattr(self, "app_id") and self.app_id:
            result["appId"] = str(self.app_id)
        elif include_empty:
            result["appId"] = str()
        if hasattr(self, "app_type") and self.app_type:
            result["appType"] = str(self.app_type)
        elif include_empty:
            result["appType"] = str()
        if hasattr(self, "base_app_id") and self.base_app_id:
            result["baseAppId"] = str(self.base_app_id)
        elif include_empty:
            result["baseAppId"] = str()
        if hasattr(self, "sku") and self.sku:
            result["sku"] = str(self.sku)
        elif include_empty:
            result["sku"] = str()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "name") and self.name:
            result["name"] = str(self.name)
        elif include_empty:
            result["name"] = str()
        if hasattr(self, "entitlement_type") and self.entitlement_type:
            result["entitlementType"] = str(self.entitlement_type)
        elif include_empty:
            result["entitlementType"] = str()
        if hasattr(self, "use_count") and self.use_count:
            result["useCount"] = int(self.use_count)
        elif include_empty:
            result["useCount"] = int()
        if hasattr(self, "status") and self.status:
            result["status"] = str(self.status)
        elif include_empty:
            result["status"] = str()
        if hasattr(self, "item_type") and self.item_type:
            result["itemType"] = str(self.item_type)
        elif include_empty:
            result["itemType"] = str()
        if hasattr(self, "tags") and self.tags:
            result["tags"] = [str(i0) for i0 in self.tags]
        elif include_empty:
            result["tags"] = []
        if hasattr(self, "features") and self.features:
            result["features"] = [str(i0) for i0 in self.features]
        elif include_empty:
            result["features"] = []
        if hasattr(self, "created_at") and self.created_at:
            result["createdAt"] = str(self.created_at)
        elif include_empty:
            result["createdAt"] = str()
        if hasattr(self, "updated_at") and self.updated_at:
            result["updatedAt"] = str(self.updated_at)
        elif include_empty:
            result["updatedAt"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        item_id: str,
        namespace: str,
        name: str,
        entitlement_type: str,
        status: str,
        item_type: str,
        created_at: str,
        updated_at: str,
        app_id: Optional[str] = None,
        app_type: Optional[str] = None,
        base_app_id: Optional[str] = None,
        sku: Optional[str] = None,
        use_count: Optional[int] = None,
        tags: Optional[List[str]] = None,
        features: Optional[List[str]] = None,
    ) -> BasicItem:
        instance = cls()
        instance.item_id = item_id
        instance.namespace = namespace
        instance.name = name
        instance.entitlement_type = entitlement_type
        instance.status = status
        instance.item_type = item_type
        instance.created_at = created_at
        instance.updated_at = updated_at
        if app_id is not None:
            instance.app_id = app_id
        if app_type is not None:
            instance.app_type = app_type
        if base_app_id is not None:
            instance.base_app_id = base_app_id
        if sku is not None:
            instance.sku = sku
        if use_count is not None:
            instance.use_count = use_count
        if tags is not None:
            instance.tags = tags
        if features is not None:
            instance.features = features
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> BasicItem:
        instance = cls()
        if not dict_:
            return instance
        if "itemId" in dict_ and dict_["itemId"] is not None:
            instance.item_id = str(dict_["itemId"])
        elif include_empty:
            instance.item_id = str()
        if "appId" in dict_ and dict_["appId"] is not None:
            instance.app_id = str(dict_["appId"])
        elif include_empty:
            instance.app_id = str()
        if "appType" in dict_ and dict_["appType"] is not None:
            instance.app_type = str(dict_["appType"])
        elif include_empty:
            instance.app_type = str()
        if "baseAppId" in dict_ and dict_["baseAppId"] is not None:
            instance.base_app_id = str(dict_["baseAppId"])
        elif include_empty:
            instance.base_app_id = str()
        if "sku" in dict_ and dict_["sku"] is not None:
            instance.sku = str(dict_["sku"])
        elif include_empty:
            instance.sku = str()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "name" in dict_ and dict_["name"] is not None:
            instance.name = str(dict_["name"])
        elif include_empty:
            instance.name = str()
        if "entitlementType" in dict_ and dict_["entitlementType"] is not None:
            instance.entitlement_type = str(dict_["entitlementType"])
        elif include_empty:
            instance.entitlement_type = str()
        if "useCount" in dict_ and dict_["useCount"] is not None:
            instance.use_count = int(dict_["useCount"])
        elif include_empty:
            instance.use_count = int()
        if "status" in dict_ and dict_["status"] is not None:
            instance.status = str(dict_["status"])
        elif include_empty:
            instance.status = str()
        if "itemType" in dict_ and dict_["itemType"] is not None:
            instance.item_type = str(dict_["itemType"])
        elif include_empty:
            instance.item_type = str()
        if "tags" in dict_ and dict_["tags"] is not None:
            instance.tags = [str(i0) for i0 in dict_["tags"]]
        elif include_empty:
            instance.tags = []
        if "features" in dict_ and dict_["features"] is not None:
            instance.features = [str(i0) for i0 in dict_["features"]]
        elif include_empty:
            instance.features = []
        if "createdAt" in dict_ and dict_["createdAt"] is not None:
            instance.created_at = str(dict_["createdAt"])
        elif include_empty:
            instance.created_at = str()
        if "updatedAt" in dict_ and dict_["updatedAt"] is not None:
            instance.updated_at = str(dict_["updatedAt"])
        elif include_empty:
            instance.updated_at = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "itemId": "item_id",
            "appId": "app_id",
            "appType": "app_type",
            "baseAppId": "base_app_id",
            "sku": "sku",
            "namespace": "namespace",
            "name": "name",
            "entitlementType": "entitlement_type",
            "useCount": "use_count",
            "status": "status",
            "itemType": "item_type",
            "tags": "tags",
            "features": "features",
            "createdAt": "created_at",
            "updatedAt": "updated_at",
        }

    # endregion static methods
