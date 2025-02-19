# Auto-generated at 2021-09-27T17:12:36.397741+08:00
# from: Justice Platform Service (3.24.0)

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


class AdyenConfig(Model):
    """A DTO object for updating adyen config.

    Properties:
        api_key: (apiKey) OPTIONAL str

        merchant_account: (merchantAccount) OPTIONAL str

        notification_hmac_key: (notificationHmacKey) OPTIONAL str

        notification_username: (notificationUsername) OPTIONAL str

        notification_password: (notificationPassword) OPTIONAL str

        return_url: (returnUrl) OPTIONAL str

        live_endpoint_url_prefix: (liveEndpointUrlPrefix) OPTIONAL str

        authorise_as_capture: (authoriseAsCapture) OPTIONAL bool

        allowed_payment_methods: (allowedPaymentMethods) OPTIONAL List[str]

        blocked_payment_methods: (blockedPaymentMethods) OPTIONAL List[str]

        settings: (settings) OPTIONAL str
    """

    # region fields

    api_key: str                                                                                   # OPTIONAL
    merchant_account: str                                                                          # OPTIONAL
    notification_hmac_key: str                                                                     # OPTIONAL
    notification_username: str                                                                     # OPTIONAL
    notification_password: str                                                                     # OPTIONAL
    return_url: str                                                                                # OPTIONAL
    live_endpoint_url_prefix: str                                                                  # OPTIONAL
    authorise_as_capture: bool                                                                     # OPTIONAL
    allowed_payment_methods: List[str]                                                             # OPTIONAL
    blocked_payment_methods: List[str]                                                             # OPTIONAL
    settings: str                                                                                  # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_api_key(self, value: str) -> AdyenConfig:
        self.api_key = value
        return self

    def with_merchant_account(self, value: str) -> AdyenConfig:
        self.merchant_account = value
        return self

    def with_notification_hmac_key(self, value: str) -> AdyenConfig:
        self.notification_hmac_key = value
        return self

    def with_notification_username(self, value: str) -> AdyenConfig:
        self.notification_username = value
        return self

    def with_notification_password(self, value: str) -> AdyenConfig:
        self.notification_password = value
        return self

    def with_return_url(self, value: str) -> AdyenConfig:
        self.return_url = value
        return self

    def with_live_endpoint_url_prefix(self, value: str) -> AdyenConfig:
        self.live_endpoint_url_prefix = value
        return self

    def with_authorise_as_capture(self, value: bool) -> AdyenConfig:
        self.authorise_as_capture = value
        return self

    def with_allowed_payment_methods(self, value: List[str]) -> AdyenConfig:
        self.allowed_payment_methods = value
        return self

    def with_blocked_payment_methods(self, value: List[str]) -> AdyenConfig:
        self.blocked_payment_methods = value
        return self

    def with_settings(self, value: str) -> AdyenConfig:
        self.settings = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "api_key") and self.api_key:
            result["apiKey"] = str(self.api_key)
        elif include_empty:
            result["apiKey"] = str()
        if hasattr(self, "merchant_account") and self.merchant_account:
            result["merchantAccount"] = str(self.merchant_account)
        elif include_empty:
            result["merchantAccount"] = str()
        if hasattr(self, "notification_hmac_key") and self.notification_hmac_key:
            result["notificationHmacKey"] = str(self.notification_hmac_key)
        elif include_empty:
            result["notificationHmacKey"] = str()
        if hasattr(self, "notification_username") and self.notification_username:
            result["notificationUsername"] = str(self.notification_username)
        elif include_empty:
            result["notificationUsername"] = str()
        if hasattr(self, "notification_password") and self.notification_password:
            result["notificationPassword"] = str(self.notification_password)
        elif include_empty:
            result["notificationPassword"] = str()
        if hasattr(self, "return_url") and self.return_url:
            result["returnUrl"] = str(self.return_url)
        elif include_empty:
            result["returnUrl"] = str()
        if hasattr(self, "live_endpoint_url_prefix") and self.live_endpoint_url_prefix:
            result["liveEndpointUrlPrefix"] = str(self.live_endpoint_url_prefix)
        elif include_empty:
            result["liveEndpointUrlPrefix"] = str()
        if hasattr(self, "authorise_as_capture") and self.authorise_as_capture:
            result["authoriseAsCapture"] = bool(self.authorise_as_capture)
        elif include_empty:
            result["authoriseAsCapture"] = bool()
        if hasattr(self, "allowed_payment_methods") and self.allowed_payment_methods:
            result["allowedPaymentMethods"] = [str(i0) for i0 in self.allowed_payment_methods]
        elif include_empty:
            result["allowedPaymentMethods"] = []
        if hasattr(self, "blocked_payment_methods") and self.blocked_payment_methods:
            result["blockedPaymentMethods"] = [str(i0) for i0 in self.blocked_payment_methods]
        elif include_empty:
            result["blockedPaymentMethods"] = []
        if hasattr(self, "settings") and self.settings:
            result["settings"] = str(self.settings)
        elif include_empty:
            result["settings"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        merchant_account: Optional[str] = None,
        notification_hmac_key: Optional[str] = None,
        notification_username: Optional[str] = None,
        notification_password: Optional[str] = None,
        return_url: Optional[str] = None,
        live_endpoint_url_prefix: Optional[str] = None,
        authorise_as_capture: Optional[bool] = None,
        allowed_payment_methods: Optional[List[str]] = None,
        blocked_payment_methods: Optional[List[str]] = None,
        settings: Optional[str] = None,
    ) -> AdyenConfig:
        instance = cls()
        if api_key is not None:
            instance.api_key = api_key
        if merchant_account is not None:
            instance.merchant_account = merchant_account
        if notification_hmac_key is not None:
            instance.notification_hmac_key = notification_hmac_key
        if notification_username is not None:
            instance.notification_username = notification_username
        if notification_password is not None:
            instance.notification_password = notification_password
        if return_url is not None:
            instance.return_url = return_url
        if live_endpoint_url_prefix is not None:
            instance.live_endpoint_url_prefix = live_endpoint_url_prefix
        if authorise_as_capture is not None:
            instance.authorise_as_capture = authorise_as_capture
        if allowed_payment_methods is not None:
            instance.allowed_payment_methods = allowed_payment_methods
        if blocked_payment_methods is not None:
            instance.blocked_payment_methods = blocked_payment_methods
        if settings is not None:
            instance.settings = settings
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> AdyenConfig:
        instance = cls()
        if not dict_:
            return instance
        if "apiKey" in dict_ and dict_["apiKey"] is not None:
            instance.api_key = str(dict_["apiKey"])
        elif include_empty:
            instance.api_key = str()
        if "merchantAccount" in dict_ and dict_["merchantAccount"] is not None:
            instance.merchant_account = str(dict_["merchantAccount"])
        elif include_empty:
            instance.merchant_account = str()
        if "notificationHmacKey" in dict_ and dict_["notificationHmacKey"] is not None:
            instance.notification_hmac_key = str(dict_["notificationHmacKey"])
        elif include_empty:
            instance.notification_hmac_key = str()
        if "notificationUsername" in dict_ and dict_["notificationUsername"] is not None:
            instance.notification_username = str(dict_["notificationUsername"])
        elif include_empty:
            instance.notification_username = str()
        if "notificationPassword" in dict_ and dict_["notificationPassword"] is not None:
            instance.notification_password = str(dict_["notificationPassword"])
        elif include_empty:
            instance.notification_password = str()
        if "returnUrl" in dict_ and dict_["returnUrl"] is not None:
            instance.return_url = str(dict_["returnUrl"])
        elif include_empty:
            instance.return_url = str()
        if "liveEndpointUrlPrefix" in dict_ and dict_["liveEndpointUrlPrefix"] is not None:
            instance.live_endpoint_url_prefix = str(dict_["liveEndpointUrlPrefix"])
        elif include_empty:
            instance.live_endpoint_url_prefix = str()
        if "authoriseAsCapture" in dict_ and dict_["authoriseAsCapture"] is not None:
            instance.authorise_as_capture = bool(dict_["authoriseAsCapture"])
        elif include_empty:
            instance.authorise_as_capture = bool()
        if "allowedPaymentMethods" in dict_ and dict_["allowedPaymentMethods"] is not None:
            instance.allowed_payment_methods = [str(i0) for i0 in dict_["allowedPaymentMethods"]]
        elif include_empty:
            instance.allowed_payment_methods = []
        if "blockedPaymentMethods" in dict_ and dict_["blockedPaymentMethods"] is not None:
            instance.blocked_payment_methods = [str(i0) for i0 in dict_["blockedPaymentMethods"]]
        elif include_empty:
            instance.blocked_payment_methods = []
        if "settings" in dict_ and dict_["settings"] is not None:
            instance.settings = str(dict_["settings"])
        elif include_empty:
            instance.settings = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "apiKey": "api_key",
            "merchantAccount": "merchant_account",
            "notificationHmacKey": "notification_hmac_key",
            "notificationUsername": "notification_username",
            "notificationPassword": "notification_password",
            "returnUrl": "return_url",
            "liveEndpointUrlPrefix": "live_endpoint_url_prefix",
            "authoriseAsCapture": "authorise_as_capture",
            "allowedPaymentMethods": "allowed_payment_methods",
            "blockedPaymentMethods": "blocked_payment_methods",
            "settings": "settings",
        }

    # endregion static methods
