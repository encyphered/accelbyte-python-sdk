# Auto-generated at 2021-09-27T17:12:31.532588+08:00
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


class ModelAssignedUserV4Response(Model):
    """Model assigned user V4 response

    Properties:
        assigned_namespaces: (assignedNamespaces) REQUIRED List[str]

        display_name: (displayName) REQUIRED str

        email: (email) REQUIRED str

        role_id: (roleId) REQUIRED str

        user_id: (userId) REQUIRED str
    """

    # region fields

    assigned_namespaces: List[str]                                                                 # REQUIRED
    display_name: str                                                                              # REQUIRED
    email: str                                                                                     # REQUIRED
    role_id: str                                                                                   # REQUIRED
    user_id: str                                                                                   # REQUIRED

    # endregion fields

    # region with_x methods

    def with_assigned_namespaces(self, value: List[str]) -> ModelAssignedUserV4Response:
        self.assigned_namespaces = value
        return self

    def with_display_name(self, value: str) -> ModelAssignedUserV4Response:
        self.display_name = value
        return self

    def with_email(self, value: str) -> ModelAssignedUserV4Response:
        self.email = value
        return self

    def with_role_id(self, value: str) -> ModelAssignedUserV4Response:
        self.role_id = value
        return self

    def with_user_id(self, value: str) -> ModelAssignedUserV4Response:
        self.user_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "assigned_namespaces") and self.assigned_namespaces:
            result["assignedNamespaces"] = [str(i0) for i0 in self.assigned_namespaces]
        elif include_empty:
            result["assignedNamespaces"] = []
        if hasattr(self, "display_name") and self.display_name:
            result["displayName"] = str(self.display_name)
        elif include_empty:
            result["displayName"] = str()
        if hasattr(self, "email") and self.email:
            result["email"] = str(self.email)
        elif include_empty:
            result["email"] = str()
        if hasattr(self, "role_id") and self.role_id:
            result["roleId"] = str(self.role_id)
        elif include_empty:
            result["roleId"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        assigned_namespaces: List[str],
        display_name: str,
        email: str,
        role_id: str,
        user_id: str,
    ) -> ModelAssignedUserV4Response:
        instance = cls()
        instance.assigned_namespaces = assigned_namespaces
        instance.display_name = display_name
        instance.email = email
        instance.role_id = role_id
        instance.user_id = user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelAssignedUserV4Response:
        instance = cls()
        if not dict_:
            return instance
        if "assignedNamespaces" in dict_ and dict_["assignedNamespaces"] is not None:
            instance.assigned_namespaces = [str(i0) for i0 in dict_["assignedNamespaces"]]
        elif include_empty:
            instance.assigned_namespaces = []
        if "displayName" in dict_ and dict_["displayName"] is not None:
            instance.display_name = str(dict_["displayName"])
        elif include_empty:
            instance.display_name = str()
        if "email" in dict_ and dict_["email"] is not None:
            instance.email = str(dict_["email"])
        elif include_empty:
            instance.email = str()
        if "roleId" in dict_ and dict_["roleId"] is not None:
            instance.role_id = str(dict_["roleId"])
        elif include_empty:
            instance.role_id = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "assignedNamespaces": "assigned_namespaces",
            "displayName": "display_name",
            "email": "email",
            "roleId": "role_id",
            "userId": "user_id",
        }

    # endregion static methods
