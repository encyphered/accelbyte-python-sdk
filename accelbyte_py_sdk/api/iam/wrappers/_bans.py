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

from ..models import AccountcommonBanReasons
from ..models import AccountcommonBanReasonsV3
from ..models import AccountcommonBans
from ..models import AccountcommonBansV3
from ..models import ModelGetUserBanV3Response
from ..models import RestapiErrorResponse

from ..operations.bans import AdminGetBannedUsersV3
from ..operations.bans import AdminGetBansTypeV3
from ..operations.bans import AdminGetBansTypeWithNamespaceV3
from ..operations.bans import AdminGetListBanReasonV3
from ..operations.bans import GetBansType
from ..operations.bans import GetListBanReason


@same_doc_as(AdminGetBannedUsersV3)
def admin_get_banned_users_v3(active_only: Optional[bool] = None, ban_type: Optional[str] = None, offset: Optional[int] = None, limit: Optional[int] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AdminGetBannedUsersV3.create(
        active_only=active_only,
        ban_type=ban_type,
        offset=offset,
        limit=limit,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(AdminGetBansTypeV3)
def admin_get_bans_type_v3():
    request = AdminGetBansTypeV3.create()
    return run_request(request)


@same_doc_as(AdminGetBansTypeWithNamespaceV3)
def admin_get_bans_type_with_namespace_v3(namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AdminGetBansTypeWithNamespaceV3.create(
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(AdminGetListBanReasonV3)
def admin_get_list_ban_reason_v3():
    request = AdminGetListBanReasonV3.create()
    return run_request(request)


@same_doc_as(GetBansType)
def get_bans_type():
    request = GetBansType.create()
    return run_request(request)


@same_doc_as(GetListBanReason)
def get_list_ban_reason():
    request = GetListBanReason.create()
    return run_request(request)
