# Auto-generated at 2021-09-27T17:12:33.452133+08:00
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

from ..models.model_notification_topic_response import ModelNotificationTopicResponse


class ModelTopicByNamespacesResponse(Model):
    """Model topic by namespaces response

    Properties:
        first: (first) REQUIRED str

        last: (last) REQUIRED str

        next_: (next) REQUIRED str

        previous: (previous) REQUIRED str

        topics: (topics) REQUIRED List[ModelNotificationTopicResponse]
    """

    # region fields

    first: str                                                                                     # REQUIRED
    last: str                                                                                      # REQUIRED
    next_: str                                                                                     # REQUIRED
    previous: str                                                                                  # REQUIRED
    topics: List[ModelNotificationTopicResponse]                                                   # REQUIRED

    # endregion fields

    # region with_x methods

    def with_first(self, value: str) -> ModelTopicByNamespacesResponse:
        self.first = value
        return self

    def with_last(self, value: str) -> ModelTopicByNamespacesResponse:
        self.last = value
        return self

    def with_next(self, value: str) -> ModelTopicByNamespacesResponse:
        self.next_ = value
        return self

    def with_previous(self, value: str) -> ModelTopicByNamespacesResponse:
        self.previous = value
        return self

    def with_topics(self, value: List[ModelNotificationTopicResponse]) -> ModelTopicByNamespacesResponse:
        self.topics = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "first") and self.first:
            result["first"] = str(self.first)
        elif include_empty:
            result["first"] = str()
        if hasattr(self, "last") and self.last:
            result["last"] = str(self.last)
        elif include_empty:
            result["last"] = str()
        if hasattr(self, "next_") and self.next_:
            result["next"] = str(self.next_)
        elif include_empty:
            result["next"] = str()
        if hasattr(self, "previous") and self.previous:
            result["previous"] = str(self.previous)
        elif include_empty:
            result["previous"] = str()
        if hasattr(self, "topics") and self.topics:
            result["topics"] = [i0.to_dict(include_empty=include_empty) for i0 in self.topics]
        elif include_empty:
            result["topics"] = []
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        first: str,
        last: str,
        next_: str,
        previous: str,
        topics: List[ModelNotificationTopicResponse],
    ) -> ModelTopicByNamespacesResponse:
        instance = cls()
        instance.first = first
        instance.last = last
        instance.next_ = next_
        instance.previous = previous
        instance.topics = topics
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelTopicByNamespacesResponse:
        instance = cls()
        if not dict_:
            return instance
        if "first" in dict_ and dict_["first"] is not None:
            instance.first = str(dict_["first"])
        elif include_empty:
            instance.first = str()
        if "last" in dict_ and dict_["last"] is not None:
            instance.last = str(dict_["last"])
        elif include_empty:
            instance.last = str()
        if "next" in dict_ and dict_["next"] is not None:
            instance.next_ = str(dict_["next"])
        elif include_empty:
            instance.next_ = str()
        if "previous" in dict_ and dict_["previous"] is not None:
            instance.previous = str(dict_["previous"])
        elif include_empty:
            instance.previous = str()
        if "topics" in dict_ and dict_["topics"] is not None:
            instance.topics = [ModelNotificationTopicResponse.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["topics"]]
        elif include_empty:
            instance.topics = []
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "first": "first",
            "last": "last",
            "next": "next_",
            "previous": "previous",
            "topics": "topics",
        }

    # endregion static methods
