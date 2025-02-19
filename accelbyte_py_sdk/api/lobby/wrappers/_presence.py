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

from ..models import HandlersGetUsersPresenceResponse
from ..models import RestapiErrorResponseBody

from ..operations.presence import UsersPresenceHandlerV1


@same_doc_as(UsersPresenceHandlerV1)
def users_presence_handler_v1(user_ids: str, count_only: Optional[bool] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = UsersPresenceHandlerV1.create(
        user_ids=user_ids,
        count_only=count_only,
        namespace=namespace,
    )
    return run_request(request)
