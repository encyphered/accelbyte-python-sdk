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

from ..models import ModelsConfigList
from ..models import ModelsConfigReq
from ..models import RestapiErrorResponseBody

from ..operations.config import AdminGetAllConfigV1
from ..operations.config import AdminGetConfigV1
from ..operations.config import AdminUpdateConfigV1


@same_doc_as(AdminGetAllConfigV1)
def admin_get_all_config_v1():
    request = AdminGetAllConfigV1.create()
    return run_request(request)


@same_doc_as(AdminGetConfigV1)
def admin_get_config_v1(namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AdminGetConfigV1.create(
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(AdminUpdateConfigV1)
def admin_update_config_v1(body: ModelsConfigReq, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AdminUpdateConfigV1.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)
