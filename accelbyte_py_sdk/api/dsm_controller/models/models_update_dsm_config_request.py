# Auto-generated at 2021-09-27T17:12:29.790301+08:00
# from: Justice DsmController Service (2.4.0)

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


class ModelsUpdateDSMConfigRequest(Model):
    """Models update DSM config request

    Properties:
        claim_timeout: (claim_timeout) REQUIRED int

        creation_timeout: (creation_timeout) REQUIRED int

        default_version: (default_version) REQUIRED str

        port: (port) REQUIRED int

        ports: (ports) REQUIRED Dict[str, int]

        protocol: (protocol) REQUIRED str

        providers: (providers) REQUIRED List[str]

        session_timeout: (session_timeout) REQUIRED int

        unreachable_timeout: (unreachable_timeout) REQUIRED int
    """

    # region fields

    claim_timeout: int                                                                             # REQUIRED
    creation_timeout: int                                                                          # REQUIRED
    default_version: str                                                                           # REQUIRED
    port: int                                                                                      # REQUIRED
    ports: Dict[str, int]                                                                          # REQUIRED
    protocol: str                                                                                  # REQUIRED
    providers: List[str]                                                                           # REQUIRED
    session_timeout: int                                                                           # REQUIRED
    unreachable_timeout: int                                                                       # REQUIRED

    # endregion fields

    # region with_x methods

    def with_claim_timeout(self, value: int) -> ModelsUpdateDSMConfigRequest:
        self.claim_timeout = value
        return self

    def with_creation_timeout(self, value: int) -> ModelsUpdateDSMConfigRequest:
        self.creation_timeout = value
        return self

    def with_default_version(self, value: str) -> ModelsUpdateDSMConfigRequest:
        self.default_version = value
        return self

    def with_port(self, value: int) -> ModelsUpdateDSMConfigRequest:
        self.port = value
        return self

    def with_ports(self, value: Dict[str, int]) -> ModelsUpdateDSMConfigRequest:
        self.ports = value
        return self

    def with_protocol(self, value: str) -> ModelsUpdateDSMConfigRequest:
        self.protocol = value
        return self

    def with_providers(self, value: List[str]) -> ModelsUpdateDSMConfigRequest:
        self.providers = value
        return self

    def with_session_timeout(self, value: int) -> ModelsUpdateDSMConfigRequest:
        self.session_timeout = value
        return self

    def with_unreachable_timeout(self, value: int) -> ModelsUpdateDSMConfigRequest:
        self.unreachable_timeout = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "claim_timeout") and self.claim_timeout:
            result["claim_timeout"] = int(self.claim_timeout)
        elif include_empty:
            result["claim_timeout"] = int()
        if hasattr(self, "creation_timeout") and self.creation_timeout:
            result["creation_timeout"] = int(self.creation_timeout)
        elif include_empty:
            result["creation_timeout"] = int()
        if hasattr(self, "default_version") and self.default_version:
            result["default_version"] = str(self.default_version)
        elif include_empty:
            result["default_version"] = str()
        if hasattr(self, "port") and self.port:
            result["port"] = int(self.port)
        elif include_empty:
            result["port"] = int()
        if hasattr(self, "ports") and self.ports:
            result["ports"] = {str(k0): int(v0) for k0, v0 in self.ports.items()}
        elif include_empty:
            result["ports"] = {}
        if hasattr(self, "protocol") and self.protocol:
            result["protocol"] = str(self.protocol)
        elif include_empty:
            result["protocol"] = str()
        if hasattr(self, "providers") and self.providers:
            result["providers"] = [str(i0) for i0 in self.providers]
        elif include_empty:
            result["providers"] = []
        if hasattr(self, "session_timeout") and self.session_timeout:
            result["session_timeout"] = int(self.session_timeout)
        elif include_empty:
            result["session_timeout"] = int()
        if hasattr(self, "unreachable_timeout") and self.unreachable_timeout:
            result["unreachable_timeout"] = int(self.unreachable_timeout)
        elif include_empty:
            result["unreachable_timeout"] = int()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        claim_timeout: int,
        creation_timeout: int,
        default_version: str,
        port: int,
        ports: Dict[str, int],
        protocol: str,
        providers: List[str],
        session_timeout: int,
        unreachable_timeout: int,
    ) -> ModelsUpdateDSMConfigRequest:
        instance = cls()
        instance.claim_timeout = claim_timeout
        instance.creation_timeout = creation_timeout
        instance.default_version = default_version
        instance.port = port
        instance.ports = ports
        instance.protocol = protocol
        instance.providers = providers
        instance.session_timeout = session_timeout
        instance.unreachable_timeout = unreachable_timeout
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsUpdateDSMConfigRequest:
        instance = cls()
        if not dict_:
            return instance
        if "claim_timeout" in dict_ and dict_["claim_timeout"] is not None:
            instance.claim_timeout = int(dict_["claim_timeout"])
        elif include_empty:
            instance.claim_timeout = int()
        if "creation_timeout" in dict_ and dict_["creation_timeout"] is not None:
            instance.creation_timeout = int(dict_["creation_timeout"])
        elif include_empty:
            instance.creation_timeout = int()
        if "default_version" in dict_ and dict_["default_version"] is not None:
            instance.default_version = str(dict_["default_version"])
        elif include_empty:
            instance.default_version = str()
        if "port" in dict_ and dict_["port"] is not None:
            instance.port = int(dict_["port"])
        elif include_empty:
            instance.port = int()
        if "ports" in dict_ and dict_["ports"] is not None:
            instance.ports = {str(k0): int(v0) for k0, v0 in dict_["ports"].items()}
        elif include_empty:
            instance.ports = {}
        if "protocol" in dict_ and dict_["protocol"] is not None:
            instance.protocol = str(dict_["protocol"])
        elif include_empty:
            instance.protocol = str()
        if "providers" in dict_ and dict_["providers"] is not None:
            instance.providers = [str(i0) for i0 in dict_["providers"]]
        elif include_empty:
            instance.providers = []
        if "session_timeout" in dict_ and dict_["session_timeout"] is not None:
            instance.session_timeout = int(dict_["session_timeout"])
        elif include_empty:
            instance.session_timeout = int()
        if "unreachable_timeout" in dict_ and dict_["unreachable_timeout"] is not None:
            instance.unreachable_timeout = int(dict_["unreachable_timeout"])
        elif include_empty:
            instance.unreachable_timeout = int()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "claim_timeout": "claim_timeout",
            "creation_timeout": "creation_timeout",
            "default_version": "default_version",
            "port": "port",
            "ports": "ports",
            "protocol": "protocol",
            "providers": "providers",
            "session_timeout": "session_timeout",
            "unreachable_timeout": "unreachable_timeout",
        }

    # endregion static methods
