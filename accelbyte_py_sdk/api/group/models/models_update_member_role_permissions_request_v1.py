# Auto-generated at 2021-09-27T17:12:37.846955+08:00
# from: Justice Group Service (2.4.0)

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

from ..models.models_role_permission import ModelsRolePermission


class ModelsUpdateMemberRolePermissionsRequestV1(Model):
    """Models update member role permissions request V1

    Properties:
        member_role_permissions: (memberRolePermissions) REQUIRED List[ModelsRolePermission]
    """

    # region fields

    member_role_permissions: List[ModelsRolePermission]                                            # REQUIRED

    # endregion fields

    # region with_x methods

    def with_member_role_permissions(self, value: List[ModelsRolePermission]) -> ModelsUpdateMemberRolePermissionsRequestV1:
        self.member_role_permissions = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "member_role_permissions") and self.member_role_permissions:
            result["memberRolePermissions"] = [i0.to_dict(include_empty=include_empty) for i0 in self.member_role_permissions]
        elif include_empty:
            result["memberRolePermissions"] = []
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        member_role_permissions: List[ModelsRolePermission],
    ) -> ModelsUpdateMemberRolePermissionsRequestV1:
        instance = cls()
        instance.member_role_permissions = member_role_permissions
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsUpdateMemberRolePermissionsRequestV1:
        instance = cls()
        if not dict_:
            return instance
        if "memberRolePermissions" in dict_ and dict_["memberRolePermissions"] is not None:
            instance.member_role_permissions = [ModelsRolePermission.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["memberRolePermissions"]]
        elif include_empty:
            instance.member_role_permissions = []
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "memberRolePermissions": "member_role_permissions",
        }

    # endregion static methods
