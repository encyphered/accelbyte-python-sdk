# Auto-generated at 2021-09-27T17:12:38.381739+08:00
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


class ValidationError(Model):
    """Validation error

    Properties:
        loc: (loc) REQUIRED List[str]

        msg: (msg) REQUIRED str

        type_: (type) REQUIRED str
    """

    # region fields

    loc: List[str]                                                                                 # REQUIRED
    msg: str                                                                                       # REQUIRED
    type_: str                                                                                     # REQUIRED

    # endregion fields

    # region with_x methods

    def with_loc(self, value: List[str]) -> ValidationError:
        self.loc = value
        return self

    def with_msg(self, value: str) -> ValidationError:
        self.msg = value
        return self

    def with_type(self, value: str) -> ValidationError:
        self.type_ = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "loc") and self.loc:
            result["loc"] = [str(i0) for i0 in self.loc]
        elif include_empty:
            result["loc"] = []
        if hasattr(self, "msg") and self.msg:
            result["msg"] = str(self.msg)
        elif include_empty:
            result["msg"] = str()
        if hasattr(self, "type_") and self.type_:
            result["type"] = str(self.type_)
        elif include_empty:
            result["type"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        loc: List[str],
        msg: str,
        type_: str,
    ) -> ValidationError:
        instance = cls()
        instance.loc = loc
        instance.msg = msg
        instance.type_ = type_
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ValidationError:
        instance = cls()
        if not dict_:
            return instance
        if "loc" in dict_ and dict_["loc"] is not None:
            instance.loc = [str(i0) for i0 in dict_["loc"]]
        elif include_empty:
            instance.loc = []
        if "msg" in dict_ and dict_["msg"] is not None:
            instance.msg = str(dict_["msg"])
        elif include_empty:
            instance.msg = str()
        if "type" in dict_ and dict_["type"] is not None:
            instance.type_ = str(dict_["type"])
        elif include_empty:
            instance.type_ = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "loc": "loc",
            "msg": "msg",
            "type": "type_",
        }

    # endregion static methods
