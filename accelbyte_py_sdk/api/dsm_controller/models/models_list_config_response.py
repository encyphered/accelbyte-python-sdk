# Auto-generated at 2021-09-21T14:10:33.104099+08:00
# from: Justice DsmController Service (2.4.0)

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

from ..models.models_dsm_config import ModelsDSMConfig


class ModelsListConfigResponse(Model):
    """Models list config response

    Properties:
        configs: (configs) REQUIRED List[ModelsDSMConfig]
    """

    # region fields

    configs: List[ModelsDSMConfig]                                                                 # REQUIRED

    # endregion fields

    # region with_x methods

    def with_configs(self, value: List[ModelsDSMConfig]) -> ModelsListConfigResponse:
        self.configs = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "configs") and self.configs:
            result["configs"] = [i0.to_dict(include_empty=include_empty) for i0 in self.configs]
        elif include_empty:
            result["configs"] = []
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        configs: List[ModelsDSMConfig],
    ) -> ModelsListConfigResponse:
        instance = cls()
        instance.configs = configs
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsListConfigResponse:
        instance = cls()
        if "configs" in dict_ and dict_["configs"] is not None:
            instance.configs = [ModelsDSMConfig.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["configs"]]
        elif include_empty:
            instance.configs = []
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "configs": "configs",
        }

    # endregion static methods