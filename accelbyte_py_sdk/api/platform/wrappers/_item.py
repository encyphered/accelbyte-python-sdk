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

from ..models import AppInfo
from ..models import AppUpdate
from ..models import BasicItem
from ..models import ErrorEntity
from ..models import FullAppInfo
from ..models import FullItemInfo
from ..models import FullItemPagingSlicedResult
from ..models import InGameItemSync
from ..models import ItemAcquireRequest
from ..models import ItemAcquireResult
from ..models import ItemCreate
from ..models import ItemDynamicDataInfo
from ..models import ItemId
from ..models import ItemInfo
from ..models import ItemPagingSlicedResult
from ..models import ItemReturnRequest
from ..models import ItemUpdate
from ..models import PopulatedItemInfo
from ..models import ValidationErrorEntity

from ..operations.item import AcquireItem
from ..operations.item import BulkGetLocaleItems
from ..operations.item import CreateItem
from ..operations.item import DefeatureItem
from ..operations.item import DeleteItem
from ..operations.item import DisableItem
from ..operations.item import EnableItem
from ..operations.item import FeatureItem
from ..operations.item import GetApp
from ..operations.item import GetItem
from ..operations.item import GetItemByAppId
from ..operations.item import GetItemBySku
from ..operations.item import GetItemDynamicData
from ..operations.item import GetItemIdBySku
from ..operations.item import GetLocaleItem
from ..operations.item import GetLocaleItemBySku
from ..operations.item import ListBasicItemsByFeatures
from ..operations.item import PublicBulkGetItems
from ..operations.item import PublicGetApp
from ..operations.item import PublicGetItem
from ..operations.item import PublicGetItemByAppId
from ..operations.item import PublicGetItemBySku
from ..operations.item import PublicGetItemDynamicData
from ..operations.item import PublicQueryItems
from ..operations.item import PublicSearchItems
from ..operations.item import QueryItems
from ..operations.item import QueryUncategorizedItems
from ..operations.item import ReturnItem
from ..operations.item import SearchItems
from ..operations.item import SyncInGameItem
from ..operations.item import UpdateApp
from ..operations.item import UpdateItem


@same_doc_as(AcquireItem)
def acquire_item(item_id: str, body: Optional[ItemAcquireRequest] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AcquireItem.create(
        item_id=item_id,
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(BulkGetLocaleItems)
def bulk_get_locale_items(item_ids: str, store_id: Optional[str] = None, region: Optional[str] = None, language: Optional[str] = None, active_only: Optional[bool] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = BulkGetLocaleItems.create(
        item_ids=item_ids,
        store_id=store_id,
        region=region,
        language=language,
        active_only=active_only,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(CreateItem)
def create_item(store_id: str, body: Optional[ItemCreate] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = CreateItem.create(
        store_id=store_id,
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(DefeatureItem)
def defeature_item(item_id: str, feature: str, store_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DefeatureItem.create(
        item_id=item_id,
        feature=feature,
        store_id=store_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(DeleteItem)
def delete_item(item_id: str, store_id: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DeleteItem.create(
        item_id=item_id,
        store_id=store_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(DisableItem)
def disable_item(item_id: str, store_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DisableItem.create(
        item_id=item_id,
        store_id=store_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(EnableItem)
def enable_item(item_id: str, store_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = EnableItem.create(
        item_id=item_id,
        store_id=store_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(FeatureItem)
def feature_item(item_id: str, feature: str, store_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = FeatureItem.create(
        item_id=item_id,
        feature=feature,
        store_id=store_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetApp)
def get_app(item_id: str, store_id: Optional[str] = None, active_only: Optional[bool] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetApp.create(
        item_id=item_id,
        store_id=store_id,
        active_only=active_only,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetItem)
def get_item(item_id: str, store_id: Optional[str] = None, active_only: Optional[bool] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetItem.create(
        item_id=item_id,
        store_id=store_id,
        active_only=active_only,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetItemByAppId)
def get_item_by_app_id(app_id: str, store_id: Optional[str] = None, active_only: Optional[bool] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetItemByAppId.create(
        app_id=app_id,
        store_id=store_id,
        active_only=active_only,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetItemBySku)
def get_item_by_sku(sku: str, store_id: Optional[str] = None, active_only: Optional[bool] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetItemBySku.create(
        sku=sku,
        store_id=store_id,
        active_only=active_only,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetItemDynamicData)
def get_item_dynamic_data(item_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetItemDynamicData.create(
        item_id=item_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetItemIdBySku)
def get_item_id_by_sku(sku: str, store_id: Optional[str] = None, active_only: Optional[bool] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetItemIdBySku.create(
        sku=sku,
        store_id=store_id,
        active_only=active_only,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetLocaleItem)
def get_locale_item(item_id: str, store_id: Optional[str] = None, region: Optional[str] = None, language: Optional[str] = None, active_only: Optional[bool] = None, populate_bundle: Optional[bool] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetLocaleItem.create(
        item_id=item_id,
        store_id=store_id,
        region=region,
        language=language,
        active_only=active_only,
        populate_bundle=populate_bundle,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetLocaleItemBySku)
def get_locale_item_by_sku(sku: str, store_id: Optional[str] = None, region: Optional[str] = None, language: Optional[str] = None, active_only: Optional[bool] = None, populate_bundle: Optional[bool] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetLocaleItemBySku.create(
        sku=sku,
        store_id=store_id,
        region=region,
        language=language,
        active_only=active_only,
        populate_bundle=populate_bundle,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(ListBasicItemsByFeatures)
def list_basic_items_by_features(features: Optional[List[str]] = None, active_only: Optional[bool] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = ListBasicItemsByFeatures.create(
        features=features,
        active_only=active_only,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicBulkGetItems)
def public_bulk_get_items(item_ids: str, store_id: Optional[str] = None, region: Optional[str] = None, language: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicBulkGetItems.create(
        item_ids=item_ids,
        store_id=store_id,
        region=region,
        language=language,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicGetApp)
def public_get_app(item_id: str, store_id: Optional[str] = None, region: Optional[str] = None, language: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicGetApp.create(
        item_id=item_id,
        store_id=store_id,
        region=region,
        language=language,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicGetItem)
def public_get_item(item_id: str, store_id: Optional[str] = None, region: Optional[str] = None, language: Optional[str] = None, populate_bundle: Optional[bool] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicGetItem.create(
        item_id=item_id,
        store_id=store_id,
        region=region,
        language=language,
        populate_bundle=populate_bundle,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicGetItemByAppId)
def public_get_item_by_app_id(app_id: str, store_id: Optional[str] = None, language: Optional[str] = None, region: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicGetItemByAppId.create(
        app_id=app_id,
        store_id=store_id,
        language=language,
        region=region,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicGetItemBySku)
def public_get_item_by_sku(sku: str, store_id: Optional[str] = None, language: Optional[str] = None, region: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicGetItemBySku.create(
        sku=sku,
        store_id=store_id,
        language=language,
        region=region,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicGetItemDynamicData)
def public_get_item_dynamic_data(item_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicGetItemDynamicData.create(
        item_id=item_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicQueryItems)
def public_query_items(store_id: Optional[str] = None, language: Optional[str] = None, region: Optional[str] = None, category_path: Optional[str] = None, item_type: Optional[str] = None, app_type: Optional[str] = None, base_app_id: Optional[str] = None, tags: Optional[str] = None, features: Optional[str] = None, offset: Optional[int] = None, limit: Optional[int] = None, sort_by: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicQueryItems.create(
        store_id=store_id,
        language=language,
        region=region,
        category_path=category_path,
        item_type=item_type,
        app_type=app_type,
        base_app_id=base_app_id,
        tags=tags,
        features=features,
        offset=offset,
        limit=limit,
        sort_by=sort_by,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicSearchItems)
def public_search_items(language: str, keyword: str, store_id: Optional[str] = None, region: Optional[str] = None, offset: Optional[int] = None, limit: Optional[int] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicSearchItems.create(
        language=language,
        keyword=keyword,
        store_id=store_id,
        region=region,
        offset=offset,
        limit=limit,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(QueryItems)
def query_items(store_id: Optional[str] = None, category_path: Optional[str] = None, item_type: Optional[str] = None, app_type: Optional[str] = None, base_app_id: Optional[str] = None, tags: Optional[str] = None, features: Optional[str] = None, active_only: Optional[bool] = None, region: Optional[str] = None, available_date: Optional[str] = None, target_namespace: Optional[str] = None, offset: Optional[int] = None, limit: Optional[int] = None, sort_by: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = QueryItems.create(
        store_id=store_id,
        category_path=category_path,
        item_type=item_type,
        app_type=app_type,
        base_app_id=base_app_id,
        tags=tags,
        features=features,
        active_only=active_only,
        region=region,
        available_date=available_date,
        target_namespace=target_namespace,
        offset=offset,
        limit=limit,
        sort_by=sort_by,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(QueryUncategorizedItems)
def query_uncategorized_items(store_id: Optional[str] = None, active_only: Optional[bool] = None, offset: Optional[int] = None, limit: Optional[int] = None, sort_by: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = QueryUncategorizedItems.create(
        store_id=store_id,
        active_only=active_only,
        offset=offset,
        limit=limit,
        sort_by=sort_by,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(ReturnItem)
def return_item(item_id: str, body: Optional[ItemReturnRequest] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = ReturnItem.create(
        item_id=item_id,
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(SearchItems)
def search_items(language: str, keyword: str, store_id: Optional[str] = None, active_only: Optional[bool] = None, offset: Optional[int] = None, limit: Optional[int] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = SearchItems.create(
        language=language,
        keyword=keyword,
        store_id=store_id,
        active_only=active_only,
        offset=offset,
        limit=limit,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(SyncInGameItem)
def sync_in_game_item(store_id: str, body: Optional[InGameItemSync] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = SyncInGameItem.create(
        store_id=store_id,
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(UpdateApp)
def update_app(item_id: str, store_id: str, body: Optional[AppUpdate] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = UpdateApp.create(
        item_id=item_id,
        store_id=store_id,
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(UpdateItem)
def update_item(item_id: str, store_id: str, body: Optional[ItemUpdate] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = UpdateItem.create(
        item_id=item_id,
        store_id=store_id,
        body=body,
        namespace=namespace,
    )
    return run_request(request)
