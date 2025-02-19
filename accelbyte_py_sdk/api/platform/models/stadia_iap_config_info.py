# Auto-generated at 2021-09-27T17:12:36.370827+08:00
# from: Justice Platform Service (3.24.0)

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


class StadiaIAPConfigInfo(Model):
    """Stadia IAP config info

    Properties:
        namespace: (namespace) REQUIRED str

        json_file: (jsonFile) OPTIONAL str
    """

    # region fields

    namespace: str                                                                                 # REQUIRED
    json_file: str                                                                                 # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_namespace(self, value: str) -> StadiaIAPConfigInfo:
        self.namespace = value
        return self

    def with_json_file(self, value: str) -> StadiaIAPConfigInfo:
        self.json_file = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "json_file") and self.json_file:
            result["jsonFile"] = str(self.json_file)
        elif include_empty:
            result["jsonFile"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        namespace: str,
        json_file: Optional[str] = None,
    ) -> StadiaIAPConfigInfo:
        instance = cls()
        instance.namespace = namespace
        if json_file is not None:
            instance.json_file = json_file
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> StadiaIAPConfigInfo:
        instance = cls()
        if not dict_:
            return instance
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "jsonFile" in dict_ and dict_["jsonFile"] is not None:
            instance.json_file = str(dict_["jsonFile"])
        elif include_empty:
            instance.json_file = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "jsonFile": "json_file",
        }

    # endregion static methods
