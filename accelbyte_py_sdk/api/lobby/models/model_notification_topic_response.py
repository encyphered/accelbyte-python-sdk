# Auto-generated at 2021-09-27T17:12:33.437781+08:00
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


class ModelNotificationTopicResponse(Model):
    """Model notification topic response

    Properties:
        created_at: (createdAt) REQUIRED int

        description: (description) REQUIRED str

        namespace: (namespace) REQUIRED str

        topic: (topic) REQUIRED str
    """

    # region fields

    created_at: int                                                                                # REQUIRED
    description: str                                                                               # REQUIRED
    namespace: str                                                                                 # REQUIRED
    topic: str                                                                                     # REQUIRED

    # endregion fields

    # region with_x methods

    def with_created_at(self, value: int) -> ModelNotificationTopicResponse:
        self.created_at = value
        return self

    def with_description(self, value: str) -> ModelNotificationTopicResponse:
        self.description = value
        return self

    def with_namespace(self, value: str) -> ModelNotificationTopicResponse:
        self.namespace = value
        return self

    def with_topic(self, value: str) -> ModelNotificationTopicResponse:
        self.topic = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "created_at") and self.created_at:
            result["createdAt"] = int(self.created_at)
        elif include_empty:
            result["createdAt"] = int()
        if hasattr(self, "description") and self.description:
            result["description"] = str(self.description)
        elif include_empty:
            result["description"] = str()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "topic") and self.topic:
            result["topic"] = str(self.topic)
        elif include_empty:
            result["topic"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        created_at: int,
        description: str,
        namespace: str,
        topic: str,
    ) -> ModelNotificationTopicResponse:
        instance = cls()
        instance.created_at = created_at
        instance.description = description
        instance.namespace = namespace
        instance.topic = topic
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelNotificationTopicResponse:
        instance = cls()
        if not dict_:
            return instance
        if "createdAt" in dict_ and dict_["createdAt"] is not None:
            instance.created_at = int(dict_["createdAt"])
        elif include_empty:
            instance.created_at = int()
        if "description" in dict_ and dict_["description"] is not None:
            instance.description = str(dict_["description"])
        elif include_empty:
            instance.description = str()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "topic" in dict_ and dict_["topic"] is not None:
            instance.topic = str(dict_["topic"])
        elif include_empty:
            instance.topic = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "createdAt": "created_at",
            "description": "description",
            "namespace": "namespace",
            "topic": "topic",
        }

    # endregion static methods
