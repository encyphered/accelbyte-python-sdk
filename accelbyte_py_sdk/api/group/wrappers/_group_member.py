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

from ..models import ModelsGetGroupMemberListResponseV1
from ..models import ModelsGetUserGroupInformationResponseV1
from ..models import ModelsJoinGroupResponseV1
from ..models import ModelsKickGroupMemberResponseV1
from ..models import ModelsLeaveGroupResponseV1
from ..models import ModelsMemberRequestGroupResponseV1
from ..models import ModelsUserInvitationResponseV1
from ..models import ResponseErrorResponse

from ..operations.group_member import AcceptGroupInvitationPublicV1
from ..operations.group_member import AcceptGroupJoinRequestPublicV1
from ..operations.group_member import CancelGroupJoinRequestV1
from ..operations.group_member import GetGroupMembersListPublicV1
from ..operations.group_member import GetGroupMembersListV1
from ..operations.group_member import GetUserGroupInformationPublicV1
from ..operations.group_member import InviteGroupPublicV1
from ..operations.group_member import JoinGroupV1
from ..operations.group_member import KickGroupMemberPublicV1
from ..operations.group_member import LeaveGroupPublicV1
from ..operations.group_member import RejectGroupInvitationPublicV1
from ..operations.group_member import RejectGroupJoinRequestPublicV1


@same_doc_as(AcceptGroupInvitationPublicV1)
def accept_group_invitation_public_v1(group_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AcceptGroupInvitationPublicV1.create(
        group_id=group_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(AcceptGroupJoinRequestPublicV1)
def accept_group_join_request_public_v1(user_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AcceptGroupJoinRequestPublicV1.create(
        user_id=user_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(CancelGroupJoinRequestV1)
def cancel_group_join_request_v1(group_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = CancelGroupJoinRequestV1.create(
        group_id=group_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetGroupMembersListPublicV1)
def get_group_members_list_public_v1(group_id: str, limit: Optional[int] = None, offset: Optional[int] = None, order: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetGroupMembersListPublicV1.create(
        group_id=group_id,
        limit=limit,
        offset=offset,
        order=order,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetGroupMembersListV1)
def get_group_members_list_v1(group_id: str, limit: Optional[int] = None, offset: Optional[int] = None, order: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetGroupMembersListV1.create(
        group_id=group_id,
        limit=limit,
        offset=offset,
        order=order,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetUserGroupInformationPublicV1)
def get_user_group_information_public_v1(user_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetUserGroupInformationPublicV1.create(
        user_id=user_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(InviteGroupPublicV1)
def invite_group_public_v1(user_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = InviteGroupPublicV1.create(
        user_id=user_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(JoinGroupV1)
def join_group_v1(group_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = JoinGroupV1.create(
        group_id=group_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(KickGroupMemberPublicV1)
def kick_group_member_public_v1(user_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = KickGroupMemberPublicV1.create(
        user_id=user_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(LeaveGroupPublicV1)
def leave_group_public_v1(namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = LeaveGroupPublicV1.create(
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(RejectGroupInvitationPublicV1)
def reject_group_invitation_public_v1(group_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = RejectGroupInvitationPublicV1.create(
        group_id=group_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(RejectGroupJoinRequestPublicV1)
def reject_group_join_request_public_v1(user_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = RejectGroupJoinRequestPublicV1.create(
        user_id=user_id,
        namespace=namespace,
    )
    return run_request(request)
