# Auto-generated at 2021-09-27T17:12:36.127240+08:00
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


class EntitlementHistoryInfo(Model):
    """Entitlement history info

    Properties:
        entitlement_id: (entitlementId) REQUIRED str

        namespace: (namespace) REQUIRED str

        action: (action) REQUIRED str

        operator: (operator) REQUIRED str

        user_id: (userId) REQUIRED str

        use_count: (useCount) OPTIONAL int

        quantity: (quantity) OPTIONAL int

        created_at: (createdAt) REQUIRED str

        updated_at: (updatedAt) REQUIRED str
    """

    # region fields

    entitlement_id: str                                                                            # REQUIRED
    namespace: str                                                                                 # REQUIRED
    action: str                                                                                    # REQUIRED
    operator: str                                                                                  # REQUIRED
    user_id: str                                                                                   # REQUIRED
    use_count: int                                                                                 # OPTIONAL
    quantity: int                                                                                  # OPTIONAL
    created_at: str                                                                                # REQUIRED
    updated_at: str                                                                                # REQUIRED

    # endregion fields

    # region with_x methods

    def with_entitlement_id(self, value: str) -> EntitlementHistoryInfo:
        self.entitlement_id = value
        return self

    def with_namespace(self, value: str) -> EntitlementHistoryInfo:
        self.namespace = value
        return self

    def with_action(self, value: str) -> EntitlementHistoryInfo:
        self.action = value
        return self

    def with_operator(self, value: str) -> EntitlementHistoryInfo:
        self.operator = value
        return self

    def with_user_id(self, value: str) -> EntitlementHistoryInfo:
        self.user_id = value
        return self

    def with_use_count(self, value: int) -> EntitlementHistoryInfo:
        self.use_count = value
        return self

    def with_quantity(self, value: int) -> EntitlementHistoryInfo:
        self.quantity = value
        return self

    def with_created_at(self, value: str) -> EntitlementHistoryInfo:
        self.created_at = value
        return self

    def with_updated_at(self, value: str) -> EntitlementHistoryInfo:
        self.updated_at = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "entitlement_id") and self.entitlement_id:
            result["entitlementId"] = str(self.entitlement_id)
        elif include_empty:
            result["entitlementId"] = str()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "action") and self.action:
            result["action"] = str(self.action)
        elif include_empty:
            result["action"] = str()
        if hasattr(self, "operator") and self.operator:
            result["operator"] = str(self.operator)
        elif include_empty:
            result["operator"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        if hasattr(self, "use_count") and self.use_count:
            result["useCount"] = int(self.use_count)
        elif include_empty:
            result["useCount"] = int()
        if hasattr(self, "quantity") and self.quantity:
            result["quantity"] = int(self.quantity)
        elif include_empty:
            result["quantity"] = int()
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
        entitlement_id: str,
        namespace: str,
        action: str,
        operator: str,
        user_id: str,
        created_at: str,
        updated_at: str,
        use_count: Optional[int] = None,
        quantity: Optional[int] = None,
    ) -> EntitlementHistoryInfo:
        instance = cls()
        instance.entitlement_id = entitlement_id
        instance.namespace = namespace
        instance.action = action
        instance.operator = operator
        instance.user_id = user_id
        instance.created_at = created_at
        instance.updated_at = updated_at
        if use_count is not None:
            instance.use_count = use_count
        if quantity is not None:
            instance.quantity = quantity
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> EntitlementHistoryInfo:
        instance = cls()
        if not dict_:
            return instance
        if "entitlementId" in dict_ and dict_["entitlementId"] is not None:
            instance.entitlement_id = str(dict_["entitlementId"])
        elif include_empty:
            instance.entitlement_id = str()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "action" in dict_ and dict_["action"] is not None:
            instance.action = str(dict_["action"])
        elif include_empty:
            instance.action = str()
        if "operator" in dict_ and dict_["operator"] is not None:
            instance.operator = str(dict_["operator"])
        elif include_empty:
            instance.operator = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        if "useCount" in dict_ and dict_["useCount"] is not None:
            instance.use_count = int(dict_["useCount"])
        elif include_empty:
            instance.use_count = int()
        if "quantity" in dict_ and dict_["quantity"] is not None:
            instance.quantity = int(dict_["quantity"])
        elif include_empty:
            instance.quantity = int()
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
            "entitlementId": "entitlement_id",
            "namespace": "namespace",
            "action": "action",
            "operator": "operator",
            "userId": "user_id",
            "useCount": "use_count",
            "quantity": "quantity",
            "createdAt": "created_at",
            "updatedAt": "updated_at",
        }

    # endregion static methods
