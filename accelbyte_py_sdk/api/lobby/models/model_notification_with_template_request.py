# Auto-generated at 2021-09-27T17:12:33.441520+08:00
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


class ModelNotificationWithTemplateRequest(Model):
    """Model notification with template request

    Properties:
        template_context: (templateContext) REQUIRED Dict[str, str]

        template_language: (templateLanguage) REQUIRED str

        template_slug: (templateSlug) REQUIRED str

        topic: (topic) REQUIRED str
    """

    # region fields

    template_context: Dict[str, str]                                                               # REQUIRED
    template_language: str                                                                         # REQUIRED
    template_slug: str                                                                             # REQUIRED
    topic: str                                                                                     # REQUIRED

    # endregion fields

    # region with_x methods

    def with_template_context(self, value: Dict[str, str]) -> ModelNotificationWithTemplateRequest:
        self.template_context = value
        return self

    def with_template_language(self, value: str) -> ModelNotificationWithTemplateRequest:
        self.template_language = value
        return self

    def with_template_slug(self, value: str) -> ModelNotificationWithTemplateRequest:
        self.template_slug = value
        return self

    def with_topic(self, value: str) -> ModelNotificationWithTemplateRequest:
        self.topic = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "template_context") and self.template_context:
            result["templateContext"] = {str(k0): str(v0) for k0, v0 in self.template_context.items()}
        elif include_empty:
            result["templateContext"] = {}
        if hasattr(self, "template_language") and self.template_language:
            result["templateLanguage"] = str(self.template_language)
        elif include_empty:
            result["templateLanguage"] = str()
        if hasattr(self, "template_slug") and self.template_slug:
            result["templateSlug"] = str(self.template_slug)
        elif include_empty:
            result["templateSlug"] = str()
        if hasattr(self, "topic") and self.topic:
            result["topic"] = str(self.topic)
        elif include_empty:
            result["topic"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        template_context: Dict[str, str],
        template_language: str,
        template_slug: str,
        topic: str,
    ) -> ModelNotificationWithTemplateRequest:
        instance = cls()
        instance.template_context = template_context
        instance.template_language = template_language
        instance.template_slug = template_slug
        instance.topic = topic
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelNotificationWithTemplateRequest:
        instance = cls()
        if not dict_:
            return instance
        if "templateContext" in dict_ and dict_["templateContext"] is not None:
            instance.template_context = {str(k0): str(v0) for k0, v0 in dict_["templateContext"].items()}
        elif include_empty:
            instance.template_context = {}
        if "templateLanguage" in dict_ and dict_["templateLanguage"] is not None:
            instance.template_language = str(dict_["templateLanguage"])
        elif include_empty:
            instance.template_language = str()
        if "templateSlug" in dict_ and dict_["templateSlug"] is not None:
            instance.template_slug = str(dict_["templateSlug"])
        elif include_empty:
            instance.template_slug = str()
        if "topic" in dict_ and dict_["topic"] is not None:
            instance.topic = str(dict_["topic"])
        elif include_empty:
            instance.topic = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "templateContext": "template_context",
            "templateLanguage": "template_language",
            "templateSlug": "template_slug",
            "topic": "topic",
        }

    # endregion static methods
