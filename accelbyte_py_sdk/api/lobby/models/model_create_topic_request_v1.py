# Auto-generated at 2021-09-27T17:12:33.421154+08:00
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


class ModelCreateTopicRequestV1(Model):
    """Model create topic request V1

    Properties:
        description: (description) REQUIRED str

        topic_name: (topicName) REQUIRED str
    """

    # region fields

    description: str                                                                               # REQUIRED
    topic_name: str                                                                                # REQUIRED

    # endregion fields

    # region with_x methods

    def with_description(self, value: str) -> ModelCreateTopicRequestV1:
        self.description = value
        return self

    def with_topic_name(self, value: str) -> ModelCreateTopicRequestV1:
        self.topic_name = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "description") and self.description:
            result["description"] = str(self.description)
        elif include_empty:
            result["description"] = str()
        if hasattr(self, "topic_name") and self.topic_name:
            result["topicName"] = str(self.topic_name)
        elif include_empty:
            result["topicName"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        description: str,
        topic_name: str,
    ) -> ModelCreateTopicRequestV1:
        instance = cls()
        instance.description = description
        instance.topic_name = topic_name
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelCreateTopicRequestV1:
        instance = cls()
        if not dict_:
            return instance
        if "description" in dict_ and dict_["description"] is not None:
            instance.description = str(dict_["description"])
        elif include_empty:
            instance.description = str()
        if "topicName" in dict_ and dict_["topicName"] is not None:
            instance.topic_name = str(dict_["topicName"])
        elif include_empty:
            instance.topic_name = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "description": "description",
            "topicName": "topic_name",
        }

    # endregion static methods
