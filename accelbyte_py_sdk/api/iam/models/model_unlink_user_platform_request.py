# Auto-generated at 2021-09-21T14:10:34.821575+08:00
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


class ModelUnlinkUserPlatformRequest(Model):
    """Model unlink user platform request

    Properties:
        platform_namespace: (platformNamespace) OPTIONAL str
    """

    # region fields

    platform_namespace: str                                                                        # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_platform_namespace(self, value: str) -> ModelUnlinkUserPlatformRequest:
        self.platform_namespace = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "platform_namespace") and self.platform_namespace:
            result["platformNamespace"] = str(self.platform_namespace)
        elif include_empty:
            result["platformNamespace"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        platform_namespace: Optional[str] = None,
    ) -> ModelUnlinkUserPlatformRequest:
        instance = cls()
        if platform_namespace is not None:
            instance.platform_namespace = platform_namespace
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelUnlinkUserPlatformRequest:
        instance = cls()
        if "platformNamespace" in dict_ and dict_["platformNamespace"] is not None:
            instance.platform_namespace = str(dict_["platformNamespace"])
        elif include_empty:
            instance.platform_namespace = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "platformNamespace": "platform_namespace",
        }

    # endregion static methods