# Auto-generated at 2021-09-21T14:10:38.790234+08:00
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


class PlaystationIAPConfigRequest(Model):
    """Playstation IAP config request

    Properties:
        environment: (environment) REQUIRED str
    """

    # region fields

    environment: str                                                                               # REQUIRED

    # endregion fields

    # region with_x methods

    def with_environment(self, value: str) -> PlaystationIAPConfigRequest:
        self.environment = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "environment") and self.environment:
            result["environment"] = str(self.environment)
        elif include_empty:
            result["environment"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        environment: str,
    ) -> PlaystationIAPConfigRequest:
        instance = cls()
        instance.environment = environment
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> PlaystationIAPConfigRequest:
        instance = cls()
        if "environment" in dict_ and dict_["environment"] is not None:
            instance.environment = str(dict_["environment"])
        elif include_empty:
            instance.environment = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "environment": "environment",
        }

    # endregion static methods