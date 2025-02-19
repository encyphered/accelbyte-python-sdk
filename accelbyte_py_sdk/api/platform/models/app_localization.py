# Auto-generated at 2021-09-27T17:12:36.181284+08:00
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


class AppLocalization(Model):
    """App localization

    Properties:
        slogan: (slogan) OPTIONAL str

        announcement: (announcement) OPTIONAL str
    """

    # region fields

    slogan: str                                                                                    # OPTIONAL
    announcement: str                                                                              # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_slogan(self, value: str) -> AppLocalization:
        self.slogan = value
        return self

    def with_announcement(self, value: str) -> AppLocalization:
        self.announcement = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "slogan") and self.slogan:
            result["slogan"] = str(self.slogan)
        elif include_empty:
            result["slogan"] = str()
        if hasattr(self, "announcement") and self.announcement:
            result["announcement"] = str(self.announcement)
        elif include_empty:
            result["announcement"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        slogan: Optional[str] = None,
        announcement: Optional[str] = None,
    ) -> AppLocalization:
        instance = cls()
        if slogan is not None:
            instance.slogan = slogan
        if announcement is not None:
            instance.announcement = announcement
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AppLocalization:
        instance = cls()
        if not dict_:
            return instance
        if "slogan" in dict_ and dict_["slogan"] is not None:
            instance.slogan = str(dict_["slogan"])
        elif include_empty:
            instance.slogan = str()
        if "announcement" in dict_ and dict_["announcement"] is not None:
            instance.announcement = str(dict_["announcement"])
        elif include_empty:
            instance.announcement = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "slogan": "slogan",
            "announcement": "announcement",
        }

    # endregion static methods
