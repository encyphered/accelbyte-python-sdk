# Auto-generated at 2021-09-27T17:12:36.428693+08:00
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


class PaymentProviderConfigEdit(Model):
    """A DTO object for creating/updating payment provider config

    Properties:
        namespace: (namespace) REQUIRED str

        region: (region) REQUIRED str

        aggregate: (aggregate) OPTIONAL str

        specials: (specials) OPTIONAL List[str]

        tax_jar_enabled: (taxJarEnabled) OPTIONAL bool

        tax_jar_api_token: (taxJarApiToken) OPTIONAL str

        sandbox_tax_jar_api_token: (sandboxTaxJarApiToken) OPTIONAL str

        use_global_tax_jar_api_token: (useGlobalTaxJarApiToken) OPTIONAL bool
    """

    # region fields

    namespace: str                                                                                 # REQUIRED
    region: str                                                                                    # REQUIRED
    aggregate: str                                                                                 # OPTIONAL
    specials: List[str]                                                                            # OPTIONAL
    tax_jar_enabled: bool                                                                          # OPTIONAL
    tax_jar_api_token: str                                                                         # OPTIONAL
    sandbox_tax_jar_api_token: str                                                                 # OPTIONAL
    use_global_tax_jar_api_token: bool                                                             # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_namespace(self, value: str) -> PaymentProviderConfigEdit:
        self.namespace = value
        return self

    def with_region(self, value: str) -> PaymentProviderConfigEdit:
        self.region = value
        return self

    def with_aggregate(self, value: str) -> PaymentProviderConfigEdit:
        self.aggregate = value
        return self

    def with_specials(self, value: List[str]) -> PaymentProviderConfigEdit:
        self.specials = value
        return self

    def with_tax_jar_enabled(self, value: bool) -> PaymentProviderConfigEdit:
        self.tax_jar_enabled = value
        return self

    def with_tax_jar_api_token(self, value: str) -> PaymentProviderConfigEdit:
        self.tax_jar_api_token = value
        return self

    def with_sandbox_tax_jar_api_token(self, value: str) -> PaymentProviderConfigEdit:
        self.sandbox_tax_jar_api_token = value
        return self

    def with_use_global_tax_jar_api_token(self, value: bool) -> PaymentProviderConfigEdit:
        self.use_global_tax_jar_api_token = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "region") and self.region:
            result["region"] = str(self.region)
        elif include_empty:
            result["region"] = str()
        if hasattr(self, "aggregate") and self.aggregate:
            result["aggregate"] = str(self.aggregate)
        elif include_empty:
            result["aggregate"] = str()
        if hasattr(self, "specials") and self.specials:
            result["specials"] = [str(i0) for i0 in self.specials]
        elif include_empty:
            result["specials"] = []
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
        if hasattr(self, "use_global_tax_jar_api_token") and self.use_global_tax_jar_api_token:
            result["useGlobalTaxJarApiToken"] = bool(self.use_global_tax_jar_api_token)
        elif include_empty:
            result["useGlobalTaxJarApiToken"] = bool()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        namespace: str,
        region: str,
        aggregate: Optional[str] = None,
        specials: Optional[List[str]] = None,
        tax_jar_enabled: Optional[bool] = None,
        tax_jar_api_token: Optional[str] = None,
        sandbox_tax_jar_api_token: Optional[str] = None,
        use_global_tax_jar_api_token: Optional[bool] = None,
    ) -> PaymentProviderConfigEdit:
        instance = cls()
        instance.namespace = namespace
        instance.region = region
        if aggregate is not None:
            instance.aggregate = aggregate
        if specials is not None:
            instance.specials = specials
        if tax_jar_enabled is not None:
            instance.tax_jar_enabled = tax_jar_enabled
        if tax_jar_api_token is not None:
            instance.tax_jar_api_token = tax_jar_api_token
        if sandbox_tax_jar_api_token is not None:
            instance.sandbox_tax_jar_api_token = sandbox_tax_jar_api_token
        if use_global_tax_jar_api_token is not None:
            instance.use_global_tax_jar_api_token = use_global_tax_jar_api_token
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> PaymentProviderConfigEdit:
        instance = cls()
        if not dict_:
            return instance
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "region" in dict_ and dict_["region"] is not None:
            instance.region = str(dict_["region"])
        elif include_empty:
            instance.region = str()
        if "aggregate" in dict_ and dict_["aggregate"] is not None:
            instance.aggregate = str(dict_["aggregate"])
        elif include_empty:
            instance.aggregate = str()
        if "specials" in dict_ and dict_["specials"] is not None:
            instance.specials = [str(i0) for i0 in dict_["specials"]]
        elif include_empty:
            instance.specials = []
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
        if "useGlobalTaxJarApiToken" in dict_ and dict_["useGlobalTaxJarApiToken"] is not None:
            instance.use_global_tax_jar_api_token = bool(dict_["useGlobalTaxJarApiToken"])
        elif include_empty:
            instance.use_global_tax_jar_api_token = bool()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "region": "region",
            "aggregate": "aggregate",
            "specials": "specials",
            "taxJarEnabled": "tax_jar_enabled",
            "taxJarApiToken": "tax_jar_api_token",
            "sandboxTaxJarApiToken": "sandbox_tax_jar_api_token",
            "useGlobalTaxJarApiToken": "use_global_tax_jar_api_token",
        }

    # endregion static methods
