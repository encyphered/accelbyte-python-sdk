# Auto-generated at 2021-09-27T17:01:30.114922+08:00
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


class PublicNormalizePaymentReturnUrl(Operation):
    """Normalize payment return url (publicNormalizePaymentReturnUrl)

    Properties:
        url: /platform/public/namespaces/{namespace}/payment/returnurl

        method: GET

        tags: PaymentStation

        consumes: []

        produces: []

        security: bearer

        namespace: (namespace) REQUIRED str in path

        return_url: (returnUrl) REQUIRED str in query

        order_no: (orderNo) REQUIRED str in query

        payment_order_no: (paymentOrderNo) REQUIRED str in query

        payment_provider: (paymentProvider) REQUIRED str in query

        user_id: (user_id) OPTIONAL str in query

        foreinginvoice: (foreinginvoice) OPTIONAL str in query

        invoice_id: (invoice_id) OPTIONAL str in query

        status: (status) OPTIONAL str in query

        result_code: (resultCode) OPTIONAL str in query

        payload: (payload) OPTIONAL str in query

        type_: (type) OPTIONAL str in query

        token: (token) OPTIONAL str in query

        payer_id: (PayerID) OPTIONAL str in query

    Responses:
        204: No Content - (successful operation)
    """

    # region fields

    _url: str = "/platform/public/namespaces/{namespace}/payment/returnurl"
    _method: str = "GET"
    _consumes: List[str] = []
    _produces: List[str] = []
    _security: Optional[str] = "bearer"
    _location_query: str = None

    namespace: str                                                                                 # REQUIRED in [path]
    return_url: str                                                                                # REQUIRED in [query]
    order_no: str                                                                                  # REQUIRED in [query]
    payment_order_no: str                                                                          # REQUIRED in [query]
    payment_provider: str                                                                          # REQUIRED in [query]
    user_id: str                                                                                   # OPTIONAL in [query]
    foreinginvoice: str                                                                            # OPTIONAL in [query]
    invoice_id: str                                                                                # OPTIONAL in [query]
    status: str                                                                                    # OPTIONAL in [query]
    result_code: str                                                                               # OPTIONAL in [query]
    payload: str                                                                                   # OPTIONAL in [query]
    type_: str                                                                                     # OPTIONAL in [query]
    token: str                                                                                     # OPTIONAL in [query]
    payer_id: str                                                                                  # OPTIONAL in [query]

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
            "return_url",
            "order_no",
            "payment_order_no",
            "payment_provider",
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
        if hasattr(self, "return_url"):
            result["returnUrl"] = self.return_url
        if hasattr(self, "order_no"):
            result["orderNo"] = self.order_no
        if hasattr(self, "payment_order_no"):
            result["paymentOrderNo"] = self.payment_order_no
        if hasattr(self, "payment_provider"):
            result["paymentProvider"] = self.payment_provider
        if hasattr(self, "user_id"):
            result["user_id"] = self.user_id
        if hasattr(self, "foreinginvoice"):
            result["foreinginvoice"] = self.foreinginvoice
        if hasattr(self, "invoice_id"):
            result["invoice_id"] = self.invoice_id
        if hasattr(self, "status"):
            result["status"] = self.status
        if hasattr(self, "result_code"):
            result["resultCode"] = self.result_code
        if hasattr(self, "payload"):
            result["payload"] = self.payload
        if hasattr(self, "type_"):
            result["type"] = self.type_
        if hasattr(self, "token"):
            result["token"] = self.token
        if hasattr(self, "payer_id"):
            result["PayerID"] = self.payer_id
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "return_url") or self.return_url is None:
            return False
        if not hasattr(self, "order_no") or self.order_no is None:
            return False
        if not hasattr(self, "payment_order_no") or self.payment_order_no is None:
            return False
        if not hasattr(self, "payment_provider") or self.payment_provider is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_namespace(self, value: str) -> PublicNormalizePaymentReturnUrl:
        self.namespace = value
        return self

    def with_return_url(self, value: str) -> PublicNormalizePaymentReturnUrl:
        self.return_url = value
        return self

    def with_order_no(self, value: str) -> PublicNormalizePaymentReturnUrl:
        self.order_no = value
        return self

    def with_payment_order_no(self, value: str) -> PublicNormalizePaymentReturnUrl:
        self.payment_order_no = value
        return self

    def with_payment_provider(self, value: str) -> PublicNormalizePaymentReturnUrl:
        self.payment_provider = value
        return self

    def with_user_id(self, value: str) -> PublicNormalizePaymentReturnUrl:
        self.user_id = value
        return self

    def with_foreinginvoice(self, value: str) -> PublicNormalizePaymentReturnUrl:
        self.foreinginvoice = value
        return self

    def with_invoice_id(self, value: str) -> PublicNormalizePaymentReturnUrl:
        self.invoice_id = value
        return self

    def with_status(self, value: str) -> PublicNormalizePaymentReturnUrl:
        self.status = value
        return self

    def with_result_code(self, value: str) -> PublicNormalizePaymentReturnUrl:
        self.result_code = value
        return self

    def with_payload(self, value: str) -> PublicNormalizePaymentReturnUrl:
        self.payload = value
        return self

    def with_type_(self, value: str) -> PublicNormalizePaymentReturnUrl:
        self.type_ = value
        return self

    def with_token(self, value: str) -> PublicNormalizePaymentReturnUrl:
        self.token = value
        return self

    def with_payer_id(self, value: str) -> PublicNormalizePaymentReturnUrl:
        self.payer_id = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "return_url") and self.return_url:
            result["returnUrl"] = str(self.return_url)
        elif include_empty:
            result["returnUrl"] = str()
        if hasattr(self, "order_no") and self.order_no:
            result["orderNo"] = str(self.order_no)
        elif include_empty:
            result["orderNo"] = str()
        if hasattr(self, "payment_order_no") and self.payment_order_no:
            result["paymentOrderNo"] = str(self.payment_order_no)
        elif include_empty:
            result["paymentOrderNo"] = str()
        if hasattr(self, "payment_provider") and self.payment_provider:
            result["paymentProvider"] = str(self.payment_provider)
        elif include_empty:
            result["paymentProvider"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["user_id"] = str(self.user_id)
        elif include_empty:
            result["user_id"] = str()
        if hasattr(self, "foreinginvoice") and self.foreinginvoice:
            result["foreinginvoice"] = str(self.foreinginvoice)
        elif include_empty:
            result["foreinginvoice"] = str()
        if hasattr(self, "invoice_id") and self.invoice_id:
            result["invoice_id"] = str(self.invoice_id)
        elif include_empty:
            result["invoice_id"] = str()
        if hasattr(self, "status") and self.status:
            result["status"] = str(self.status)
        elif include_empty:
            result["status"] = str()
        if hasattr(self, "result_code") and self.result_code:
            result["resultCode"] = str(self.result_code)
        elif include_empty:
            result["resultCode"] = str()
        if hasattr(self, "payload") and self.payload:
            result["payload"] = str(self.payload)
        elif include_empty:
            result["payload"] = str()
        if hasattr(self, "type_") and self.type_:
            result["type"] = str(self.type_)
        elif include_empty:
            result["type"] = str()
        if hasattr(self, "token") and self.token:
            result["token"] = str(self.token)
        elif include_empty:
            result["token"] = str()
        if hasattr(self, "payer_id") and self.payer_id:
            result["PayerID"] = str(self.payer_id)
        elif include_empty:
            result["PayerID"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, HttpResponse], Union[None, HttpResponse]]:
        """Parse the given response.

        204: No Content - (successful operation)
        """
        if code == 204:
            return HttpResponse.create(code, "No Content"), None
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
        return_url: str,
        order_no: str,
        payment_order_no: str,
        payment_provider: str,
        user_id: Optional[str] = None,
        foreinginvoice: Optional[str] = None,
        invoice_id: Optional[str] = None,
        status: Optional[str] = None,
        result_code: Optional[str] = None,
        payload: Optional[str] = None,
        type_: Optional[str] = None,
        token: Optional[str] = None,
        payer_id: Optional[str] = None,
    ) -> PublicNormalizePaymentReturnUrl:
        instance = cls()
        instance.namespace = namespace
        instance.return_url = return_url
        instance.order_no = order_no
        instance.payment_order_no = payment_order_no
        instance.payment_provider = payment_provider
        if user_id is not None:
            instance.user_id = user_id
        if foreinginvoice is not None:
            instance.foreinginvoice = foreinginvoice
        if invoice_id is not None:
            instance.invoice_id = invoice_id
        if status is not None:
            instance.status = status
        if result_code is not None:
            instance.result_code = result_code
        if payload is not None:
            instance.payload = payload
        if type_ is not None:
            instance.type_ = type_
        if token is not None:
            instance.token = token
        if payer_id is not None:
            instance.payer_id = payer_id
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> PublicNormalizePaymentReturnUrl:
        instance = cls()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "returnUrl" in dict_ and dict_["returnUrl"] is not None:
            instance.return_url = str(dict_["returnUrl"])
        elif include_empty:
            instance.return_url = str()
        if "orderNo" in dict_ and dict_["orderNo"] is not None:
            instance.order_no = str(dict_["orderNo"])
        elif include_empty:
            instance.order_no = str()
        if "paymentOrderNo" in dict_ and dict_["paymentOrderNo"] is not None:
            instance.payment_order_no = str(dict_["paymentOrderNo"])
        elif include_empty:
            instance.payment_order_no = str()
        if "paymentProvider" in dict_ and dict_["paymentProvider"] is not None:
            instance.payment_provider = str(dict_["paymentProvider"])
        elif include_empty:
            instance.payment_provider = str()
        if "user_id" in dict_ and dict_["user_id"] is not None:
            instance.user_id = str(dict_["user_id"])
        elif include_empty:
            instance.user_id = str()
        if "foreinginvoice" in dict_ and dict_["foreinginvoice"] is not None:
            instance.foreinginvoice = str(dict_["foreinginvoice"])
        elif include_empty:
            instance.foreinginvoice = str()
        if "invoice_id" in dict_ and dict_["invoice_id"] is not None:
            instance.invoice_id = str(dict_["invoice_id"])
        elif include_empty:
            instance.invoice_id = str()
        if "status" in dict_ and dict_["status"] is not None:
            instance.status = str(dict_["status"])
        elif include_empty:
            instance.status = str()
        if "resultCode" in dict_ and dict_["resultCode"] is not None:
            instance.result_code = str(dict_["resultCode"])
        elif include_empty:
            instance.result_code = str()
        if "payload" in dict_ and dict_["payload"] is not None:
            instance.payload = str(dict_["payload"])
        elif include_empty:
            instance.payload = str()
        if "type" in dict_ and dict_["type"] is not None:
            instance.type_ = str(dict_["type"])
        elif include_empty:
            instance.type_ = str()
        if "token" in dict_ and dict_["token"] is not None:
            instance.token = str(dict_["token"])
        elif include_empty:
            instance.token = str()
        if "PayerID" in dict_ and dict_["PayerID"] is not None:
            instance.payer_id = str(dict_["PayerID"])
        elif include_empty:
            instance.payer_id = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "returnUrl": "return_url",
            "orderNo": "order_no",
            "paymentOrderNo": "payment_order_no",
            "paymentProvider": "payment_provider",
            "user_id": "user_id",
            "foreinginvoice": "foreinginvoice",
            "invoice_id": "invoice_id",
            "status": "status",
            "resultCode": "result_code",
            "payload": "payload",
            "type": "type_",
            "token": "token",
            "PayerID": "payer_id",
        }

    # endregion static methods
