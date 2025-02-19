# Auto-generated at 2021-09-27T17:12:36.339502+08:00
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


class PaymentNotificationInfo(Model):
    """Payment notification info

    Properties:
        id_: (id) REQUIRED str

        payment_order_no: (paymentOrderNo) REQUIRED str

        external_id: (externalId) OPTIONAL str

        namespace: (namespace) REQUIRED str

        notification_type: (notificationType) REQUIRED str

        notification: (notification) REQUIRED Dict[str, Any]

        status: (status) REQUIRED str

        notification_source: (notificationSource) REQUIRED str

        status_reason: (statusReason) OPTIONAL str

        created_at: (createdAt) REQUIRED str

        updated_at: (updatedAt) REQUIRED str
    """

    # region fields

    id_: str                                                                                       # REQUIRED
    payment_order_no: str                                                                          # REQUIRED
    external_id: str                                                                               # OPTIONAL
    namespace: str                                                                                 # REQUIRED
    notification_type: str                                                                         # REQUIRED
    notification: Dict[str, Any]                                                                   # REQUIRED
    status: str                                                                                    # REQUIRED
    notification_source: str                                                                       # REQUIRED
    status_reason: str                                                                             # OPTIONAL
    created_at: str                                                                                # REQUIRED
    updated_at: str                                                                                # REQUIRED

    # endregion fields

    # region with_x methods

    def with_id(self, value: str) -> PaymentNotificationInfo:
        self.id_ = value
        return self

    def with_payment_order_no(self, value: str) -> PaymentNotificationInfo:
        self.payment_order_no = value
        return self

    def with_external_id(self, value: str) -> PaymentNotificationInfo:
        self.external_id = value
        return self

    def with_namespace(self, value: str) -> PaymentNotificationInfo:
        self.namespace = value
        return self

    def with_notification_type(self, value: str) -> PaymentNotificationInfo:
        self.notification_type = value
        return self

    def with_notification(self, value: Dict[str, Any]) -> PaymentNotificationInfo:
        self.notification = value
        return self

    def with_status(self, value: str) -> PaymentNotificationInfo:
        self.status = value
        return self

    def with_notification_source(self, value: str) -> PaymentNotificationInfo:
        self.notification_source = value
        return self

    def with_status_reason(self, value: str) -> PaymentNotificationInfo:
        self.status_reason = value
        return self

    def with_created_at(self, value: str) -> PaymentNotificationInfo:
        self.created_at = value
        return self

    def with_updated_at(self, value: str) -> PaymentNotificationInfo:
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
        if hasattr(self, "payment_order_no") and self.payment_order_no:
            result["paymentOrderNo"] = str(self.payment_order_no)
        elif include_empty:
            result["paymentOrderNo"] = str()
        if hasattr(self, "external_id") and self.external_id:
            result["externalId"] = str(self.external_id)
        elif include_empty:
            result["externalId"] = str()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "notification_type") and self.notification_type:
            result["notificationType"] = str(self.notification_type)
        elif include_empty:
            result["notificationType"] = str()
        if hasattr(self, "notification") and self.notification:
            result["notification"] = {str(k0): v0 for k0, v0 in self.notification.items()}
        elif include_empty:
            result["notification"] = {}
        if hasattr(self, "status") and self.status:
            result["status"] = str(self.status)
        elif include_empty:
            result["status"] = str()
        if hasattr(self, "notification_source") and self.notification_source:
            result["notificationSource"] = str(self.notification_source)
        elif include_empty:
            result["notificationSource"] = str()
        if hasattr(self, "status_reason") and self.status_reason:
            result["statusReason"] = str(self.status_reason)
        elif include_empty:
            result["statusReason"] = str()
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
        payment_order_no: str,
        namespace: str,
        notification_type: str,
        notification: Dict[str, Any],
        status: str,
        notification_source: str,
        created_at: str,
        updated_at: str,
        external_id: Optional[str] = None,
        status_reason: Optional[str] = None,
    ) -> PaymentNotificationInfo:
        instance = cls()
        instance.id_ = id_
        instance.payment_order_no = payment_order_no
        instance.namespace = namespace
        instance.notification_type = notification_type
        instance.notification = notification
        instance.status = status
        instance.notification_source = notification_source
        instance.created_at = created_at
        instance.updated_at = updated_at
        if external_id is not None:
            instance.external_id = external_id
        if status_reason is not None:
            instance.status_reason = status_reason
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> PaymentNotificationInfo:
        instance = cls()
        if not dict_:
            return instance
        if "id" in dict_ and dict_["id"] is not None:
            instance.id_ = str(dict_["id"])
        elif include_empty:
            instance.id_ = str()
        if "paymentOrderNo" in dict_ and dict_["paymentOrderNo"] is not None:
            instance.payment_order_no = str(dict_["paymentOrderNo"])
        elif include_empty:
            instance.payment_order_no = str()
        if "externalId" in dict_ and dict_["externalId"] is not None:
            instance.external_id = str(dict_["externalId"])
        elif include_empty:
            instance.external_id = str()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "notificationType" in dict_ and dict_["notificationType"] is not None:
            instance.notification_type = str(dict_["notificationType"])
        elif include_empty:
            instance.notification_type = str()
        if "notification" in dict_ and dict_["notification"] is not None:
            instance.notification = {str(k0): v0 for k0, v0 in dict_["notification"].items()}
        elif include_empty:
            instance.notification = {}
        if "status" in dict_ and dict_["status"] is not None:
            instance.status = str(dict_["status"])
        elif include_empty:
            instance.status = str()
        if "notificationSource" in dict_ and dict_["notificationSource"] is not None:
            instance.notification_source = str(dict_["notificationSource"])
        elif include_empty:
            instance.notification_source = str()
        if "statusReason" in dict_ and dict_["statusReason"] is not None:
            instance.status_reason = str(dict_["statusReason"])
        elif include_empty:
            instance.status_reason = str()
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
            "paymentOrderNo": "payment_order_no",
            "externalId": "external_id",
            "namespace": "namespace",
            "notificationType": "notification_type",
            "notification": "notification",
            "status": "status",
            "notificationSource": "notification_source",
            "statusReason": "status_reason",
            "createdAt": "created_at",
            "updatedAt": "updated_at",
        }

    # endregion static methods
