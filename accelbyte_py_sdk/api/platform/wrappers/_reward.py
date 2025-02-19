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

from ..models import ErrorEntity
from ..models import RewardCreate
from ..models import RewardInfo
from ..models import RewardPagingSlicedResult
from ..models import RewardUpdate
from ..models import ValidationErrorEntity

from ..operations.reward import CreateReward
from ..operations.reward import DeleteReward
from ..operations.reward import ExportRewards
from ..operations.reward import GetReward
from ..operations.reward import GetReward1
from ..operations.reward import ImportRewards
from ..operations.reward import QueryRewards
from ..operations.reward import QueryRewards1
from ..operations.reward import UpdateReward


@same_doc_as(CreateReward)
def create_reward(body: Optional[RewardCreate] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = CreateReward.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(DeleteReward)
def delete_reward(reward_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DeleteReward.create(
        reward_id=reward_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(ExportRewards)
def export_rewards(namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = ExportRewards.create(
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetReward)
def get_reward(reward_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetReward.create(
        reward_id=reward_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetReward1)
def get_reward_1(reward_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetReward1.create(
        reward_id=reward_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(ImportRewards)
def import_rewards(replace_existing: bool, file: Optional[Any] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = ImportRewards.create(
        replace_existing=replace_existing,
        file=file,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(QueryRewards)
def query_rewards(event_topic: Optional[str] = None, offset: Optional[int] = None, limit: Optional[int] = None, sort_by: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = QueryRewards.create(
        event_topic=event_topic,
        offset=offset,
        limit=limit,
        sort_by=sort_by,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(QueryRewards1)
def query_rewards_1(event_topic: Optional[str] = None, offset: Optional[int] = None, limit: Optional[int] = None, sort_by: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = QueryRewards1.create(
        event_topic=event_topic,
        offset=offset,
        limit=limit,
        sort_by=sort_by,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(UpdateReward)
def update_reward(reward_id: str, body: Optional[RewardUpdate] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = UpdateReward.create(
        reward_id=reward_id,
        body=body,
        namespace=namespace,
    )
    return run_request(request)
