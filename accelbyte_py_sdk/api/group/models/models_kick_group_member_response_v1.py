# Auto-generated at 2021-09-27T17:12:37.823600+08:00
# from: Justice Group Service (2.4.0)

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


class ModelsKickGroupMemberResponseV1(Model):
    """Models kick group member response V1

    Properties:
        group_id: (groupId) REQUIRED str

        kicked_user_id: (kickedUserId) REQUIRED str
    """

    # region fields

    group_id: str                                                                                  # REQUIRED
    kicked_user_id: str                                                                            # REQUIRED

    # endregion fields

    # region with_x methods

    def with_group_id(self, value: str) -> ModelsKickGroupMemberResponseV1:
        self.group_id = value
        return self

    def with_kicked_user_id(self, value: str) -> ModelsKickGroupMemberResponseV1:
        self.kicked_user_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "group_id") and self.group_id:
            result["groupId"] = str(self.group_id)
        elif include_empty:
            result["groupId"] = str()
        if hasattr(self, "kicked_user_id") and self.kicked_user_id:
            result["kickedUserId"] = str(self.kicked_user_id)
        elif include_empty:
            result["kickedUserId"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        group_id: str,
        kicked_user_id: str,
    ) -> ModelsKickGroupMemberResponseV1:
        instance = cls()
        instance.group_id = group_id
        instance.kicked_user_id = kicked_user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsKickGroupMemberResponseV1:
        instance = cls()
        if not dict_:
            return instance
        if "groupId" in dict_ and dict_["groupId"] is not None:
            instance.group_id = str(dict_["groupId"])
        elif include_empty:
            instance.group_id = str()
        if "kickedUserId" in dict_ and dict_["kickedUserId"] is not None:
            instance.kicked_user_id = str(dict_["kickedUserId"])
        elif include_empty:
            instance.kicked_user_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "groupId": "group_id",
            "kickedUserId": "kicked_user_id",
        }

    # endregion static methods
