# Auto-generated at 2021-09-27T17:12:31.683856+08:00
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


class ModelUserUpdateRequest(Model):
    """Model user update request

    Properties:
        country: (Country) OPTIONAL str

        date_of_birth: (DateOfBirth) OPTIONAL str

        display_name: (DisplayName) OPTIONAL str

        language_tag: (LanguageTag) OPTIONAL str
    """

    # region fields

    country: str                                                                                   # OPTIONAL
    date_of_birth: str                                                                             # OPTIONAL
    display_name: str                                                                              # OPTIONAL
    language_tag: str                                                                              # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_country(self, value: str) -> ModelUserUpdateRequest:
        self.country = value
        return self

    def with_date_of_birth(self, value: str) -> ModelUserUpdateRequest:
        self.date_of_birth = value
        return self

    def with_display_name(self, value: str) -> ModelUserUpdateRequest:
        self.display_name = value
        return self

    def with_language_tag(self, value: str) -> ModelUserUpdateRequest:
        self.language_tag = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
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
        if hasattr(self, "language_tag") and self.language_tag:
            result["LanguageTag"] = str(self.language_tag)
        elif include_empty:
            result["LanguageTag"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        country: Optional[str] = None,
        date_of_birth: Optional[str] = None,
        display_name: Optional[str] = None,
        language_tag: Optional[str] = None,
    ) -> ModelUserUpdateRequest:
        instance = cls()
        if country is not None:
            instance.country = country
        if date_of_birth is not None:
            instance.date_of_birth = date_of_birth
        if display_name is not None:
            instance.display_name = display_name
        if language_tag is not None:
            instance.language_tag = language_tag
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelUserUpdateRequest:
        instance = cls()
        if not dict_:
            return instance
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
        if "LanguageTag" in dict_ and dict_["LanguageTag"] is not None:
            instance.language_tag = str(dict_["LanguageTag"])
        elif include_empty:
            instance.language_tag = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "Country": "country",
            "DateOfBirth": "date_of_birth",
            "DisplayName": "display_name",
            "LanguageTag": "language_tag",
        }

    # endregion static methods
