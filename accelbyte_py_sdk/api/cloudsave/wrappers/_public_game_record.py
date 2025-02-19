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

from ..models import ModelsGameRecord
from ..models import ModelsGameRecordRequest
from ..models import ResponseError

from ..operations.public_game_record import DeleteGameRecordHandlerV1
from ..operations.public_game_record import GetGameRecordHandlerV1
from ..operations.public_game_record import PostGameRecordHandlerV1
from ..operations.public_game_record import PutGameRecordHandlerV1


@same_doc_as(DeleteGameRecordHandlerV1)
def delete_game_record_handler_v1(key: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DeleteGameRecordHandlerV1.create(
        key=key,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetGameRecordHandlerV1)
def get_game_record_handler_v1(key: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetGameRecordHandlerV1.create(
        key=key,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PostGameRecordHandlerV1)
def post_game_record_handler_v1(body: ModelsGameRecordRequest, key: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PostGameRecordHandlerV1.create(
        body=body,
        key=key,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PutGameRecordHandlerV1)
def put_game_record_handler_v1(body: ModelsGameRecordRequest, key: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PutGameRecordHandlerV1.create(
        body=body,
        key=key,
        namespace=namespace,
    )
    return run_request(request)
