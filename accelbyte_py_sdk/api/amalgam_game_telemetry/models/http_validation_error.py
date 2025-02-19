# Auto-generated at 2021-09-27T17:12:38.375245+08:00
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

from ..models.validation_error import ValidationError


class HTTPValidationError(Model):
    """HTTP validation error

    Properties:
        detail: (detail) OPTIONAL List[ValidationError]
    """

    # region fields

    detail: List[ValidationError]                                                                  # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_detail(self, value: List[ValidationError]) -> HTTPValidationError:
        self.detail = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "detail") and self.detail:
            result["detail"] = [i0.to_dict(include_empty=include_empty) for i0 in self.detail]
        elif include_empty:
            result["detail"] = []
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        detail: Optional[List[ValidationError]] = None,
    ) -> HTTPValidationError:
        instance = cls()
        if detail is not None:
            instance.detail = detail
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> HTTPValidationError:
        instance = cls()
        if not dict_:
            return instance
        if "detail" in dict_ and dict_["detail"] is not None:
            instance.detail = [ValidationError.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["detail"]]
        elif include_empty:
            instance.detail = []
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "detail": "detail",
        }

    # endregion static methods
