# Auto-generated at 2021-09-27T17:12:36.245782+08:00
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


class RegionDataItem(Model):
    """Region data

    Properties:
        price: (price) REQUIRED int

        discount_percentage: (discountPercentage) OPTIONAL int

        discount_amount: (discountAmount) OPTIONAL int

        discounted_price: (discountedPrice) OPTIONAL int

        currency_code: (currencyCode) REQUIRED str

        currency_type: (currencyType) REQUIRED str

        currency_namespace: (currencyNamespace) REQUIRED str

        trial_price: (trialPrice) OPTIONAL int

        purchase_at: (purchaseAt) OPTIONAL str

        expire_at: (expireAt) OPTIONAL str

        discount_purchase_at: (discountPurchaseAt) OPTIONAL str

        discount_expire_at: (discountExpireAt) OPTIONAL str
    """

    # region fields

    price: int                                                                                     # REQUIRED
    discount_percentage: int                                                                       # OPTIONAL
    discount_amount: int                                                                           # OPTIONAL
    discounted_price: int                                                                          # OPTIONAL
    currency_code: str                                                                             # REQUIRED
    currency_type: str                                                                             # REQUIRED
    currency_namespace: str                                                                        # REQUIRED
    trial_price: int                                                                               # OPTIONAL
    purchase_at: str                                                                               # OPTIONAL
    expire_at: str                                                                                 # OPTIONAL
    discount_purchase_at: str                                                                      # OPTIONAL
    discount_expire_at: str                                                                        # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_price(self, value: int) -> RegionDataItem:
        self.price = value
        return self

    def with_discount_percentage(self, value: int) -> RegionDataItem:
        self.discount_percentage = value
        return self

    def with_discount_amount(self, value: int) -> RegionDataItem:
        self.discount_amount = value
        return self

    def with_discounted_price(self, value: int) -> RegionDataItem:
        self.discounted_price = value
        return self

    def with_currency_code(self, value: str) -> RegionDataItem:
        self.currency_code = value
        return self

    def with_currency_type(self, value: str) -> RegionDataItem:
        self.currency_type = value
        return self

    def with_currency_namespace(self, value: str) -> RegionDataItem:
        self.currency_namespace = value
        return self

    def with_trial_price(self, value: int) -> RegionDataItem:
        self.trial_price = value
        return self

    def with_purchase_at(self, value: str) -> RegionDataItem:
        self.purchase_at = value
        return self

    def with_expire_at(self, value: str) -> RegionDataItem:
        self.expire_at = value
        return self

    def with_discount_purchase_at(self, value: str) -> RegionDataItem:
        self.discount_purchase_at = value
        return self

    def with_discount_expire_at(self, value: str) -> RegionDataItem:
        self.discount_expire_at = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "price") and self.price:
            result["price"] = int(self.price)
        elif include_empty:
            result["price"] = int()
        if hasattr(self, "discount_percentage") and self.discount_percentage:
            result["discountPercentage"] = int(self.discount_percentage)
        elif include_empty:
            result["discountPercentage"] = int()
        if hasattr(self, "discount_amount") and self.discount_amount:
            result["discountAmount"] = int(self.discount_amount)
        elif include_empty:
            result["discountAmount"] = int()
        if hasattr(self, "discounted_price") and self.discounted_price:
            result["discountedPrice"] = int(self.discounted_price)
        elif include_empty:
            result["discountedPrice"] = int()
        if hasattr(self, "currency_code") and self.currency_code:
            result["currencyCode"] = str(self.currency_code)
        elif include_empty:
            result["currencyCode"] = str()
        if hasattr(self, "currency_type") and self.currency_type:
            result["currencyType"] = str(self.currency_type)
        elif include_empty:
            result["currencyType"] = str()
        if hasattr(self, "currency_namespace") and self.currency_namespace:
            result["currencyNamespace"] = str(self.currency_namespace)
        elif include_empty:
            result["currencyNamespace"] = str()
        if hasattr(self, "trial_price") and self.trial_price:
            result["trialPrice"] = int(self.trial_price)
        elif include_empty:
            result["trialPrice"] = int()
        if hasattr(self, "purchase_at") and self.purchase_at:
            result["purchaseAt"] = str(self.purchase_at)
        elif include_empty:
            result["purchaseAt"] = str()
        if hasattr(self, "expire_at") and self.expire_at:
            result["expireAt"] = str(self.expire_at)
        elif include_empty:
            result["expireAt"] = str()
        if hasattr(self, "discount_purchase_at") and self.discount_purchase_at:
            result["discountPurchaseAt"] = str(self.discount_purchase_at)
        elif include_empty:
            result["discountPurchaseAt"] = str()
        if hasattr(self, "discount_expire_at") and self.discount_expire_at:
            result["discountExpireAt"] = str(self.discount_expire_at)
        elif include_empty:
            result["discountExpireAt"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        price: int,
        currency_code: str,
        currency_type: str,
        currency_namespace: str,
        discount_percentage: Optional[int] = None,
        discount_amount: Optional[int] = None,
        discounted_price: Optional[int] = None,
        trial_price: Optional[int] = None,
        purchase_at: Optional[str] = None,
        expire_at: Optional[str] = None,
        discount_purchase_at: Optional[str] = None,
        discount_expire_at: Optional[str] = None,
    ) -> RegionDataItem:
        instance = cls()
        instance.price = price
        instance.currency_code = currency_code
        instance.currency_type = currency_type
        instance.currency_namespace = currency_namespace
        if discount_percentage is not None:
            instance.discount_percentage = discount_percentage
        if discount_amount is not None:
            instance.discount_amount = discount_amount
        if discounted_price is not None:
            instance.discounted_price = discounted_price
        if trial_price is not None:
            instance.trial_price = trial_price
        if purchase_at is not None:
            instance.purchase_at = purchase_at
        if expire_at is not None:
            instance.expire_at = expire_at
        if discount_purchase_at is not None:
            instance.discount_purchase_at = discount_purchase_at
        if discount_expire_at is not None:
            instance.discount_expire_at = discount_expire_at
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> RegionDataItem:
        instance = cls()
        if not dict_:
            return instance
        if "price" in dict_ and dict_["price"] is not None:
            instance.price = int(dict_["price"])
        elif include_empty:
            instance.price = int()
        if "discountPercentage" in dict_ and dict_["discountPercentage"] is not None:
            instance.discount_percentage = int(dict_["discountPercentage"])
        elif include_empty:
            instance.discount_percentage = int()
        if "discountAmount" in dict_ and dict_["discountAmount"] is not None:
            instance.discount_amount = int(dict_["discountAmount"])
        elif include_empty:
            instance.discount_amount = int()
        if "discountedPrice" in dict_ and dict_["discountedPrice"] is not None:
            instance.discounted_price = int(dict_["discountedPrice"])
        elif include_empty:
            instance.discounted_price = int()
        if "currencyCode" in dict_ and dict_["currencyCode"] is not None:
            instance.currency_code = str(dict_["currencyCode"])
        elif include_empty:
            instance.currency_code = str()
        if "currencyType" in dict_ and dict_["currencyType"] is not None:
            instance.currency_type = str(dict_["currencyType"])
        elif include_empty:
            instance.currency_type = str()
        if "currencyNamespace" in dict_ and dict_["currencyNamespace"] is not None:
            instance.currency_namespace = str(dict_["currencyNamespace"])
        elif include_empty:
            instance.currency_namespace = str()
        if "trialPrice" in dict_ and dict_["trialPrice"] is not None:
            instance.trial_price = int(dict_["trialPrice"])
        elif include_empty:
            instance.trial_price = int()
        if "purchaseAt" in dict_ and dict_["purchaseAt"] is not None:
            instance.purchase_at = str(dict_["purchaseAt"])
        elif include_empty:
            instance.purchase_at = str()
        if "expireAt" in dict_ and dict_["expireAt"] is not None:
            instance.expire_at = str(dict_["expireAt"])
        elif include_empty:
            instance.expire_at = str()
        if "discountPurchaseAt" in dict_ and dict_["discountPurchaseAt"] is not None:
            instance.discount_purchase_at = str(dict_["discountPurchaseAt"])
        elif include_empty:
            instance.discount_purchase_at = str()
        if "discountExpireAt" in dict_ and dict_["discountExpireAt"] is not None:
            instance.discount_expire_at = str(dict_["discountExpireAt"])
        elif include_empty:
            instance.discount_expire_at = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "price": "price",
            "discountPercentage": "discount_percentage",
            "discountAmount": "discount_amount",
            "discountedPrice": "discounted_price",
            "currencyCode": "currency_code",
            "currencyType": "currency_type",
            "currencyNamespace": "currency_namespace",
            "trialPrice": "trial_price",
            "purchaseAt": "purchase_at",
            "expireAt": "expire_at",
            "discountPurchaseAt": "discount_purchase_at",
            "discountExpireAt": "discount_expire_at",
        }

    # endregion static methods
