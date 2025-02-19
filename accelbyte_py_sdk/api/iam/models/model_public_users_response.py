# Auto-generated at 2021-09-27T17:12:31.583795+08:00
# from: Justice Iam Service (4.1.0)

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

from ..models.model_public_user_response import ModelPublicUserResponse


class ModelPublicUsersResponse(Model):
    """Model public users response

    Properties:
        users: (Users) OPTIONAL List[ModelPublicUserResponse]
    """

    # region fields

    users: List[ModelPublicUserResponse]                                                           # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_users(self, value: List[ModelPublicUserResponse]) -> ModelPublicUsersResponse:
        self.users = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "users") and self.users:
            result["Users"] = [i0.to_dict(include_empty=include_empty) for i0 in self.users]
        elif include_empty:
            result["Users"] = []
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        users: Optional[List[ModelPublicUserResponse]] = None,
    ) -> ModelPublicUsersResponse:
        instance = cls()
        if users is not None:
            instance.users = users
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelPublicUsersResponse:
        instance = cls()
        if not dict_:
            return instance
        if "Users" in dict_ and dict_["Users"] is not None:
            instance.users = [ModelPublicUserResponse.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["Users"]]
        elif include_empty:
            instance.users = []
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "Users": "users",
        }

    # endregion static methods
