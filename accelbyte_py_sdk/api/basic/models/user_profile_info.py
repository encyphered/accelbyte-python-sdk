# Auto-generated at 2021-09-27T17:12:38.727657+08:00
# from: Justice Basic Service (1.17.0)

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


class UserProfileInfo(Model):
    """User profile info

    Properties:
        user_id: (userId) OPTIONAL str

        namespace: (namespace) OPTIONAL str

        first_name: (firstName) OPTIONAL str

        last_name: (lastName) OPTIONAL str

        avatar_small_url: (avatarSmallUrl) OPTIONAL str

        avatar_url: (avatarUrl) OPTIONAL str

        avatar_large_url: (avatarLargeUrl) OPTIONAL str

        status: (status) OPTIONAL str

        language: (language) OPTIONAL str

        time_zone: (timeZone) OPTIONAL str

        date_of_birth: (dateOfBirth) OPTIONAL str

        custom_attributes: (customAttributes) OPTIONAL Dict[str, Any]

        zip_code: (zipCode) OPTIONAL str
    """

    # region fields

    user_id: str                                                                                   # OPTIONAL
    namespace: str                                                                                 # OPTIONAL
    first_name: str                                                                                # OPTIONAL
    last_name: str                                                                                 # OPTIONAL
    avatar_small_url: str                                                                          # OPTIONAL
    avatar_url: str                                                                                # OPTIONAL
    avatar_large_url: str                                                                          # OPTIONAL
    status: str                                                                                    # OPTIONAL
    language: str                                                                                  # OPTIONAL
    time_zone: str                                                                                 # OPTIONAL
    date_of_birth: str                                                                             # OPTIONAL
    custom_attributes: Dict[str, Any]                                                              # OPTIONAL
    zip_code: str                                                                                  # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_user_id(self, value: str) -> UserProfileInfo:
        self.user_id = value
        return self

    def with_namespace(self, value: str) -> UserProfileInfo:
        self.namespace = value
        return self

    def with_first_name(self, value: str) -> UserProfileInfo:
        self.first_name = value
        return self

    def with_last_name(self, value: str) -> UserProfileInfo:
        self.last_name = value
        return self

    def with_avatar_small_url(self, value: str) -> UserProfileInfo:
        self.avatar_small_url = value
        return self

    def with_avatar_url(self, value: str) -> UserProfileInfo:
        self.avatar_url = value
        return self

    def with_avatar_large_url(self, value: str) -> UserProfileInfo:
        self.avatar_large_url = value
        return self

    def with_status(self, value: str) -> UserProfileInfo:
        self.status = value
        return self

    def with_language(self, value: str) -> UserProfileInfo:
        self.language = value
        return self

    def with_time_zone(self, value: str) -> UserProfileInfo:
        self.time_zone = value
        return self

    def with_date_of_birth(self, value: str) -> UserProfileInfo:
        self.date_of_birth = value
        return self

    def with_custom_attributes(self, value: Dict[str, Any]) -> UserProfileInfo:
        self.custom_attributes = value
        return self

    def with_zip_code(self, value: str) -> UserProfileInfo:
        self.zip_code = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "first_name") and self.first_name:
            result["firstName"] = str(self.first_name)
        elif include_empty:
            result["firstName"] = str()
        if hasattr(self, "last_name") and self.last_name:
            result["lastName"] = str(self.last_name)
        elif include_empty:
            result["lastName"] = str()
        if hasattr(self, "avatar_small_url") and self.avatar_small_url:
            result["avatarSmallUrl"] = str(self.avatar_small_url)
        elif include_empty:
            result["avatarSmallUrl"] = str()
        if hasattr(self, "avatar_url") and self.avatar_url:
            result["avatarUrl"] = str(self.avatar_url)
        elif include_empty:
            result["avatarUrl"] = str()
        if hasattr(self, "avatar_large_url") and self.avatar_large_url:
            result["avatarLargeUrl"] = str(self.avatar_large_url)
        elif include_empty:
            result["avatarLargeUrl"] = str()
        if hasattr(self, "status") and self.status:
            result["status"] = str(self.status)
        elif include_empty:
            result["status"] = str()
        if hasattr(self, "language") and self.language:
            result["language"] = str(self.language)
        elif include_empty:
            result["language"] = str()
        if hasattr(self, "time_zone") and self.time_zone:
            result["timeZone"] = str(self.time_zone)
        elif include_empty:
            result["timeZone"] = str()
        if hasattr(self, "date_of_birth") and self.date_of_birth:
            result["dateOfBirth"] = str(self.date_of_birth)
        elif include_empty:
            result["dateOfBirth"] = str()
        if hasattr(self, "custom_attributes") and self.custom_attributes:
            result["customAttributes"] = {str(k0): v0 for k0, v0 in self.custom_attributes.items()}
        elif include_empty:
            result["customAttributes"] = {}
        if hasattr(self, "zip_code") and self.zip_code:
            result["zipCode"] = str(self.zip_code)
        elif include_empty:
            result["zipCode"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        user_id: Optional[str] = None,
        namespace: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        avatar_small_url: Optional[str] = None,
        avatar_url: Optional[str] = None,
        avatar_large_url: Optional[str] = None,
        status: Optional[str] = None,
        language: Optional[str] = None,
        time_zone: Optional[str] = None,
        date_of_birth: Optional[str] = None,
        custom_attributes: Optional[Dict[str, Any]] = None,
        zip_code: Optional[str] = None,
    ) -> UserProfileInfo:
        instance = cls()
        if user_id is not None:
            instance.user_id = user_id
        if namespace is not None:
            instance.namespace = namespace
        if first_name is not None:
            instance.first_name = first_name
        if last_name is not None:
            instance.last_name = last_name
        if avatar_small_url is not None:
            instance.avatar_small_url = avatar_small_url
        if avatar_url is not None:
            instance.avatar_url = avatar_url
        if avatar_large_url is not None:
            instance.avatar_large_url = avatar_large_url
        if status is not None:
            instance.status = status
        if language is not None:
            instance.language = language
        if time_zone is not None:
            instance.time_zone = time_zone
        if date_of_birth is not None:
            instance.date_of_birth = date_of_birth
        if custom_attributes is not None:
            instance.custom_attributes = custom_attributes
        if zip_code is not None:
            instance.zip_code = zip_code
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> UserProfileInfo:
        instance = cls()
        if not dict_:
            return instance
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "firstName" in dict_ and dict_["firstName"] is not None:
            instance.first_name = str(dict_["firstName"])
        elif include_empty:
            instance.first_name = str()
        if "lastName" in dict_ and dict_["lastName"] is not None:
            instance.last_name = str(dict_["lastName"])
        elif include_empty:
            instance.last_name = str()
        if "avatarSmallUrl" in dict_ and dict_["avatarSmallUrl"] is not None:
            instance.avatar_small_url = str(dict_["avatarSmallUrl"])
        elif include_empty:
            instance.avatar_small_url = str()
        if "avatarUrl" in dict_ and dict_["avatarUrl"] is not None:
            instance.avatar_url = str(dict_["avatarUrl"])
        elif include_empty:
            instance.avatar_url = str()
        if "avatarLargeUrl" in dict_ and dict_["avatarLargeUrl"] is not None:
            instance.avatar_large_url = str(dict_["avatarLargeUrl"])
        elif include_empty:
            instance.avatar_large_url = str()
        if "status" in dict_ and dict_["status"] is not None:
            instance.status = str(dict_["status"])
        elif include_empty:
            instance.status = str()
        if "language" in dict_ and dict_["language"] is not None:
            instance.language = str(dict_["language"])
        elif include_empty:
            instance.language = str()
        if "timeZone" in dict_ and dict_["timeZone"] is not None:
            instance.time_zone = str(dict_["timeZone"])
        elif include_empty:
            instance.time_zone = str()
        if "dateOfBirth" in dict_ and dict_["dateOfBirth"] is not None:
            instance.date_of_birth = str(dict_["dateOfBirth"])
        elif include_empty:
            instance.date_of_birth = str()
        if "customAttributes" in dict_ and dict_["customAttributes"] is not None:
            instance.custom_attributes = {str(k0): v0 for k0, v0 in dict_["customAttributes"].items()}
        elif include_empty:
            instance.custom_attributes = {}
        if "zipCode" in dict_ and dict_["zipCode"] is not None:
            instance.zip_code = str(dict_["zipCode"])
        elif include_empty:
            instance.zip_code = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "userId": "user_id",
            "namespace": "namespace",
            "firstName": "first_name",
            "lastName": "last_name",
            "avatarSmallUrl": "avatar_small_url",
            "avatarUrl": "avatar_url",
            "avatarLargeUrl": "avatar_large_url",
            "status": "status",
            "language": "language",
            "timeZone": "time_zone",
            "dateOfBirth": "date_of_birth",
            "customAttributes": "custom_attributes",
            "zipCode": "zip_code",
        }

    # endregion static methods
