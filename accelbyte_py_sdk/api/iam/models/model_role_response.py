# Auto-generated at 2021-09-27T17:12:31.604802+08:00
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

from ..models.accountcommon_permission import AccountcommonPermission


class ModelRoleResponse(Model):
    """Model role response

    Properties:
        is_wildcard: (IsWildcard) REQUIRED bool

        permissions: (Permissions) REQUIRED List[AccountcommonPermission]

        role_id: (RoleId) REQUIRED str

        role_name: (RoleName) REQUIRED str
    """

    # region fields

    is_wildcard: bool                                                                              # REQUIRED
    permissions: List[AccountcommonPermission]                                                     # REQUIRED
    role_id: str                                                                                   # REQUIRED
    role_name: str                                                                                 # REQUIRED

    # endregion fields

    # region with_x methods

    def with_is_wildcard(self, value: bool) -> ModelRoleResponse:
        self.is_wildcard = value
        return self

    def with_permissions(self, value: List[AccountcommonPermission]) -> ModelRoleResponse:
        self.permissions = value
        return self

    def with_role_id(self, value: str) -> ModelRoleResponse:
        self.role_id = value
        return self

    def with_role_name(self, value: str) -> ModelRoleResponse:
        self.role_name = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "is_wildcard") and self.is_wildcard:
            result["IsWildcard"] = bool(self.is_wildcard)
        elif include_empty:
            result["IsWildcard"] = bool()
        if hasattr(self, "permissions") and self.permissions:
            result["Permissions"] = [i0.to_dict(include_empty=include_empty) for i0 in self.permissions]
        elif include_empty:
            result["Permissions"] = []
        if hasattr(self, "role_id") and self.role_id:
            result["RoleId"] = str(self.role_id)
        elif include_empty:
            result["RoleId"] = str()
        if hasattr(self, "role_name") and self.role_name:
            result["RoleName"] = str(self.role_name)
        elif include_empty:
            result["RoleName"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        is_wildcard: bool,
        permissions: List[AccountcommonPermission],
        role_id: str,
        role_name: str,
    ) -> ModelRoleResponse:
        instance = cls()
        instance.is_wildcard = is_wildcard
        instance.permissions = permissions
        instance.role_id = role_id
        instance.role_name = role_name
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelRoleResponse:
        instance = cls()
        if not dict_:
            return instance
        if "IsWildcard" in dict_ and dict_["IsWildcard"] is not None:
            instance.is_wildcard = bool(dict_["IsWildcard"])
        elif include_empty:
            instance.is_wildcard = bool()
        if "Permissions" in dict_ and dict_["Permissions"] is not None:
            instance.permissions = [AccountcommonPermission.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["Permissions"]]
        elif include_empty:
            instance.permissions = []
        if "RoleId" in dict_ and dict_["RoleId"] is not None:
            instance.role_id = str(dict_["RoleId"])
        elif include_empty:
            instance.role_id = str()
        if "RoleName" in dict_ and dict_["RoleName"] is not None:
            instance.role_name = str(dict_["RoleName"])
        elif include_empty:
            instance.role_name = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "IsWildcard": "is_wildcard",
            "Permissions": "permissions",
            "RoleId": "role_id",
            "RoleName": "role_name",
        }

    # endregion static methods
