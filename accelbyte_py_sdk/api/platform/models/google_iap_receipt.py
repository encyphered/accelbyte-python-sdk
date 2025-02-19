# Auto-generated at 2021-09-27T17:12:36.380383+08:00
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


class GoogleIAPReceipt(Model):
    """Google IAP receipt

    Properties:
        order_id: (orderId) REQUIRED str

        package_name: (packageName) REQUIRED str

        product_id: (productId) REQUIRED str

        purchase_time: (purchaseTime) REQUIRED int

        purchase_token: (purchaseToken) REQUIRED str

        region: (region) OPTIONAL str

        language: (language) OPTIONAL str
    """

    # region fields

    order_id: str                                                                                  # REQUIRED
    package_name: str                                                                              # REQUIRED
    product_id: str                                                                                # REQUIRED
    purchase_time: int                                                                             # REQUIRED
    purchase_token: str                                                                            # REQUIRED
    region: str                                                                                    # OPTIONAL
    language: str                                                                                  # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_order_id(self, value: str) -> GoogleIAPReceipt:
        self.order_id = value
        return self

    def with_package_name(self, value: str) -> GoogleIAPReceipt:
        self.package_name = value
        return self

    def with_product_id(self, value: str) -> GoogleIAPReceipt:
        self.product_id = value
        return self

    def with_purchase_time(self, value: int) -> GoogleIAPReceipt:
        self.purchase_time = value
        return self

    def with_purchase_token(self, value: str) -> GoogleIAPReceipt:
        self.purchase_token = value
        return self

    def with_region(self, value: str) -> GoogleIAPReceipt:
        self.region = value
        return self

    def with_language(self, value: str) -> GoogleIAPReceipt:
        self.language = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "order_id") and self.order_id:
            result["orderId"] = str(self.order_id)
        elif include_empty:
            result["orderId"] = str()
        if hasattr(self, "package_name") and self.package_name:
            result["packageName"] = str(self.package_name)
        elif include_empty:
            result["packageName"] = str()
        if hasattr(self, "product_id") and self.product_id:
            result["productId"] = str(self.product_id)
        elif include_empty:
            result["productId"] = str()
        if hasattr(self, "purchase_time") and self.purchase_time:
            result["purchaseTime"] = int(self.purchase_time)
        elif include_empty:
            result["purchaseTime"] = int()
        if hasattr(self, "purchase_token") and self.purchase_token:
            result["purchaseToken"] = str(self.purchase_token)
        elif include_empty:
            result["purchaseToken"] = str()
        if hasattr(self, "region") and self.region:
            result["region"] = str(self.region)
        elif include_empty:
            result["region"] = str()
        if hasattr(self, "language") and self.language:
            result["language"] = str(self.language)
        elif include_empty:
            result["language"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        order_id: str,
        package_name: str,
        product_id: str,
        purchase_time: int,
        purchase_token: str,
        region: Optional[str] = None,
        language: Optional[str] = None,
    ) -> GoogleIAPReceipt:
        instance = cls()
        instance.order_id = order_id
        instance.package_name = package_name
        instance.product_id = product_id
        instance.purchase_time = purchase_time
        instance.purchase_token = purchase_token
        if region is not None:
            instance.region = region
        if language is not None:
            instance.language = language
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> GoogleIAPReceipt:
        instance = cls()
        if not dict_:
            return instance
        if "orderId" in dict_ and dict_["orderId"] is not None:
            instance.order_id = str(dict_["orderId"])
        elif include_empty:
            instance.order_id = str()
        if "packageName" in dict_ and dict_["packageName"] is not None:
            instance.package_name = str(dict_["packageName"])
        elif include_empty:
            instance.package_name = str()
        if "productId" in dict_ and dict_["productId"] is not None:
            instance.product_id = str(dict_["productId"])
        elif include_empty:
            instance.product_id = str()
        if "purchaseTime" in dict_ and dict_["purchaseTime"] is not None:
            instance.purchase_time = int(dict_["purchaseTime"])
        elif include_empty:
            instance.purchase_time = int()
        if "purchaseToken" in dict_ and dict_["purchaseToken"] is not None:
            instance.purchase_token = str(dict_["purchaseToken"])
        elif include_empty:
            instance.purchase_token = str()
        if "region" in dict_ and dict_["region"] is not None:
            instance.region = str(dict_["region"])
        elif include_empty:
            instance.region = str()
        if "language" in dict_ and dict_["language"] is not None:
            instance.language = str(dict_["language"])
        elif include_empty:
            instance.language = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "orderId": "order_id",
            "packageName": "package_name",
            "productId": "product_id",
            "purchaseTime": "purchase_time",
            "purchaseToken": "purchase_token",
            "region": "region",
            "language": "language",
        }

    # endregion static methods
