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

from ..models import AccountCreateUserRequestV4
from ..models import AccountCreateUserResponseV4
from ..models import AccountUpgradeHeadlessAccountRequestV4
from ..models import AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4
from ..models import AccountUserResponseV4
from ..models import ModelAddUserRoleV4Request
from ..models import ModelEmailUpdateRequestV4
from ..models import ModelListUserRolesV4Response
from ..models import ModelRemoveUserRoleV4Request
from ..models import ModelUserCreateFromInvitationRequestV4
from ..models import ModelUserResponseV3
from ..models import ModelUserUpdateRequestV3
from ..models import RestErrorResponse

from ..operations.users_v4 import AdminAddUserRoleV4
from ..operations.users_v4 import AdminListUserRolesV4
from ..operations.users_v4 import AdminRemoveUserRoleV4
from ..operations.users_v4 import AdminUpdateUserEmailAddressV4
from ..operations.users_v4 import AdminUpdateUserRoleV4
from ..operations.users_v4 import AdminUpdateUserV4
from ..operations.users_v4 import CreateUserFromInvitationV4
from ..operations.users_v4 import PublicCreateUserV4
from ..operations.users_v4 import PublicUpdateUserEmailAddressV4
from ..operations.users_v4 import PublicUpdateUserV4
from ..operations.users_v4 import PublicUpgradeHeadlessAccountV4
from ..operations.users_v4 import PublicUpgradeHeadlessAccountWithVerificationCodeV4


@same_doc_as(AdminAddUserRoleV4)
def admin_add_user_role_v4(body: ModelAddUserRoleV4Request, user_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AdminAddUserRoleV4.create(
        body=body,
        user_id=user_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(AdminListUserRolesV4)
def admin_list_user_roles_v4(user_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AdminListUserRolesV4.create(
        user_id=user_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(AdminRemoveUserRoleV4)
def admin_remove_user_role_v4(body: ModelRemoveUserRoleV4Request, user_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AdminRemoveUserRoleV4.create(
        body=body,
        user_id=user_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(AdminUpdateUserEmailAddressV4)
def admin_update_user_email_address_v4(body: ModelEmailUpdateRequestV4, user_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AdminUpdateUserEmailAddressV4.create(
        body=body,
        user_id=user_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(AdminUpdateUserRoleV4)
def admin_update_user_role_v4(body: ModelAddUserRoleV4Request, user_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AdminUpdateUserRoleV4.create(
        body=body,
        user_id=user_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(AdminUpdateUserV4)
def admin_update_user_v4(body: ModelUserUpdateRequestV3, user_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AdminUpdateUserV4.create(
        body=body,
        user_id=user_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(CreateUserFromInvitationV4)
def create_user_from_invitation_v4(body: ModelUserCreateFromInvitationRequestV4, invitation_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = CreateUserFromInvitationV4.create(
        body=body,
        invitation_id=invitation_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicCreateUserV4)
def public_create_user_v4(body: AccountCreateUserRequestV4, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicCreateUserV4.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicUpdateUserEmailAddressV4)
def public_update_user_email_address_v4(body: ModelEmailUpdateRequestV4, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicUpdateUserEmailAddressV4.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicUpdateUserV4)
def public_update_user_v4(body: ModelUserUpdateRequestV3, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicUpdateUserV4.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicUpgradeHeadlessAccountV4)
def public_upgrade_headless_account_v4(body: AccountUpgradeHeadlessAccountRequestV4, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicUpgradeHeadlessAccountV4.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicUpgradeHeadlessAccountWithVerificationCodeV4)
def public_upgrade_headless_account_with_verification_code_v4(body: AccountUpgradeHeadlessAccountWithVerificationCodeRequestV4, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicUpgradeHeadlessAccountWithVerificationCodeV4.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)
