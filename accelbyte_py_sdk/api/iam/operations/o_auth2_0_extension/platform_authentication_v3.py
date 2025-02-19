# Auto-generated at 2021-09-27T17:01:25.403196+08:00
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

from .....core import Operation
from .....core import HttpResponse


class PlatformAuthenticationV3(Operation):
    """Platform Authentication API (PlatformAuthenticationV3)

    Properties:
        url: /iam/v3/platforms/{platformId}/authenticate

        method: GET

        tags: OAuth2.0 - Extension

        consumes: ["application/x-www-form-urlencoded"]

        produces: ["application/json"]

        security: bearer

        location query: PLACEHOLDER

        platform_id: (platformId) REQUIRED str in path

        state: (state) REQUIRED str in query

        openid_ns: (openid.ns) OPTIONAL str in query

        openid_mode: (openid.mode) OPTIONAL str in query

        openid_op_endpoint: (openid.op_endpoint) OPTIONAL str in query

        openid_claimed_id: (openid.claimed_id) OPTIONAL str in query

        openid_identity: (openid.identity) OPTIONAL str in query

        openid_return_to: (openid.return_to) OPTIONAL str in query

        openid_response_nonce: (openid.response_nonce) OPTIONAL str in query

        openid_assoc_handle: (openid.assoc_handle) OPTIONAL str in query

        openid_signed: (openid.signed) OPTIONAL str in query

        openid_sig: (openid.sig) OPTIONAL str in query

        code: (code) OPTIONAL str in query

        error: (error) OPTIONAL str in query

    Responses:
        302: Found - (Found. Redirect to clients redirection URL with either code or error on the query parameter)
    """

    # region fields

    _url: str = "/iam/v3/platforms/{platformId}/authenticate"
    _method: str = "GET"
    _consumes: List[str] = ["application/x-www-form-urlencoded"]
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = "PLACEHOLDER"

    platform_id: str                                                                               # REQUIRED in [path]
    state: str                                                                                     # REQUIRED in [query]
    openid_ns: str                                                                                 # OPTIONAL in [query]
    openid_mode: str                                                                               # OPTIONAL in [query]
    openid_op_endpoint: str                                                                        # OPTIONAL in [query]
    openid_claimed_id: str                                                                         # OPTIONAL in [query]
    openid_identity: str                                                                           # OPTIONAL in [query]
    openid_return_to: str                                                                          # OPTIONAL in [query]
    openid_response_nonce: str                                                                     # OPTIONAL in [query]
    openid_assoc_handle: str                                                                       # OPTIONAL in [query]
    openid_signed: str                                                                             # OPTIONAL in [query]
    openid_sig: str                                                                                # OPTIONAL in [query]
    code: str                                                                                      # OPTIONAL in [query]
    error: str                                                                                     # OPTIONAL in [query]

    # endregion fields

    # region properties

    @property
    def url(self) -> str:
        return self._url

    @property
    def method(self) -> str:
        return self._method

    @property
    def consumes(self) -> List[str]:
        return self._consumes

    @property
    def produces(self) -> List[str]:
        return self._produces

    @property
    def security(self) -> Optional[str]:
        return self._security

    @property
    def location_query(self) -> str:
        return self._location_query

    # endregion properties

    # region get methods

    def get_full_url(self, base_url: Union[None, str] = None) -> str:
        result = base_url if base_url is not None else ""

        # path params
        url = self.url
        for k, v in self.get_path_params().items():
            url = url.replace(f"{{{k}}}", v)
        result += url

        # query params
        result += "?" + "&".join([f"{k}={v}" for k, v in self.get_query_params().items()])

        return result

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
            "platform_id",
            "state",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "path": self.get_path_params(),
            "query": self.get_query_params(),
        }

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "platform_id"):
            result["platformId"] = self.platform_id
        return result

    def get_query_params(self) -> dict:
        result = {}
        if hasattr(self, "state"):
            result["state"] = self.state
        if hasattr(self, "openid_ns"):
            result["openid.ns"] = self.openid_ns
        if hasattr(self, "openid_mode"):
            result["openid.mode"] = self.openid_mode
        if hasattr(self, "openid_op_endpoint"):
            result["openid.op_endpoint"] = self.openid_op_endpoint
        if hasattr(self, "openid_claimed_id"):
            result["openid.claimed_id"] = self.openid_claimed_id
        if hasattr(self, "openid_identity"):
            result["openid.identity"] = self.openid_identity
        if hasattr(self, "openid_return_to"):
            result["openid.return_to"] = self.openid_return_to
        if hasattr(self, "openid_response_nonce"):
            result["openid.response_nonce"] = self.openid_response_nonce
        if hasattr(self, "openid_assoc_handle"):
            result["openid.assoc_handle"] = self.openid_assoc_handle
        if hasattr(self, "openid_signed"):
            result["openid.signed"] = self.openid_signed
        if hasattr(self, "openid_sig"):
            result["openid.sig"] = self.openid_sig
        if hasattr(self, "code"):
            result["code"] = self.code
        if hasattr(self, "error"):
            result["error"] = self.error
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "platform_id") or self.platform_id is None:
            return False
        if not hasattr(self, "state") or self.state is None:
            return False
        return True

    # noinspection PyMethodMayBeStatic
    def has_redirects(self) -> bool:
        """Returns True if this operation has redirects, otherwise False.

        302: Found - (Found. Redirect to clients redirection URL with either code or error on the query parameter)
        """
        return True

    # endregion is/has methods

    # region with_x methods

    def with_platform_id(self, value: str) -> PlatformAuthenticationV3:
        self.platform_id = value
        return self

    def with_state(self, value: str) -> PlatformAuthenticationV3:
        self.state = value
        return self

    def with_openid_ns(self, value: str) -> PlatformAuthenticationV3:
        self.openid_ns = value
        return self

    def with_openid_mode(self, value: str) -> PlatformAuthenticationV3:
        self.openid_mode = value
        return self

    def with_openid_op_endpoint(self, value: str) -> PlatformAuthenticationV3:
        self.openid_op_endpoint = value
        return self

    def with_openid_claimed_id(self, value: str) -> PlatformAuthenticationV3:
        self.openid_claimed_id = value
        return self

    def with_openid_identity(self, value: str) -> PlatformAuthenticationV3:
        self.openid_identity = value
        return self

    def with_openid_return_to(self, value: str) -> PlatformAuthenticationV3:
        self.openid_return_to = value
        return self

    def with_openid_response_nonce(self, value: str) -> PlatformAuthenticationV3:
        self.openid_response_nonce = value
        return self

    def with_openid_assoc_handle(self, value: str) -> PlatformAuthenticationV3:
        self.openid_assoc_handle = value
        return self

    def with_openid_signed(self, value: str) -> PlatformAuthenticationV3:
        self.openid_signed = value
        return self

    def with_openid_sig(self, value: str) -> PlatformAuthenticationV3:
        self.openid_sig = value
        return self

    def with_code(self, value: str) -> PlatformAuthenticationV3:
        self.code = value
        return self

    def with_error(self, value: str) -> PlatformAuthenticationV3:
        self.error = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "platform_id") and self.platform_id:
            result["platformId"] = str(self.platform_id)
        elif include_empty:
            result["platformId"] = str()
        if hasattr(self, "state") and self.state:
            result["state"] = str(self.state)
        elif include_empty:
            result["state"] = str()
        if hasattr(self, "openid_ns") and self.openid_ns:
            result["openid.ns"] = str(self.openid_ns)
        elif include_empty:
            result["openid.ns"] = str()
        if hasattr(self, "openid_mode") and self.openid_mode:
            result["openid.mode"] = str(self.openid_mode)
        elif include_empty:
            result["openid.mode"] = str()
        if hasattr(self, "openid_op_endpoint") and self.openid_op_endpoint:
            result["openid.op_endpoint"] = str(self.openid_op_endpoint)
        elif include_empty:
            result["openid.op_endpoint"] = str()
        if hasattr(self, "openid_claimed_id") and self.openid_claimed_id:
            result["openid.claimed_id"] = str(self.openid_claimed_id)
        elif include_empty:
            result["openid.claimed_id"] = str()
        if hasattr(self, "openid_identity") and self.openid_identity:
            result["openid.identity"] = str(self.openid_identity)
        elif include_empty:
            result["openid.identity"] = str()
        if hasattr(self, "openid_return_to") and self.openid_return_to:
            result["openid.return_to"] = str(self.openid_return_to)
        elif include_empty:
            result["openid.return_to"] = str()
        if hasattr(self, "openid_response_nonce") and self.openid_response_nonce:
            result["openid.response_nonce"] = str(self.openid_response_nonce)
        elif include_empty:
            result["openid.response_nonce"] = str()
        if hasattr(self, "openid_assoc_handle") and self.openid_assoc_handle:
            result["openid.assoc_handle"] = str(self.openid_assoc_handle)
        elif include_empty:
            result["openid.assoc_handle"] = str()
        if hasattr(self, "openid_signed") and self.openid_signed:
            result["openid.signed"] = str(self.openid_signed)
        elif include_empty:
            result["openid.signed"] = str()
        if hasattr(self, "openid_sig") and self.openid_sig:
            result["openid.sig"] = str(self.openid_sig)
        elif include_empty:
            result["openid.sig"] = str()
        if hasattr(self, "code") and self.code:
            result["code"] = str(self.code)
        elif include_empty:
            result["code"] = str()
        if hasattr(self, "error") and self.error:
            result["error"] = str(self.error)
        elif include_empty:
            result["error"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, HttpResponse], Union[None, HttpResponse]]:
        """Parse the given response.

        302: Found - (Found. Redirect to clients redirection URL with either code or error on the query parameter)
        """
        if code == 302:
            return HttpResponse.create_redirect(code, content), None
        was_handled, undocumented_response = HttpResponse.try_create_undocumented_response(code, content)
        if was_handled:
            return None, undocumented_response
        return None, HttpResponse.create_unhandled_error()

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        platform_id: str,
        state: str,
        openid_ns: Optional[str] = None,
        openid_mode: Optional[str] = None,
        openid_op_endpoint: Optional[str] = None,
        openid_claimed_id: Optional[str] = None,
        openid_identity: Optional[str] = None,
        openid_return_to: Optional[str] = None,
        openid_response_nonce: Optional[str] = None,
        openid_assoc_handle: Optional[str] = None,
        openid_signed: Optional[str] = None,
        openid_sig: Optional[str] = None,
        code: Optional[str] = None,
        error: Optional[str] = None,
    ) -> PlatformAuthenticationV3:
        instance = cls()
        instance.platform_id = platform_id
        instance.state = state
        if openid_ns is not None:
            instance.openid_ns = openid_ns
        if openid_mode is not None:
            instance.openid_mode = openid_mode
        if openid_op_endpoint is not None:
            instance.openid_op_endpoint = openid_op_endpoint
        if openid_claimed_id is not None:
            instance.openid_claimed_id = openid_claimed_id
        if openid_identity is not None:
            instance.openid_identity = openid_identity
        if openid_return_to is not None:
            instance.openid_return_to = openid_return_to
        if openid_response_nonce is not None:
            instance.openid_response_nonce = openid_response_nonce
        if openid_assoc_handle is not None:
            instance.openid_assoc_handle = openid_assoc_handle
        if openid_signed is not None:
            instance.openid_signed = openid_signed
        if openid_sig is not None:
            instance.openid_sig = openid_sig
        if code is not None:
            instance.code = code
        if error is not None:
            instance.error = error
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> PlatformAuthenticationV3:
        instance = cls()
        if "platformId" in dict_ and dict_["platformId"] is not None:
            instance.platform_id = str(dict_["platformId"])
        elif include_empty:
            instance.platform_id = str()
        if "state" in dict_ and dict_["state"] is not None:
            instance.state = str(dict_["state"])
        elif include_empty:
            instance.state = str()
        if "openid.ns" in dict_ and dict_["openid.ns"] is not None:
            instance.openid_ns = str(dict_["openid.ns"])
        elif include_empty:
            instance.openid_ns = str()
        if "openid.mode" in dict_ and dict_["openid.mode"] is not None:
            instance.openid_mode = str(dict_["openid.mode"])
        elif include_empty:
            instance.openid_mode = str()
        if "openid.op_endpoint" in dict_ and dict_["openid.op_endpoint"] is not None:
            instance.openid_op_endpoint = str(dict_["openid.op_endpoint"])
        elif include_empty:
            instance.openid_op_endpoint = str()
        if "openid.claimed_id" in dict_ and dict_["openid.claimed_id"] is not None:
            instance.openid_claimed_id = str(dict_["openid.claimed_id"])
        elif include_empty:
            instance.openid_claimed_id = str()
        if "openid.identity" in dict_ and dict_["openid.identity"] is not None:
            instance.openid_identity = str(dict_["openid.identity"])
        elif include_empty:
            instance.openid_identity = str()
        if "openid.return_to" in dict_ and dict_["openid.return_to"] is not None:
            instance.openid_return_to = str(dict_["openid.return_to"])
        elif include_empty:
            instance.openid_return_to = str()
        if "openid.response_nonce" in dict_ and dict_["openid.response_nonce"] is not None:
            instance.openid_response_nonce = str(dict_["openid.response_nonce"])
        elif include_empty:
            instance.openid_response_nonce = str()
        if "openid.assoc_handle" in dict_ and dict_["openid.assoc_handle"] is not None:
            instance.openid_assoc_handle = str(dict_["openid.assoc_handle"])
        elif include_empty:
            instance.openid_assoc_handle = str()
        if "openid.signed" in dict_ and dict_["openid.signed"] is not None:
            instance.openid_signed = str(dict_["openid.signed"])
        elif include_empty:
            instance.openid_signed = str()
        if "openid.sig" in dict_ and dict_["openid.sig"] is not None:
            instance.openid_sig = str(dict_["openid.sig"])
        elif include_empty:
            instance.openid_sig = str()
        if "code" in dict_ and dict_["code"] is not None:
            instance.code = str(dict_["code"])
        elif include_empty:
            instance.code = str()
        if "error" in dict_ and dict_["error"] is not None:
            instance.error = str(dict_["error"])
        elif include_empty:
            instance.error = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "platformId": "platform_id",
            "state": "state",
            "openid.ns": "openid_ns",
            "openid.mode": "openid_mode",
            "openid.op_endpoint": "openid_op_endpoint",
            "openid.claimed_id": "openid_claimed_id",
            "openid.identity": "openid_identity",
            "openid.return_to": "openid_return_to",
            "openid.response_nonce": "openid_response_nonce",
            "openid.assoc_handle": "openid_assoc_handle",
            "openid.signed": "openid_signed",
            "openid.sig": "openid_sig",
            "code": "code",
            "error": "error",
        }

    # endregion static methods
