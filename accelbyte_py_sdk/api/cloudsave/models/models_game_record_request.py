# Auto-generated at 2021-09-27T17:12:38.261730+08:00
# from: Justice Cloudsave Service (3.38.0)

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


class ModelsGameRecordRequest(Model):
    """Models game record request

    Properties:
    """

    # region fields


    # endregion fields

    # region with_x methods

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
    ) -> ModelsGameRecordRequest:
        instance = cls()
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsGameRecordRequest:
        instance = cls()
        if not dict_:
            return instance
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
        }

    # endregion static methods
