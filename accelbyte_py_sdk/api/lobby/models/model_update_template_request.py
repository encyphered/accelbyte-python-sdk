# Auto-generated at 2021-09-27T17:12:33.453655+08:00
# from: Justice Lobby Service (1.33.0)

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


class ModelUpdateTemplateRequest(Model):
    """Model update template request

    Properties:
        template_content: (templateContent) REQUIRED str
    """

    # region fields

    template_content: str                                                                          # REQUIRED

    # endregion fields

    # region with_x methods

    def with_template_content(self, value: str) -> ModelUpdateTemplateRequest:
        self.template_content = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "template_content") and self.template_content:
            result["templateContent"] = str(self.template_content)
        elif include_empty:
            result["templateContent"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        template_content: str,
    ) -> ModelUpdateTemplateRequest:
        instance = cls()
        instance.template_content = template_content
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelUpdateTemplateRequest:
        instance = cls()
        if not dict_:
            return instance
        if "templateContent" in dict_ and dict_["templateContent"] is not None:
            instance.template_content = str(dict_["templateContent"])
        elif include_empty:
            instance.template_content = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "templateContent": "template_content",
        }

    # endregion static methods
