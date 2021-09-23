# Auto-generated at 2021-09-21T14:10:36.214960+08:00
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


class ModelsAdminCreateProfanityListRequest(Model):
    """Models admin create profanity list request

    Properties:
        is_enabled: (isEnabled) REQUIRED bool

        is_mandatory: (isMandatory) REQUIRED bool

        name: (name) REQUIRED str
    """

    # region fields

    is_enabled: bool                                                                               # REQUIRED
    is_mandatory: bool                                                                             # REQUIRED
    name: str                                                                                      # REQUIRED

    # endregion fields

    # region with_x methods

    def with_is_enabled(self, value: bool) -> ModelsAdminCreateProfanityListRequest:
        self.is_enabled = value
        return self

    def with_is_mandatory(self, value: bool) -> ModelsAdminCreateProfanityListRequest:
        self.is_mandatory = value
        return self

    def with_name(self, value: str) -> ModelsAdminCreateProfanityListRequest:
        self.name = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "is_enabled") and self.is_enabled:
            result["isEnabled"] = bool(self.is_enabled)
        elif include_empty:
            result["isEnabled"] = bool()
        if hasattr(self, "is_mandatory") and self.is_mandatory:
            result["isMandatory"] = bool(self.is_mandatory)
        elif include_empty:
            result["isMandatory"] = bool()
        if hasattr(self, "name") and self.name:
            result["name"] = str(self.name)
        elif include_empty:
            result["name"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        is_enabled: bool,
        is_mandatory: bool,
        name: str,
    ) -> ModelsAdminCreateProfanityListRequest:
        instance = cls()
        instance.is_enabled = is_enabled
        instance.is_mandatory = is_mandatory
        instance.name = name
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsAdminCreateProfanityListRequest:
        instance = cls()
        if "isEnabled" in dict_ and dict_["isEnabled"] is not None:
            instance.is_enabled = bool(dict_["isEnabled"])
        elif include_empty:
            instance.is_enabled = bool()
        if "isMandatory" in dict_ and dict_["isMandatory"] is not None:
            instance.is_mandatory = bool(dict_["isMandatory"])
        elif include_empty:
            instance.is_mandatory = bool()
        if "name" in dict_ and dict_["name"] is not None:
            instance.name = str(dict_["name"])
        elif include_empty:
            instance.name = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "isEnabled": "is_enabled",
            "isMandatory": "is_mandatory",
            "name": "name",
        }

    # endregion static methods