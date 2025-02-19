# Auto-generated at 2021-09-27T17:12:36.434970+08:00
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


class PaymentTaxConfigInfo(Model):
    """Payment tax config info

    Properties:
        tax_jar_enabled: (taxJarEnabled) OPTIONAL bool

        tax_jar_api_token: (taxJarApiToken) OPTIONAL str

        sandbox_tax_jar_api_token: (sandboxTaxJarApiToken) OPTIONAL str

        tax_jar_product_codes_mapping: (taxJarProductCodesMapping) OPTIONAL Dict[str, str]
    """

    # region fields

    tax_jar_enabled: bool                                                                          # OPTIONAL
    tax_jar_api_token: str                                                                         # OPTIONAL
    sandbox_tax_jar_api_token: str                                                                 # OPTIONAL
    tax_jar_product_codes_mapping: Dict[str, str]                                                  # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_tax_jar_enabled(self, value: bool) -> PaymentTaxConfigInfo:
        self.tax_jar_enabled = value
        return self

    def with_tax_jar_api_token(self, value: str) -> PaymentTaxConfigInfo:
        self.tax_jar_api_token = value
        return self

    def with_sandbox_tax_jar_api_token(self, value: str) -> PaymentTaxConfigInfo:
        self.sandbox_tax_jar_api_token = value
        return self

    def with_tax_jar_product_codes_mapping(self, value: Dict[str, str]) -> PaymentTaxConfigInfo:
        self.tax_jar_product_codes_mapping = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "tax_jar_enabled") and self.tax_jar_enabled:
            result["taxJarEnabled"] = bool(self.tax_jar_enabled)
        elif include_empty:
            result["taxJarEnabled"] = bool()
        if hasattr(self, "tax_jar_api_token") and self.tax_jar_api_token:
            result["taxJarApiToken"] = str(self.tax_jar_api_token)
        elif include_empty:
            result["taxJarApiToken"] = str()
        if hasattr(self, "sandbox_tax_jar_api_token") and self.sandbox_tax_jar_api_token:
            result["sandboxTaxJarApiToken"] = str(self.sandbox_tax_jar_api_token)
        elif include_empty:
            result["sandboxTaxJarApiToken"] = str()
        if hasattr(self, "tax_jar_product_codes_mapping") and self.tax_jar_product_codes_mapping:
            result["taxJarProductCodesMapping"] = {str(k0): str(v0) for k0, v0 in self.tax_jar_product_codes_mapping.items()}
        elif include_empty:
            result["taxJarProductCodesMapping"] = {}
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        tax_jar_enabled: Optional[bool] = None,
        tax_jar_api_token: Optional[str] = None,
        sandbox_tax_jar_api_token: Optional[str] = None,
        tax_jar_product_codes_mapping: Optional[Dict[str, str]] = None,
    ) -> PaymentTaxConfigInfo:
        instance = cls()
        if tax_jar_enabled is not None:
            instance.tax_jar_enabled = tax_jar_enabled
        if tax_jar_api_token is not None:
            instance.tax_jar_api_token = tax_jar_api_token
        if sandbox_tax_jar_api_token is not None:
            instance.sandbox_tax_jar_api_token = sandbox_tax_jar_api_token
        if tax_jar_product_codes_mapping is not None:
            instance.tax_jar_product_codes_mapping = tax_jar_product_codes_mapping
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> PaymentTaxConfigInfo:
        instance = cls()
        if not dict_:
            return instance
        if "taxJarEnabled" in dict_ and dict_["taxJarEnabled"] is not None:
            instance.tax_jar_enabled = bool(dict_["taxJarEnabled"])
        elif include_empty:
            instance.tax_jar_enabled = bool()
        if "taxJarApiToken" in dict_ and dict_["taxJarApiToken"] is not None:
            instance.tax_jar_api_token = str(dict_["taxJarApiToken"])
        elif include_empty:
            instance.tax_jar_api_token = str()
        if "sandboxTaxJarApiToken" in dict_ and dict_["sandboxTaxJarApiToken"] is not None:
            instance.sandbox_tax_jar_api_token = str(dict_["sandboxTaxJarApiToken"])
        elif include_empty:
            instance.sandbox_tax_jar_api_token = str()
        if "taxJarProductCodesMapping" in dict_ and dict_["taxJarProductCodesMapping"] is not None:
            instance.tax_jar_product_codes_mapping = {str(k0): str(v0) for k0, v0 in dict_["taxJarProductCodesMapping"].items()}
        elif include_empty:
            instance.tax_jar_product_codes_mapping = {}
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "taxJarEnabled": "tax_jar_enabled",
            "taxJarApiToken": "tax_jar_api_token",
            "sandboxTaxJarApiToken": "sandbox_tax_jar_api_token",
            "taxJarProductCodesMapping": "tax_jar_product_codes_mapping",
        }

    # endregion static methods
