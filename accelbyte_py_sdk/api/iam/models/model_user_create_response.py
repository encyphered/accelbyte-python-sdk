# Auto-generated at 2021-09-27T17:12:31.657105+08:00
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


class ModelUserCreateResponse(Model):
    """Model user create response

    Properties:
        auth_type: (AuthType) REQUIRED str

        country: (Country) REQUIRED str

        date_of_birth: (DateOfBirth) REQUIRED str

        display_name: (DisplayName) REQUIRED str

        login_id: (LoginId) REQUIRED str

        namespace: (Namespace) REQUIRED str

        user_id: (UserId) REQUIRED str
    """

    # region fields

    auth_type: str                                                                                 # REQUIRED
    country: str                                                                                   # REQUIRED
    date_of_birth: str                                                                             # REQUIRED
    display_name: str                                                                              # REQUIRED
    login_id: str                                                                                  # REQUIRED
    namespace: str                                                                                 # REQUIRED
    user_id: str                                                                                   # REQUIRED

    # endregion fields

    # region with_x methods

    def with_auth_type(self, value: str) -> ModelUserCreateResponse:
        self.auth_type = value
        return self

    def with_country(self, value: str) -> ModelUserCreateResponse:
        self.country = value
        return self

    def with_date_of_birth(self, value: str) -> ModelUserCreateResponse:
        self.date_of_birth = value
        return self

    def with_display_name(self, value: str) -> ModelUserCreateResponse:
        self.display_name = value
        return self

    def with_login_id(self, value: str) -> ModelUserCreateResponse:
        self.login_id = value
        return self

    def with_namespace(self, value: str) -> ModelUserCreateResponse:
        self.namespace = value
        return self

    def with_user_id(self, value: str) -> ModelUserCreateResponse:
        self.user_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "auth_type") and self.auth_type:
            result["AuthType"] = str(self.auth_type)
        elif include_empty:
            result["AuthType"] = str()
        if hasattr(self, "country") and self.country:
            result["Country"] = str(self.country)
        elif include_empty:
            result["Country"] = str()
        if hasattr(self, "date_of_birth") and self.date_of_birth:
            result["DateOfBirth"] = str(self.date_of_birth)
        elif include_empty:
            result["DateOfBirth"] = str()
        if hasattr(self, "display_name") and self.display_name:
            result["DisplayName"] = str(self.display_name)
        elif include_empty:
            result["DisplayName"] = str()
        if hasattr(self, "login_id") and self.login_id:
            result["LoginId"] = str(self.login_id)
        elif include_empty:
            result["LoginId"] = str()
        if hasattr(self, "namespace") and self.namespace:
            result["Namespace"] = str(self.namespace)
        elif include_empty:
            result["Namespace"] = str()
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
        auth_type: str,
        country: str,
        date_of_birth: str,
        display_name: str,
        login_id: str,
        namespace: str,
        user_id: str,
    ) -> ModelUserCreateResponse:
        instance = cls()
        instance.auth_type = auth_type
        instance.country = country
        instance.date_of_birth = date_of_birth
        instance.display_name = display_name
        instance.login_id = login_id
        instance.namespace = namespace
        instance.user_id = user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelUserCreateResponse:
        instance = cls()
        if not dict_:
            return instance
        if "AuthType" in dict_ and dict_["AuthType"] is not None:
            instance.auth_type = str(dict_["AuthType"])
        elif include_empty:
            instance.auth_type = str()
        if "Country" in dict_ and dict_["Country"] is not None:
            instance.country = str(dict_["Country"])
        elif include_empty:
            instance.country = str()
        if "DateOfBirth" in dict_ and dict_["DateOfBirth"] is not None:
            instance.date_of_birth = str(dict_["DateOfBirth"])
        elif include_empty:
            instance.date_of_birth = str()
        if "DisplayName" in dict_ and dict_["DisplayName"] is not None:
            instance.display_name = str(dict_["DisplayName"])
        elif include_empty:
            instance.display_name = str()
        if "LoginId" in dict_ and dict_["LoginId"] is not None:
            instance.login_id = str(dict_["LoginId"])
        elif include_empty:
            instance.login_id = str()
        if "Namespace" in dict_ and dict_["Namespace"] is not None:
            instance.namespace = str(dict_["Namespace"])
        elif include_empty:
            instance.namespace = str()
        if "UserId" in dict_ and dict_["UserId"] is not None:
            instance.user_id = str(dict_["UserId"])
        elif include_empty:
            instance.user_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "AuthType": "auth_type",
            "Country": "country",
            "DateOfBirth": "date_of_birth",
            "DisplayName": "display_name",
            "LoginId": "login_id",
            "Namespace": "namespace",
            "UserId": "user_id",
        }

    # endregion static methods
