# Auto-generated at 2021-09-27T17:12:34.234998+08:00
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


class BulkStatItemOperationResult(Model):
    """Bulk stat item operation result

    Properties:
        success: (success) OPTIONAL bool

        stat_code: (statCode) OPTIONAL str

        details: (details) OPTIONAL Dict[str, Any]
    """

    # region fields

    success: bool                                                                                  # OPTIONAL
    stat_code: str                                                                                 # OPTIONAL
    details: Dict[str, Any]                                                                        # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_success(self, value: bool) -> BulkStatItemOperationResult:
        self.success = value
        return self

    def with_stat_code(self, value: str) -> BulkStatItemOperationResult:
        self.stat_code = value
        return self

    def with_details(self, value: Dict[str, Any]) -> BulkStatItemOperationResult:
        self.details = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "success") and self.success:
            result["success"] = bool(self.success)
        elif include_empty:
            result["success"] = bool()
        if hasattr(self, "stat_code") and self.stat_code:
            result["statCode"] = str(self.stat_code)
        elif include_empty:
            result["statCode"] = str()
        if hasattr(self, "details") and self.details:
            result["details"] = {str(k0): v0 for k0, v0 in self.details.items()}
        elif include_empty:
            result["details"] = {}
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        success: Optional[bool] = None,
        stat_code: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
    ) -> BulkStatItemOperationResult:
        instance = cls()
        if success is not None:
            instance.success = success
        if stat_code is not None:
            instance.stat_code = stat_code
        if details is not None:
            instance.details = details
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> BulkStatItemOperationResult:
        instance = cls()
        if not dict_:
            return instance
        if "success" in dict_ and dict_["success"] is not None:
            instance.success = bool(dict_["success"])
        elif include_empty:
            instance.success = bool()
        if "statCode" in dict_ and dict_["statCode"] is not None:
            instance.stat_code = str(dict_["statCode"])
        elif include_empty:
            instance.stat_code = str()
        if "details" in dict_ and dict_["details"] is not None:
            instance.details = {str(k0): v0 for k0, v0 in dict_["details"].items()}
        elif include_empty:
            instance.details = {}
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "success": "success",
            "statCode": "stat_code",
            "details": "details",
        }

    # endregion static methods
