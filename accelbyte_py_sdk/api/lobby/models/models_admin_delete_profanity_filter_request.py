# Auto-generated at 2021-09-27T17:12:33.466065+08:00
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


class ModelsAdminDeleteProfanityFilterRequest(Model):
    """Models admin delete profanity filter request

    Properties:
        filter_: (filter) REQUIRED str
    """

    # region fields

    filter_: str                                                                                   # REQUIRED

    # endregion fields

    # region with_x methods

    def with_filter(self, value: str) -> ModelsAdminDeleteProfanityFilterRequest:
        self.filter_ = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "filter_") and self.filter_:
            result["filter"] = str(self.filter_)
        elif include_empty:
            result["filter"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        filter_: str,
    ) -> ModelsAdminDeleteProfanityFilterRequest:
        instance = cls()
        instance.filter_ = filter_
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsAdminDeleteProfanityFilterRequest:
        instance = cls()
        if not dict_:
            return instance
        if "filter" in dict_ and dict_["filter"] is not None:
            instance.filter_ = str(dict_["filter"])
        elif include_empty:
            instance.filter_ = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "filter": "filter_",
        }

    # endregion static methods
