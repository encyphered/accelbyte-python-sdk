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

from ..models import NamespaceSlotConfigInfo
from ..models import SlotConfigUpdate
from ..models import UserSlotConfigInfo

from ..operations.slot_config import DeleteNamespaceSlotConfig
from ..operations.slot_config import DeleteUserSlotConfig
from ..operations.slot_config import GetNamespaceSlotConfig
from ..operations.slot_config import GetUserSlotConfig
from ..operations.slot_config import UpdateNamespaceSlotConfig
from ..operations.slot_config import UpdateUserSlotConfig


@same_doc_as(DeleteNamespaceSlotConfig)
def delete_namespace_slot_config(namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DeleteNamespaceSlotConfig.create(
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(DeleteUserSlotConfig)
def delete_user_slot_config(user_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DeleteUserSlotConfig.create(
        user_id=user_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetNamespaceSlotConfig)
def get_namespace_slot_config(namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetNamespaceSlotConfig.create(
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetUserSlotConfig)
def get_user_slot_config(user_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetUserSlotConfig.create(
        user_id=user_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(UpdateNamespaceSlotConfig)
def update_namespace_slot_config(body: Optional[SlotConfigUpdate] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = UpdateNamespaceSlotConfig.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(UpdateUserSlotConfig)
def update_user_slot_config(user_id: str, body: Optional[SlotConfigUpdate] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = UpdateUserSlotConfig.create(
        user_id=user_id,
        body=body,
        namespace=namespace,
    )
    return run_request(request)
