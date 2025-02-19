# Auto-generated at 2021-09-27T17:12:36.240897+08:00
# from: Justice Platform Service (3.24.0)

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


class Paging(Model):
    """Paging

    Properties:
        previous: (previous) OPTIONAL str

        next_: (next) OPTIONAL str
    """

    # region fields

    previous: str                                                                                  # OPTIONAL
    next_: str                                                                                     # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_previous(self, value: str) -> Paging:
        self.previous = value
        return self

    def with_next(self, value: str) -> Paging:
        self.next_ = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "previous") and self.previous:
            result["previous"] = str(self.previous)
        elif include_empty:
            result["previous"] = str()
        if hasattr(self, "next_") and self.next_:
            result["next"] = str(self.next_)
        elif include_empty:
            result["next"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        previous: Optional[str] = None,
        next_: Optional[str] = None,
    ) -> Paging:
        instance = cls()
        if previous is not None:
            instance.previous = previous
        if next_ is not None:
            instance.next_ = next_
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> Paging:
        instance = cls()
        if not dict_:
            return instance
        if "previous" in dict_ and dict_["previous"] is not None:
            instance.previous = str(dict_["previous"])
        elif include_empty:
            instance.previous = str()
        if "next" in dict_ and dict_["next"] is not None:
            instance.next_ = str(dict_["next"])
        elif include_empty:
            instance.next_ = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "previous": "previous",
            "next": "next_",
        }

    # endregion static methods
