# Auto-generated at 2021-09-27T17:01:29.802388+08:00
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

from .....core import Operation
from .....core import HttpResponse

from ...models import ErrorEntity
from ...models import RewardInfo


class DeleteReward(Operation):
    """Delete a reward (deleteReward)

    Properties:
        url: /platform/admin/namespaces/{namespace}/rewards/{rewardId}

        method: DELETE

        tags: Reward

        consumes: []

        produces: ["application/json"]

        security: bearer

        namespace: (namespace) REQUIRED str in path

        reward_id: (rewardId) REQUIRED str in path

    Responses:
        200: OK - RewardInfo (successful operation)

        404: Not Found - ErrorEntity (ErrorCode: 34041 | ErrorMessage: Reward [{rewardId}] does not exist in namespace [{namespace}])
    """

    # region fields

    _url: str = "/platform/admin/namespaces/{namespace}/rewards/{rewardId}"
    _method: str = "DELETE"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    namespace: str                                                                                 # REQUIRED in [path]
    reward_id: str                                                                                 # REQUIRED in [path]

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

        return result

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
            "namespace",
            "reward_id",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "path": self.get_path_params(),
        }

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        if hasattr(self, "reward_id"):
            result["rewardId"] = self.reward_id
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "reward_id") or self.reward_id is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_namespace(self, value: str) -> DeleteReward:
        self.namespace = value
        return self

    def with_reward_id(self, value: str) -> DeleteReward:
        self.reward_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "reward_id") and self.reward_id:
            result["rewardId"] = str(self.reward_id)
        elif include_empty:
            result["rewardId"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, RewardInfo], Union[None, ErrorEntity]]:
        """Parse the given response.

        200: OK - RewardInfo (successful operation)

        404: Not Found - ErrorEntity (ErrorCode: 34041 | ErrorMessage: Reward [{rewardId}] does not exist in namespace [{namespace}])
        """
        if code == 200:
            return RewardInfo.create_from_dict(content), None
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
        reward_id: str,
    ) -> DeleteReward:
        instance = cls()
        instance.namespace = namespace
        instance.reward_id = reward_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> DeleteReward:
        instance = cls()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "rewardId" in dict_ and dict_["rewardId"] is not None:
            instance.reward_id = str(dict_["rewardId"])
        elif include_empty:
            instance.reward_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "rewardId": "reward_id",
        }

    # endregion static methods
