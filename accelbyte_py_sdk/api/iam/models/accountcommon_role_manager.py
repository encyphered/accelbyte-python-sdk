# Auto-generated at 2021-09-27T17:12:31.486524+08:00
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


class AccountcommonRoleManager(Model):
    """Accountcommon role manager

    Properties:
        display_name: (DisplayName) REQUIRED str

        namespace: (Namespace) REQUIRED str

        user_id: (UserId) REQUIRED str
    """

    # region fields

    display_name: str                                                                              # REQUIRED
    namespace: str                                                                                 # REQUIRED
    user_id: str                                                                                   # REQUIRED

    # endregion fields

    # region with_x methods

    def with_display_name(self, value: str) -> AccountcommonRoleManager:
        self.display_name = value
        return self

    def with_namespace(self, value: str) -> AccountcommonRoleManager:
        self.namespace = value
        return self

    def with_user_id(self, value: str) -> AccountcommonRoleManager:
        self.user_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "display_name") and self.display_name:
            result["DisplayName"] = str(self.display_name)
        elif include_empty:
            result["DisplayName"] = str()
        if hasattr(self, "namespace") and self.namespace:
            result["Namespace"] = str(self.namespace)
        elif include_empty:
            result["Namespace"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["UserId"] = str(self.user_id)
        elif include_empty:
            result["UserId"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        display_name: str,
        namespace: str,
        user_id: str,
    ) -> AccountcommonRoleManager:
        instance = cls()
        instance.display_name = display_name
        instance.namespace = namespace
        instance.user_id = user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AccountcommonRoleManager:
        instance = cls()
        if not dict_:
            return instance
        if "DisplayName" in dict_ and dict_["DisplayName"] is not None:
            instance.display_name = str(dict_["DisplayName"])
        elif include_empty:
            instance.display_name = str()
        if "Namespace" in dict_ and dict_["Namespace"] is not None:
            instance.namespace = str(dict_["Namespace"])
        elif include_empty:
            instance.namespace = str()
        if "UserId" in dict_ and dict_["UserId"] is not None:
            instance.user_id = str(dict_["UserId"])
        elif include_empty:
            instance.user_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "DisplayName": "display_name",
            "Namespace": "namespace",
            "UserId": "user_id",
        }

    # endregion static methods
