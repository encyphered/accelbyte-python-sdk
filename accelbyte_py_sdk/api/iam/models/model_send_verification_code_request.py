# Auto-generated at 2021-09-27T17:12:31.624984+08:00
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


class ModelSendVerificationCodeRequest(Model):
    """Model send verification code request

    Properties:
        context: (Context) OPTIONAL str

        language_tag: (LanguageTag) REQUIRED str

        login_id: (LoginID) REQUIRED str
    """

    # region fields

    context: str                                                                                   # OPTIONAL
    language_tag: str                                                                              # REQUIRED
    login_id: str                                                                                  # REQUIRED

    # endregion fields

    # region with_x methods

    def with_context(self, value: str) -> ModelSendVerificationCodeRequest:
        self.context = value
        return self

    def with_language_tag(self, value: str) -> ModelSendVerificationCodeRequest:
        self.language_tag = value
        return self

    def with_login_id(self, value: str) -> ModelSendVerificationCodeRequest:
        self.login_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "context") and self.context:
            result["Context"] = str(self.context)
        elif include_empty:
            result["Context"] = str()
        if hasattr(self, "language_tag") and self.language_tag:
            result["LanguageTag"] = str(self.language_tag)
        elif include_empty:
            result["LanguageTag"] = str()
        if hasattr(self, "login_id") and self.login_id:
            result["LoginID"] = str(self.login_id)
        elif include_empty:
            result["LoginID"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        language_tag: str,
        login_id: str,
        context: Optional[str] = None,
    ) -> ModelSendVerificationCodeRequest:
        instance = cls()
        instance.language_tag = language_tag
        instance.login_id = login_id
        if context is not None:
            instance.context = context
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelSendVerificationCodeRequest:
        instance = cls()
        if not dict_:
            return instance
        if "Context" in dict_ and dict_["Context"] is not None:
            instance.context = str(dict_["Context"])
        elif include_empty:
            instance.context = str()
        if "LanguageTag" in dict_ and dict_["LanguageTag"] is not None:
            instance.language_tag = str(dict_["LanguageTag"])
        elif include_empty:
            instance.language_tag = str()
        if "LoginID" in dict_ and dict_["LoginID"] is not None:
            instance.login_id = str(dict_["LoginID"])
        elif include_empty:
            instance.login_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "Context": "context",
            "LanguageTag": "language_tag",
            "LoginID": "login_id",
        }

    # endregion static methods
