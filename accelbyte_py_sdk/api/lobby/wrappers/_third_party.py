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

from ..models import ModelsCreateConfigRequest
from ..models import ModelsCreateConfigResponse
from ..models import ModelsGetConfigResponse
from ..models import ModelsUpdateConfigRequest
from ..models import ModelsUpdateConfigResponse
from ..models import RestapiErrorResponseV1

from ..operations.third_party import AdminCreateThirdPartyConfig
from ..operations.third_party import AdminDeleteThirdPartyConfig
from ..operations.third_party import AdminGetThirdPartyConfig
from ..operations.third_party import AdminUpdateThirdPartyConfig


@same_doc_as(AdminCreateThirdPartyConfig)
def admin_create_third_party_config(body: ModelsCreateConfigRequest, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AdminCreateThirdPartyConfig.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(AdminDeleteThirdPartyConfig)
def admin_delete_third_party_config(namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AdminDeleteThirdPartyConfig.create(
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(AdminGetThirdPartyConfig)
def admin_get_third_party_config(namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AdminGetThirdPartyConfig.create(
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(AdminUpdateThirdPartyConfig)
def admin_update_third_party_config(body: ModelsUpdateConfigRequest, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AdminUpdateThirdPartyConfig.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)
