# Auto-generated at 2021-09-21T14:10:34.718719+08:00
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


class AccountcommonPlatformAccount(Model):
    """Accountcommon platform account

    Properties:
        namespace: (namespace) REQUIRED str

        platform_user_id: (platformUserId) REQUIRED str
    """

    # region fields

    namespace: str                                                                                 # REQUIRED
    platform_user_id: str                                                                          # REQUIRED

    # endregion fields

    # region with_x methods

    def with_namespace(self, value: str) -> AccountcommonPlatformAccount:
        self.namespace = value
        return self

    def with_platform_user_id(self, value: str) -> AccountcommonPlatformAccount:
        self.platform_user_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "platform_user_id") and self.platform_user_id:
            result["platformUserId"] = str(self.platform_user_id)
        elif include_empty:
            result["platformUserId"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        namespace: str,
        platform_user_id: str,
    ) -> AccountcommonPlatformAccount:
        instance = cls()
        instance.namespace = namespace
        instance.platform_user_id = platform_user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AccountcommonPlatformAccount:
        instance = cls()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "platformUserId" in dict_ and dict_["platformUserId"] is not None:
            instance.platform_user_id = str(dict_["platformUserId"])
        elif include_empty:
            instance.platform_user_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "platformUserId": "platform_user_id",
        }

    # endregion static methods