# Auto-generated at 2021-09-27T17:12:31.572476+08:00
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


class ModelPublicThirdPartyPlatformInfo(Model):
    """Model public third party platform info

    Properties:
        app_id: (AppId) REQUIRED str

        client_id: (ClientId) REQUIRED str

        environment: (Environment) REQUIRED str

        is_active: (IsActive) REQUIRED bool

        platform_id: (PlatformId) REQUIRED str
    """

    # region fields

    app_id: str                                                                                    # REQUIRED
    client_id: str                                                                                 # REQUIRED
    environment: str                                                                               # REQUIRED
    is_active: bool                                                                                # REQUIRED
    platform_id: str                                                                               # REQUIRED

    # endregion fields

    # region with_x methods

    def with_app_id(self, value: str) -> ModelPublicThirdPartyPlatformInfo:
        self.app_id = value
        return self

    def with_client_id(self, value: str) -> ModelPublicThirdPartyPlatformInfo:
        self.client_id = value
        return self

    def with_environment(self, value: str) -> ModelPublicThirdPartyPlatformInfo:
        self.environment = value
        return self

    def with_is_active(self, value: bool) -> ModelPublicThirdPartyPlatformInfo:
        self.is_active = value
        return self

    def with_platform_id(self, value: str) -> ModelPublicThirdPartyPlatformInfo:
        self.platform_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "app_id") and self.app_id:
            result["AppId"] = str(self.app_id)
        elif include_empty:
            result["AppId"] = str()
        if hasattr(self, "client_id") and self.client_id:
            result["ClientId"] = str(self.client_id)
        elif include_empty:
            result["ClientId"] = str()
        if hasattr(self, "environment") and self.environment:
            result["Environment"] = str(self.environment)
        elif include_empty:
            result["Environment"] = str()
        if hasattr(self, "is_active") and self.is_active:
            result["IsActive"] = bool(self.is_active)
        elif include_empty:
            result["IsActive"] = bool()
        if hasattr(self, "platform_id") and self.platform_id:
            result["PlatformId"] = str(self.platform_id)
        elif include_empty:
            result["PlatformId"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        app_id: str,
        client_id: str,
        environment: str,
        is_active: bool,
        platform_id: str,
    ) -> ModelPublicThirdPartyPlatformInfo:
        instance = cls()
        instance.app_id = app_id
        instance.client_id = client_id
        instance.environment = environment
        instance.is_active = is_active
        instance.platform_id = platform_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelPublicThirdPartyPlatformInfo:
        instance = cls()
        if not dict_:
            return instance
        if "AppId" in dict_ and dict_["AppId"] is not None:
            instance.app_id = str(dict_["AppId"])
        elif include_empty:
            instance.app_id = str()
        if "ClientId" in dict_ and dict_["ClientId"] is not None:
            instance.client_id = str(dict_["ClientId"])
        elif include_empty:
            instance.client_id = str()
        if "Environment" in dict_ and dict_["Environment"] is not None:
            instance.environment = str(dict_["Environment"])
        elif include_empty:
            instance.environment = str()
        if "IsActive" in dict_ and dict_["IsActive"] is not None:
            instance.is_active = bool(dict_["IsActive"])
        elif include_empty:
            instance.is_active = bool()
        if "PlatformId" in dict_ and dict_["PlatformId"] is not None:
            instance.platform_id = str(dict_["PlatformId"])
        elif include_empty:
            instance.platform_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "AppId": "app_id",
            "ClientId": "client_id",
            "Environment": "environment",
            "IsActive": "is_active",
            "PlatformId": "platform_id",
        }

    # endregion static methods
