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

from ..models import AddCountryGroupRequest
from ..models import AddCountryGroupResponse
from ..models import CountryGroupObject
from ..models import CountryObject
from ..models import ErrorEntity
from ..models import RetrieveCountryGroupResponse
from ..models import UpdateCountryGroupRequest
from ..models import ValidationErrorEntity

from ..operations.misc import AddCountryGroup
from ..operations.misc import DeleteCountryGroup
from ..operations.misc import GetCountries
from ..operations.misc import GetCountryGroups
from ..operations.misc import GetLanguages
from ..operations.misc import GetTimeZones
from ..operations.misc import PublicGetCountries
from ..operations.misc import PublicGetLanguages
from ..operations.misc import PublicGetTimeZones
from ..operations.misc import UpdateCountryGroup


@same_doc_as(AddCountryGroup)
def add_country_group(body: Optional[AddCountryGroupRequest] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = AddCountryGroup.create(
        body=body,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(DeleteCountryGroup)
def delete_country_group(country_group_code: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = DeleteCountryGroup.create(
        country_group_code=country_group_code,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetCountries)
def get_countries(lang: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetCountries.create(
        lang=lang,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetCountryGroups)
def get_country_groups(group_code: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetCountryGroups.create(
        group_code=group_code,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetLanguages)
def get_languages(namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetLanguages.create(
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GetTimeZones)
def get_time_zones(namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetTimeZones.create(
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicGetCountries)
def public_get_countries(lang: Optional[str] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicGetCountries.create(
        lang=lang,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicGetLanguages)
def public_get_languages(namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicGetLanguages.create(
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicGetTimeZones)
def public_get_time_zones(namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicGetTimeZones.create(
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(UpdateCountryGroup)
def update_country_group(country_group_code: str, body: Optional[UpdateCountryGroupRequest] = None, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = UpdateCountryGroup.create(
        country_group_code=country_group_code,
        body=body,
        namespace=namespace,
    )
    return run_request(request)
