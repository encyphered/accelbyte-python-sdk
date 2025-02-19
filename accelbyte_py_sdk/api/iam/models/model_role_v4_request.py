# Auto-generated at 2021-09-27T17:12:31.614475+08:00
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


class ModelRoleV4Request(Model):
    """Model role V4 request

    Properties:
        admin_role: (adminRole) REQUIRED bool

        is_wildcard: (isWildcard) REQUIRED bool

        role_name: (roleName) REQUIRED str
    """

    # region fields

    admin_role: bool                                                                               # REQUIRED
    is_wildcard: bool                                                                              # REQUIRED
    role_name: str                                                                                 # REQUIRED

    # endregion fields

    # region with_x methods

    def with_admin_role(self, value: bool) -> ModelRoleV4Request:
        self.admin_role = value
        return self

    def with_is_wildcard(self, value: bool) -> ModelRoleV4Request:
        self.is_wildcard = value
        return self

    def with_role_name(self, value: str) -> ModelRoleV4Request:
        self.role_name = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "admin_role") and self.admin_role:
            result["adminRole"] = bool(self.admin_role)
        elif include_empty:
            result["adminRole"] = bool()
        if hasattr(self, "is_wildcard") and self.is_wildcard:
            result["isWildcard"] = bool(self.is_wildcard)
        elif include_empty:
            result["isWildcard"] = bool()
        if hasattr(self, "role_name") and self.role_name:
            result["roleName"] = str(self.role_name)
        elif include_empty:
            result["roleName"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        admin_role: bool,
        is_wildcard: bool,
        role_name: str,
    ) -> ModelRoleV4Request:
        instance = cls()
        instance.admin_role = admin_role
        instance.is_wildcard = is_wildcard
        instance.role_name = role_name
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelRoleV4Request:
        instance = cls()
        if not dict_:
            return instance
        if "adminRole" in dict_ and dict_["adminRole"] is not None:
            instance.admin_role = bool(dict_["adminRole"])
        elif include_empty:
            instance.admin_role = bool()
        if "isWildcard" in dict_ and dict_["isWildcard"] is not None:
            instance.is_wildcard = bool(dict_["isWildcard"])
        elif include_empty:
            instance.is_wildcard = bool()
        if "roleName" in dict_ and dict_["roleName"] is not None:
            instance.role_name = str(dict_["roleName"])
        elif include_empty:
            instance.role_name = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "adminRole": "admin_role",
            "isWildcard": "is_wildcard",
            "roleName": "role_name",
        }

    # endregion static methods
