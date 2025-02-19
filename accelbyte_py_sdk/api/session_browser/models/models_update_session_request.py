# Auto-generated at 2021-09-27T17:12:37.378411+08:00
# from: Justice SessionBrowser Service ()

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


class ModelsUpdateSessionRequest(Model):
    """Models update session request

    Properties:
        game_current_player: (game_current_player) REQUIRED int

        game_max_player: (game_max_player) REQUIRED int
    """

    # region fields

    game_current_player: int                                                                       # REQUIRED
    game_max_player: int                                                                           # REQUIRED

    # endregion fields

    # region with_x methods

    def with_game_current_player(self, value: int) -> ModelsUpdateSessionRequest:
        self.game_current_player = value
        return self

    def with_game_max_player(self, value: int) -> ModelsUpdateSessionRequest:
        self.game_max_player = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "game_current_player") and self.game_current_player:
            result["game_current_player"] = int(self.game_current_player)
        elif include_empty:
            result["game_current_player"] = int()
        if hasattr(self, "game_max_player") and self.game_max_player:
            result["game_max_player"] = int(self.game_max_player)
        elif include_empty:
            result["game_max_player"] = int()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        game_current_player: int,
        game_max_player: int,
    ) -> ModelsUpdateSessionRequest:
        instance = cls()
        instance.game_current_player = game_current_player
        instance.game_max_player = game_max_player
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsUpdateSessionRequest:
        instance = cls()
        if not dict_:
            return instance
        if "game_current_player" in dict_ and dict_["game_current_player"] is not None:
            instance.game_current_player = int(dict_["game_current_player"])
        elif include_empty:
            instance.game_current_player = int()
        if "game_max_player" in dict_ and dict_["game_max_player"] is not None:
            instance.game_max_player = int(dict_["game_max_player"])
        elif include_empty:
            instance.game_max_player = int()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "game_current_player": "game_current_player",
            "game_max_player": "game_max_player",
        }

    # endregion static methods
