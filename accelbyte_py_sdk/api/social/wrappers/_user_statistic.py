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

from ..models import BulkStatItemCreate
from ..models import BulkStatItemInc
from ..models import BulkStatItemOperationResult
from ..models import BulkStatItemReset
from ..models import BulkStatItemUpdate
from ..models import BulkUserStatItemInc
from ..models import BulkUserStatItemReset
from ..models import BulkUserStatItemUpdate
from ..models import ErrorEntity
from ..models import StatItemInc
from ..models import StatItemIncResult
from ..models import StatItemUpdate
from ..models import StatResetInfo
from ..models import UserStatItemInfo
from ..models import UserStatItemPagingSlicedResult
from ..models import ValidationErrorEntity

from ..operations.user_statistic import BulkCreateUserStatItems
from ..operations.user_statistic import BulkFetchStatItems
from ..operations.user_statistic import BulkFetchStatItems1
from ..operations.user_statistic import BulkIncUserStatItem
from ..operations.user_statistic import BulkIncUserStatItem1
from ..operations.user_statistic import BulkIncUserStatItemValue
from ..operations.user_statistic import BulkIncUserStatItemValue1
from ..operations.user_statistic import BulkIncUserStatItemValue2
from ..operations.user_statistic import BulkResetUserStatItem
from ..operations.user_statistic import BulkResetUserStatItem1
from ..operations.user_statistic import BulkResetUserStatItem2
from ..operations.user_statistic import BulkResetUserStatItem3
from ..operations.user_statistic import BulkUpdateUserStatItem
from ..operations.user_statistic import BulkUpdateUserStatItem1
from ..operations.user_statistic import BulkUpdateUserStatItem2
from ..operations.user_statistic import BulkUpdateUserStatItemV2
from ..operations.user_statistic import CreateUserStatItem
from ..operations.user_statistic import DeleteUserStatItems
from ..operations.user_statistic import DeleteUserStatItems1
from ..operations.user_statistic import DeleteUserStatItems2
from ..operations.user_statistic import GetUserStatItems
from ..operations.user_statistic import IncUserStatItemValue
from ..operations.user_statistic import PublicBulkCreateUserStatItems
from ..operations.user_statistic import PublicBulkIncUserStatItem
from ..operations.user_statistic import PublicBulkIncUserStatItem1
from ..operations.user_statistic import PublicBulkIncUserStatItemValue
from ..operations.user_statistic import PublicCreateUserStatItem
from ..operations.user_statistic import PublicIncUserStatItem
from ..operations.user_statistic import PublicIncUserStatItemValue
from ..operations.user_statistic import PublicQueryUserStatItems
from ..operations.user_statistic import ResetUserStatItemValue
from ..operations.user_statistic import ResetUserStatItemValue1
from ..operations.user_statistic import UpdateUserStatItemValue
from ..operations.user_statistic import UpdateUserStatItemValue1


@same_doc_as(BulkCreateUserStatItems)
def bulk_create_user_stat_items(user_id: str, body: Optional[List[BulkStatItemCreate]] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = BulkCreateUserStatItems.create(
        user_id=user_id,
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(BulkFetchStatItems)
def bulk_fetch_stat_items(stat_code: str, user_ids: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = BulkFetchStatItems.create(
        stat_code=stat_code,
        user_ids=user_ids,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(BulkFetchStatItems1)
def bulk_fetch_stat_items_1(stat_code: str, user_ids: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = BulkFetchStatItems1.create(
        stat_code=stat_code,
        user_ids=user_ids,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(BulkIncUserStatItem)
def bulk_inc_user_stat_item(body: Optional[List[BulkUserStatItemInc]] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = BulkIncUserStatItem.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(BulkIncUserStatItem1)
def bulk_inc_user_stat_item_1(user_id: str, body: Optional[List[BulkStatItemInc]] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = BulkIncUserStatItem1.create(
        user_id=user_id,
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(BulkIncUserStatItemValue)
def bulk_inc_user_stat_item_value(body: Optional[List[BulkUserStatItemInc]] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = BulkIncUserStatItemValue.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(BulkIncUserStatItemValue1)
def bulk_inc_user_stat_item_value_1(user_id: str, body: Optional[List[BulkStatItemInc]] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = BulkIncUserStatItemValue1.create(
        user_id=user_id,
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(BulkIncUserStatItemValue2)
def bulk_inc_user_stat_item_value_2(user_id: str, body: Optional[List[BulkStatItemInc]] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = BulkIncUserStatItemValue2.create(
        user_id=user_id,
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(BulkResetUserStatItem)
def bulk_reset_user_stat_item(body: Optional[List[BulkUserStatItemReset]] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = BulkResetUserStatItem.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(BulkResetUserStatItem1)
def bulk_reset_user_stat_item_1(user_id: str, body: Optional[List[BulkStatItemReset]] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = BulkResetUserStatItem1.create(
        user_id=user_id,
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(BulkResetUserStatItem2)
def bulk_reset_user_stat_item_2(body: Optional[List[BulkUserStatItemReset]] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = BulkResetUserStatItem2.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(BulkResetUserStatItem3)
def bulk_reset_user_stat_item_3(user_id: str, body: Optional[List[BulkStatItemReset]] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = BulkResetUserStatItem3.create(
        user_id=user_id,
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(BulkUpdateUserStatItem)
def bulk_update_user_stat_item(user_id: str, body: Optional[List[BulkStatItemUpdate]] = None, additional_key: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = BulkUpdateUserStatItem.create(
        user_id=user_id,
        body=body,
        additional_key=additional_key,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(BulkUpdateUserStatItem1)
def bulk_update_user_stat_item_1(body: Optional[List[BulkUserStatItemUpdate]] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = BulkUpdateUserStatItem1.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(BulkUpdateUserStatItem2)
def bulk_update_user_stat_item_2(user_id: str, body: Optional[List[BulkStatItemUpdate]] = None, additional_key: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = BulkUpdateUserStatItem2.create(
        user_id=user_id,
        body=body,
        additional_key=additional_key,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(BulkUpdateUserStatItemV2)
def bulk_update_user_stat_item_v2(body: Optional[List[BulkUserStatItemUpdate]] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = BulkUpdateUserStatItemV2.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(CreateUserStatItem)
def create_user_stat_item(user_id: str, stat_code: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = CreateUserStatItem.create(
        user_id=user_id,
        stat_code=stat_code,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(DeleteUserStatItems)
def delete_user_stat_items(user_id: str, stat_code: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DeleteUserStatItems.create(
        user_id=user_id,
        stat_code=stat_code,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(DeleteUserStatItems1)
def delete_user_stat_items_1(user_id: str, stat_code: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DeleteUserStatItems1.create(
        user_id=user_id,
        stat_code=stat_code,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(DeleteUserStatItems2)
def delete_user_stat_items_2(user_id: str, stat_code: str, additional_key: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DeleteUserStatItems2.create(
        user_id=user_id,
        stat_code=stat_code,
        additional_key=additional_key,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetUserStatItems)
def get_user_stat_items(user_id: str, stat_codes: Optional[str] = None, tags: Optional[str] = None, offset: Optional[int] = None, limit: Optional[int] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetUserStatItems.create(
        user_id=user_id,
        stat_codes=stat_codes,
        tags=tags,
        offset=offset,
        limit=limit,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(IncUserStatItemValue)
def inc_user_stat_item_value(user_id: str, stat_code: str, body: Optional[StatItemInc] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = IncUserStatItemValue.create(
        user_id=user_id,
        stat_code=stat_code,
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicBulkCreateUserStatItems)
def public_bulk_create_user_stat_items(user_id: str, body: Optional[List[BulkStatItemCreate]] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicBulkCreateUserStatItems.create(
        user_id=user_id,
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicBulkIncUserStatItem)
def public_bulk_inc_user_stat_item(body: Optional[List[BulkUserStatItemInc]] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicBulkIncUserStatItem.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicBulkIncUserStatItem1)
def public_bulk_inc_user_stat_item_1(user_id: str, body: Optional[List[BulkStatItemInc]] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicBulkIncUserStatItem1.create(
        user_id=user_id,
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicBulkIncUserStatItemValue)
def public_bulk_inc_user_stat_item_value(body: Optional[List[BulkUserStatItemInc]] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicBulkIncUserStatItemValue.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicCreateUserStatItem)
def public_create_user_stat_item(user_id: str, stat_code: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicCreateUserStatItem.create(
        user_id=user_id,
        stat_code=stat_code,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicIncUserStatItem)
def public_inc_user_stat_item(user_id: str, stat_code: str, body: Optional[StatItemInc] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicIncUserStatItem.create(
        user_id=user_id,
        stat_code=stat_code,
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicIncUserStatItemValue)
def public_inc_user_stat_item_value(user_id: str, stat_code: str, body: Optional[StatItemInc] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicIncUserStatItemValue.create(
        user_id=user_id,
        stat_code=stat_code,
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicQueryUserStatItems)
def public_query_user_stat_items(user_id: str, stat_codes: Optional[str] = None, tags: Optional[str] = None, offset: Optional[int] = None, limit: Optional[int] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicQueryUserStatItems.create(
        user_id=user_id,
        stat_codes=stat_codes,
        tags=tags,
        offset=offset,
        limit=limit,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(ResetUserStatItemValue)
def reset_user_stat_item_value(user_id: str, stat_code: str, body: Optional[StatResetInfo] = None, additional_key: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = ResetUserStatItemValue.create(
        user_id=user_id,
        stat_code=stat_code,
        body=body,
        additional_key=additional_key,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(ResetUserStatItemValue1)
def reset_user_stat_item_value_1(user_id: str, stat_code: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = ResetUserStatItemValue1.create(
        user_id=user_id,
        stat_code=stat_code,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(UpdateUserStatItemValue)
def update_user_stat_item_value(user_id: str, stat_code: str, body: Optional[StatItemUpdate] = None, additional_key: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = UpdateUserStatItemValue.create(
        user_id=user_id,
        stat_code=stat_code,
        body=body,
        additional_key=additional_key,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(UpdateUserStatItemValue1)
def update_user_stat_item_value_1(user_id: str, stat_code: str, body: Optional[StatItemUpdate] = None, additional_key: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = UpdateUserStatItemValue1.create(
        user_id=user_id,
        stat_code=stat_code,
        body=body,
        additional_key=additional_key,
        namespace=namespace,
    )
    return run_request(request)
