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

from ..models import ErrorEntity
from ..models import StoreBackupInfo
from ..models import StoreCreate
from ..models import StoreInfo
from ..models import StoreUpdate
from ..models import ValidationErrorEntity

from ..operations.store import CloneStore
from ..operations.store import CreateStore
from ..operations.store import DeletePublishedStore
from ..operations.store import DeleteStore
from ..operations.store import ExportStore
from ..operations.store import GetPublishedStore
from ..operations.store import GetPublishedStoreBackup
from ..operations.store import GetStore
from ..operations.store import ImportStore
from ..operations.store import ListStores
from ..operations.store import PublicListStores
from ..operations.store import RollbackPublishedStore
from ..operations.store import UpdateStore


@same_doc_as(CloneStore)
def clone_store(store_id: str, target_store_id: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = CloneStore.create(
        store_id=store_id,
        target_store_id=target_store_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(CreateStore)
def create_store(body: Optional[StoreCreate] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = CreateStore.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(DeletePublishedStore)
def delete_published_store(namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DeletePublishedStore.create(
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(DeleteStore)
def delete_store(store_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DeleteStore.create(
        store_id=store_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(ExportStore)
def export_store(store_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = ExportStore.create(
        store_id=store_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetPublishedStore)
def get_published_store(namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetPublishedStore.create(
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetPublishedStoreBackup)
def get_published_store_backup(namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetPublishedStoreBackup.create(
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetStore)
def get_store(store_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetStore.create(
        store_id=store_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(ImportStore)
def import_store(file: Optional[Any] = None, store_id: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = ImportStore.create(
        file=file,
        store_id=store_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(ListStores)
def list_stores(namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = ListStores.create(
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicListStores)
def public_list_stores(namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicListStores.create(
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(RollbackPublishedStore)
def rollback_published_store(namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = RollbackPublishedStore.create(
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(UpdateStore)
def update_store(store_id: str, body: Optional[StoreUpdate] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = UpdateStore.create(
        store_id=store_id,
        body=body,
        namespace=namespace,
    )
    return run_request(request)
