# Auto-generated at 2021-09-27T17:12:31.495428+08:00
# from: Justice Iam Service (4.1.0)

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


class AccountcommonUserLinkedPlatformV3(Model):
    """Accountcommon user linked platform V3

    Properties:
        account_group: (accountGroup) REQUIRED str

        display_name: (displayName) OPTIONAL str

        email_address: (emailAddress) OPTIONAL str

        linked_at: (linkedAt) REQUIRED str

        namespace: (namespace) REQUIRED str

        origin_namespace: (originNamespace) REQUIRED str

        platform_id: (platformId) OPTIONAL str

        platform_user_id: (platformUserId) OPTIONAL str

        user_id: (userId) REQUIRED str
    """

    # region fields

    account_group: str                                                                             # REQUIRED
    display_name: str                                                                              # OPTIONAL
    email_address: str                                                                             # OPTIONAL
    linked_at: str                                                                                 # REQUIRED
    namespace: str                                                                                 # REQUIRED
    origin_namespace: str                                                                          # REQUIRED
    platform_id: str                                                                               # OPTIONAL
    platform_user_id: str                                                                          # OPTIONAL
    user_id: str                                                                                   # REQUIRED

    # endregion fields

    # region with_x methods

    def with_account_group(self, value: str) -> AccountcommonUserLinkedPlatformV3:
        self.account_group = value
        return self

    def with_display_name(self, value: str) -> AccountcommonUserLinkedPlatformV3:
        self.display_name = value
        return self

    def with_email_address(self, value: str) -> AccountcommonUserLinkedPlatformV3:
        self.email_address = value
        return self

    def with_linked_at(self, value: str) -> AccountcommonUserLinkedPlatformV3:
        self.linked_at = value
        return self

    def with_namespace(self, value: str) -> AccountcommonUserLinkedPlatformV3:
        self.namespace = value
        return self

    def with_origin_namespace(self, value: str) -> AccountcommonUserLinkedPlatformV3:
        self.origin_namespace = value
        return self

    def with_platform_id(self, value: str) -> AccountcommonUserLinkedPlatformV3:
        self.platform_id = value
        return self

    def with_platform_user_id(self, value: str) -> AccountcommonUserLinkedPlatformV3:
        self.platform_user_id = value
        return self

    def with_user_id(self, value: str) -> AccountcommonUserLinkedPlatformV3:
        self.user_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "account_group") and self.account_group:
            result["accountGroup"] = str(self.account_group)
        elif include_empty:
            result["accountGroup"] = str()
        if hasattr(self, "display_name") and self.display_name:
            result["displayName"] = str(self.display_name)
        elif include_empty:
            result["displayName"] = str()
        if hasattr(self, "email_address") and self.email_address:
            result["emailAddress"] = str(self.email_address)
        elif include_empty:
            result["emailAddress"] = str()
        if hasattr(self, "linked_at") and self.linked_at:
            result["linkedAt"] = str(self.linked_at)
        elif include_empty:
            result["linkedAt"] = str()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "origin_namespace") and self.origin_namespace:
            result["originNamespace"] = str(self.origin_namespace)
        elif include_empty:
            result["originNamespace"] = str()
        if hasattr(self, "platform_id") and self.platform_id:
            result["platformId"] = str(self.platform_id)
        elif include_empty:
            result["platformId"] = str()
        if hasattr(self, "platform_user_id") and self.platform_user_id:
            result["platformUserId"] = str(self.platform_user_id)
        elif include_empty:
            result["platformUserId"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        account_group: str,
        linked_at: str,
        namespace: str,
        origin_namespace: str,
        user_id: str,
        display_name: Optional[str] = None,
        email_address: Optional[str] = None,
        platform_id: Optional[str] = None,
        platform_user_id: Optional[str] = None,
    ) -> AccountcommonUserLinkedPlatformV3:
        instance = cls()
        instance.account_group = account_group
        instance.linked_at = linked_at
        instance.namespace = namespace
        instance.origin_namespace = origin_namespace
        instance.user_id = user_id
        if display_name is not None:
            instance.display_name = display_name
        if email_address is not None:
            instance.email_address = email_address
        if platform_id is not None:
            instance.platform_id = platform_id
        if platform_user_id is not None:
            instance.platform_user_id = platform_user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AccountcommonUserLinkedPlatformV3:
        instance = cls()
        if not dict_:
            return instance
        if "accountGroup" in dict_ and dict_["accountGroup"] is not None:
            instance.account_group = str(dict_["accountGroup"])
        elif include_empty:
            instance.account_group = str()
        if "displayName" in dict_ and dict_["displayName"] is not None:
            instance.display_name = str(dict_["displayName"])
        elif include_empty:
            instance.display_name = str()
        if "emailAddress" in dict_ and dict_["emailAddress"] is not None:
            instance.email_address = str(dict_["emailAddress"])
        elif include_empty:
            instance.email_address = str()
        if "linkedAt" in dict_ and dict_["linkedAt"] is not None:
            instance.linked_at = str(dict_["linkedAt"])
        elif include_empty:
            instance.linked_at = str()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "originNamespace" in dict_ and dict_["originNamespace"] is not None:
            instance.origin_namespace = str(dict_["originNamespace"])
        elif include_empty:
            instance.origin_namespace = str()
        if "platformId" in dict_ and dict_["platformId"] is not None:
            instance.platform_id = str(dict_["platformId"])
        elif include_empty:
            instance.platform_id = str()
        if "platformUserId" in dict_ and dict_["platformUserId"] is not None:
            instance.platform_user_id = str(dict_["platformUserId"])
        elif include_empty:
            instance.platform_user_id = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "accountGroup": "account_group",
            "displayName": "display_name",
            "emailAddress": "email_address",
            "linkedAt": "linked_at",
            "namespace": "namespace",
            "originNamespace": "origin_namespace",
            "platformId": "platform_id",
            "platformUserId": "platform_user_id",
            "userId": "user_id",
        }

    # endregion static methods
