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

from ..models import ModelsCreateGroupConfigurationRequestV1
from ..models import ModelsCreateGroupConfigurationResponseV1
from ..models import ModelsGetGroupConfigurationResponseV1
from ..models import ModelsUpdateGroupConfigurationGlobalRulesRequestV1
from ..models import ModelsUpdateGroupConfigurationRequestV1
from ..models import ModelsUpdateGroupConfigurationResponseV1
from ..models import ResponseErrorResponse

from ..operations.configuration import CreateGroupConfigurationAdminV1
from ..operations.configuration import DeleteGroupConfigurationAdminV1
from ..operations.configuration import DeleteGroupConfigurationGlobalRuleAdminV1
from ..operations.configuration import GetGroupConfigurationAdminV1
from ..operations.configuration import InitiateGroupConfigurationAdminV1
from ..operations.configuration import ListGroupConfigurationAdminV1
from ..operations.configuration import UpdateGroupConfigurationAdminV1
from ..operations.configuration import UpdateGroupConfigurationGlobalRuleAdminV1


@same_doc_as(CreateGroupConfigurationAdminV1)
def create_group_configuration_admin_v1(body: ModelsCreateGroupConfigurationRequestV1, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = CreateGroupConfigurationAdminV1.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(DeleteGroupConfigurationAdminV1)
def delete_group_configuration_admin_v1(configuration_code: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DeleteGroupConfigurationAdminV1.create(
        configuration_code=configuration_code,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(DeleteGroupConfigurationGlobalRuleAdminV1)
def delete_group_configuration_global_rule_admin_v1(configuration_code: str, allowed_action: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DeleteGroupConfigurationGlobalRuleAdminV1.create(
        configuration_code=configuration_code,
        allowed_action=allowed_action,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetGroupConfigurationAdminV1)
def get_group_configuration_admin_v1(configuration_code: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetGroupConfigurationAdminV1.create(
        configuration_code=configuration_code,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(InitiateGroupConfigurationAdminV1)
def initiate_group_configuration_admin_v1(namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = InitiateGroupConfigurationAdminV1.create(
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(ListGroupConfigurationAdminV1)
def list_group_configuration_admin_v1(limit: Optional[int] = None, offset: Optional[int] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = ListGroupConfigurationAdminV1.create(
        limit=limit,
        offset=offset,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(UpdateGroupConfigurationAdminV1)
def update_group_configuration_admin_v1(body: ModelsUpdateGroupConfigurationRequestV1, configuration_code: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = UpdateGroupConfigurationAdminV1.create(
        body=body,
        configuration_code=configuration_code,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(UpdateGroupConfigurationGlobalRuleAdminV1)
def update_group_configuration_global_rule_admin_v1(body: ModelsUpdateGroupConfigurationGlobalRulesRequestV1, configuration_code: str, allowed_action: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = UpdateGroupConfigurationGlobalRuleAdminV1.create(
        body=body,
        configuration_code=configuration_code,
        allowed_action=allowed_action,
        namespace=namespace,
    )
    return run_request(request)
