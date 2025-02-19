# Auto-generated at 2021-09-27T17:12:31.450043+08:00
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


class AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4(Model):
    """Account upgrade headless account with verification code request V4

    Properties:
        code: (code) REQUIRED str

        country: (country) OPTIONAL str

        date_of_birth: (dateOfBirth) OPTIONAL str

        display_name: (displayName) OPTIONAL str

        email_address: (emailAddress) REQUIRED str

        password: (password) REQUIRED str

        username: (username) REQUIRED str
    """

    # region fields

    code: str                                                                                      # REQUIRED
    country: str                                                                                   # OPTIONAL
    date_of_birth: str                                                                             # OPTIONAL
    display_name: str                                                                              # OPTIONAL
    email_address: str                                                                             # REQUIRED
    password: str                                                                                  # REQUIRED
    username: str                                                                                  # REQUIRED

    # endregion fields

    # region with_x methods

    def with_code(self, value: str) -> AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4:
        self.code = value
        return self

    def with_country(self, value: str) -> AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4:
        self.country = value
        return self

    def with_date_of_birth(self, value: str) -> AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4:
        self.date_of_birth = value
        return self

    def with_display_name(self, value: str) -> AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4:
        self.display_name = value
        return self

    def with_email_address(self, value: str) -> AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4:
        self.email_address = value
        return self

    def with_password(self, value: str) -> AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4:
        self.password = value
        return self

    def with_username(self, value: str) -> AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4:
        self.username = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "code") and self.code:
            result["code"] = str(self.code)
        elif include_empty:
            result["code"] = str()
        if hasattr(self, "country") and self.country:
            result["country"] = str(self.country)
        elif include_empty:
            result["country"] = str()
        if hasattr(self, "date_of_birth") and self.date_of_birth:
            result["dateOfBirth"] = str(self.date_of_birth)
        elif include_empty:
            result["dateOfBirth"] = str()
        if hasattr(self, "display_name") and self.display_name:
            result["displayName"] = str(self.display_name)
        elif include_empty:
            result["displayName"] = str()
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
        code: str,
        email_address: str,
        password: str,
        username: str,
        country: Optional[str] = None,
        date_of_birth: Optional[str] = None,
        display_name: Optional[str] = None,
    ) -> AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4:
        instance = cls()
        instance.code = code
        instance.email_address = email_address
        instance.password = password
        instance.username = username
        if country is not None:
            instance.country = country
        if date_of_birth is not None:
            instance.date_of_birth = date_of_birth
        if display_name is not None:
            instance.display_name = display_name
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4:
        instance = cls()
        if not dict_:
            return instance
        if "code" in dict_ and dict_["code"] is not None:
            instance.code = str(dict_["code"])
        elif include_empty:
            instance.code = str()
        if "country" in dict_ and dict_["country"] is not None:
            instance.country = str(dict_["country"])
        elif include_empty:
            instance.country = str()
        if "dateOfBirth" in dict_ and dict_["dateOfBirth"] is not None:
            instance.date_of_birth = str(dict_["dateOfBirth"])
        elif include_empty:
            instance.date_of_birth = str()
        if "displayName" in dict_ and dict_["displayName"] is not None:
            instance.display_name = str(dict_["displayName"])
        elif include_empty:
            instance.display_name = str()
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
            "code": "code",
            "country": "country",
            "dateOfBirth": "date_of_birth",
            "displayName": "display_name",
            "emailAddress": "email_address",
            "password": "password",
            "username": "username",
        }

    # endregion static methods
