# Auto-generated at 2021-09-27T17:12:31.636572+08:00
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


class ModelUpgradeHeadlessAccountRequest(Model):
    """Model upgrade headless account request

    Properties:
        login_id: (LoginID) REQUIRED str

        password: (Password) REQUIRED str
    """

    # region fields

    login_id: str                                                                                  # REQUIRED
    password: str                                                                                  # REQUIRED

    # endregion fields

    # region with_x methods

    def with_login_id(self, value: str) -> ModelUpgradeHeadlessAccountRequest:
        self.login_id = value
        return self

    def with_password(self, value: str) -> ModelUpgradeHeadlessAccountRequest:
        self.password = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "login_id") and self.login_id:
            result["LoginID"] = str(self.login_id)
        elif include_empty:
            result["LoginID"] = str()
        if hasattr(self, "password") and self.password:
            result["Password"] = str(self.password)
        elif include_empty:
            result["Password"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        login_id: str,
        password: str,
    ) -> ModelUpgradeHeadlessAccountRequest:
        instance = cls()
        instance.login_id = login_id
        instance.password = password
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelUpgradeHeadlessAccountRequest:
        instance = cls()
        if not dict_:
            return instance
        if "LoginID" in dict_ and dict_["LoginID"] is not None:
            instance.login_id = str(dict_["LoginID"])
        elif include_empty:
            instance.login_id = str()
        if "Password" in dict_ and dict_["Password"] is not None:
            instance.password = str(dict_["Password"])
        elif include_empty:
            instance.password = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "LoginID": "login_id",
            "Password": "password",
        }

    # endregion static methods
