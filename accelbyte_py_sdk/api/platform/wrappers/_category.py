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

from ..models import BasicCategoryInfo
from ..models import CategoryCreate
from ..models import CategoryInfo
from ..models import CategoryUpdate
from ..models import ErrorEntity
from ..models import FullCategoryInfo
from ..models import HierarchicalCategoryInfo
from ..models import ValidationErrorEntity

from ..operations.category import CreateCategory
from ..operations.category import DeleteCategory
from ..operations.category import DownloadCategories
from ..operations.category import GetCategory
from ..operations.category import GetChildCategories
from ..operations.category import GetDescendantCategories
from ..operations.category import GetRootCategories
from ..operations.category import ListCategoriesBasic
from ..operations.category import PublicGetCategory
from ..operations.category import PublicGetChildCategories
from ..operations.category import PublicGetDescendantCategories
from ..operations.category import PublicGetRootCategories
from ..operations.category import UpdateCategory


@same_doc_as(CreateCategory)
def create_category(store_id: str, body: Optional[CategoryCreate] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = CreateCategory.create(
        store_id=store_id,
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(DeleteCategory)
def delete_category(category_path: str, store_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DeleteCategory.create(
        category_path=category_path,
        store_id=store_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(DownloadCategories)
def download_categories(store_id: Optional[str] = None, language: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DownloadCategories.create(
        store_id=store_id,
        language=language,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetCategory)
def get_category(category_path: str, store_id: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetCategory.create(
        category_path=category_path,
        store_id=store_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetChildCategories)
def get_child_categories(category_path: str, store_id: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetChildCategories.create(
        category_path=category_path,
        store_id=store_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetDescendantCategories)
def get_descendant_categories(category_path: str, store_id: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetDescendantCategories.create(
        category_path=category_path,
        store_id=store_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetRootCategories)
def get_root_categories(store_id: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetRootCategories.create(
        store_id=store_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(ListCategoriesBasic)
def list_categories_basic(store_id: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = ListCategoriesBasic.create(
        store_id=store_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicGetCategory)
def public_get_category(category_path: str, store_id: Optional[str] = None, language: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicGetCategory.create(
        category_path=category_path,
        store_id=store_id,
        language=language,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicGetChildCategories)
def public_get_child_categories(category_path: str, store_id: Optional[str] = None, language: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicGetChildCategories.create(
        category_path=category_path,
        store_id=store_id,
        language=language,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicGetDescendantCategories)
def public_get_descendant_categories(category_path: str, language: Optional[str] = None, store_id: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicGetDescendantCategories.create(
        category_path=category_path,
        language=language,
        store_id=store_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicGetRootCategories)
def public_get_root_categories(store_id: Optional[str] = None, language: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicGetRootCategories.create(
        store_id=store_id,
        language=language,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(UpdateCategory)
def update_category(category_path: str, store_id: str, body: Optional[CategoryUpdate] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = UpdateCategory.create(
        category_path=category_path,
        store_id=store_id,
        body=body,
        namespace=namespace,
    )
    return run_request(request)
