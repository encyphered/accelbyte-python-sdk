# Auto-generated at 2021-09-27T17:12:31.592641+08:00
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

from ..models.accountcommon_permission_v3 import AccountcommonPermissionV3
from ..models.accountcommon_role_manager_v3 import AccountcommonRoleManagerV3
from ..models.accountcommon_role_member_v3 import AccountcommonRoleMemberV3


class ModelRoleCreateV3Request(Model):
    """Model role create V3 request

    Properties:
        admin_role: (adminRole) REQUIRED bool

        is_wildcard: (isWildcard) REQUIRED bool

        managers: (managers) REQUIRED List[AccountcommonRoleManagerV3]

        members: (members) REQUIRED List[AccountcommonRoleMemberV3]

        permissions: (permissions) REQUIRED List[AccountcommonPermissionV3]

        role_name: (roleName) REQUIRED str
    """

    # region fields

    admin_role: bool                                                                               # REQUIRED
    is_wildcard: bool                                                                              # REQUIRED
    managers: List[AccountcommonRoleManagerV3]                                                     # REQUIRED
    members: List[AccountcommonRoleMemberV3]                                                       # REQUIRED
    permissions: List[AccountcommonPermissionV3]                                                   # REQUIRED
    role_name: str                                                                                 # REQUIRED

    # endregion fields

    # region with_x methods

    def with_admin_role(self, value: bool) -> ModelRoleCreateV3Request:
        self.admin_role = value
        return self

    def with_is_wildcard(self, value: bool) -> ModelRoleCreateV3Request:
        self.is_wildcard = value
        return self

    def with_managers(self, value: List[AccountcommonRoleManagerV3]) -> ModelRoleCreateV3Request:
        self.managers = value
        return self

    def with_members(self, value: List[AccountcommonRoleMemberV3]) -> ModelRoleCreateV3Request:
        self.members = value
        return self

    def with_permissions(self, value: List[AccountcommonPermissionV3]) -> ModelRoleCreateV3Request:
        self.permissions = value
        return self

    def with_role_name(self, value: str) -> ModelRoleCreateV3Request:
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
        if hasattr(self, "managers") and self.managers:
            result["managers"] = [i0.to_dict(include_empty=include_empty) for i0 in self.managers]
        elif include_empty:
            result["managers"] = []
        if hasattr(self, "members") and self.members:
            result["members"] = [i0.to_dict(include_empty=include_empty) for i0 in self.members]
        elif include_empty:
            result["members"] = []
        if hasattr(self, "permissions") and self.permissions:
            result["permissions"] = [i0.to_dict(include_empty=include_empty) for i0 in self.permissions]
        elif include_empty:
            result["permissions"] = []
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
        managers: List[AccountcommonRoleManagerV3],
        members: List[AccountcommonRoleMemberV3],
        permissions: List[AccountcommonPermissionV3],
        role_name: str,
    ) -> ModelRoleCreateV3Request:
        instance = cls()
        instance.admin_role = admin_role
        instance.is_wildcard = is_wildcard
        instance.managers = managers
        instance.members = members
        instance.permissions = permissions
        instance.role_name = role_name
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelRoleCreateV3Request:
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
        if "managers" in dict_ and dict_["managers"] is not None:
            instance.managers = [AccountcommonRoleManagerV3.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["managers"]]
        elif include_empty:
            instance.managers = []
        if "members" in dict_ and dict_["members"] is not None:
            instance.members = [AccountcommonRoleMemberV3.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["members"]]
        elif include_empty:
            instance.members = []
        if "permissions" in dict_ and dict_["permissions"] is not None:
            instance.permissions = [AccountcommonPermissionV3.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["permissions"]]
        elif include_empty:
            instance.permissions = []
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
            "managers": "managers",
            "members": "members",
            "permissions": "permissions",
            "roleName": "role_name",
        }

    # endregion static methods
