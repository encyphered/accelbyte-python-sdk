# Auto-generated at 2021-09-27T17:12:31.448853+08:00
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


class AccountUpgradeHeadlessAccountRequestV4(Model):
    """Account upgrade headless account request V4

    Properties:
        email_address: (emailAddress) REQUIRED str

        password: (password) REQUIRED str

        username: (username) REQUIRED str
    """

    # region fields

    email_address: str                                                                             # REQUIRED
    password: str                                                                                  # REQUIRED
    username: str                                                                                  # REQUIRED

    # endregion fields

    # region with_x methods

    def with_email_address(self, value: str) -> AccountUpgradeHeadlessAccountRequestV4:
        self.email_address = value
        return self

    def with_password(self, value: str) -> AccountUpgradeHeadlessAccountRequestV4:
        self.password = value
        return self

    def with_username(self, value: str) -> AccountUpgradeHeadlessAccountRequestV4:
        self.username = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "email_address") and self.email_address:
            result["emailAddress"] = str(self.email_address)
        elif include_empty:
            result["emailAddress"] = str()
        if hasattr(self, "password") and self.password:
            result["password"] = str(self.password)
        elif include_empty:
            result["password"] = str()
        if hasattr(self, "username") and self.username:
            result["username"] = str(self.username)
        elif include_empty:
            result["username"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        email_address: str,
        password: str,
        username: str,
    ) -> AccountUpgradeHeadlessAccountRequestV4:
        instance = cls()
        instance.email_address = email_address
        instance.password = password
        instance.username = username
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AccountUpgradeHeadlessAccountRequestV4:
        instance = cls()
        if not dict_:
            return instance
        if "emailAddress" in dict_ and dict_["emailAddress"] is not None:
            instance.email_address = str(dict_["emailAddress"])
        elif include_empty:
            instance.email_address = str()
        if "password" in dict_ and dict_["password"] is not None:
            instance.password = str(dict_["password"])
        elif include_empty:
            instance.password = str()
        if "username" in dict_ and dict_["username"] is not None:
            instance.username = str(dict_["username"])
        elif include_empty:
            instance.username = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "emailAddress": "email_address",
            "password": "password",
            "username": "username",
        }

    # endregion static methods
