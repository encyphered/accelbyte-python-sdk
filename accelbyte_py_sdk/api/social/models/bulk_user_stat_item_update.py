# Auto-generated at 2021-09-21T14:10:36.852902+08:00
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


class BulkUserStatItemUpdate(Model):
    """Bulk user stat item update

    Properties:
        user_id: (userId) REQUIRED str

        additional_key: (additionalKey) OPTIONAL str

        stat_code: (statCode) REQUIRED str

        update_strategy: (updateStrategy) REQUIRED str

        value: (value) REQUIRED float

        additional_data: (additionalData) OPTIONAL Dict[str, Any]
    """

    # region fields

    user_id: str                                                                                   # REQUIRED
    additional_key: str                                                                            # OPTIONAL
    stat_code: str                                                                                 # REQUIRED
    update_strategy: str                                                                           # REQUIRED
    value: float                                                                                   # REQUIRED
    additional_data: Dict[str, Any]                                                                # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_user_id(self, value: str) -> BulkUserStatItemUpdate:
        self.user_id = value
        return self

    def with_additional_key(self, value: str) -> BulkUserStatItemUpdate:
        self.additional_key = value
        return self

    def with_stat_code(self, value: str) -> BulkUserStatItemUpdate:
        self.stat_code = value
        return self

    def with_update_strategy(self, value: str) -> BulkUserStatItemUpdate:
        self.update_strategy = value
        return self

    def with_value(self, value: float) -> BulkUserStatItemUpdate:
        self.value = value
        return self

    def with_additional_data(self, value: Dict[str, Any]) -> BulkUserStatItemUpdate:
        self.additional_data = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        if hasattr(self, "additional_key") and self.additional_key:
            result["additionalKey"] = str(self.additional_key)
        elif include_empty:
            result["additionalKey"] = str()
        if hasattr(self, "stat_code") and self.stat_code:
            result["statCode"] = str(self.stat_code)
        elif include_empty:
            result["statCode"] = str()
        if hasattr(self, "update_strategy") and self.update_strategy:
            result["updateStrategy"] = str(self.update_strategy)
        elif include_empty:
            result["updateStrategy"] = str()
        if hasattr(self, "value") and self.value:
            result["value"] = float(self.value)
        elif include_empty:
            result["value"] = float()
        if hasattr(self, "additional_data") and self.additional_data:
            result["additionalData"] = {str(k0): v0 for k0, v0 in self.additional_data.items()}
        elif include_empty:
            result["additionalData"] = {}
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        user_id: str,
        stat_code: str,
        update_strategy: str,
        value: float,
        additional_key: Optional[str] = None,
        additional_data: Optional[Dict[str, Any]] = None,
    ) -> BulkUserStatItemUpdate:
        instance = cls()
        instance.user_id = user_id
        instance.stat_code = stat_code
        instance.update_strategy = update_strategy
        instance.value = value
        if additional_key is not None:
            instance.additional_key = additional_key
        if additional_data is not None:
            instance.additional_data = additional_data
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> BulkUserStatItemUpdate:
        instance = cls()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        if "additionalKey" in dict_ and dict_["additionalKey"] is not None:
            instance.additional_key = str(dict_["additionalKey"])
        elif include_empty:
            instance.additional_key = str()
        if "statCode" in dict_ and dict_["statCode"] is not None:
            instance.stat_code = str(dict_["statCode"])
        elif include_empty:
            instance.stat_code = str()
        if "updateStrategy" in dict_ and dict_["updateStrategy"] is not None:
            instance.update_strategy = str(dict_["updateStrategy"])
        elif include_empty:
            instance.update_strategy = str()
        if "value" in dict_ and dict_["value"] is not None:
            instance.value = float(dict_["value"])
        elif include_empty:
            instance.value = float()
        if "additionalData" in dict_ and dict_["additionalData"] is not None:
            instance.additional_data = {str(k0): v0 for k0, v0 in dict_["additionalData"].items()}
        elif include_empty:
            instance.additional_data = {}
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "userId": "user_id",
            "additionalKey": "additional_key",
            "statCode": "stat_code",
            "updateStrategy": "update_strategy",
            "value": "value",
            "additionalData": "additional_data",
        }

    # endregion static methods