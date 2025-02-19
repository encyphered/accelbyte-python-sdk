# Auto-generated at 2021-09-27T17:12:34.229355+08:00
# from: Justice Social Service (1.17.1)

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

from ..models.game_profile_public_info import GameProfilePublicInfo


class UserGameProfiles(Model):
    """User game profiles

    Properties:
        user_id: (userId) OPTIONAL str

        game_profiles: (gameProfiles) OPTIONAL List[GameProfilePublicInfo]
    """

    # region fields

    user_id: str                                                                                   # OPTIONAL
    game_profiles: List[GameProfilePublicInfo]                                                     # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_user_id(self, value: str) -> UserGameProfiles:
        self.user_id = value
        return self

    def with_game_profiles(self, value: List[GameProfilePublicInfo]) -> UserGameProfiles:
        self.game_profiles = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        if hasattr(self, "game_profiles") and self.game_profiles:
            result["gameProfiles"] = [i0.to_dict(include_empty=include_empty) for i0 in self.game_profiles]
        elif include_empty:
            result["gameProfiles"] = []
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        user_id: Optional[str] = None,
        game_profiles: Optional[List[GameProfilePublicInfo]] = None,
    ) -> UserGameProfiles:
        instance = cls()
        if user_id is not None:
            instance.user_id = user_id
        if game_profiles is not None:
            instance.game_profiles = game_profiles
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> UserGameProfiles:
        instance = cls()
        if not dict_:
            return instance
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        if "gameProfiles" in dict_ and dict_["gameProfiles"] is not None:
            instance.game_profiles = [GameProfilePublicInfo.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["gameProfiles"]]
        elif include_empty:
            instance.game_profiles = []
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "userId": "user_id",
            "gameProfiles": "game_profiles",
        }

    # endregion static methods
