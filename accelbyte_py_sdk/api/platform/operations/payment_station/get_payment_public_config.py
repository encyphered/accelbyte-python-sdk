# Auto-generated at 2021-09-27T17:01:30.112868+08:00
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

from .....core import Operation
from .....core import HttpResponse


class GetPaymentPublicConfig(Operation):
    """Get payment provider public config (getPaymentPublicConfig)

    Properties:
        url: /platform/public/namespaces/{namespace}/payment/publicconfig

        method: GET

        tags: PaymentStation

        consumes: ["application/json"]

        produces: ["application/json"]

        security: bearer

        namespace: (namespace) REQUIRED str in path

        payment_provider: (paymentProvider) REQUIRED str in query

        region: (region) REQUIRED str in query

        sandbox: (sandbox) OPTIONAL bool in query

    Responses:
        200: OK - Dict[str, Any] (successful operation)
    """

    # region fields

    _url: str = "/platform/public/namespaces/{namespace}/payment/publicconfig"
    _method: str = "GET"
    _consumes: List[str] = ["application/json"]
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    namespace: str                                                                                 # REQUIRED in [path]
    payment_provider: str                                                                          # REQUIRED in [query]
    region: str                                                                                    # REQUIRED in [query]
    sandbox: bool                                                                                  # OPTIONAL in [query]

    # endregion fields

    # region properties

    @property
    def url(self) -> str:
        return self._url

    @property
    def method(self) -> str:
        return self._method

    @property
    def consumes(self) -> List[str]:
        return self._consumes

    @property
    def produces(self) -> List[str]:
        return self._produces

    @property
    def security(self) -> Optional[str]:
        return self._security

    @property
    def location_query(self) -> str:
        return self._location_query

    # endregion properties

    # region get methods

    def get_full_url(self, base_url: Union[None, str] = None) -> str:
        result = base_url if base_url is not None else ""

        # path params
        url = self.url
        for k, v in self.get_path_params().items():
            url = url.replace(f"{{{k}}}", v)
        result += url

        # query params
        result += "?" + "&".join([f"{k}={v}" for k, v in self.get_query_params().items()])

        return result

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
            "namespace",
            "payment_provider",
            "region",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "path": self.get_path_params(),
            "query": self.get_query_params(),
        }

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        return result

    def get_query_params(self) -> dict:
        result = {}
        if hasattr(self, "payment_provider"):
            result["paymentProvider"] = self.payment_provider
        if hasattr(self, "region"):
            result["region"] = self.region
        if hasattr(self, "sandbox"):
            result["sandbox"] = self.sandbox
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "payment_provider") or self.payment_provider is None:
            return False
        if not hasattr(self, "region") or self.region is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_namespace(self, value: str) -> GetPaymentPublicConfig:
        self.namespace = value
        return self

    def with_payment_provider(self, value: str) -> GetPaymentPublicConfig:
        self.payment_provider = value
        return self

    def with_region(self, value: str) -> GetPaymentPublicConfig:
        self.region = value
        return self

    def with_sandbox(self, value: bool) -> GetPaymentPublicConfig:
        self.sandbox = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "payment_provider") and self.payment_provider:
            result["paymentProvider"] = str(self.payment_provider)
        elif include_empty:
            result["paymentProvider"] = str()
        if hasattr(self, "region") and self.region:
            result["region"] = str(self.region)
        elif include_empty:
            result["region"] = str()
        if hasattr(self, "sandbox") and self.sandbox:
            result["sandbox"] = bool(self.sandbox)
        elif include_empty:
            result["sandbox"] = bool()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, Dict[str, Any]], Union[None, HttpResponse]]:
        """Parse the given response.

        200: OK - Dict[str, Any] (successful operation)
        """
        if code == 200:
            return {str(k): v for k, v in content.items()}, None
        was_handled, undocumented_response = HttpResponse.try_create_undocumented_response(code, content)
        if was_handled:
            return None, undocumented_response
        return None, HttpResponse.create_unhandled_error()

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        namespace: str,
        payment_provider: str,
        region: str,
        sandbox: Optional[bool] = None,
    ) -> GetPaymentPublicConfig:
        instance = cls()
        instance.namespace = namespace
        instance.payment_provider = payment_provider
        instance.region = region
        if sandbox is not None:
            instance.sandbox = sandbox
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> GetPaymentPublicConfig:
        instance = cls()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "paymentProvider" in dict_ and dict_["paymentProvider"] is not None:
            instance.payment_provider = str(dict_["paymentProvider"])
        elif include_empty:
            instance.payment_provider = str()
        if "region" in dict_ and dict_["region"] is not None:
            instance.region = str(dict_["region"])
        elif include_empty:
            instance.region = str()
        if "sandbox" in dict_ and dict_["sandbox"] is not None:
            instance.sandbox = bool(dict_["sandbox"])
        elif include_empty:
            instance.sandbox = bool()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "paymentProvider": "payment_provider",
            "region": "region",
            "sandbox": "sandbox",
        }

    # endregion static methods
