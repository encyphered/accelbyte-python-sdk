# Auto-generated at 2021-09-27T17:01:25.571929+08:00
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

from ...models import ModelRoleNamesResponseV3
from ...models import RestErrorResponse


class PublicGetRolesV3(Operation):
    """Get Roles (PublicGetRolesV3)

    Properties:
        url: /iam/v3/public/roles

        method: GET

        tags: Roles

        consumes: ["application/json"]

        produces: ["application/json"]

        security: bearer

        limit: (limit) OPTIONAL int in query

        after: (after) OPTIONAL str in query

        before: (before) OPTIONAL str in query

        is_wildcard: (isWildcard) OPTIONAL bool in query

    Responses:
        200: OK - ModelRoleNamesResponseV3 (OK)

        400: Bad Request - RestErrorResponse (errorCode: 20002 | errorMessage: validation error)
    """

    # region fields

    _url: str = "/iam/v3/public/roles"
    _method: str = "GET"
    _consumes: List[str] = ["application/json"]
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    limit: int                                                                                     # OPTIONAL in [query]
    after: str                                                                                     # OPTIONAL in [query]
    before: str                                                                                    # OPTIONAL in [query]
    is_wildcard: bool                                                                              # OPTIONAL in [query]

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

        # query params
        result += "?" + "&".join([f"{k}={v}" for k, v in self.get_query_params().items()])

        return result

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "query": self.get_query_params(),
        }

    def get_query_params(self) -> dict:
        result = {}
        if hasattr(self, "limit"):
            result["limit"] = self.limit
        if hasattr(self, "after"):
            result["after"] = self.after
        if hasattr(self, "before"):
            result["before"] = self.before
        if hasattr(self, "is_wildcard"):
            result["isWildcard"] = self.is_wildcard
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        return True

    # endregion is/has methods

    # region with_x methods

    def with_limit(self, value: int) -> PublicGetRolesV3:
        self.limit = value
        return self

    def with_after(self, value: str) -> PublicGetRolesV3:
        self.after = value
        return self

    def with_before(self, value: str) -> PublicGetRolesV3:
        self.before = value
        return self

    def with_is_wildcard(self, value: bool) -> PublicGetRolesV3:
        self.is_wildcard = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "limit") and self.limit:
            result["limit"] = int(self.limit)
        elif include_empty:
            result["limit"] = int()
        if hasattr(self, "after") and self.after:
            result["after"] = str(self.after)
        elif include_empty:
            result["after"] = str()
        if hasattr(self, "before") and self.before:
            result["before"] = str(self.before)
        elif include_empty:
            result["before"] = str()
        if hasattr(self, "is_wildcard") and self.is_wildcard:
            result["isWildcard"] = bool(self.is_wildcard)
        elif include_empty:
            result["isWildcard"] = bool()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, ModelRoleNamesResponseV3], Union[None, RestErrorResponse]]:
        """Parse the given response.

        200: OK - ModelRoleNamesResponseV3 (OK)

        400: Bad Request - RestErrorResponse (errorCode: 20002 | errorMessage: validation error)
        """
        if code == 200:
            return ModelRoleNamesResponseV3.create_from_dict(content), None
        if code == 400:
            return None, RestErrorResponse.create_from_dict(content)
        was_handled, undocumented_response = HttpResponse.try_create_undocumented_response(code, content)
        if was_handled:
            return None, undocumented_response
        return None, HttpResponse.create_unhandled_error()

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        limit: Optional[int] = None,
        after: Optional[str] = None,
        before: Optional[str] = None,
        is_wildcard: Optional[bool] = None,
    ) -> PublicGetRolesV3:
        instance = cls()
        if limit is not None:
            instance.limit = limit
        if after is not None:
            instance.after = after
        if before is not None:
            instance.before = before
        if is_wildcard is not None:
            instance.is_wildcard = is_wildcard
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> PublicGetRolesV3:
        instance = cls()
        if "limit" in dict_ and dict_["limit"] is not None:
            instance.limit = int(dict_["limit"])
        elif include_empty:
            instance.limit = int()
        if "after" in dict_ and dict_["after"] is not None:
            instance.after = str(dict_["after"])
        elif include_empty:
            instance.after = str()
        if "before" in dict_ and dict_["before"] is not None:
            instance.before = str(dict_["before"])
        elif include_empty:
            instance.before = str()
        if "isWildcard" in dict_ and dict_["isWildcard"] is not None:
            instance.is_wildcard = bool(dict_["isWildcard"])
        elif include_empty:
            instance.is_wildcard = bool()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "limit": "limit",
            "after": "after",
            "before": "before",
            "isWildcard": "is_wildcard",
        }

    # endregion static methods
