# Auto-generated at 2021-09-27T17:12:29.741916+08:00
# from: Justice DsmController Service (2.4.0)

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

from ..models.models_image_record import ModelsImageRecord
from ..models.models_paging_cursor import ModelsPagingCursor


class ModelsListImageResponse(Model):
    """Models list image response

    Properties:
        images: (images) REQUIRED List[ModelsImageRecord]

        paging: (paging) REQUIRED ModelsPagingCursor
    """

    # region fields

    images: List[ModelsImageRecord]                                                                # REQUIRED
    paging: ModelsPagingCursor                                                                     # REQUIRED

    # endregion fields

    # region with_x methods

    def with_images(self, value: List[ModelsImageRecord]) -> ModelsListImageResponse:
        self.images = value
        return self

    def with_paging(self, value: ModelsPagingCursor) -> ModelsListImageResponse:
        self.paging = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "images") and self.images:
            result["images"] = [i0.to_dict(include_empty=include_empty) for i0 in self.images]
        elif include_empty:
            result["images"] = []
        if hasattr(self, "paging") and self.paging:
            result["paging"] = self.paging.to_dict(include_empty=include_empty)
        elif include_empty:
            result["paging"] = ModelsPagingCursor()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        images: List[ModelsImageRecord],
        paging: ModelsPagingCursor,
    ) -> ModelsListImageResponse:
        instance = cls()
        instance.images = images
        instance.paging = paging
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> ModelsListImageResponse:
        instance = cls()
        if not dict_:
            return instance
        if "images" in dict_ and dict_["images"] is not None:
            instance.images = [ModelsImageRecord.create_from_dict(i0, include_empty=include_empty) for i0 in dict_["images"]]
        elif include_empty:
            instance.images = []
        if "paging" in dict_ and dict_["paging"] is not None:
            instance.paging = ModelsPagingCursor.create_from_dict(dict_["paging"], include_empty=include_empty)
        elif include_empty:
            instance.paging = ModelsPagingCursor()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "images": "images",
            "paging": "paging",
        }

    # endregion static methods
