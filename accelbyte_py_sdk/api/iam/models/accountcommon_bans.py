# Auto-generated at 2021-09-21T14:10:34.703887+08:00
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

from ..models.accountcommon_ban import AccountcommonBan


class AccountcommonBans(Model):
    """Accountcommon bans

    Properties:
        bans: (Bans) REQUIRED List[AccountcommonBan]
    """

    # region fields

    bans: List[AccountcommonBan]                                                                   # REQUIRED

    # endregion fields

    # region with_x methods

    def with_bans(self, value: List[AccountcommonBan]) -> AccountcommonBans:
        self.bans = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "bans") and self.bans:
            result["Bans"] = [i0.to_dict(include_empty=include_empty) for i0 in self.bans]
        elif include_empty:
            result["Bans"] = []
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        bans: List[AccountcommonBan],
    ) -> AccountcommonBans:
        instance = cls()
        instance.bans = bans
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AccountcommonBans:
        instance = cls()
        if "Bans" in dict_ and dict_["Bans"] is not None:
            instance.bans = [AccountcommonBan.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["Bans"]]
        elif include_empty:
            instance.bans = []
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "Bans": "bans",
        }

    # endregion static methods