# Auto-generated at 2021-09-27T17:12:31.502865+08:00
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

from ..models.accountcommon_user_linked_platform import AccountcommonUserLinkedPlatform


class AccountcommonUserSearchResult(Model):
    """Accountcommon user search result

    Properties:
        display_name: (DisplayName) REQUIRED str

        email_address: (EmailAddress) REQUIRED str

        linked_platforms: (LinkedPlatforms) REQUIRED List[AccountcommonUserLinkedPlatform]

        phone_number: (PhoneNumber) REQUIRED str

        user_id: (UserId) REQUIRED str
    """

    # region fields

    display_name: str                                                                              # REQUIRED
    email_address: str                                                                             # REQUIRED
    linked_platforms: List[AccountcommonUserLinkedPlatform]                                        # REQUIRED
    phone_number: str                                                                              # REQUIRED
    user_id: str                                                                                   # REQUIRED

    # endregion fields

    # region with_x methods

    def with_display_name(self, value: str) -> AccountcommonUserSearchResult:
        self.display_name = value
        return self

    def with_email_address(self, value: str) -> AccountcommonUserSearchResult:
        self.email_address = value
        return self

    def with_linked_platforms(self, value: List[AccountcommonUserLinkedPlatform]) -> AccountcommonUserSearchResult:
        self.linked_platforms = value
        return self

    def with_phone_number(self, value: str) -> AccountcommonUserSearchResult:
        self.phone_number = value
        return self

    def with_user_id(self, value: str) -> AccountcommonUserSearchResult:
        self.user_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "display_name") and self.display_name:
            result["DisplayName"] = str(self.display_name)
        elif include_empty:
            result["DisplayName"] = str()
        if hasattr(self, "email_address") and self.email_address:
            result["EmailAddress"] = str(self.email_address)
        elif include_empty:
            result["EmailAddress"] = str()
        if hasattr(self, "linked_platforms") and self.linked_platforms:
            result["LinkedPlatforms"] = [i0.to_dict(include_empty=include_empty) for i0 in self.linked_platforms]
        elif include_empty:
            result["LinkedPlatforms"] = []
        if hasattr(self, "phone_number") and self.phone_number:
            result["PhoneNumber"] = str(self.phone_number)
        elif include_empty:
            result["PhoneNumber"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["UserId"] = str(self.user_id)
        elif include_empty:
            result["UserId"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        display_name: str,
        email_address: str,
        linked_platforms: List[AccountcommonUserLinkedPlatform],
        phone_number: str,
        user_id: str,
    ) -> AccountcommonUserSearchResult:
        instance = cls()
        instance.display_name = display_name
        instance.email_address = email_address
        instance.linked_platforms = linked_platforms
        instance.phone_number = phone_number
        instance.user_id = user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AccountcommonUserSearchResult:
        instance = cls()
        if not dict_:
            return instance
        if "DisplayName" in dict_ and dict_["DisplayName"] is not None:
            instance.display_name = str(dict_["DisplayName"])
        elif include_empty:
            instance.display_name = str()
        if "EmailAddress" in dict_ and dict_["EmailAddress"] is not None:
            instance.email_address = str(dict_["EmailAddress"])
        elif include_empty:
            instance.email_address = str()
        if "LinkedPlatforms" in dict_ and dict_["LinkedPlatforms"] is not None:
            instance.linked_platforms = [AccountcommonUserLinkedPlatform.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["LinkedPlatforms"]]
        elif include_empty:
            instance.linked_platforms = []
        if "PhoneNumber" in dict_ and dict_["PhoneNumber"] is not None:
            instance.phone_number = str(dict_["PhoneNumber"])
        elif include_empty:
            instance.phone_number = str()
        if "UserId" in dict_ and dict_["UserId"] is not None:
            instance.user_id = str(dict_["UserId"])
        elif include_empty:
            instance.user_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "DisplayName": "display_name",
            "EmailAddress": "email_address",
            "LinkedPlatforms": "linked_platforms",
            "PhoneNumber": "phone_number",
            "UserId": "user_id",
        }

    # endregion static methods
