# Auto-generated at 2021-09-27T17:12:38.378481+08:00
# from: Justice AmalgamGameTelemetry Service (0.0.1)

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


class TelemetryBody(Model):
    """Telemetry body

    Properties:
        event_id: (EventId) OPTIONAL str

        event_name: (EventName) REQUIRED str

        event_namespace: (EventNamespace) REQUIRED str

        event_timestamp: (EventTimestamp) OPTIONAL str

        payload: (Payload) REQUIRED Dict[str, Any]
    """

    # region fields

    event_id: str                                                                                  # OPTIONAL
    event_name: str                                                                                # REQUIRED
    event_namespace: str                                                                           # REQUIRED
    event_timestamp: str                                                                           # OPTIONAL
    payload: Dict[str, Any]                                                                        # REQUIRED

    # endregion fields

    # region with_x methods

    def with_event_id(self, value: str) -> TelemetryBody:
        self.event_id = value
        return self

    def with_event_name(self, value: str) -> TelemetryBody:
        self.event_name = value
        return self

    def with_event_namespace(self, value: str) -> TelemetryBody:
        self.event_namespace = value
        return self

    def with_event_timestamp(self, value: str) -> TelemetryBody:
        self.event_timestamp = value
        return self

    def with_payload(self, value: Dict[str, Any]) -> TelemetryBody:
        self.payload = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "event_id") and self.event_id:
            result["EventId"] = str(self.event_id)
        elif include_empty:
            result["EventId"] = str()
        if hasattr(self, "event_name") and self.event_name:
            result["EventName"] = str(self.event_name)
        elif include_empty:
            result["EventName"] = str()
        if hasattr(self, "event_namespace") and self.event_namespace:
            result["EventNamespace"] = str(self.event_namespace)
        elif include_empty:
            result["EventNamespace"] = str()
        if hasattr(self, "event_timestamp") and self.event_timestamp:
            result["EventTimestamp"] = str(self.event_timestamp)
        elif include_empty:
            result["EventTimestamp"] = str()
        if hasattr(self, "payload") and self.payload:
            result["Payload"] = {str(k0): v0 for k0, v0 in self.payload.items()}
        elif include_empty:
            result["Payload"] = {}
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        event_name: str,
        event_namespace: str,
        payload: Dict[str, Any],
        event_id: Optional[str] = None,
        event_timestamp: Optional[str] = None,
    ) -> TelemetryBody:
        instance = cls()
        instance.event_name = event_name
        instance.event_namespace = event_namespace
        instance.payload = payload
        if event_id is not None:
            instance.event_id = event_id
        if event_timestamp is not None:
            instance.event_timestamp = event_timestamp
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> TelemetryBody:
        instance = cls()
        if not dict_:
            return instance
        if "EventId" in dict_ and dict_["EventId"] is not None:
            instance.event_id = str(dict_["EventId"])
        elif include_empty:
            instance.event_id = str()
        if "EventName" in dict_ and dict_["EventName"] is not None:
            instance.event_name = str(dict_["EventName"])
        elif include_empty:
            instance.event_name = str()
        if "EventNamespace" in dict_ and dict_["EventNamespace"] is not None:
            instance.event_namespace = str(dict_["EventNamespace"])
        elif include_empty:
            instance.event_namespace = str()
        if "EventTimestamp" in dict_ and dict_["EventTimestamp"] is not None:
            instance.event_timestamp = str(dict_["EventTimestamp"])
        elif include_empty:
            instance.event_timestamp = str()
        if "Payload" in dict_ and dict_["Payload"] is not None:
            instance.payload = {str(k0): v0 for k0, v0 in dict_["Payload"].items()}
        elif include_empty:
            instance.payload = {}
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "EventId": "event_id",
            "EventName": "event_name",
            "EventNamespace": "event_namespace",
            "EventTimestamp": "event_timestamp",
            "Payload": "payload",
        }

    # endregion static methods
