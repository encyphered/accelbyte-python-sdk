# Auto-generated at 2021-09-27T17:12:33.415030+08:00
# from: Justice Lobby Service (1.33.0)

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


class ModelBulkAddFriendsRequest(Model):
    """Model bulk add friends request

    Properties:
        friend_ids: (friendIds) REQUIRED List[str]
    """

    # region fields

    friend_ids: List[str]                                                                          # REQUIRED

    # endregion fields

    # region with_x methods

    def with_friend_ids(self, value: List[str]) -> ModelBulkAddFriendsRequest:
        self.friend_ids = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "friend_ids") and self.friend_ids:
            result["friendIds"] = [str(i0) for i0 in self.friend_ids]
        elif include_empty:
            result["friendIds"] = []
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        friend_ids: List[str],
    ) -> ModelBulkAddFriendsRequest:
        instance = cls()
        instance.friend_ids = friend_ids
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelBulkAddFriendsRequest:
        instance = cls()
        if not dict_:
            return instance
        if "friendIds" in dict_ and dict_["friendIds"] is not None:
            instance.friend_ids = [str(i0) for i0 in dict_["friendIds"]]
        elif include_empty:
            instance.friend_ids = []
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "friendIds": "friend_ids",
        }

    # endregion static methods
