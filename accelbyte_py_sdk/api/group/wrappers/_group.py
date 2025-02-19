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

from ..models import ModelsGetGroupsListResponseV1
from ..models import ModelsGroupResponseV1
from ..models import ModelsPublicCreateNewGroupRequestV1
from ..models import ModelsUpdateGroupCustomAttributesRequestV1
from ..models import ModelsUpdateGroupCustomRuleRequestV1
from ..models import ModelsUpdateGroupPredefinedRuleRequestV1
from ..models import ModelsUpdateGroupRequestV1
from ..models import ResponseErrorResponse

from ..operations.group import CreateNewGroupPublicV1
from ..operations.group import DeleteGroupAdminV1
from ..operations.group import DeleteGroupPredefinedRulePublicV1
from ..operations.group import DeleteGroupPublicV1
from ..operations.group import GetGroupListAdminV1
from ..operations.group import GetGroupListPublicV1
from ..operations.group import GetSingleGroupAdminV1
from ..operations.group import GetSingleGroupPublicV1
from ..operations.group import UpdateGroupCustomAttributesPublicV1
from ..operations.group import UpdateGroupCustomRulePublicV1
from ..operations.group import UpdateGroupPredefinedRulePublicV1
from ..operations.group import UpdateSingleGroupPartialPublicV1
from ..operations.group import UpdateSingleGroupPublicV1


@same_doc_as(CreateNewGroupPublicV1)
def create_new_group_public_v1(body: ModelsPublicCreateNewGroupRequestV1, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = CreateNewGroupPublicV1.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(DeleteGroupAdminV1)
def delete_group_admin_v1(group_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DeleteGroupAdminV1.create(
        group_id=group_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(DeleteGroupPredefinedRulePublicV1)
def delete_group_predefined_rule_public_v1(group_id: str, allowed_action: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DeleteGroupPredefinedRulePublicV1.create(
        group_id=group_id,
        allowed_action=allowed_action,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(DeleteGroupPublicV1)
def delete_group_public_v1(group_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DeleteGroupPublicV1.create(
        group_id=group_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetGroupListAdminV1)
def get_group_list_admin_v1(limit: Optional[int] = None, offset: Optional[int] = None, group_name: Optional[str] = None, group_region: Optional[str] = None, configuration_code: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetGroupListAdminV1.create(
        limit=limit,
        offset=offset,
        group_name=group_name,
        group_region=group_region,
        configuration_code=configuration_code,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetGroupListPublicV1)
def get_group_list_public_v1(limit: Optional[int] = None, offset: Optional[int] = None, group_name: Optional[str] = None, group_region: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetGroupListPublicV1.create(
        limit=limit,
        offset=offset,
        group_name=group_name,
        group_region=group_region,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetSingleGroupAdminV1)
def get_single_group_admin_v1(group_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetSingleGroupAdminV1.create(
        group_id=group_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetSingleGroupPublicV1)
def get_single_group_public_v1(group_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetSingleGroupPublicV1.create(
        group_id=group_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(UpdateGroupCustomAttributesPublicV1)
def update_group_custom_attributes_public_v1(body: ModelsUpdateGroupCustomAttributesRequestV1, group_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = UpdateGroupCustomAttributesPublicV1.create(
        body=body,
        group_id=group_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(UpdateGroupCustomRulePublicV1)
def update_group_custom_rule_public_v1(body: ModelsUpdateGroupCustomRuleRequestV1, group_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = UpdateGroupCustomRulePublicV1.create(
        body=body,
        group_id=group_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(UpdateGroupPredefinedRulePublicV1)
def update_group_predefined_rule_public_v1(body: ModelsUpdateGroupPredefinedRuleRequestV1, group_id: str, allowed_action: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = UpdateGroupPredefinedRulePublicV1.create(
        body=body,
        group_id=group_id,
        allowed_action=allowed_action,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(UpdateSingleGroupPartialPublicV1)
def update_single_group_partial_public_v1(body: ModelsUpdateGroupRequestV1, group_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = UpdateSingleGroupPartialPublicV1.create(
        body=body,
        group_id=group_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(UpdateSingleGroupPublicV1)
def update_single_group_public_v1(body: ModelsUpdateGroupRequestV1, group_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = UpdateSingleGroupPublicV1.create(
        body=body,
        group_id=group_id,
        namespace=namespace,
    )
    return run_request(request)
