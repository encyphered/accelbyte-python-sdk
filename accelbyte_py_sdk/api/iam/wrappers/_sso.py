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

from ..models import RestErrorResponse

from ..operations.sso import LoginSSOClient
from ..operations.sso import LogoutSSOClient


@same_doc_as(LoginSSOClient)
def login_sso_client(platform_id: str, payload: Optional[str] = None):
    request = LoginSSOClient.create(
        platform_id=platform_id,
        payload=payload,
    )
    return run_request(request)


@same_doc_as(LogoutSSOClient)
def logout_sso_client(platform_id: str):
    request = LogoutSSOClient.create(
        platform_id=platform_id,
    )
    return run_request(request)
