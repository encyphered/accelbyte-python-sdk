# Auto-generated at 2021-09-27T17:12:33.436703+08:00
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

from ..models.model_localization import ModelLocalization


class ModelNotificationTemplateResponse(Model):
    """Model notification template response

    Properties:
        template_localizations: (templateLocalizations) REQUIRED List[ModelLocalization]

        template_slug: (templateSlug) REQUIRED str
    """

    # region fields

    template_localizations: List[ModelLocalization]                                                # REQUIRED
    template_slug: str                                                                             # REQUIRED

    # endregion fields

    # region with_x methods

    def with_template_localizations(self, value: List[ModelLocalization]) -> ModelNotificationTemplateResponse:
        self.template_localizations = value
        return self

    def with_template_slug(self, value: str) -> ModelNotificationTemplateResponse:
        self.template_slug = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "template_localizations") and self.template_localizations:
            result["templateLocalizations"] = [i0.to_dict(include_empty=include_empty) for i0 in self.template_localizations]
        elif include_empty:
            result["templateLocalizations"] = []
        if hasattr(self, "template_slug") and self.template_slug:
            result["templateSlug"] = str(self.template_slug)
        elif include_empty:
            result["templateSlug"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        template_localizations: List[ModelLocalization],
        template_slug: str,
    ) -> ModelNotificationTemplateResponse:
        instance = cls()
        instance.template_localizations = template_localizations
        instance.template_slug = template_slug
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelNotificationTemplateResponse:
        instance = cls()
        if not dict_:
            return instance
        if "templateLocalizations" in dict_ and dict_["templateLocalizations"] is not None:
            instance.template_localizations = [ModelLocalization.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["templateLocalizations"]]
        elif include_empty:
            instance.template_localizations = []
        if "templateSlug" in dict_ and dict_["templateSlug"] is not None:
            instance.template_slug = str(dict_["templateSlug"])
        elif include_empty:
            instance.template_slug = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "templateLocalizations": "template_localizations",
            "templateSlug": "template_slug",
        }

    # endregion static methods
