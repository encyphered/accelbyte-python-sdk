# Auto-generated at 2021-09-27T17:12:36.363069+08:00
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


class GoogleIAPConfigInfo(Model):
    """Google IAP config info

    Properties:
        namespace: (namespace) REQUIRED str

        application_name: (applicationName) OPTIONAL str

        service_account_id: (serviceAccountId) OPTIONAL str

        p12_file_name: (p12FileName) OPTIONAL str
    """

    # region fields

    namespace: str                                                                                 # REQUIRED
    application_name: str                                                                          # OPTIONAL
    service_account_id: str                                                                        # OPTIONAL
    p12_file_name: str                                                                             # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_namespace(self, value: str) -> GoogleIAPConfigInfo:
        self.namespace = value
        return self

    def with_application_name(self, value: str) -> GoogleIAPConfigInfo:
        self.application_name = value
        return self

    def with_service_account_id(self, value: str) -> GoogleIAPConfigInfo:
        self.service_account_id = value
        return self

    def with_p12_file_name(self, value: str) -> GoogleIAPConfigInfo:
        self.p12_file_name = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "application_name") and self.application_name:
            result["applicationName"] = str(self.application_name)
        elif include_empty:
            result["applicationName"] = str()
        if hasattr(self, "service_account_id") and self.service_account_id:
            result["serviceAccountId"] = str(self.service_account_id)
        elif include_empty:
            result["serviceAccountId"] = str()
        if hasattr(self, "p12_file_name") and self.p12_file_name:
            result["p12FileName"] = str(self.p12_file_name)
        elif include_empty:
            result["p12FileName"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        namespace: str,
        application_name: Optional[str] = None,
        service_account_id: Optional[str] = None,
        p12_file_name: Optional[str] = None,
    ) -> GoogleIAPConfigInfo:
        instance = cls()
        instance.namespace = namespace
        if application_name is not None:
            instance.application_name = application_name
        if service_account_id is not None:
            instance.service_account_id = service_account_id
        if p12_file_name is not None:
            instance.p12_file_name = p12_file_name
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> GoogleIAPConfigInfo:
        instance = cls()
        if not dict_:
            return instance
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "applicationName" in dict_ and dict_["applicationName"] is not None:
            instance.application_name = str(dict_["applicationName"])
        elif include_empty:
            instance.application_name = str()
        if "serviceAccountId" in dict_ and dict_["serviceAccountId"] is not None:
            instance.service_account_id = str(dict_["serviceAccountId"])
        elif include_empty:
            instance.service_account_id = str()
        if "p12FileName" in dict_ and dict_["p12FileName"] is not None:
            instance.p12_file_name = str(dict_["p12FileName"])
        elif include_empty:
            instance.p12_file_name = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "applicationName": "application_name",
            "serviceAccountId": "service_account_id",
            "p12FileName": "p12_file_name",
        }

    # endregion static methods
