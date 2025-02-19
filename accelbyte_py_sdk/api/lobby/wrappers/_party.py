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

from ..models import ModelsPartyData
from ..models import ModelsPartyPUTCustomAttributesRequest
from ..models import RestapiErrorResponseBody

from ..operations.party import AdminGetPartiesDataV1
from ..operations.party import AdminGetPartyDataV1
from ..operations.party import AdminGetUserPartyV1
from ..operations.party import AdminUpdatePartyAttributesV1
from ..operations.party import PublicGetPartyDataV1
from ..operations.party import PublicUpdatePartyAttributesV1


@same_doc_as(AdminGetPartiesDataV1)
def admin_get_parties_data_v1(limit: Optional[str] = None, offset: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AdminGetPartiesDataV1.create(
        limit=limit,
        offset=offset,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(AdminGetPartyDataV1)
def admin_get_party_data_v1(party_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AdminGetPartyDataV1.create(
        party_id=party_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(AdminGetUserPartyV1)
def admin_get_user_party_v1(user_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AdminGetUserPartyV1.create(
        user_id=user_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(AdminUpdatePartyAttributesV1)
def admin_update_party_attributes_v1(body: ModelsPartyPUTCustomAttributesRequest, party_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AdminUpdatePartyAttributesV1.create(
        body=body,
        party_id=party_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicGetPartyDataV1)
def public_get_party_data_v1(party_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicGetPartyDataV1.create(
        party_id=party_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicUpdatePartyAttributesV1)
def public_update_party_attributes_v1(body: ModelsPartyPUTCustomAttributesRequest, party_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicUpdatePartyAttributesV1.create(
        body=body,
        party_id=party_id,
        namespace=namespace,
    )
    return run_request(request)
