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

from ..models import ModelChatMessageResponse
from ..models import RestapiErrorResponseBody

from ..operations.chat import AdminChatHistory
from ..operations.chat import GetPersonalChatHistoryV1Public
from ..operations.chat import PersonalChatHistory


@same_doc_as(AdminChatHistory)
def admin_chat_history(user_id: str, friend_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AdminChatHistory.create(
        user_id=user_id,
        friend_id=friend_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetPersonalChatHistoryV1Public)
def get_personal_chat_history_v1_public(friend_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetPersonalChatHistoryV1Public.create(
        friend_id=friend_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PersonalChatHistory)
def personal_chat_history(user_id: str, friend_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PersonalChatHistory.create(
        user_id=user_id,
        friend_id=friend_id,
        namespace=namespace,
    )
    return run_request(request)
