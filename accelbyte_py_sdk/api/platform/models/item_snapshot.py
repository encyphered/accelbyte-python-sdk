# Auto-generated at 2021-09-27T17:12:36.257172+08:00
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

from ..models.recurring import Recurring
from ..models.region_data_item import RegionDataItem


class ItemSnapshot(Model):
    """Item snapshot

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

        stackable: (stackable) OPTIONAL bool

        item_type: (itemType) REQUIRED str

        thumbnail_url: (thumbnailUrl) OPTIONAL str

        target_namespace: (targetNamespace) OPTIONAL str

        target_currency_code: (targetCurrencyCode) OPTIONAL str

        target_item_id: (targetItemId) OPTIONAL str

        title: (title) REQUIRED str

        description: (description) OPTIONAL str

        region_data_item: (regionDataItem) OPTIONAL RegionDataItem

        recurring: (recurring) OPTIONAL Recurring

        item_ids: (itemIds) OPTIONAL List[str]

        features: (features) OPTIONAL List[str]

        max_count_per_user: (maxCountPerUser) OPTIONAL int

        max_count: (maxCount) OPTIONAL int

        booth_name: (boothName) OPTIONAL str

        region: (region) REQUIRED str

        language: (language) REQUIRED str

        created_at: (createdAt) OPTIONAL str

        updated_at: (updatedAt) OPTIONAL str
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
    stackable: bool                                                                                # OPTIONAL
    item_type: str                                                                                 # REQUIRED
    thumbnail_url: str                                                                             # OPTIONAL
    target_namespace: str                                                                          # OPTIONAL
    target_currency_code: str                                                                      # OPTIONAL
    target_item_id: str                                                                            # OPTIONAL
    title: str                                                                                     # REQUIRED
    description: str                                                                               # OPTIONAL
    region_data_item: RegionDataItem                                                               # OPTIONAL
    recurring: Recurring                                                                           # OPTIONAL
    item_ids: List[str]                                                                            # OPTIONAL
    features: List[str]                                                                            # OPTIONAL
    max_count_per_user: int                                                                        # OPTIONAL
    max_count: int                                                                                 # OPTIONAL
    booth_name: str                                                                                # OPTIONAL
    region: str                                                                                    # REQUIRED
    language: str                                                                                  # REQUIRED
    created_at: str                                                                                # OPTIONAL
    updated_at: str                                                                                # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_item_id(self, value: str) -> ItemSnapshot:
        self.item_id = value
        return self

    def with_app_id(self, value: str) -> ItemSnapshot:
        self.app_id = value
        return self

    def with_app_type(self, value: str) -> ItemSnapshot:
        self.app_type = value
        return self

    def with_base_app_id(self, value: str) -> ItemSnapshot:
        self.base_app_id = value
        return self

    def with_sku(self, value: str) -> ItemSnapshot:
        self.sku = value
        return self

    def with_namespace(self, value: str) -> ItemSnapshot:
        self.namespace = value
        return self

    def with_name(self, value: str) -> ItemSnapshot:
        self.name = value
        return self

    def with_entitlement_type(self, value: str) -> ItemSnapshot:
        self.entitlement_type = value
        return self

    def with_use_count(self, value: int) -> ItemSnapshot:
        self.use_count = value
        return self

    def with_stackable(self, value: bool) -> ItemSnapshot:
        self.stackable = value
        return self

    def with_item_type(self, value: str) -> ItemSnapshot:
        self.item_type = value
        return self

    def with_thumbnail_url(self, value: str) -> ItemSnapshot:
        self.thumbnail_url = value
        return self

    def with_target_namespace(self, value: str) -> ItemSnapshot:
        self.target_namespace = value
        return self

    def with_target_currency_code(self, value: str) -> ItemSnapshot:
        self.target_currency_code = value
        return self

    def with_target_item_id(self, value: str) -> ItemSnapshot:
        self.target_item_id = value
        return self

    def with_title(self, value: str) -> ItemSnapshot:
        self.title = value
        return self

    def with_description(self, value: str) -> ItemSnapshot:
        self.description = value
        return self

    def with_region_data_item(self, value: RegionDataItem) -> ItemSnapshot:
        self.region_data_item = value
        return self

    def with_recurring(self, value: Recurring) -> ItemSnapshot:
        self.recurring = value
        return self

    def with_item_ids(self, value: List[str]) -> ItemSnapshot:
        self.item_ids = value
        return self

    def with_features(self, value: List[str]) -> ItemSnapshot:
        self.features = value
        return self

    def with_max_count_per_user(self, value: int) -> ItemSnapshot:
        self.max_count_per_user = value
        return self

    def with_max_count(self, value: int) -> ItemSnapshot:
        self.max_count = value
        return self

    def with_booth_name(self, value: str) -> ItemSnapshot:
        self.booth_name = value
        return self

    def with_region(self, value: str) -> ItemSnapshot:
        self.region = value
        return self

    def with_language(self, value: str) -> ItemSnapshot:
        self.language = value
        return self

    def with_created_at(self, value: str) -> ItemSnapshot:
        self.created_at = value
        return self

    def with_updated_at(self, value: str) -> ItemSnapshot:
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
        if hasattr(self, "stackable") and self.stackable:
            result["stackable"] = bool(self.stackable)
        elif include_empty:
            result["stackable"] = bool()
        if hasattr(self, "item_type") and self.item_type:
            result["itemType"] = str(self.item_type)
        elif include_empty:
            result["itemType"] = str()
        if hasattr(self, "thumbnail_url") and self.thumbnail_url:
            result["thumbnailUrl"] = str(self.thumbnail_url)
        elif include_empty:
            result["thumbnailUrl"] = str()
        if hasattr(self, "target_namespace") and self.target_namespace:
            result["targetNamespace"] = str(self.target_namespace)
        elif include_empty:
            result["targetNamespace"] = str()
        if hasattr(self, "target_currency_code") and self.target_currency_code:
            result["targetCurrencyCode"] = str(self.target_currency_code)
        elif include_empty:
            result["targetCurrencyCode"] = str()
        if hasattr(self, "target_item_id") and self.target_item_id:
            result["targetItemId"] = str(self.target_item_id)
        elif include_empty:
            result["targetItemId"] = str()
        if hasattr(self, "title") and self.title:
            result["title"] = str(self.title)
        elif include_empty:
            result["title"] = str()
        if hasattr(self, "description") and self.description:
            result["description"] = str(self.description)
        elif include_empty:
            result["description"] = str()
        if hasattr(self, "region_data_item") and self.region_data_item:
            result["regionDataItem"] = self.region_data_item.to_dict(include_empty=include_empty)
        elif include_empty:
            result["regionDataItem"] = RegionDataItem()
        if hasattr(self, "recurring") and self.recurring:
            result["recurring"] = self.recurring.to_dict(include_empty=include_empty)
        elif include_empty:
            result["recurring"] = Recurring()
        if hasattr(self, "item_ids") and self.item_ids:
            result["itemIds"] = [str(i0) for i0 in self.item_ids]
        elif include_empty:
            result["itemIds"] = []
        if hasattr(self, "features") and self.features:
            result["features"] = [str(i0) for i0 in self.features]
        elif include_empty:
            result["features"] = []
        if hasattr(self, "max_count_per_user") and self.max_count_per_user:
            result["maxCountPerUser"] = int(self.max_count_per_user)
        elif include_empty:
            result["maxCountPerUser"] = int()
        if hasattr(self, "max_count") and self.max_count:
            result["maxCount"] = int(self.max_count)
        elif include_empty:
            result["maxCount"] = int()
        if hasattr(self, "booth_name") and self.booth_name:
            result["boothName"] = str(self.booth_name)
        elif include_empty:
            result["boothName"] = str()
        if hasattr(self, "region") and self.region:
            result["region"] = str(self.region)
        elif include_empty:
            result["region"] = str()
        if hasattr(self, "language") and self.language:
            result["language"] = str(self.language)
        elif include_empty:
            result["language"] = str()
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
        item_type: str,
        title: str,
        region: str,
        language: str,
        app_id: Optional[str] = None,
        app_type: Optional[str] = None,
        base_app_id: Optional[str] = None,
        sku: Optional[str] = None,
        use_count: Optional[int] = None,
        stackable: Optional[bool] = None,
        thumbnail_url: Optional[str] = None,
        target_namespace: Optional[str] = None,
        target_currency_code: Optional[str] = None,
        target_item_id: Optional[str] = None,
        description: Optional[str] = None,
        region_data_item: Optional[RegionDataItem] = None,
        recurring: Optional[Recurring] = None,
        item_ids: Optional[List[str]] = None,
        features: Optional[List[str]] = None,
        max_count_per_user: Optional[int] = None,
        max_count: Optional[int] = None,
        booth_name: Optional[str] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
    ) -> ItemSnapshot:
        instance = cls()
        instance.item_id = item_id
        instance.namespace = namespace
        instance.name = name
        instance.entitlement_type = entitlement_type
        instance.item_type = item_type
        instance.title = title
        instance.region = region
        instance.language = language
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
        if stackable is not None:
            instance.stackable = stackable
        if thumbnail_url is not None:
            instance.thumbnail_url = thumbnail_url
        if target_namespace is not None:
            instance.target_namespace = target_namespace
        if target_currency_code is not None:
            instance.target_currency_code = target_currency_code
        if target_item_id is not None:
            instance.target_item_id = target_item_id
        if description is not None:
            instance.description = description
        if region_data_item is not None:
            instance.region_data_item = region_data_item
        if recurring is not None:
            instance.recurring = recurring
        if item_ids is not None:
            instance.item_ids = item_ids
        if features is not None:
            instance.features = features
        if max_count_per_user is not None:
            instance.max_count_per_user = max_count_per_user
        if max_count is not None:
            instance.max_count = max_count
        if booth_name is not None:
            instance.booth_name = booth_name
        if created_at is not None:
            instance.created_at = created_at
        if updated_at is not None:
            instance.updated_at = updated_at
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ItemSnapshot:
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
        if "stackable" in dict_ and dict_["stackable"] is not None:
            instance.stackable = bool(dict_["stackable"])
        elif include_empty:
            instance.stackable = bool()
        if "itemType" in dict_ and dict_["itemType"] is not None:
            instance.item_type = str(dict_["itemType"])
        elif include_empty:
            instance.item_type = str()
        if "thumbnailUrl" in dict_ and dict_["thumbnailUrl"] is not None:
            instance.thumbnail_url = str(dict_["thumbnailUrl"])
        elif include_empty:
            instance.thumbnail_url = str()
        if "targetNamespace" in dict_ and dict_["targetNamespace"] is not None:
            instance.target_namespace = str(dict_["targetNamespace"])
        elif include_empty:
            instance.target_namespace = str()
        if "targetCurrencyCode" in dict_ and dict_["targetCurrencyCode"] is not None:
            instance.target_currency_code = str(dict_["targetCurrencyCode"])
        elif include_empty:
            instance.target_currency_code = str()
        if "targetItemId" in dict_ and dict_["targetItemId"] is not None:
            instance.target_item_id = str(dict_["targetItemId"])
        elif include_empty:
            instance.target_item_id = str()
        if "title" in dict_ and dict_["title"] is not None:
            instance.title = str(dict_["title"])
        elif include_empty:
            instance.title = str()
        if "description" in dict_ and dict_["description"] is not None:
            instance.description = str(dict_["description"])
        elif include_empty:
            instance.description = str()
        if "regionDataItem" in dict_ and dict_["regionDataItem"] is not None:
            instance.region_data_item = RegionDataItem.create_from_dict(dict_["regionDataItem"], include_empty=include_empty)
        elif include_empty:
            instance.region_data_item = RegionDataItem()
        if "recurring" in dict_ and dict_["recurring"] is not None:
            instance.recurring = Recurring.create_from_dict(dict_["recurring"], include_empty=include_empty)
        elif include_empty:
            instance.recurring = Recurring()
        if "itemIds" in dict_ and dict_["itemIds"] is not None:
            instance.item_ids = [str(i0) for i0 in dict_["itemIds"]]
        elif include_empty:
            instance.item_ids = []
        if "features" in dict_ and dict_["features"] is not None:
            instance.features = [str(i0) for i0 in dict_["features"]]
        elif include_empty:
            instance.features = []
        if "maxCountPerUser" in dict_ and dict_["maxCountPerUser"] is not None:
            instance.max_count_per_user = int(dict_["maxCountPerUser"])
        elif include_empty:
            instance.max_count_per_user = int()
        if "maxCount" in dict_ and dict_["maxCount"] is not None:
            instance.max_count = int(dict_["maxCount"])
        elif include_empty:
            instance.max_count = int()
        if "boothName" in dict_ and dict_["boothName"] is not None:
            instance.booth_name = str(dict_["boothName"])
        elif include_empty:
            instance.booth_name = str()
        if "region" in dict_ and dict_["region"] is not None:
            instance.region = str(dict_["region"])
        elif include_empty:
            instance.region = str()
        if "language" in dict_ and dict_["language"] is not None:
            instance.language = str(dict_["language"])
        elif include_empty:
            instance.language = str()
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
            "stackable": "stackable",
            "itemType": "item_type",
            "thumbnailUrl": "thumbnail_url",
            "targetNamespace": "target_namespace",
            "targetCurrencyCode": "target_currency_code",
            "targetItemId": "target_item_id",
            "title": "title",
            "description": "description",
            "regionDataItem": "region_data_item",
            "recurring": "recurring",
            "itemIds": "item_ids",
            "features": "features",
            "maxCountPerUser": "max_count_per_user",
            "maxCount": "max_count",
            "boothName": "booth_name",
            "region": "region",
            "language": "language",
            "createdAt": "created_at",
            "updatedAt": "updated_at",
        }

    # endregion static methods
