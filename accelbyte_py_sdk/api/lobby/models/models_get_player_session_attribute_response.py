# Auto-generated at 2021-09-27T17:12:33.491262+08:00
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


class ModelsGetPlayerSessionAttributeResponse(Model):
    """Models get player session attribute response

    Properties:
        key: (key) REQUIRED str

        value: (value) REQUIRED str
    """

    # region fields

    key: str                                                                                       # REQUIRED
    value: str                                                                                     # REQUIRED

    # endregion fields

    # region with_x methods

    def with_key(self, value: str) -> ModelsGetPlayerSessionAttributeResponse:
        self.key = value
        return self

    def with_value(self, value: str) -> ModelsGetPlayerSessionAttributeResponse:
        self.value = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "key") and self.key:
            result["key"] = str(self.key)
        elif include_empty:
            result["key"] = str()
        if hasattr(self, "value") and self.value:
            result["value"] = str(self.value)
        elif include_empty:
            result["value"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        key: str,
        value: str,
    ) -> ModelsGetPlayerSessionAttributeResponse:
        instance = cls()
        instance.key = key
        instance.value = value
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsGetPlayerSessionAttributeResponse:
        instance = cls()
        if not dict_:
            return instance
        if "key" in dict_ and dict_["key"] is not None:
            instance.key = str(dict_["key"])
        elif include_empty:
            instance.key = str()
        if "value" in dict_ and dict_["value"] is not None:
            instance.value = str(dict_["value"])
        elif include_empty:
            instance.value = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "key": "key",
            "value": "value",
        }

    # endregion static methods
