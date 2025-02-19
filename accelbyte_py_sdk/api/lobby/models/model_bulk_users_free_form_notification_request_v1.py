# Auto-generated at 2021-09-27T17:12:33.415989+08:00
# from: Justice Lobby Service (1.33.0)

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


class ModelBulkUsersFreeFormNotificationRequestV1(Model):
    """Model bulk users free form notification request V1

    Properties:
        message: (message) REQUIRED str

        topic_name: (topicName) REQUIRED str

        user_ids: (userIds) REQUIRED List[str]
    """

    # region fields

    message: str                                                                                   # REQUIRED
    topic_name: str                                                                                # REQUIRED
    user_ids: List[str]                                                                            # REQUIRED

    # endregion fields

    # region with_x methods

    def with_message(self, value: str) -> ModelBulkUsersFreeFormNotificationRequestV1:
        self.message = value
        return self

    def with_topic_name(self, value: str) -> ModelBulkUsersFreeFormNotificationRequestV1:
        self.topic_name = value
        return self

    def with_user_ids(self, value: List[str]) -> ModelBulkUsersFreeFormNotificationRequestV1:
        self.user_ids = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "message") and self.message:
            result["message"] = str(self.message)
        elif include_empty:
            result["message"] = str()
        if hasattr(self, "topic_name") and self.topic_name:
            result["topicName"] = str(self.topic_name)
        elif include_empty:
            result["topicName"] = str()
        if hasattr(self, "user_ids") and self.user_ids:
            result["userIds"] = [str(i0) for i0 in self.user_ids]
        elif include_empty:
            result["userIds"] = []
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        message: str,
        topic_name: str,
        user_ids: List[str],
    ) -> ModelBulkUsersFreeFormNotificationRequestV1:
        instance = cls()
        instance.message = message
        instance.topic_name = topic_name
        instance.user_ids = user_ids
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelBulkUsersFreeFormNotificationRequestV1:
        instance = cls()
        if not dict_:
            return instance
        if "message" in dict_ and dict_["message"] is not None:
            instance.message = str(dict_["message"])
        elif include_empty:
            instance.message = str()
        if "topicName" in dict_ and dict_["topicName"] is not None:
            instance.topic_name = str(dict_["topicName"])
        elif include_empty:
            instance.topic_name = str()
        if "userIds" in dict_ and dict_["userIds"] is not None:
            instance.user_ids = [str(i0) for i0 in dict_["userIds"]]
        elif include_empty:
            instance.user_ids = []
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "message": "message",
            "topicName": "topic_name",
            "userIds": "user_ids",
        }

    # endregion static methods
