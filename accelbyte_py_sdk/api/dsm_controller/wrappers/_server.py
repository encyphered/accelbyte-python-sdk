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

from ..models import ModelsDeregisterLocalServerRequest
from ..models import ModelsRegisterLocalServerRequest
from ..models import ModelsRegisterServerRequest
from ..models import ModelsServer
from ..models import ModelsServerSessionResponse
from ..models import ModelsShutdownServerRequest
from ..models import ResponseError

from ..operations.server import DeregisterLocalServer
from ..operations.server import GetServerSession
from ..operations.server import RegisterLocalServer
from ..operations.server import RegisterServer
from ..operations.server import ShutdownServer


@same_doc_as(DeregisterLocalServer)
def deregister_local_server(body: ModelsDeregisterLocalServerRequest, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DeregisterLocalServer.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetServerSession)
def get_server_session(pod_name: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetServerSession.create(
        pod_name=pod_name,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(RegisterLocalServer)
def register_local_server(body: ModelsRegisterLocalServerRequest, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = RegisterLocalServer.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(RegisterServer)
def register_server(body: ModelsRegisterServerRequest, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = RegisterServer.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(ShutdownServer)
def shutdown_server(body: ModelsShutdownServerRequest, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = ShutdownServer.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)
