# Auto-generated at 2021-09-27T17:12:31.690069+08:00
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


class ModelUserVerificationRequestV3(Model):
    """Model user verification request V3

    Properties:
        code: (code) REQUIRED str

        contact_type: (contactType) REQUIRED str

        language_tag: (languageTag) REQUIRED str
    """

    # region fields

    code: str                                                                                      # REQUIRED
    contact_type: str                                                                              # REQUIRED
    language_tag: str                                                                              # REQUIRED

    # endregion fields

    # region with_x methods

    def with_code(self, value: str) -> ModelUserVerificationRequestV3:
        self.code = value
        return self

    def with_contact_type(self, value: str) -> ModelUserVerificationRequestV3:
        self.contact_type = value
        return self

    def with_language_tag(self, value: str) -> ModelUserVerificationRequestV3:
        self.language_tag = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "code") and self.code:
            result["code"] = str(self.code)
        elif include_empty:
            result["code"] = str()
        if hasattr(self, "contact_type") and self.contact_type:
            result["contactType"] = str(self.contact_type)
        elif include_empty:
            result["contactType"] = str()
        if hasattr(self, "language_tag") and self.language_tag:
            result["languageTag"] = str(self.language_tag)
        elif include_empty:
            result["languageTag"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        code: str,
        contact_type: str,
        language_tag: str,
    ) -> ModelUserVerificationRequestV3:
        instance = cls()
        instance.code = code
        instance.contact_type = contact_type
        instance.language_tag = language_tag
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelUserVerificationRequestV3:
        instance = cls()
        if not dict_:
            return instance
        if "code" in dict_ and dict_["code"] is not None:
            instance.code = str(dict_["code"])
        elif include_empty:
            instance.code = str()
        if "contactType" in dict_ and dict_["contactType"] is not None:
            instance.contact_type = str(dict_["contactType"])
        elif include_empty:
            instance.contact_type = str()
        if "languageTag" in dict_ and dict_["languageTag"] is not None:
            instance.language_tag = str(dict_["languageTag"])
        elif include_empty:
            instance.language_tag = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "code": "code",
            "contactType": "contact_type",
            "languageTag": "language_tag",
        }

    # endregion static methods
