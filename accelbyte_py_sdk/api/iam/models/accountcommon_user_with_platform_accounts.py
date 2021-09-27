# Auto-generated at 2021-09-27T17:12:31.506577+08:00
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

from ..models.accountcommon_platform_account import AccountcommonPlatformAccount


class AccountcommonUserWithPlatformAccounts(Model):
    """Accountcommon user with platform accounts

    Properties:
        linked_platforms: (linkedPlatforms) REQUIRED List[AccountcommonPlatformAccount]

        namespace: (namespace) REQUIRED str

        user_id: (userId) REQUIRED str
    """

    # region fields

    linked_platforms: List[AccountcommonPlatformAccount]                                           # REQUIRED
    namespace: str                                                                                 # REQUIRED
    user_id: str                                                                                   # REQUIRED

    # endregion fields

    # region with_x methods

    def with_linked_platforms(self, value: List[AccountcommonPlatformAccount]) -> AccountcommonUserWithPlatformAccounts:
        self.linked_platforms = value
        return self

    def with_namespace(self, value: str) -> AccountcommonUserWithPlatformAccounts:
        self.namespace = value
        return self

    def with_user_id(self, value: str) -> AccountcommonUserWithPlatformAccounts:
        self.user_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "linked_platforms") and self.linked_platforms:
            result["linkedPlatforms"] = [i0.to_dict(include_empty=include_empty) for i0 in self.linked_platforms]
        elif include_empty:
            result["linkedPlatforms"] = []
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
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
        linked_platforms: List[AccountcommonPlatformAccount],
        namespace: str,
        user_id: str,
    ) -> AccountcommonUserWithPlatformAccounts:
        instance = cls()
        instance.linked_platforms = linked_platforms
        instance.namespace = namespace
        instance.user_id = user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AccountcommonUserWithPlatformAccounts:
        instance = cls()
        if not dict_:
            return instance
        if "linkedPlatforms" in dict_ and dict_["linkedPlatforms"] is not None:
            instance.linked_platforms = [AccountcommonPlatformAccount.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["linkedPlatforms"]]
        elif include_empty:
            instance.linked_platforms = []
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "linkedPlatforms": "linked_platforms",
            "namespace": "namespace",
            "userId": "user_id",
        }

    # endregion static methods
