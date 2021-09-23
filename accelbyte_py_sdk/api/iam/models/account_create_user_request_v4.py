# Auto-generated at 2021-09-21T14:10:34.693389+08:00
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

from ..models.legal_accepted_policies_request import LegalAcceptedPoliciesRequest


class AccountCreateUserRequestV4(Model):
    """Account create user request V4

    Properties:
        accepted_policies: (acceptedPolicies) OPTIONAL List[LegalAcceptedPoliciesRequest]

        auth_type: (authType) REQUIRED str

        country: (country) REQUIRED str

        date_of_birth: (dateOfBirth) REQUIRED str

        display_name: (displayName) REQUIRED str

        email_address: (emailAddress) REQUIRED str

        password: (password) REQUIRED str

        password_md5_sum: (passwordMD5Sum) REQUIRED str

        username: (username) REQUIRED str
    """

    # region fields

    accepted_policies: List[LegalAcceptedPoliciesRequest]                                          # OPTIONAL
    auth_type: str                                                                                 # REQUIRED
    country: str                                                                                   # REQUIRED
    date_of_birth: str                                                                             # REQUIRED
    display_name: str                                                                              # REQUIRED
    email_address: str                                                                             # REQUIRED
    password: str                                                                                  # REQUIRED
    password_md5_sum: str                                                                          # REQUIRED
    username: str                                                                                  # REQUIRED

    # endregion fields

    # region with_x methods

    def with_accepted_policies(self, value: List[LegalAcceptedPoliciesRequest]) -> AccountCreateUserRequestV4:
        self.accepted_policies = value
        return self

    def with_auth_type(self, value: str) -> AccountCreateUserRequestV4:
        self.auth_type = value
        return self

    def with_country(self, value: str) -> AccountCreateUserRequestV4:
        self.country = value
        return self

    def with_date_of_birth(self, value: str) -> AccountCreateUserRequestV4:
        self.date_of_birth = value
        return self

    def with_display_name(self, value: str) -> AccountCreateUserRequestV4:
        self.display_name = value
        return self

    def with_email_address(self, value: str) -> AccountCreateUserRequestV4:
        self.email_address = value
        return self

    def with_password(self, value: str) -> AccountCreateUserRequestV4:
        self.password = value
        return self

    def with_password_md5_sum(self, value: str) -> AccountCreateUserRequestV4:
        self.password_md5_sum = value
        return self

    def with_username(self, value: str) -> AccountCreateUserRequestV4:
        self.username = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "accepted_policies") and self.accepted_policies:
            result["acceptedPolicies"] = [i0.to_dict(include_empty=include_empty) for i0 in self.accepted_policies]
        elif include_empty:
            result["acceptedPolicies"] = []
        if hasattr(self, "auth_type") and self.auth_type:
            result["authType"] = str(self.auth_type)
        elif include_empty:
            result["authType"] = str()
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
        if hasattr(self, "password_md5_sum") and self.password_md5_sum:
            result["passwordMD5Sum"] = str(self.password_md5_sum)
        elif include_empty:
            result["passwordMD5Sum"] = str()
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
        auth_type: str,
        country: str,
        date_of_birth: str,
        display_name: str,
        email_address: str,
        password: str,
        password_md5_sum: str,
        username: str,
        accepted_policies: Optional[List[LegalAcceptedPoliciesRequest]] = None,
    ) -> AccountCreateUserRequestV4:
        instance = cls()
        instance.auth_type = auth_type
        instance.country = country
        instance.date_of_birth = date_of_birth
        instance.display_name = display_name
        instance.email_address = email_address
        instance.password = password
        instance.password_md5_sum = password_md5_sum
        instance.username = username
        if accepted_policies is not None:
            instance.accepted_policies = accepted_policies
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AccountCreateUserRequestV4:
        instance = cls()
        if "acceptedPolicies" in dict_ and dict_["acceptedPolicies"] is not None:
            instance.accepted_policies = [LegalAcceptedPoliciesRequest.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["acceptedPolicies"]]
        elif include_empty:
            instance.accepted_policies = []
        if "authType" in dict_ and dict_["authType"] is not None:
            instance.auth_type = str(dict_["authType"])
        elif include_empty:
            instance.auth_type = str()
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
        if "passwordMD5Sum" in dict_ and dict_["passwordMD5Sum"] is not None:
            instance.password_md5_sum = str(dict_["passwordMD5Sum"])
        elif include_empty:
            instance.password_md5_sum = str()
        if "username" in dict_ and dict_["username"] is not None:
            instance.username = str(dict_["username"])
        elif include_empty:
            instance.username = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "acceptedPolicies": "accepted_policies",
            "authType": "auth_type",
            "country": "country",
            "dateOfBirth": "date_of_birth",
            "displayName": "display_name",
            "emailAddress": "email_address",
            "password": "password",
            "passwordMD5Sum": "password_md5_sum",
            "username": "username",
        }

    # endregion static methods