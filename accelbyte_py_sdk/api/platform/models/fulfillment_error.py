# Auto-generated at 2021-09-27T17:12:36.122580+08:00
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


class FulfillmentError(Model):
    """Fulfillment error

    Properties:
        http_status: (httpStatus) OPTIONAL int

        code: (code) OPTIONAL int

        message: (message) OPTIONAL str
    """

    # region fields

    http_status: int                                                                               # OPTIONAL
    code: int                                                                                      # OPTIONAL
    message: str                                                                                   # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_http_status(self, value: int) -> FulfillmentError:
        self.http_status = value
        return self

    def with_code(self, value: int) -> FulfillmentError:
        self.code = value
        return self

    def with_message(self, value: str) -> FulfillmentError:
        self.message = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "http_status") and self.http_status:
            result["httpStatus"] = int(self.http_status)
        elif include_empty:
            result["httpStatus"] = int()
        if hasattr(self, "code") and self.code:
            result["code"] = int(self.code)
        elif include_empty:
            result["code"] = int()
        if hasattr(self, "message") and self.message:
            result["message"] = str(self.message)
        elif include_empty:
            result["message"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        http_status: Optional[int] = None,
        code: Optional[int] = None,
        message: Optional[str] = None,
    ) -> FulfillmentError:
        instance = cls()
        if http_status is not None:
            instance.http_status = http_status
        if code is not None:
            instance.code = code
        if message is not None:
            instance.message = message
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> FulfillmentError:
        instance = cls()
        if not dict_:
            return instance
        if "httpStatus" in dict_ and dict_["httpStatus"] is not None:
            instance.http_status = int(dict_["httpStatus"])
        elif include_empty:
            instance.http_status = int()
        if "code" in dict_ and dict_["code"] is not None:
            instance.code = int(dict_["code"])
        elif include_empty:
            instance.code = int()
        if "message" in dict_ and dict_["message"] is not None:
            instance.message = str(dict_["message"])
        elif include_empty:
            instance.message = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "httpStatus": "http_status",
            "code": "code",
            "message": "message",
        }

    # endregion static methods
