# Auto-generated at 2021-09-27T17:12:36.148329+08:00
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

from ..models.credit_summary import CreditSummary
from ..models.entitlement_summary import EntitlementSummary
from ..models.fulfillment_error import FulfillmentError
from ..models.fulfillment_item import FulfillmentItem


class FulfillmentHistoryInfo(Model):
    """Fulfillment history info

    Properties:
        id_: (id) REQUIRED str

        namespace: (namespace) REQUIRED str

        user_id: (userId) REQUIRED str

        order_no: (orderNo) OPTIONAL str

        code: (code) OPTIONAL str

        fulfill_items: (fulfillItems) OPTIONAL List[FulfillmentItem]

        granted_item_ids: (grantedItemIds) OPTIONAL List[str]

        entitlement_summaries: (entitlementSummaries) OPTIONAL List[EntitlementSummary]

        credit_summaries: (creditSummaries) OPTIONAL List[CreditSummary]

        status: (status) REQUIRED str

        fulfillment_error: (fulfillmentError) OPTIONAL FulfillmentError

        created_at: (createdAt) REQUIRED str

        updated_at: (updatedAt) REQUIRED str
    """

    # region fields

    id_: str                                                                                       # REQUIRED
    namespace: str                                                                                 # REQUIRED
    user_id: str                                                                                   # REQUIRED
    order_no: str                                                                                  # OPTIONAL
    code: str                                                                                      # OPTIONAL
    fulfill_items: List[FulfillmentItem]                                                           # OPTIONAL
    granted_item_ids: List[str]                                                                    # OPTIONAL
    entitlement_summaries: List[EntitlementSummary]                                                # OPTIONAL
    credit_summaries: List[CreditSummary]                                                          # OPTIONAL
    status: str                                                                                    # REQUIRED
    fulfillment_error: FulfillmentError                                                            # OPTIONAL
    created_at: str                                                                                # REQUIRED
    updated_at: str                                                                                # REQUIRED

    # endregion fields

    # region with_x methods

    def with_id(self, value: str) -> FulfillmentHistoryInfo:
        self.id_ = value
        return self

    def with_namespace(self, value: str) -> FulfillmentHistoryInfo:
        self.namespace = value
        return self

    def with_user_id(self, value: str) -> FulfillmentHistoryInfo:
        self.user_id = value
        return self

    def with_order_no(self, value: str) -> FulfillmentHistoryInfo:
        self.order_no = value
        return self

    def with_code(self, value: str) -> FulfillmentHistoryInfo:
        self.code = value
        return self

    def with_fulfill_items(self, value: List[FulfillmentItem]) -> FulfillmentHistoryInfo:
        self.fulfill_items = value
        return self

    def with_granted_item_ids(self, value: List[str]) -> FulfillmentHistoryInfo:
        self.granted_item_ids = value
        return self

    def with_entitlement_summaries(self, value: List[EntitlementSummary]) -> FulfillmentHistoryInfo:
        self.entitlement_summaries = value
        return self

    def with_credit_summaries(self, value: List[CreditSummary]) -> FulfillmentHistoryInfo:
        self.credit_summaries = value
        return self

    def with_status(self, value: str) -> FulfillmentHistoryInfo:
        self.status = value
        return self

    def with_fulfillment_error(self, value: FulfillmentError) -> FulfillmentHistoryInfo:
        self.fulfillment_error = value
        return self

    def with_created_at(self, value: str) -> FulfillmentHistoryInfo:
        self.created_at = value
        return self

    def with_updated_at(self, value: str) -> FulfillmentHistoryInfo:
        self.updated_at = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "id_") and self.id_:
            result["id"] = str(self.id_)
        elif include_empty:
            result["id"] = str()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        if hasattr(self, "order_no") and self.order_no:
            result["orderNo"] = str(self.order_no)
        elif include_empty:
            result["orderNo"] = str()
        if hasattr(self, "code") and self.code:
            result["code"] = str(self.code)
        elif include_empty:
            result["code"] = str()
        if hasattr(self, "fulfill_items") and self.fulfill_items:
            result["fulfillItems"] = [i0.to_dict(include_empty=include_empty) for i0 in self.fulfill_items]
        elif include_empty:
            result["fulfillItems"] = []
        if hasattr(self, "granted_item_ids") and self.granted_item_ids:
            result["grantedItemIds"] = [str(i0) for i0 in self.granted_item_ids]
        elif include_empty:
            result["grantedItemIds"] = []
        if hasattr(self, "entitlement_summaries") and self.entitlement_summaries:
            result["entitlementSummaries"] = [i0.to_dict(include_empty=include_empty) for i0 in self.entitlement_summaries]
        elif include_empty:
            result["entitlementSummaries"] = []
        if hasattr(self, "credit_summaries") and self.credit_summaries:
            result["creditSummaries"] = [i0.to_dict(include_empty=include_empty) for i0 in self.credit_summaries]
        elif include_empty:
            result["creditSummaries"] = []
        if hasattr(self, "status") and self.status:
            result["status"] = str(self.status)
        elif include_empty:
            result["status"] = str()
        if hasattr(self, "fulfillment_error") and self.fulfillment_error:
            result["fulfillmentError"] = self.fulfillment_error.to_dict(include_empty=include_empty)
        elif include_empty:
            result["fulfillmentError"] = FulfillmentError()
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
        id_: str,
        namespace: str,
        user_id: str,
        status: str,
        created_at: str,
        updated_at: str,
        order_no: Optional[str] = None,
        code: Optional[str] = None,
        fulfill_items: Optional[List[FulfillmentItem]] = None,
        granted_item_ids: Optional[List[str]] = None,
        entitlement_summaries: Optional[List[EntitlementSummary]] = None,
        credit_summaries: Optional[List[CreditSummary]] = None,
        fulfillment_error: Optional[FulfillmentError] = None,
    ) -> FulfillmentHistoryInfo:
        instance = cls()
        instance.id_ = id_
        instance.namespace = namespace
        instance.user_id = user_id
        instance.status = status
        instance.created_at = created_at
        instance.updated_at = updated_at
        if order_no is not None:
            instance.order_no = order_no
        if code is not None:
            instance.code = code
        if fulfill_items is not None:
            instance.fulfill_items = fulfill_items
        if granted_item_ids is not None:
            instance.granted_item_ids = granted_item_ids
        if entitlement_summaries is not None:
            instance.entitlement_summaries = entitlement_summaries
        if credit_summaries is not None:
            instance.credit_summaries = credit_summaries
        if fulfillment_error is not None:
            instance.fulfillment_error = fulfillment_error
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> FulfillmentHistoryInfo:
        instance = cls()
        if not dict_:
            return instance
        if "id" in dict_ and dict_["id"] is not None:
            instance.id_ = str(dict_["id"])
        elif include_empty:
            instance.id_ = str()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        if "orderNo" in dict_ and dict_["orderNo"] is not None:
            instance.order_no = str(dict_["orderNo"])
        elif include_empty:
            instance.order_no = str()
        if "code" in dict_ and dict_["code"] is not None:
            instance.code = str(dict_["code"])
        elif include_empty:
            instance.code = str()
        if "fulfillItems" in dict_ and dict_["fulfillItems"] is not None:
            instance.fulfill_items = [FulfillmentItem.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["fulfillItems"]]
        elif include_empty:
            instance.fulfill_items = []
        if "grantedItemIds" in dict_ and dict_["grantedItemIds"] is not None:
            instance.granted_item_ids = [str(i0) for i0 in dict_["grantedItemIds"]]
        elif include_empty:
            instance.granted_item_ids = []
        if "entitlementSummaries" in dict_ and dict_["entitlementSummaries"] is not None:
            instance.entitlement_summaries = [EntitlementSummary.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["entitlementSummaries"]]
        elif include_empty:
            instance.entitlement_summaries = []
        if "creditSummaries" in dict_ and dict_["creditSummaries"] is not None:
            instance.credit_summaries = [CreditSummary.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["creditSummaries"]]
        elif include_empty:
            instance.credit_summaries = []
        if "status" in dict_ and dict_["status"] is not None:
            instance.status = str(dict_["status"])
        elif include_empty:
            instance.status = str()
        if "fulfillmentError" in dict_ and dict_["fulfillmentError"] is not None:
            instance.fulfillment_error = FulfillmentError.create_from_dict(dict_["fulfillmentError"], include_empty=include_empty)
        elif include_empty:
            instance.fulfillment_error = FulfillmentError()
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
            "id": "id_",
            "namespace": "namespace",
            "userId": "user_id",
            "orderNo": "order_no",
            "code": "code",
            "fulfillItems": "fulfill_items",
            "grantedItemIds": "granted_item_ids",
            "entitlementSummaries": "entitlement_summaries",
            "creditSummaries": "credit_summaries",
            "status": "status",
            "fulfillmentError": "fulfillment_error",
            "createdAt": "created_at",
            "updatedAt": "updated_at",
        }

    # endregion static methods
