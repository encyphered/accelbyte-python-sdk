# Auto-generated at 2021-09-27T17:12:33.493384+08:00
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


class ModelsPartyData(Model):
    """Models party data

    Properties:
        custom_attribute: (custom_attribute) REQUIRED Dict[str, Any]

        invitees: (invitees) REQUIRED List[str]

        leader: (leader) REQUIRED str

        members: (members) REQUIRED List[str]

        namespace: (namespace) REQUIRED str

        party_id: (partyId) REQUIRED str

        updated_at: (updatedAt) REQUIRED int
    """

    # region fields

    custom_attribute: Dict[str, Any]                                                               # REQUIRED
    invitees: List[str]                                                                            # REQUIRED
    leader: str                                                                                    # REQUIRED
    members: List[str]                                                                             # REQUIRED
    namespace: str                                                                                 # REQUIRED
    party_id: str                                                                                  # REQUIRED
    updated_at: int                                                                                # REQUIRED

    # endregion fields

    # region with_x methods

    def with_custom_attribute(self, value: Dict[str, Any]) -> ModelsPartyData:
        self.custom_attribute = value
        return self

    def with_invitees(self, value: List[str]) -> ModelsPartyData:
        self.invitees = value
        return self

    def with_leader(self, value: str) -> ModelsPartyData:
        self.leader = value
        return self

    def with_members(self, value: List[str]) -> ModelsPartyData:
        self.members = value
        return self

    def with_namespace(self, value: str) -> ModelsPartyData:
        self.namespace = value
        return self

    def with_party_id(self, value: str) -> ModelsPartyData:
        self.party_id = value
        return self

    def with_updated_at(self, value: int) -> ModelsPartyData:
        self.updated_at = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "custom_attribute") and self.custom_attribute:
            result["custom_attribute"] = {str(k0): v0 for k0, v0 in self.custom_attribute.items()}
        elif include_empty:
            result["custom_attribute"] = {}
        if hasattr(self, "invitees") and self.invitees:
            result["invitees"] = [str(i0) for i0 in self.invitees]
        elif include_empty:
            result["invitees"] = []
        if hasattr(self, "leader") and self.leader:
            result["leader"] = str(self.leader)
        elif include_empty:
            result["leader"] = str()
        if hasattr(self, "members") and self.members:
            result["members"] = [str(i0) for i0 in self.members]
        elif include_empty:
            result["members"] = []
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "party_id") and self.party_id:
            result["partyId"] = str(self.party_id)
        elif include_empty:
            result["partyId"] = str()
        if hasattr(self, "updated_at") and self.updated_at:
            result["updatedAt"] = int(self.updated_at)
        elif include_empty:
            result["updatedAt"] = int()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        custom_attribute: Dict[str, Any],
        invitees: List[str],
        leader: str,
        members: List[str],
        namespace: str,
        party_id: str,
        updated_at: int,
    ) -> ModelsPartyData:
        instance = cls()
        instance.custom_attribute = custom_attribute
        instance.invitees = invitees
        instance.leader = leader
        instance.members = members
        instance.namespace = namespace
        instance.party_id = party_id
        instance.updated_at = updated_at
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsPartyData:
        instance = cls()
        if not dict_:
            return instance
        if "custom_attribute" in dict_ and dict_["custom_attribute"] is not None:
            instance.custom_attribute = {str(k0): v0 for k0, v0 in dict_["custom_attribute"].items()}
        elif include_empty:
            instance.custom_attribute = {}
        if "invitees" in dict_ and dict_["invitees"] is not None:
            instance.invitees = [str(i0) for i0 in dict_["invitees"]]
        elif include_empty:
            instance.invitees = []
        if "leader" in dict_ and dict_["leader"] is not None:
            instance.leader = str(dict_["leader"])
        elif include_empty:
            instance.leader = str()
        if "members" in dict_ and dict_["members"] is not None:
            instance.members = [str(i0) for i0 in dict_["members"]]
        elif include_empty:
            instance.members = []
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "partyId" in dict_ and dict_["partyId"] is not None:
            instance.party_id = str(dict_["partyId"])
        elif include_empty:
            instance.party_id = str()
        if "updatedAt" in dict_ and dict_["updatedAt"] is not None:
            instance.updated_at = int(dict_["updatedAt"])
        elif include_empty:
            instance.updated_at = int()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "custom_attribute": "custom_attribute",
            "invitees": "invitees",
            "leader": "leader",
            "members": "members",
            "namespace": "namespace",
            "partyId": "party_id",
            "updatedAt": "updated_at",
        }

    # endregion static methods
