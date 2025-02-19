# Auto-generated at 2021-09-27T17:12:31.453424+08:00
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


class AccountcommonBanReason(Model):
    """Accountcommon ban reason

    Properties:
        description: (Description) REQUIRED str

        reason: (Reason) REQUIRED str
    """

    # region fields

    description: str                                                                               # REQUIRED
    reason: str                                                                                    # REQUIRED

    # endregion fields

    # region with_x methods

    def with_description(self, value: str) -> AccountcommonBanReason:
        self.description = value
        return self

    def with_reason(self, value: str) -> AccountcommonBanReason:
        self.reason = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "description") and self.description:
            result["Description"] = str(self.description)
        elif include_empty:
            result["Description"] = str()
        if hasattr(self, "reason") and self.reason:
            result["Reason"] = str(self.reason)
        elif include_empty:
            result["Reason"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        description: str,
        reason: str,
    ) -> AccountcommonBanReason:
        instance = cls()
        instance.description = description
        instance.reason = reason
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AccountcommonBanReason:
        instance = cls()
        if not dict_:
            return instance
        if "Description" in dict_ and dict_["Description"] is not None:
            instance.description = str(dict_["Description"])
        elif include_empty:
            instance.description = str()
        if "Reason" in dict_ and dict_["Reason"] is not None:
            instance.reason = str(dict_["Reason"])
        elif include_empty:
            instance.reason = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "Description": "description",
            "Reason": "reason",
        }

    # endregion static methods
