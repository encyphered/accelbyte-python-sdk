# Auto-generated at 2021-09-27T17:12:31.439417+08:00
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

from ..models.account_user_active_ban_response_v4 import AccountUserActiveBanResponseV4
from ..models.account_user_permissions_response_v4 import AccountUserPermissionsResponseV4


class AccountUserResponseV4(Model):
    """Account user response V4

    Properties:
        auth_type: (authType) REQUIRED str

        bans: (bans) REQUIRED List[AccountUserActiveBanResponseV4]

        country: (country) REQUIRED str

        created_at: (createdAt) REQUIRED str

        date_of_birth: (dateOfBirth) REQUIRED str

        deletion_status: (deletionStatus) REQUIRED bool

        display_name: (displayName) REQUIRED str

        email_address: (emailAddress) REQUIRED str

        email_verified: (emailVerified) REQUIRED bool

        enabled: (enabled) REQUIRED bool

        last_date_of_birth_changed_time: (lastDateOfBirthChangedTime) REQUIRED str

        last_enabled_changed_time: (lastEnabledChangedTime) REQUIRED str

        namespace: (namespace) REQUIRED str

        new_email_address: (newEmailAddress) OPTIONAL str

        old_email_address: (oldEmailAddress) REQUIRED str

        permissions: (permissions) REQUIRED List[AccountUserPermissionsResponseV4]

        phone_number: (phoneNumber) OPTIONAL str

        phone_verified: (phoneVerified) REQUIRED bool

        platform_id: (platformId) OPTIONAL str

        platform_user_id: (platformUserId) OPTIONAL str

        roles: (roles) REQUIRED List[str]

        user_id: (userId) REQUIRED str

        username: (username) OPTIONAL str
    """

    # region fields

    auth_type: str                                                                                 # REQUIRED
    bans: List[AccountUserActiveBanResponseV4]                                                     # REQUIRED
    country: str                                                                                   # REQUIRED
    created_at: str                                                                                # REQUIRED
    date_of_birth: str                                                                             # REQUIRED
    deletion_status: bool                                                                          # REQUIRED
    display_name: str                                                                              # REQUIRED
    email_address: str                                                                             # REQUIRED
    email_verified: bool                                                                           # REQUIRED
    enabled: bool                                                                                  # REQUIRED
    last_date_of_birth_changed_time: str                                                           # REQUIRED
    last_enabled_changed_time: str                                                                 # REQUIRED
    namespace: str                                                                                 # REQUIRED
    new_email_address: str                                                                         # OPTIONAL
    old_email_address: str                                                                         # REQUIRED
    permissions: List[AccountUserPermissionsResponseV4]                                            # REQUIRED
    phone_number: str                                                                              # OPTIONAL
    phone_verified: bool                                                                           # REQUIRED
    platform_id: str                                                                               # OPTIONAL
    platform_user_id: str                                                                          # OPTIONAL
    roles: List[str]                                                                               # REQUIRED
    user_id: str                                                                                   # REQUIRED
    username: str                                                                                  # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_auth_type(self, value: str) -> AccountUserResponseV4:
        self.auth_type = value
        return self

    def with_bans(self, value: List[AccountUserActiveBanResponseV4]) -> AccountUserResponseV4:
        self.bans = value
        return self

    def with_country(self, value: str) -> AccountUserResponseV4:
        self.country = value
        return self

    def with_created_at(self, value: str) -> AccountUserResponseV4:
        self.created_at = value
        return self

    def with_date_of_birth(self, value: str) -> AccountUserResponseV4:
        self.date_of_birth = value
        return self

    def with_deletion_status(self, value: bool) -> AccountUserResponseV4:
        self.deletion_status = value
        return self

    def with_display_name(self, value: str) -> AccountUserResponseV4:
        self.display_name = value
        return self

    def with_email_address(self, value: str) -> AccountUserResponseV4:
        self.email_address = value
        return self

    def with_email_verified(self, value: bool) -> AccountUserResponseV4:
        self.email_verified = value
        return self

    def with_enabled(self, value: bool) -> AccountUserResponseV4:
        self.enabled = value
        return self

    def with_last_date_of_birth_changed_time(self, value: str) -> AccountUserResponseV4:
        self.last_date_of_birth_changed_time = value
        return self

    def with_last_enabled_changed_time(self, value: str) -> AccountUserResponseV4:
        self.last_enabled_changed_time = value
        return self

    def with_namespace(self, value: str) -> AccountUserResponseV4:
        self.namespace = value
        return self

    def with_new_email_address(self, value: str) -> AccountUserResponseV4:
        self.new_email_address = value
        return self

    def with_old_email_address(self, value: str) -> AccountUserResponseV4:
        self.old_email_address = value
        return self

    def with_permissions(self, value: List[AccountUserPermissionsResponseV4]) -> AccountUserResponseV4:
        self.permissions = value
        return self

    def with_phone_number(self, value: str) -> AccountUserResponseV4:
        self.phone_number = value
        return self

    def with_phone_verified(self, value: bool) -> AccountUserResponseV4:
        self.phone_verified = value
        return self

    def with_platform_id(self, value: str) -> AccountUserResponseV4:
        self.platform_id = value
        return self

    def with_platform_user_id(self, value: str) -> AccountUserResponseV4:
        self.platform_user_id = value
        return self

    def with_roles(self, value: List[str]) -> AccountUserResponseV4:
        self.roles = value
        return self

    def with_user_id(self, value: str) -> AccountUserResponseV4:
        self.user_id = value
        return self

    def with_username(self, value: str) -> AccountUserResponseV4:
        self.username = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "auth_type") and self.auth_type:
            result["authType"] = str(self.auth_type)
        elif include_empty:
            result["authType"] = str()
        if hasattr(self, "bans") and self.bans:
            result["bans"] = [i0.to_dict(include_empty=include_empty) for i0 in self.bans]
        elif include_empty:
            result["bans"] = []
        if hasattr(self, "country") and self.country:
            result["country"] = str(self.country)
        elif include_empty:
            result["country"] = str()
        if hasattr(self, "created_at") and self.created_at:
            result["createdAt"] = str(self.created_at)
        elif include_empty:
            result["createdAt"] = str()
        if hasattr(self, "date_of_birth") and self.date_of_birth:
            result["dateOfBirth"] = str(self.date_of_birth)
        elif include_empty:
            result["dateOfBirth"] = str()
        if hasattr(self, "deletion_status") and self.deletion_status:
            result["deletionStatus"] = bool(self.deletion_status)
        elif include_empty:
            result["deletionStatus"] = bool()
        if hasattr(self, "display_name") and self.display_name:
            result["displayName"] = str(self.display_name)
        elif include_empty:
            result["displayName"] = str()
        if hasattr(self, "email_address") and self.email_address:
            result["emailAddress"] = str(self.email_address)
        elif include_empty:
            result["emailAddress"] = str()
        if hasattr(self, "email_verified") and self.email_verified:
            result["emailVerified"] = bool(self.email_verified)
        elif include_empty:
            result["emailVerified"] = bool()
        if hasattr(self, "enabled") and self.enabled:
            result["enabled"] = bool(self.enabled)
        elif include_empty:
            result["enabled"] = bool()
        if hasattr(self, "last_date_of_birth_changed_time") and self.last_date_of_birth_changed_time:
            result["lastDateOfBirthChangedTime"] = str(self.last_date_of_birth_changed_time)
        elif include_empty:
            result["lastDateOfBirthChangedTime"] = str()
        if hasattr(self, "last_enabled_changed_time") and self.last_enabled_changed_time:
            result["lastEnabledChangedTime"] = str(self.last_enabled_changed_time)
        elif include_empty:
            result["lastEnabledChangedTime"] = str()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "new_email_address") and self.new_email_address:
            result["newEmailAddress"] = str(self.new_email_address)
        elif include_empty:
            result["newEmailAddress"] = str()
        if hasattr(self, "old_email_address") and self.old_email_address:
            result["oldEmailAddress"] = str(self.old_email_address)
        elif include_empty:
            result["oldEmailAddress"] = str()
        if hasattr(self, "permissions") and self.permissions:
            result["permissions"] = [i0.to_dict(include_empty=include_empty) for i0 in self.permissions]
        elif include_empty:
            result["permissions"] = []
        if hasattr(self, "phone_number") and self.phone_number:
            result["phoneNumber"] = str(self.phone_number)
        elif include_empty:
            result["phoneNumber"] = str()
        if hasattr(self, "phone_verified") and self.phone_verified:
            result["phoneVerified"] = bool(self.phone_verified)
        elif include_empty:
            result["phoneVerified"] = bool()
        if hasattr(self, "platform_id") and self.platform_id:
            result["platformId"] = str(self.platform_id)
        elif include_empty:
            result["platformId"] = str()
        if hasattr(self, "platform_user_id") and self.platform_user_id:
            result["platformUserId"] = str(self.platform_user_id)
        elif include_empty:
            result["platformUserId"] = str()
        if hasattr(self, "roles") and self.roles:
            result["roles"] = [str(i0) for i0 in self.roles]
        elif include_empty:
            result["roles"] = []
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
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
        bans: List[AccountUserActiveBanResponseV4],
        country: str,
        created_at: str,
        date_of_birth: str,
        deletion_status: bool,
        display_name: str,
        email_address: str,
        email_verified: bool,
        enabled: bool,
        last_date_of_birth_changed_time: str,
        last_enabled_changed_time: str,
        namespace: str,
        old_email_address: str,
        permissions: List[AccountUserPermissionsResponseV4],
        phone_verified: bool,
        roles: List[str],
        user_id: str,
        new_email_address: Optional[str] = None,
        phone_number: Optional[str] = None,
        platform_id: Optional[str] = None,
        platform_user_id: Optional[str] = None,
        username: Optional[str] = None,
    ) -> AccountUserResponseV4:
        instance = cls()
        instance.auth_type = auth_type
        instance.bans = bans
        instance.country = country
        instance.created_at = created_at
        instance.date_of_birth = date_of_birth
        instance.deletion_status = deletion_status
        instance.display_name = display_name
        instance.email_address = email_address
        instance.email_verified = email_verified
        instance.enabled = enabled
        instance.last_date_of_birth_changed_time = last_date_of_birth_changed_time
        instance.last_enabled_changed_time = last_enabled_changed_time
        instance.namespace = namespace
        instance.old_email_address = old_email_address
        instance.permissions = permissions
        instance.phone_verified = phone_verified
        instance.roles = roles
        instance.user_id = user_id
        if new_email_address is not None:
            instance.new_email_address = new_email_address
        if phone_number is not None:
            instance.phone_number = phone_number
        if platform_id is not None:
            instance.platform_id = platform_id
        if platform_user_id is not None:
            instance.platform_user_id = platform_user_id
        if username is not None:
            instance.username = username
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AccountUserResponseV4:
        instance = cls()
        if not dict_:
            return instance
        if "authType" in dict_ and dict_["authType"] is not None:
            instance.auth_type = str(dict_["authType"])
        elif include_empty:
            instance.auth_type = str()
        if "bans" in dict_ and dict_["bans"] is not None:
            instance.bans = [AccountUserActiveBanResponseV4.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["bans"]]
        elif include_empty:
            instance.bans = []
        if "country" in dict_ and dict_["country"] is not None:
            instance.country = str(dict_["country"])
        elif include_empty:
            instance.country = str()
        if "createdAt" in dict_ and dict_["createdAt"] is not None:
            instance.created_at = str(dict_["createdAt"])
        elif include_empty:
            instance.created_at = str()
        if "dateOfBirth" in dict_ and dict_["dateOfBirth"] is not None:
            instance.date_of_birth = str(dict_["dateOfBirth"])
        elif include_empty:
            instance.date_of_birth = str()
        if "deletionStatus" in dict_ and dict_["deletionStatus"] is not None:
            instance.deletion_status = bool(dict_["deletionStatus"])
        elif include_empty:
            instance.deletion_status = bool()
        if "displayName" in dict_ and dict_["displayName"] is not None:
            instance.display_name = str(dict_["displayName"])
        elif include_empty:
            instance.display_name = str()
        if "emailAddress" in dict_ and dict_["emailAddress"] is not None:
            instance.email_address = str(dict_["emailAddress"])
        elif include_empty:
            instance.email_address = str()
        if "emailVerified" in dict_ and dict_["emailVerified"] is not None:
            instance.email_verified = bool(dict_["emailVerified"])
        elif include_empty:
            instance.email_verified = bool()
        if "enabled" in dict_ and dict_["enabled"] is not None:
            instance.enabled = bool(dict_["enabled"])
        elif include_empty:
            instance.enabled = bool()
        if "lastDateOfBirthChangedTime" in dict_ and dict_["lastDateOfBirthChangedTime"] is not None:
            instance.last_date_of_birth_changed_time = str(dict_["lastDateOfBirthChangedTime"])
        elif include_empty:
            instance.last_date_of_birth_changed_time = str()
        if "lastEnabledChangedTime" in dict_ and dict_["lastEnabledChangedTime"] is not None:
            instance.last_enabled_changed_time = str(dict_["lastEnabledChangedTime"])
        elif include_empty:
            instance.last_enabled_changed_time = str()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "newEmailAddress" in dict_ and dict_["newEmailAddress"] is not None:
            instance.new_email_address = str(dict_["newEmailAddress"])
        elif include_empty:
            instance.new_email_address = str()
        if "oldEmailAddress" in dict_ and dict_["oldEmailAddress"] is not None:
            instance.old_email_address = str(dict_["oldEmailAddress"])
        elif include_empty:
            instance.old_email_address = str()
        if "permissions" in dict_ and dict_["permissions"] is not None:
            instance.permissions = [AccountUserPermissionsResponseV4.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["permissions"]]
        elif include_empty:
            instance.permissions = []
        if "phoneNumber" in dict_ and dict_["phoneNumber"] is not None:
            instance.phone_number = str(dict_["phoneNumber"])
        elif include_empty:
            instance.phone_number = str()
        if "phoneVerified" in dict_ and dict_["phoneVerified"] is not None:
            instance.phone_verified = bool(dict_["phoneVerified"])
        elif include_empty:
            instance.phone_verified = bool()
        if "platformId" in dict_ and dict_["platformId"] is not None:
            instance.platform_id = str(dict_["platformId"])
        elif include_empty:
            instance.platform_id = str()
        if "platformUserId" in dict_ and dict_["platformUserId"] is not None:
            instance.platform_user_id = str(dict_["platformUserId"])
        elif include_empty:
            instance.platform_user_id = str()
        if "roles" in dict_ and dict_["roles"] is not None:
            instance.roles = [str(i0) for i0 in dict_["roles"]]
        elif include_empty:
            instance.roles = []
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        if "username" in dict_ and dict_["username"] is not None:
            instance.username = str(dict_["username"])
        elif include_empty:
            instance.username = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "authType": "auth_type",
            "bans": "bans",
            "country": "country",
            "createdAt": "created_at",
            "dateOfBirth": "date_of_birth",
            "deletionStatus": "deletion_status",
            "displayName": "display_name",
            "emailAddress": "email_address",
            "emailVerified": "email_verified",
            "enabled": "enabled",
            "lastDateOfBirthChangedTime": "last_date_of_birth_changed_time",
            "lastEnabledChangedTime": "last_enabled_changed_time",
            "namespace": "namespace",
            "newEmailAddress": "new_email_address",
            "oldEmailAddress": "old_email_address",
            "permissions": "permissions",
            "phoneNumber": "phone_number",
            "phoneVerified": "phone_verified",
            "platformId": "platform_id",
            "platformUserId": "platform_user_id",
            "roles": "roles",
            "userId": "user_id",
            "username": "username",
        }

    # endregion static methods
