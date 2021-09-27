# Auto-generated at 2021-09-27T17:12:37.826562+08:00
# from: Justice Group Service (2.4.0)

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


class ModelsMemberRequestResponseV1(Model):
    """Models member request response V1

    Properties:
        group_id: (groupId) REQUIRED str

        request_type: (requestType) REQUIRED str

        user_id: (userId) REQUIRED str
    """

    # region fields

    group_id: str                                                                                  # REQUIRED
    request_type: str                                                                              # REQUIRED
    user_id: str                                                                                   # REQUIRED

    # endregion fields

    # region with_x methods

    def with_group_id(self, value: str) -> ModelsMemberRequestResponseV1:
        self.group_id = value
        return self

    def with_request_type(self, value: str) -> ModelsMemberRequestResponseV1:
        self.request_type = value
        return self

    def with_user_id(self, value: str) -> ModelsMemberRequestResponseV1:
        self.user_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "group_id") and self.group_id:
            result["groupId"] = str(self.group_id)
        elif include_empty:
            result["groupId"] = str()
        if hasattr(self, "request_type") and self.request_type:
            result["requestType"] = str(self.request_type)
        elif include_empty:
            result["requestType"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        group_id: str,
        request_type: str,
        user_id: str,
    ) -> ModelsMemberRequestResponseV1:
        instance = cls()
        instance.group_id = group_id
        instance.request_type = request_type
        instance.user_id = user_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsMemberRequestResponseV1:
        instance = cls()
        if not dict_:
            return instance
        if "groupId" in dict_ and dict_["groupId"] is not None:
            instance.group_id = str(dict_["groupId"])
        elif include_empty:
            instance.group_id = str()
        if "requestType" in dict_ and dict_["requestType"] is not None:
            instance.request_type = str(dict_["requestType"])
        elif include_empty:
            instance.request_type = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "groupId": "group_id",
            "requestType": "request_type",
            "userId": "user_id",
        }

    # endregion static methods
