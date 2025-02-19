# Auto-generated at 2021-09-27T17:12:31.531416+08:00
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


class ModelAssignUserV4Request(Model):
    """Model assign user V4 request

    Properties:
        assigned_namespaces: (assignedNamespaces) REQUIRED List[str]

        namespace: (namespace) REQUIRED str

        user_id: (userId) REQUIRED str
    """

    # region fields

    assigned_namespaces: List[str]                                                                 # REQUIRED
    namespace: str                                                                                 # REQUIRED
    user_id: str                                                                                   # REQUIRED

    # endregion fields

    # region with_x methods

    def with_assigned_namespaces(self, value: List[str]) -> ModelAssignUserV4Request:
        self.assigned_namespaces = value
        return self

    def with_namespace(self, value: str) -> ModelAssignUserV4Request:
        self.namespace = value
        return self

    def with_user_id(self, value: str) -> ModelAssignUserV4Request:
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
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
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
        namespace: str,
        user_id: str,
    ) -> ModelAssignUserV4Request:
        instance = cls()
        instance.assigned_namespaces = assigned_namespaces
        instance.namespace = namespace
        instance.user_id = user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelAssignUserV4Request:
        instance = cls()
        if not dict_:
            return instance
        if "assignedNamespaces" in dict_ and dict_["assignedNamespaces"] is not None:
            instance.assigned_namespaces = [str(i0) for i0 in dict_["assignedNamespaces"]]
        elif include_empty:
            instance.assigned_namespaces = []
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "assignedNamespaces": "assigned_namespaces",
            "namespace": "namespace",
            "userId": "user_id",
        }

    # endregion static methods
