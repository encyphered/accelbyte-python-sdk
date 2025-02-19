# Auto-generated at 2021-09-27T17:12:34.230807+08:00
# from: Justice Social Service (1.17.1)

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


class GlobalStatItemInfo(Model):
    """Global stat item info

    Properties:
        stat_code: (statCode) REQUIRED str

        stat_name: (statName) REQUIRED str

        namespace: (namespace) REQUIRED str

        value: (value) REQUIRED float

        tags: (tags) OPTIONAL List[str]

        created_at: (createdAt) REQUIRED str

        updated_at: (updatedAt) REQUIRED str
    """

    # region fields

    stat_code: str                                                                                 # REQUIRED
    stat_name: str                                                                                 # REQUIRED
    namespace: str                                                                                 # REQUIRED
    value: float                                                                                   # REQUIRED
    tags: List[str]                                                                                # OPTIONAL
    created_at: str                                                                                # REQUIRED
    updated_at: str                                                                                # REQUIRED

    # endregion fields

    # region with_x methods

    def with_stat_code(self, value: str) -> GlobalStatItemInfo:
        self.stat_code = value
        return self

    def with_stat_name(self, value: str) -> GlobalStatItemInfo:
        self.stat_name = value
        return self

    def with_namespace(self, value: str) -> GlobalStatItemInfo:
        self.namespace = value
        return self

    def with_value(self, value: float) -> GlobalStatItemInfo:
        self.value = value
        return self

    def with_tags(self, value: List[str]) -> GlobalStatItemInfo:
        self.tags = value
        return self

    def with_created_at(self, value: str) -> GlobalStatItemInfo:
        self.created_at = value
        return self

    def with_updated_at(self, value: str) -> GlobalStatItemInfo:
        self.updated_at = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "stat_code") and self.stat_code:
            result["statCode"] = str(self.stat_code)
        elif include_empty:
            result["statCode"] = str()
        if hasattr(self, "stat_name") and self.stat_name:
            result["statName"] = str(self.stat_name)
        elif include_empty:
            result["statName"] = str()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "value") and self.value:
            result["value"] = float(self.value)
        elif include_empty:
            result["value"] = float()
        if hasattr(self, "tags") and self.tags:
            result["tags"] = [str(i0) for i0 in self.tags]
        elif include_empty:
            result["tags"] = []
        if hasattr(self, "created_at") and self.created_at:
            result["createdAt"] = str(self.created_at)
        elif include_empty:
            result["createdAt"] = str()
        if hasattr(self, "updated_at") and self.updated_at:
            result["updatedAt"] = str(self.updated_at)
        elif include_empty:
            result["updatedAt"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        stat_code: str,
        stat_name: str,
        namespace: str,
        value: float,
        created_at: str,
        updated_at: str,
        tags: Optional[List[str]] = None,
    ) -> GlobalStatItemInfo:
        instance = cls()
        instance.stat_code = stat_code
        instance.stat_name = stat_name
        instance.namespace = namespace
        instance.value = value
        instance.created_at = created_at
        instance.updated_at = updated_at
        if tags is not None:
            instance.tags = tags
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> GlobalStatItemInfo:
        instance = cls()
        if not dict_:
            return instance
        if "statCode" in dict_ and dict_["statCode"] is not None:
            instance.stat_code = str(dict_["statCode"])
        elif include_empty:
            instance.stat_code = str()
        if "statName" in dict_ and dict_["statName"] is not None:
            instance.stat_name = str(dict_["statName"])
        elif include_empty:
            instance.stat_name = str()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "value" in dict_ and dict_["value"] is not None:
            instance.value = float(dict_["value"])
        elif include_empty:
            instance.value = float()
        if "tags" in dict_ and dict_["tags"] is not None:
            instance.tags = [str(i0) for i0 in dict_["tags"]]
        elif include_empty:
            instance.tags = []
        if "createdAt" in dict_ and dict_["createdAt"] is not None:
            instance.created_at = str(dict_["createdAt"])
        elif include_empty:
            instance.created_at = str()
        if "updatedAt" in dict_ and dict_["updatedAt"] is not None:
            instance.updated_at = str(dict_["updatedAt"])
        elif include_empty:
            instance.updated_at = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "statCode": "stat_code",
            "statName": "stat_name",
            "namespace": "namespace",
            "value": "value",
            "tags": "tags",
            "createdAt": "created_at",
            "updatedAt": "updated_at",
        }

    # endregion static methods
