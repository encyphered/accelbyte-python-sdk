# Auto-generated at 2021-09-27T17:12:31.525236+08:00
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

from ..models.accountcommon_namespace_role import AccountcommonNamespaceRole


class ModelAdminInvitationV3(Model):
    """Model admin invitation V3

    Properties:
        email: (email) REQUIRED str

        expired_at: (expiredAt) REQUIRED str

        id_: (id) OPTIONAL str

        roles: (roles) REQUIRED List[AccountcommonNamespaceRole]
    """

    # region fields

    email: str                                                                                     # REQUIRED
    expired_at: str                                                                                # REQUIRED
    id_: str                                                                                       # OPTIONAL
    roles: List[AccountcommonNamespaceRole]                                                        # REQUIRED

    # endregion fields

    # region with_x methods

    def with_email(self, value: str) -> ModelAdminInvitationV3:
        self.email = value
        return self

    def with_expired_at(self, value: str) -> ModelAdminInvitationV3:
        self.expired_at = value
        return self

    def with_id(self, value: str) -> ModelAdminInvitationV3:
        self.id_ = value
        return self

    def with_roles(self, value: List[AccountcommonNamespaceRole]) -> ModelAdminInvitationV3:
        self.roles = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "email") and self.email:
            result["email"] = str(self.email)
        elif include_empty:
            result["email"] = str()
        if hasattr(self, "expired_at") and self.expired_at:
            result["expiredAt"] = str(self.expired_at)
        elif include_empty:
            result["expiredAt"] = str()
        if hasattr(self, "id_") and self.id_:
            result["id"] = str(self.id_)
        elif include_empty:
            result["id"] = str()
        if hasattr(self, "roles") and self.roles:
            result["roles"] = [i0.to_dict(include_empty=include_empty) for i0 in self.roles]
        elif include_empty:
            result["roles"] = []
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        email: str,
        expired_at: str,
        roles: List[AccountcommonNamespaceRole],
        id_: Optional[str] = None,
    ) -> ModelAdminInvitationV3:
        instance = cls()
        instance.email = email
        instance.expired_at = expired_at
        instance.roles = roles
        if id_ is not None:
            instance.id_ = id_
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelAdminInvitationV3:
        instance = cls()
        if not dict_:
            return instance
        if "email" in dict_ and dict_["email"] is not None:
            instance.email = str(dict_["email"])
        elif include_empty:
            instance.email = str()
        if "expiredAt" in dict_ and dict_["expiredAt"] is not None:
            instance.expired_at = str(dict_["expiredAt"])
        elif include_empty:
            instance.expired_at = str()
        if "id" in dict_ and dict_["id"] is not None:
            instance.id_ = str(dict_["id"])
        elif include_empty:
            instance.id_ = str()
        if "roles" in dict_ and dict_["roles"] is not None:
            instance.roles = [AccountcommonNamespaceRole.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["roles"]]
        elif include_empty:
            instance.roles = []
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "email": "email",
            "expiredAt": "expired_at",
            "id": "id_",
            "roles": "roles",
        }

    # endregion static methods
