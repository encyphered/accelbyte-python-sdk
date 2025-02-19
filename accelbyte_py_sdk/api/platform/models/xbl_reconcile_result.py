# Auto-generated at 2021-09-27T17:12:36.383504+08:00
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


class XblReconcileResult(Model):
    """Xbl reconcile result

    Properties:
        transaction_id: (transactionId) OPTIONAL str

        xbox_product_id: (xboxProductId) OPTIONAL str

        item_id: (itemId) OPTIONAL str

        sku: (sku) OPTIONAL str

        iap_order_status: (iapOrderStatus) OPTIONAL str
    """

    # region fields

    transaction_id: str                                                                            # OPTIONAL
    xbox_product_id: str                                                                           # OPTIONAL
    item_id: str                                                                                   # OPTIONAL
    sku: str                                                                                       # OPTIONAL
    iap_order_status: str                                                                          # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_transaction_id(self, value: str) -> XblReconcileResult:
        self.transaction_id = value
        return self

    def with_xbox_product_id(self, value: str) -> XblReconcileResult:
        self.xbox_product_id = value
        return self

    def with_item_id(self, value: str) -> XblReconcileResult:
        self.item_id = value
        return self

    def with_sku(self, value: str) -> XblReconcileResult:
        self.sku = value
        return self

    def with_iap_order_status(self, value: str) -> XblReconcileResult:
        self.iap_order_status = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "transaction_id") and self.transaction_id:
            result["transactionId"] = str(self.transaction_id)
        elif include_empty:
            result["transactionId"] = str()
        if hasattr(self, "xbox_product_id") and self.xbox_product_id:
            result["xboxProductId"] = str(self.xbox_product_id)
        elif include_empty:
            result["xboxProductId"] = str()
        if hasattr(self, "item_id") and self.item_id:
            result["itemId"] = str(self.item_id)
        elif include_empty:
            result["itemId"] = str()
        if hasattr(self, "sku") and self.sku:
            result["sku"] = str(self.sku)
        elif include_empty:
            result["sku"] = str()
        if hasattr(self, "iap_order_status") and self.iap_order_status:
            result["iapOrderStatus"] = str(self.iap_order_status)
        elif include_empty:
            result["iapOrderStatus"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        transaction_id: Optional[str] = None,
        xbox_product_id: Optional[str] = None,
        item_id: Optional[str] = None,
        sku: Optional[str] = None,
        iap_order_status: Optional[str] = None,
    ) -> XblReconcileResult:
        instance = cls()
        if transaction_id is not None:
            instance.transaction_id = transaction_id
        if xbox_product_id is not None:
            instance.xbox_product_id = xbox_product_id
        if item_id is not None:
            instance.item_id = item_id
        if sku is not None:
            instance.sku = sku
        if iap_order_status is not None:
            instance.iap_order_status = iap_order_status
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> XblReconcileResult:
        instance = cls()
        if not dict_:
            return instance
        if "transactionId" in dict_ and dict_["transactionId"] is not None:
            instance.transaction_id = str(dict_["transactionId"])
        elif include_empty:
            instance.transaction_id = str()
        if "xboxProductId" in dict_ and dict_["xboxProductId"] is not None:
            instance.xbox_product_id = str(dict_["xboxProductId"])
        elif include_empty:
            instance.xbox_product_id = str()
        if "itemId" in dict_ and dict_["itemId"] is not None:
            instance.item_id = str(dict_["itemId"])
        elif include_empty:
            instance.item_id = str()
        if "sku" in dict_ and dict_["sku"] is not None:
            instance.sku = str(dict_["sku"])
        elif include_empty:
            instance.sku = str()
        if "iapOrderStatus" in dict_ and dict_["iapOrderStatus"] is not None:
            instance.iap_order_status = str(dict_["iapOrderStatus"])
        elif include_empty:
            instance.iap_order_status = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "transactionId": "transaction_id",
            "xboxProductId": "xbox_product_id",
            "itemId": "item_id",
            "sku": "sku",
            "iapOrderStatus": "iap_order_status",
        }

    # endregion static methods
