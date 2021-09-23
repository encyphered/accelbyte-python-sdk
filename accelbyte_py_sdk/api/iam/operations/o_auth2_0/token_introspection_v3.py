# Auto-generated at 2021-09-21T14:10:35.389278+08:00
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

from ...models import OauthmodelErrorResponse
from ...models import OauthmodelTokenIntrospectResponse


class TokenIntrospectionV3(Operation):
    """OAuth2 token introspection API (TokenIntrospectionV3)

    Properties:
        url: /iam/v3/oauth/introspect

        method: POST

        tags: OAuth2.0

        consumes: ["application/x-www-form-urlencoded"]

        produces: ["application/json"]

        security: bearer

        token: (token) REQUIRED str in form_data

    Responses:
        200: OK - OauthmodelTokenIntrospectResponse (OK)

        400: Bad Request - OauthmodelErrorResponse (invalid input)

        401: Unauthorized - OauthmodelErrorResponse (invalid bearer or basic authorization header)
    """

    # region fields

    _url: str = "/iam/v3/oauth/introspect"
    _method: str = "POST"
    _consumes: List[str] = ["application/x-www-form-urlencoded"]
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    token: str                                                                                     # REQUIRED in [form_data]

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

        result += self.url

        return result

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
            "token",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "form_data": self.get_form_data_params(),
        }

    def get_form_data_params(self) -> dict:
        result = {}
        if hasattr(self, "token"):
            result["token"] = self.token
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "token") or self.token is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_token(self, value: str) -> TokenIntrospectionV3:
        self.token = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "token") and self.token:
            result["token"] = str(self.token)
        elif include_empty:
            result["token"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, OauthmodelTokenIntrospectResponse], Union[None, OauthmodelErrorResponse]]:
        """Parse the given response.

        200: OK - OauthmodelTokenIntrospectResponse (OK)

        400: Bad Request - OauthmodelErrorResponse (invalid input)

        401: Unauthorized - OauthmodelErrorResponse (invalid bearer or basic authorization header)
        """
        if code == 200:
            return OauthmodelTokenIntrospectResponse.create_from_dict(content), None
        if code == 400:
            return None, OauthmodelErrorResponse.create_from_dict(content)
        if code == 401:
            return None, OauthmodelErrorResponse.create_from_dict(content)
        return None, HttpResponse.create_unhandled_error()

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        token: str,
    ) -> TokenIntrospectionV3:
        instance = cls()
        instance.token = token
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> TokenIntrospectionV3:
        instance = cls()
        if "token" in dict_ and dict_["token"] is not None:
            instance.token = str(dict_["token"])
        elif include_empty:
            instance.token = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "token": "token",
        }

    # endregion static methods