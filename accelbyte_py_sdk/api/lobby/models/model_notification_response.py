# Auto-generated at 2021-09-27T17:12:33.435312+08:00
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


class ModelNotificationResponse(Model):
    """Model notification response

    Properties:
        from_: (from) REQUIRED str

        id_: (id) REQUIRED str

        payload: (payload) REQUIRED str

        sent_at: (sentAt) REQUIRED int

        to: (to) REQUIRED str

        topic: (topic) REQUIRED str
    """

    # region fields

    from_: str                                                                                     # REQUIRED
    id_: str                                                                                       # REQUIRED
    payload: str                                                                                   # REQUIRED
    sent_at: int                                                                                   # REQUIRED
    to: str                                                                                        # REQUIRED
    topic: str                                                                                     # REQUIRED

    # endregion fields

    # region with_x methods

    def with_from(self, value: str) -> ModelNotificationResponse:
        self.from_ = value
        return self

    def with_id(self, value: str) -> ModelNotificationResponse:
        self.id_ = value
        return self

    def with_payload(self, value: str) -> ModelNotificationResponse:
        self.payload = value
        return self

    def with_sent_at(self, value: int) -> ModelNotificationResponse:
        self.sent_at = value
        return self

    def with_to(self, value: str) -> ModelNotificationResponse:
        self.to = value
        return self

    def with_topic(self, value: str) -> ModelNotificationResponse:
        self.topic = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "from_") and self.from_:
            result["from"] = str(self.from_)
        elif include_empty:
            result["from"] = str()
        if hasattr(self, "id_") and self.id_:
            result["id"] = str(self.id_)
        elif include_empty:
            result["id"] = str()
        if hasattr(self, "payload") and self.payload:
            result["payload"] = str(self.payload)
        elif include_empty:
            result["payload"] = str()
        if hasattr(self, "sent_at") and self.sent_at:
            result["sentAt"] = int(self.sent_at)
        elif include_empty:
            result["sentAt"] = int()
        if hasattr(self, "to") and self.to:
            result["to"] = str(self.to)
        elif include_empty:
            result["to"] = str()
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
        from_: str,
        id_: str,
        payload: str,
        sent_at: int,
        to: str,
        topic: str,
    ) -> ModelNotificationResponse:
        instance = cls()
        instance.from_ = from_
        instance.id_ = id_
        instance.payload = payload
        instance.sent_at = sent_at
        instance.to = to
        instance.topic = topic
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelNotificationResponse:
        instance = cls()
        if not dict_:
            return instance
        if "from" in dict_ and dict_["from"] is not None:
            instance.from_ = str(dict_["from"])
        elif include_empty:
            instance.from_ = str()
        if "id" in dict_ and dict_["id"] is not None:
            instance.id_ = str(dict_["id"])
        elif include_empty:
            instance.id_ = str()
        if "payload" in dict_ and dict_["payload"] is not None:
            instance.payload = str(dict_["payload"])
        elif include_empty:
            instance.payload = str()
        if "sentAt" in dict_ and dict_["sentAt"] is not None:
            instance.sent_at = int(dict_["sentAt"])
        elif include_empty:
            instance.sent_at = int()
        if "to" in dict_ and dict_["to"] is not None:
            instance.to = str(dict_["to"])
        elif include_empty:
            instance.to = str()
        if "topic" in dict_ and dict_["topic"] is not None:
            instance.topic = str(dict_["topic"])
        elif include_empty:
            instance.topic = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "from": "from_",
            "id": "id_",
            "payload": "payload",
            "sentAt": "sent_at",
            "to": "to",
            "topic": "topic",
        }

    # endregion static methods
