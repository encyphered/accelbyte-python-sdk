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

from ..models import ModelsGetMemberRequestsListResponseV1
from ..models import ResponseErrorResponse

from ..operations.member_request import GetGroupInvitationRequestPublicV1
from ..operations.member_request import GetGroupJoinRequestPublicV1


@same_doc_as(GetGroupInvitationRequestPublicV1)
def get_group_invitation_request_public_v1(limit: Optional[int] = None, offset: Optional[int] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetGroupInvitationRequestPublicV1.create(
        limit=limit,
        offset=offset,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetGroupJoinRequestPublicV1)
def get_group_join_request_public_v1(group_id: str, limit: Optional[int] = None, offset: Optional[int] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetGroupJoinRequestPublicV1.create(
        group_id=group_id,
        limit=limit,
        offset=offset,
        namespace=namespace,
    )
    return run_request(request)
