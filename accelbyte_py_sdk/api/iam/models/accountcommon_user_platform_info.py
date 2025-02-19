# Auto-generated at 2021-09-27T17:12:31.498658+08:00
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


class AccountcommonUserPlatformInfo(Model):
    """Accountcommon user platform info

    Properties:
        platform_id: (platformId) REQUIRED str

        platform_user_id: (platformUserId) REQUIRED str

        user_id: (userId) REQUIRED str
    """

    # region fields

    platform_id: str                                                                               # REQUIRED
    platform_user_id: str                                                                          # REQUIRED
    user_id: str                                                                                   # REQUIRED

    # endregion fields

    # region with_x methods

    def with_platform_id(self, value: str) -> AccountcommonUserPlatformInfo:
        self.platform_id = value
        return self

    def with_platform_user_id(self, value: str) -> AccountcommonUserPlatformInfo:
        self.platform_user_id = value
        return self

    def with_user_id(self, value: str) -> AccountcommonUserPlatformInfo:
        self.user_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
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
        platform_id: str,
        platform_user_id: str,
        user_id: str,
    ) -> AccountcommonUserPlatformInfo:
        instance = cls()
        instance.platform_id = platform_id
        instance.platform_user_id = platform_user_id
        instance.user_id = user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AccountcommonUserPlatformInfo:
        instance = cls()
        if not dict_:
            return instance
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
            "platformId": "platform_id",
            "platformUserId": "platform_user_id",
            "userId": "user_id",
        }

    # endregion static methods
