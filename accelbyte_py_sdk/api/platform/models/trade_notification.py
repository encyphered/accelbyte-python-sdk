# Auto-generated at 2021-09-27T17:12:36.310070+08:00
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

from ..models.additional_data import AdditionalData
from ..models.currency_summary import CurrencySummary


class TradeNotification(Model):
    """Trade notification

    Properties:
        namespace: (namespace) REQUIRED str

        user_id: (userId) OPTIONAL str

        issued_at: (issuedAt) REQUIRED str

        type_: (type) REQUIRED str

        target_namespace: (targetNamespace) OPTIONAL str

        target_user_id: (targetUserId) OPTIONAL str

        nonce_str: (nonceStr) REQUIRED str

        payment_order_no: (paymentOrderNo) REQUIRED str

        ext_order_no: (extOrderNo) REQUIRED str

        sku: (sku) OPTIONAL str

        ext_user_id: (extUserId) OPTIONAL str

        sandbox: (sandbox) REQUIRED bool

        price: (price) REQUIRED int

        payment_provider: (paymentProvider) REQUIRED str

        payment_method: (paymentMethod) OPTIONAL str

        tax: (tax) OPTIONAL int

        vat: (vat) OPTIONAL int

        sales_tax: (salesTax) OPTIONAL int

        payment_provider_fee: (paymentProviderFee) OPTIONAL int

        payment_method_fee: (paymentMethodFee) OPTIONAL int

        currency: (currency) REQUIRED CurrencySummary

        payment_station_url: (paymentStationUrl) OPTIONAL str

        status: (status) REQUIRED str

        status_reason: (statusReason) OPTIONAL str

        authorised_time: (authorisedTime) OPTIONAL str

        created_time: (createdTime) OPTIONAL str

        charged_time: (chargedTime) OPTIONAL str

        refunded_time: (refundedTime) OPTIONAL str

        chargeback_time: (chargebackTime) OPTIONAL str

        chargeback_reversed_time: (chargebackReversedTime) OPTIONAL str

        custom_parameters: (customParameters) OPTIONAL Dict[str, Any]

        metadata: (metadata) OPTIONAL Dict[str, str]

        subscription_id: (subscriptionId) OPTIONAL str

        total_tax: (totalTax) OPTIONAL int

        total_price: (totalPrice) OPTIONAL int

        subtotal_price: (subtotalPrice) OPTIONAL int

        ext_tx_id: (extTxId) OPTIONAL str

        tx_end_time: (txEndTime) OPTIONAL str

        additional_data: (additionalData) OPTIONAL AdditionalData
    """

    # region fields

    namespace: str                                                                                 # REQUIRED
    user_id: str                                                                                   # OPTIONAL
    issued_at: str                                                                                 # REQUIRED
    type_: str                                                                                     # REQUIRED
    target_namespace: str                                                                          # OPTIONAL
    target_user_id: str                                                                            # OPTIONAL
    nonce_str: str                                                                                 # REQUIRED
    payment_order_no: str                                                                          # REQUIRED
    ext_order_no: str                                                                              # REQUIRED
    sku: str                                                                                       # OPTIONAL
    ext_user_id: str                                                                               # OPTIONAL
    sandbox: bool                                                                                  # REQUIRED
    price: int                                                                                     # REQUIRED
    payment_provider: str                                                                          # REQUIRED
    payment_method: str                                                                            # OPTIONAL
    tax: int                                                                                       # OPTIONAL
    vat: int                                                                                       # OPTIONAL
    sales_tax: int                                                                                 # OPTIONAL
    payment_provider_fee: int                                                                      # OPTIONAL
    payment_method_fee: int                                                                        # OPTIONAL
    currency: CurrencySummary                                                                      # REQUIRED
    payment_station_url: str                                                                       # OPTIONAL
    status: str                                                                                    # REQUIRED
    status_reason: str                                                                             # OPTIONAL
    authorised_time: str                                                                           # OPTIONAL
    created_time: str                                                                              # OPTIONAL
    charged_time: str                                                                              # OPTIONAL
    refunded_time: str                                                                             # OPTIONAL
    chargeback_time: str                                                                           # OPTIONAL
    chargeback_reversed_time: str                                                                  # OPTIONAL
    custom_parameters: Dict[str, Any]                                                              # OPTIONAL
    metadata: Dict[str, str]                                                                       # OPTIONAL
    subscription_id: str                                                                           # OPTIONAL
    total_tax: int                                                                                 # OPTIONAL
    total_price: int                                                                               # OPTIONAL
    subtotal_price: int                                                                            # OPTIONAL
    ext_tx_id: str                                                                                 # OPTIONAL
    tx_end_time: str                                                                               # OPTIONAL
    additional_data: AdditionalData                                                                # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_namespace(self, value: str) -> TradeNotification:
        self.namespace = value
        return self

    def with_user_id(self, value: str) -> TradeNotification:
        self.user_id = value
        return self

    def with_issued_at(self, value: str) -> TradeNotification:
        self.issued_at = value
        return self

    def with_type(self, value: str) -> TradeNotification:
        self.type_ = value
        return self

    def with_target_namespace(self, value: str) -> TradeNotification:
        self.target_namespace = value
        return self

    def with_target_user_id(self, value: str) -> TradeNotification:
        self.target_user_id = value
        return self

    def with_nonce_str(self, value: str) -> TradeNotification:
        self.nonce_str = value
        return self

    def with_payment_order_no(self, value: str) -> TradeNotification:
        self.payment_order_no = value
        return self

    def with_ext_order_no(self, value: str) -> TradeNotification:
        self.ext_order_no = value
        return self

    def with_sku(self, value: str) -> TradeNotification:
        self.sku = value
        return self

    def with_ext_user_id(self, value: str) -> TradeNotification:
        self.ext_user_id = value
        return self

    def with_sandbox(self, value: bool) -> TradeNotification:
        self.sandbox = value
        return self

    def with_price(self, value: int) -> TradeNotification:
        self.price = value
        return self

    def with_payment_provider(self, value: str) -> TradeNotification:
        self.payment_provider = value
        return self

    def with_payment_method(self, value: str) -> TradeNotification:
        self.payment_method = value
        return self

    def with_tax(self, value: int) -> TradeNotification:
        self.tax = value
        return self

    def with_vat(self, value: int) -> TradeNotification:
        self.vat = value
        return self

    def with_sales_tax(self, value: int) -> TradeNotification:
        self.sales_tax = value
        return self

    def with_payment_provider_fee(self, value: int) -> TradeNotification:
        self.payment_provider_fee = value
        return self

    def with_payment_method_fee(self, value: int) -> TradeNotification:
        self.payment_method_fee = value
        return self

    def with_currency(self, value: CurrencySummary) -> TradeNotification:
        self.currency = value
        return self

    def with_payment_station_url(self, value: str) -> TradeNotification:
        self.payment_station_url = value
        return self

    def with_status(self, value: str) -> TradeNotification:
        self.status = value
        return self

    def with_status_reason(self, value: str) -> TradeNotification:
        self.status_reason = value
        return self

    def with_authorised_time(self, value: str) -> TradeNotification:
        self.authorised_time = value
        return self

    def with_created_time(self, value: str) -> TradeNotification:
        self.created_time = value
        return self

    def with_charged_time(self, value: str) -> TradeNotification:
        self.charged_time = value
        return self

    def with_refunded_time(self, value: str) -> TradeNotification:
        self.refunded_time = value
        return self

    def with_chargeback_time(self, value: str) -> TradeNotification:
        self.chargeback_time = value
        return self

    def with_chargeback_reversed_time(self, value: str) -> TradeNotification:
        self.chargeback_reversed_time = value
        return self

    def with_custom_parameters(self, value: Dict[str, Any]) -> TradeNotification:
        self.custom_parameters = value
        return self

    def with_metadata(self, value: Dict[str, str]) -> TradeNotification:
        self.metadata = value
        return self

    def with_subscription_id(self, value: str) -> TradeNotification:
        self.subscription_id = value
        return self

    def with_total_tax(self, value: int) -> TradeNotification:
        self.total_tax = value
        return self

    def with_total_price(self, value: int) -> TradeNotification:
        self.total_price = value
        return self

    def with_subtotal_price(self, value: int) -> TradeNotification:
        self.subtotal_price = value
        return self

    def with_ext_tx_id(self, value: str) -> TradeNotification:
        self.ext_tx_id = value
        return self

    def with_tx_end_time(self, value: str) -> TradeNotification:
        self.tx_end_time = value
        return self

    def with_additional_data(self, value: AdditionalData) -> TradeNotification:
        self.additional_data = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        if hasattr(self, "issued_at") and self.issued_at:
            result["issuedAt"] = str(self.issued_at)
        elif include_empty:
            result["issuedAt"] = str()
        if hasattr(self, "type_") and self.type_:
            result["type"] = str(self.type_)
        elif include_empty:
            result["type"] = str()
        if hasattr(self, "target_namespace") and self.target_namespace:
            result["targetNamespace"] = str(self.target_namespace)
        elif include_empty:
            result["targetNamespace"] = str()
        if hasattr(self, "target_user_id") and self.target_user_id:
            result["targetUserId"] = str(self.target_user_id)
        elif include_empty:
            result["targetUserId"] = str()
        if hasattr(self, "nonce_str") and self.nonce_str:
            result["nonceStr"] = str(self.nonce_str)
        elif include_empty:
            result["nonceStr"] = str()
        if hasattr(self, "payment_order_no") and self.payment_order_no:
            result["paymentOrderNo"] = str(self.payment_order_no)
        elif include_empty:
            result["paymentOrderNo"] = str()
        if hasattr(self, "ext_order_no") and self.ext_order_no:
            result["extOrderNo"] = str(self.ext_order_no)
        elif include_empty:
            result["extOrderNo"] = str()
        if hasattr(self, "sku") and self.sku:
            result["sku"] = str(self.sku)
        elif include_empty:
            result["sku"] = str()
        if hasattr(self, "ext_user_id") and self.ext_user_id:
            result["extUserId"] = str(self.ext_user_id)
        elif include_empty:
            result["extUserId"] = str()
        if hasattr(self, "sandbox") and self.sandbox:
            result["sandbox"] = bool(self.sandbox)
        elif include_empty:
            result["sandbox"] = bool()
        if hasattr(self, "price") and self.price:
            result["price"] = int(self.price)
        elif include_empty:
            result["price"] = int()
        if hasattr(self, "payment_provider") and self.payment_provider:
            result["paymentProvider"] = str(self.payment_provider)
        elif include_empty:
            result["paymentProvider"] = str()
        if hasattr(self, "payment_method") and self.payment_method:
            result["paymentMethod"] = str(self.payment_method)
        elif include_empty:
            result["paymentMethod"] = str()
        if hasattr(self, "tax") and self.tax:
            result["tax"] = int(self.tax)
        elif include_empty:
            result["tax"] = int()
        if hasattr(self, "vat") and self.vat:
            result["vat"] = int(self.vat)
        elif include_empty:
            result["vat"] = int()
        if hasattr(self, "sales_tax") and self.sales_tax:
            result["salesTax"] = int(self.sales_tax)
        elif include_empty:
            result["salesTax"] = int()
        if hasattr(self, "payment_provider_fee") and self.payment_provider_fee:
            result["paymentProviderFee"] = int(self.payment_provider_fee)
        elif include_empty:
            result["paymentProviderFee"] = int()
        if hasattr(self, "payment_method_fee") and self.payment_method_fee:
            result["paymentMethodFee"] = int(self.payment_method_fee)
        elif include_empty:
            result["paymentMethodFee"] = int()
        if hasattr(self, "currency") and self.currency:
            result["currency"] = self.currency.to_dict(include_empty=include_empty)
        elif include_empty:
            result["currency"] = CurrencySummary()
        if hasattr(self, "payment_station_url") and self.payment_station_url:
            result["paymentStationUrl"] = str(self.payment_station_url)
        elif include_empty:
            result["paymentStationUrl"] = str()
        if hasattr(self, "status") and self.status:
            result["status"] = str(self.status)
        elif include_empty:
            result["status"] = str()
        if hasattr(self, "status_reason") and self.status_reason:
            result["statusReason"] = str(self.status_reason)
        elif include_empty:
            result["statusReason"] = str()
        if hasattr(self, "authorised_time") and self.authorised_time:
            result["authorisedTime"] = str(self.authorised_time)
        elif include_empty:
            result["authorisedTime"] = str()
        if hasattr(self, "created_time") and self.created_time:
            result["createdTime"] = str(self.created_time)
        elif include_empty:
            result["createdTime"] = str()
        if hasattr(self, "charged_time") and self.charged_time:
            result["chargedTime"] = str(self.charged_time)
        elif include_empty:
            result["chargedTime"] = str()
        if hasattr(self, "refunded_time") and self.refunded_time:
            result["refundedTime"] = str(self.refunded_time)
        elif include_empty:
            result["refundedTime"] = str()
        if hasattr(self, "chargeback_time") and self.chargeback_time:
            result["chargebackTime"] = str(self.chargeback_time)
        elif include_empty:
            result["chargebackTime"] = str()
        if hasattr(self, "chargeback_reversed_time") and self.chargeback_reversed_time:
            result["chargebackReversedTime"] = str(self.chargeback_reversed_time)
        elif include_empty:
            result["chargebackReversedTime"] = str()
        if hasattr(self, "custom_parameters") and self.custom_parameters:
            result["customParameters"] = {str(k0): v0 for k0, v0 in self.custom_parameters.items()}
        elif include_empty:
            result["customParameters"] = {}
        if hasattr(self, "metadata") and self.metadata:
            result["metadata"] = {str(k0): str(v0) for k0, v0 in self.metadata.items()}
        elif include_empty:
            result["metadata"] = {}
        if hasattr(self, "subscription_id") and self.subscription_id:
            result["subscriptionId"] = str(self.subscription_id)
        elif include_empty:
            result["subscriptionId"] = str()
        if hasattr(self, "total_tax") and self.total_tax:
            result["totalTax"] = int(self.total_tax)
        elif include_empty:
            result["totalTax"] = int()
        if hasattr(self, "total_price") and self.total_price:
            result["totalPrice"] = int(self.total_price)
        elif include_empty:
            result["totalPrice"] = int()
        if hasattr(self, "subtotal_price") and self.subtotal_price:
            result["subtotalPrice"] = int(self.subtotal_price)
        elif include_empty:
            result["subtotalPrice"] = int()
        if hasattr(self, "ext_tx_id") and self.ext_tx_id:
            result["extTxId"] = str(self.ext_tx_id)
        elif include_empty:
            result["extTxId"] = str()
        if hasattr(self, "tx_end_time") and self.tx_end_time:
            result["txEndTime"] = str(self.tx_end_time)
        elif include_empty:
            result["txEndTime"] = str()
        if hasattr(self, "additional_data") and self.additional_data:
            result["additionalData"] = self.additional_data.to_dict(include_empty=include_empty)
        elif include_empty:
            result["additionalData"] = AdditionalData()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        namespace: str,
        issued_at: str,
        type_: str,
        nonce_str: str,
        payment_order_no: str,
        ext_order_no: str,
        sandbox: bool,
        price: int,
        payment_provider: str,
        currency: CurrencySummary,
        status: str,
        user_id: Optional[str] = None,
        target_namespace: Optional[str] = None,
        target_user_id: Optional[str] = None,
        sku: Optional[str] = None,
        ext_user_id: Optional[str] = None,
        payment_method: Optional[str] = None,
        tax: Optional[int] = None,
        vat: Optional[int] = None,
        sales_tax: Optional[int] = None,
        payment_provider_fee: Optional[int] = None,
        payment_method_fee: Optional[int] = None,
        payment_station_url: Optional[str] = None,
        status_reason: Optional[str] = None,
        authorised_time: Optional[str] = None,
        created_time: Optional[str] = None,
        charged_time: Optional[str] = None,
        refunded_time: Optional[str] = None,
        chargeback_time: Optional[str] = None,
        chargeback_reversed_time: Optional[str] = None,
        custom_parameters: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, str]] = None,
        subscription_id: Optional[str] = None,
        total_tax: Optional[int] = None,
        total_price: Optional[int] = None,
        subtotal_price: Optional[int] = None,
        ext_tx_id: Optional[str] = None,
        tx_end_time: Optional[str] = None,
        additional_data: Optional[AdditionalData] = None,
    ) -> TradeNotification:
        instance = cls()
        instance.namespace = namespace
        instance.issued_at = issued_at
        instance.type_ = type_
        instance.nonce_str = nonce_str
        instance.payment_order_no = payment_order_no
        instance.ext_order_no = ext_order_no
        instance.sandbox = sandbox
        instance.price = price
        instance.payment_provider = payment_provider
        instance.currency = currency
        instance.status = status
        if user_id is not None:
            instance.user_id = user_id
        if target_namespace is not None:
            instance.target_namespace = target_namespace
        if target_user_id is not None:
            instance.target_user_id = target_user_id
        if sku is not None:
            instance.sku = sku
        if ext_user_id is not None:
            instance.ext_user_id = ext_user_id
        if payment_method is not None:
            instance.payment_method = payment_method
        if tax is not None:
            instance.tax = tax
        if vat is not None:
            instance.vat = vat
        if sales_tax is not None:
            instance.sales_tax = sales_tax
        if payment_provider_fee is not None:
            instance.payment_provider_fee = payment_provider_fee
        if payment_method_fee is not None:
            instance.payment_method_fee = payment_method_fee
        if payment_station_url is not None:
            instance.payment_station_url = payment_station_url
        if status_reason is not None:
            instance.status_reason = status_reason
        if authorised_time is not None:
            instance.authorised_time = authorised_time
        if created_time is not None:
            instance.created_time = created_time
        if charged_time is not None:
            instance.charged_time = charged_time
        if refunded_time is not None:
            instance.refunded_time = refunded_time
        if chargeback_time is not None:
            instance.chargeback_time = chargeback_time
        if chargeback_reversed_time is not None:
            instance.chargeback_reversed_time = chargeback_reversed_time
        if custom_parameters is not None:
            instance.custom_parameters = custom_parameters
        if metadata is not None:
            instance.metadata = metadata
        if subscription_id is not None:
            instance.subscription_id = subscription_id
        if total_tax is not None:
            instance.total_tax = total_tax
        if total_price is not None:
            instance.total_price = total_price
        if subtotal_price is not None:
            instance.subtotal_price = subtotal_price
        if ext_tx_id is not None:
            instance.ext_tx_id = ext_tx_id
        if tx_end_time is not None:
            instance.tx_end_time = tx_end_time
        if additional_data is not None:
            instance.additional_data = additional_data
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> TradeNotification:
        instance = cls()
        if not dict_:
            return instance
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        if "issuedAt" in dict_ and dict_["issuedAt"] is not None:
            instance.issued_at = str(dict_["issuedAt"])
        elif include_empty:
            instance.issued_at = str()
        if "type" in dict_ and dict_["type"] is not None:
            instance.type_ = str(dict_["type"])
        elif include_empty:
            instance.type_ = str()
        if "targetNamespace" in dict_ and dict_["targetNamespace"] is not None:
            instance.target_namespace = str(dict_["targetNamespace"])
        elif include_empty:
            instance.target_namespace = str()
        if "targetUserId" in dict_ and dict_["targetUserId"] is not None:
            instance.target_user_id = str(dict_["targetUserId"])
        elif include_empty:
            instance.target_user_id = str()
        if "nonceStr" in dict_ and dict_["nonceStr"] is not None:
            instance.nonce_str = str(dict_["nonceStr"])
        elif include_empty:
            instance.nonce_str = str()
        if "paymentOrderNo" in dict_ and dict_["paymentOrderNo"] is not None:
            instance.payment_order_no = str(dict_["paymentOrderNo"])
        elif include_empty:
            instance.payment_order_no = str()
        if "extOrderNo" in dict_ and dict_["extOrderNo"] is not None:
            instance.ext_order_no = str(dict_["extOrderNo"])
        elif include_empty:
            instance.ext_order_no = str()
        if "sku" in dict_ and dict_["sku"] is not None:
            instance.sku = str(dict_["sku"])
        elif include_empty:
            instance.sku = str()
        if "extUserId" in dict_ and dict_["extUserId"] is not None:
            instance.ext_user_id = str(dict_["extUserId"])
        elif include_empty:
            instance.ext_user_id = str()
        if "sandbox" in dict_ and dict_["sandbox"] is not None:
            instance.sandbox = bool(dict_["sandbox"])
        elif include_empty:
            instance.sandbox = bool()
        if "price" in dict_ and dict_["price"] is not None:
            instance.price = int(dict_["price"])
        elif include_empty:
            instance.price = int()
        if "paymentProvider" in dict_ and dict_["paymentProvider"] is not None:
            instance.payment_provider = str(dict_["paymentProvider"])
        elif include_empty:
            instance.payment_provider = str()
        if "paymentMethod" in dict_ and dict_["paymentMethod"] is not None:
            instance.payment_method = str(dict_["paymentMethod"])
        elif include_empty:
            instance.payment_method = str()
        if "tax" in dict_ and dict_["tax"] is not None:
            instance.tax = int(dict_["tax"])
        elif include_empty:
            instance.tax = int()
        if "vat" in dict_ and dict_["vat"] is not None:
            instance.vat = int(dict_["vat"])
        elif include_empty:
            instance.vat = int()
        if "salesTax" in dict_ and dict_["salesTax"] is not None:
            instance.sales_tax = int(dict_["salesTax"])
        elif include_empty:
            instance.sales_tax = int()
        if "paymentProviderFee" in dict_ and dict_["paymentProviderFee"] is not None:
            instance.payment_provider_fee = int(dict_["paymentProviderFee"])
        elif include_empty:
            instance.payment_provider_fee = int()
        if "paymentMethodFee" in dict_ and dict_["paymentMethodFee"] is not None:
            instance.payment_method_fee = int(dict_["paymentMethodFee"])
        elif include_empty:
            instance.payment_method_fee = int()
        if "currency" in dict_ and dict_["currency"] is not None:
            instance.currency = CurrencySummary.create_from_dict(dict_["currency"], include_empty=include_empty)
        elif include_empty:
            instance.currency = CurrencySummary()
        if "paymentStationUrl" in dict_ and dict_["paymentStationUrl"] is not None:
            instance.payment_station_url = str(dict_["paymentStationUrl"])
        elif include_empty:
            instance.payment_station_url = str()
        if "status" in dict_ and dict_["status"] is not None:
            instance.status = str(dict_["status"])
        elif include_empty:
            instance.status = str()
        if "statusReason" in dict_ and dict_["statusReason"] is not None:
            instance.status_reason = str(dict_["statusReason"])
        elif include_empty:
            instance.status_reason = str()
        if "authorisedTime" in dict_ and dict_["authorisedTime"] is not None:
            instance.authorised_time = str(dict_["authorisedTime"])
        elif include_empty:
            instance.authorised_time = str()
        if "createdTime" in dict_ and dict_["createdTime"] is not None:
            instance.created_time = str(dict_["createdTime"])
        elif include_empty:
            instance.created_time = str()
        if "chargedTime" in dict_ and dict_["chargedTime"] is not None:
            instance.charged_time = str(dict_["chargedTime"])
        elif include_empty:
            instance.charged_time = str()
        if "refundedTime" in dict_ and dict_["refundedTime"] is not None:
            instance.refunded_time = str(dict_["refundedTime"])
        elif include_empty:
            instance.refunded_time = str()
        if "chargebackTime" in dict_ and dict_["chargebackTime"] is not None:
            instance.chargeback_time = str(dict_["chargebackTime"])
        elif include_empty:
            instance.chargeback_time = str()
        if "chargebackReversedTime" in dict_ and dict_["chargebackReversedTime"] is not None:
            instance.chargeback_reversed_time = str(dict_["chargebackReversedTime"])
        elif include_empty:
            instance.chargeback_reversed_time = str()
        if "customParameters" in dict_ and dict_["customParameters"] is not None:
            instance.custom_parameters = {str(k0): v0 for k0, v0 in dict_["customParameters"].items()}
        elif include_empty:
            instance.custom_parameters = {}
        if "metadata" in dict_ and dict_["metadata"] is not None:
            instance.metadata = {str(k0): str(v0) for k0, v0 in dict_["metadata"].items()}
        elif include_empty:
            instance.metadata = {}
        if "subscriptionId" in dict_ and dict_["subscriptionId"] is not None:
            instance.subscription_id = str(dict_["subscriptionId"])
        elif include_empty:
            instance.subscription_id = str()
        if "totalTax" in dict_ and dict_["totalTax"] is not None:
            instance.total_tax = int(dict_["totalTax"])
        elif include_empty:
            instance.total_tax = int()
        if "totalPrice" in dict_ and dict_["totalPrice"] is not None:
            instance.total_price = int(dict_["totalPrice"])
        elif include_empty:
            instance.total_price = int()
        if "subtotalPrice" in dict_ and dict_["subtotalPrice"] is not None:
            instance.subtotal_price = int(dict_["subtotalPrice"])
        elif include_empty:
            instance.subtotal_price = int()
        if "extTxId" in dict_ and dict_["extTxId"] is not None:
            instance.ext_tx_id = str(dict_["extTxId"])
        elif include_empty:
            instance.ext_tx_id = str()
        if "txEndTime" in dict_ and dict_["txEndTime"] is not None:
            instance.tx_end_time = str(dict_["txEndTime"])
        elif include_empty:
            instance.tx_end_time = str()
        if "additionalData" in dict_ and dict_["additionalData"] is not None:
            instance.additional_data = AdditionalData.create_from_dict(dict_["additionalData"], include_empty=include_empty)
        elif include_empty:
            instance.additional_data = AdditionalData()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "userId": "user_id",
            "issuedAt": "issued_at",
            "type": "type_",
            "targetNamespace": "target_namespace",
            "targetUserId": "target_user_id",
            "nonceStr": "nonce_str",
            "paymentOrderNo": "payment_order_no",
            "extOrderNo": "ext_order_no",
            "sku": "sku",
            "extUserId": "ext_user_id",
            "sandbox": "sandbox",
            "price": "price",
            "paymentProvider": "payment_provider",
            "paymentMethod": "payment_method",
            "tax": "tax",
            "vat": "vat",
            "salesTax": "sales_tax",
            "paymentProviderFee": "payment_provider_fee",
            "paymentMethodFee": "payment_method_fee",
            "currency": "currency",
            "paymentStationUrl": "payment_station_url",
            "status": "status",
            "statusReason": "status_reason",
            "authorisedTime": "authorised_time",
            "createdTime": "created_time",
            "chargedTime": "charged_time",
            "refundedTime": "refunded_time",
            "chargebackTime": "chargeback_time",
            "chargebackReversedTime": "chargeback_reversed_time",
            "customParameters": "custom_parameters",
            "metadata": "metadata",
            "subscriptionId": "subscription_id",
            "totalTax": "total_tax",
            "totalPrice": "total_price",
            "subtotalPrice": "subtotal_price",
            "extTxId": "ext_tx_id",
            "txEndTime": "tx_end_time",
            "additionalData": "additional_data",
        }

    # endregion static methods
