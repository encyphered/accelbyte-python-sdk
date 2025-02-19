# pylint: disable=duplicate-code
# pylint: disable=line-too-long
# pylint: disable=missing-function-docstring
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

from typing import Any, Dict, List, Optional, Tuple, Union

from ....core import get_namespace as get_services_namespace
from ....core import run_request
from ....core import same_doc_as

from ..models import CurrencyConfig
from ..models import CurrencyCreate
from ..models import CurrencyInfo
from ..models import CurrencySummary
from ..models import CurrencyUpdate
from ..models import ErrorEntity
from ..models import ValidationErrorEntity

from ..operations.currency import CreateCurrency
from ..operations.currency import DeleteCurrency
from ..operations.currency import GetCurrencyConfig
from ..operations.currency import GetCurrencySummary
from ..operations.currency import ListCurrencies
from ..operations.currency import PublicListCurrencies
from ..operations.currency import UpdateCurrency


@same_doc_as(CreateCurrency)
def create_currency(body: Optional[CurrencyCreate] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = CreateCurrency.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(DeleteCurrency)
def delete_currency(currency_code: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DeleteCurrency.create(
        currency_code=currency_code,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetCurrencyConfig)
def get_currency_config(currency_code: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetCurrencyConfig.create(
        currency_code=currency_code,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetCurrencySummary)
def get_currency_summary(currency_code: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetCurrencySummary.create(
        currency_code=currency_code,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(ListCurrencies)
def list_currencies(namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = ListCurrencies.create(
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicListCurrencies)
def public_list_currencies(namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicListCurrencies.create(
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(UpdateCurrency)
def update_currency(currency_code: str, body: Optional[CurrencyUpdate] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = UpdateCurrency.create(
        currency_code=currency_code,
        body=body,
        namespace=namespace,
    )
    return run_request(request)
