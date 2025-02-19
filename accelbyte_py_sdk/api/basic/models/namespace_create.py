# Auto-generated at 2021-09-27T17:12:38.712902+08:00
# from: Justice Basic Service (1.17.0)

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


class NamespaceCreate(Model):
    """Namespace create

    Properties:
        display_name: (displayName) REQUIRED str

        namespace: (namespace) REQUIRED str
    """

    # region fields

    display_name: str                                                                              # REQUIRED
    namespace: str                                                                                 # REQUIRED

    # endregion fields

    # region with_x methods

    def with_display_name(self, value: str) -> NamespaceCreate:
        self.display_name = value
        return self

    def with_namespace(self, value: str) -> NamespaceCreate:
        self.namespace = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "display_name") and self.display_name:
            result["displayName"] = str(self.display_name)
        elif include_empty:
            result["displayName"] = str()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        display_name: str,
        namespace: str,
    ) -> NamespaceCreate:
        instance = cls()
        instance.display_name = display_name
        instance.namespace = namespace
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> NamespaceCreate:
        instance = cls()
        if not dict_:
            return instance
        if "displayName" in dict_ and dict_["displayName"] is not None:
            instance.display_name = str(dict_["displayName"])
        elif include_empty:
            instance.display_name = str()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "displayName": "display_name",
            "namespace": "namespace",
        }

    # endregion static methods
