# Auto-generated at 2021-09-27T17:01:27.382474+08:00
# from: Justice Social Service (1.17.1)

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

from ...models import ErrorEntity


class DeleteUserStatItems2(Operation):
    """Delete User's statItems (deleteUserStatItems_2)

    Properties:
        url: /social/v2/admin/namespaces/{namespace}/users/{userId}/stats/{statCode}/statitems

        method: DELETE

        tags: UserStatistic

        consumes: []

        produces: ["application/json"]

        security: bearer

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

        stat_code: (statCode) REQUIRED str in path

        additional_key: (additionalKey) OPTIONAL str in query

    Responses:
        204: No Content - (delete successfully)

        401: Unauthorized - ErrorEntity (ErrorCode: 20001 | ErrorMessage: unauthorized access)

        403: Forbidden - ErrorEntity (ErrorCode: 20013 | ErrorMessage: insufficient permission)

        404: Not Found - ErrorEntity (ErrorCode: 12242 | ErrorMessage: Stat item of [{statCode}] of user [{profileId}] cannot be found in namespace [{namespace}])
    """

    # region fields

    _url: str = "/social/v2/admin/namespaces/{namespace}/users/{userId}/stats/{statCode}/statitems"
    _method: str = "DELETE"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    namespace: str                                                                                 # REQUIRED in [path]
    user_id: str                                                                                   # REQUIRED in [path]
    stat_code: str                                                                                 # REQUIRED in [path]
    additional_key: str                                                                            # OPTIONAL in [query]

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
            "namespace",
            "user_id",
            "stat_code",
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
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        if hasattr(self, "user_id"):
            result["userId"] = self.user_id
        if hasattr(self, "stat_code"):
            result["statCode"] = self.stat_code
        return result

    def get_query_params(self) -> dict:
        result = {}
        if hasattr(self, "additional_key"):
            result["additionalKey"] = self.additional_key
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "user_id") or self.user_id is None:
            return False
        if not hasattr(self, "stat_code") or self.stat_code is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_namespace(self, value: str) -> DeleteUserStatItems2:
        self.namespace = value
        return self

    def with_user_id(self, value: str) -> DeleteUserStatItems2:
        self.user_id = value
        return self

    def with_stat_code(self, value: str) -> DeleteUserStatItems2:
        self.stat_code = value
        return self

    def with_additional_key(self, value: str) -> DeleteUserStatItems2:
        self.additional_key = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        if hasattr(self, "stat_code") and self.stat_code:
            result["statCode"] = str(self.stat_code)
        elif include_empty:
            result["statCode"] = str()
        if hasattr(self, "additional_key") and self.additional_key:
            result["additionalKey"] = str(self.additional_key)
        elif include_empty:
            result["additionalKey"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, HttpResponse], Union[None, ErrorEntity]]:
        """Parse the given response.

        204: No Content - (delete successfully)

        401: Unauthorized - ErrorEntity (ErrorCode: 20001 | ErrorMessage: unauthorized access)

        403: Forbidden - ErrorEntity (ErrorCode: 20013 | ErrorMessage: insufficient permission)

        404: Not Found - ErrorEntity (ErrorCode: 12242 | ErrorMessage: Stat item of [{statCode}] of user [{profileId}] cannot be found in namespace [{namespace}])
        """
        if code == 204:
            return HttpResponse.create(code, "No Content"), None
        if code == 401:
            return None, ErrorEntity.create_from_dict(content)
        if code == 403:
            return None, ErrorEntity.create_from_dict(content)
        if code == 404:
            return None, ErrorEntity.create_from_dict(content)
        was_handled, undocumented_response = HttpResponse.try_create_undocumented_response(code, content)
        if was_handled:
            return None, undocumented_response
        return None, HttpResponse.create_unhandled_error()

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        namespace: str,
        user_id: str,
        stat_code: str,
        additional_key: Optional[str] = None,
    ) -> DeleteUserStatItems2:
        instance = cls()
        instance.namespace = namespace
        instance.user_id = user_id
        instance.stat_code = stat_code
        if additional_key is not None:
            instance.additional_key = additional_key
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> DeleteUserStatItems2:
        instance = cls()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        if "statCode" in dict_ and dict_["statCode"] is not None:
            instance.stat_code = str(dict_["statCode"])
        elif include_empty:
            instance.stat_code = str()
        if "additionalKey" in dict_ and dict_["additionalKey"] is not None:
            instance.additional_key = str(dict_["additionalKey"])
        elif include_empty:
            instance.additional_key = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "userId": "user_id",
            "statCode": "stat_code",
            "additionalKey": "additional_key",
        }

    # endregion static methods
