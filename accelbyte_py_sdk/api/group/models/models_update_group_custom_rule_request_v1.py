# Auto-generated at 2021-09-27T17:12:37.840811+08:00
# from: Justice Group Service (2.4.0)

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

from ..models.models_update_group_custom_rule_request_v1_group_custom_rule import ModelsUpdateGroupCustomRuleRequestV1GroupCustomRule


class ModelsUpdateGroupCustomRuleRequestV1(Model):
    """Models update group custom rule request V1

    Properties:
        group_custom_rule: (groupCustomRule) REQUIRED ModelsUpdateGroupCustomRuleRequestV1GroupCustomRule
    """

    # region fields

    group_custom_rule: ModelsUpdateGroupCustomRuleRequestV1GroupCustomRule                         # REQUIRED

    # endregion fields

    # region with_x methods

    def with_group_custom_rule(self, value: ModelsUpdateGroupCustomRuleRequestV1GroupCustomRule) -> ModelsUpdateGroupCustomRuleRequestV1:
        self.group_custom_rule = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "group_custom_rule") and self.group_custom_rule:
            result["groupCustomRule"] = self.group_custom_rule.to_dict(include_empty=include_empty)
        elif include_empty:
            result["groupCustomRule"] = ModelsUpdateGroupCustomRuleRequestV1GroupCustomRule()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        group_custom_rule: ModelsUpdateGroupCustomRuleRequestV1GroupCustomRule,
    ) -> ModelsUpdateGroupCustomRuleRequestV1:
        instance = cls()
        instance.group_custom_rule = group_custom_rule
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsUpdateGroupCustomRuleRequestV1:
        instance = cls()
        if not dict_:
            return instance
        if "groupCustomRule" in dict_ and dict_["groupCustomRule"] is not None:
            instance.group_custom_rule = ModelsUpdateGroupCustomRuleRequestV1GroupCustomRule.create_from_dict(dict_["groupCustomRule"], include_empty=include_empty)
        elif include_empty:
            instance.group_custom_rule = ModelsUpdateGroupCustomRuleRequestV1GroupCustomRule()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "groupCustomRule": "group_custom_rule",
        }

    # endregion static methods
