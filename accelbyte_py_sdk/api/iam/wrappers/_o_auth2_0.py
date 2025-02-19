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

from ..models import OauthapiRevocationList
from ..models import OauthcommonJWKSet
from ..models import OauthmodelErrorResponse
from ..models import OauthmodelTokenIntrospectResponse
from ..models import OauthmodelTokenResponse
from ..models import OauthmodelTokenResponseV3
from ..models import OauthmodelTokenThirdPartyResponse
from ..models import RestErrorResponse

from ..operations.o_auth2_0 import AuthCodeRequestV3
from ..operations.o_auth2_0 import AuthorizeV3
from ..operations.o_auth2_0 import GetJWKSV3
from ..operations.o_auth2_0 import GetRevocationListV3
from ..operations.o_auth2_0 import PlatformTokenGrantV3
from ..operations.o_auth2_0 import RetrieveUserThirdPartyPlatformTokenV3
from ..operations.o_auth2_0 import RevokeUserV3
from ..operations.o_auth2_0 import TokenGrantV3
from ..operations.o_auth2_0 import TokenIntrospectionV3
from ..operations.o_auth2_0 import TokenRevocationV3


@same_doc_as(AuthCodeRequestV3)
def auth_code_request_v3(platform_id: str, request_id: str, client_id: Optional[str] = None, redirect_uri: Optional[str] = None):
    request = AuthCodeRequestV3.create(
        platform_id=platform_id,
        request_id=request_id,
        client_id=client_id,
        redirect_uri=redirect_uri,
    )
    return run_request(request)


@same_doc_as(AuthorizeV3)
def authorize_v3(response_type: str, client_id: str, redirect_uri: Optional[str] = None, state: Optional[str] = None, scope: Optional[str] = None, code_challenge: Optional[str] = None, code_challenge_method: Optional[str] = None, target_auth_page: Optional[str] = None):
    request = AuthorizeV3.create(
        response_type=response_type,
        client_id=client_id,
        redirect_uri=redirect_uri,
        state=state,
        scope=scope,
        code_challenge=code_challenge,
        code_challenge_method=code_challenge_method,
        target_auth_page=target_auth_page,
    )
    return run_request(request)


@same_doc_as(GetJWKSV3)
def get_jwksv3():
    request = GetJWKSV3.create()
    return run_request(request)


@same_doc_as(GetRevocationListV3)
def get_revocation_list_v3():
    request = GetRevocationListV3.create()
    return run_request(request)


@same_doc_as(PlatformTokenGrantV3)
def platform_token_grant_v3(platform_id: str, platform_token: Optional[str] = None, client_id: Optional[str] = None, device_id: Optional[str] = None):
    request = PlatformTokenGrantV3.create(
        platform_id=platform_id,
        platform_token=platform_token,
        client_id=client_id,
        device_id=device_id,
    )
    return run_request(request)


@same_doc_as(RetrieveUserThirdPartyPlatformTokenV3)
def retrieve_user_third_party_platform_token_v3(user_id: str, platform_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = RetrieveUserThirdPartyPlatformTokenV3.create(
        user_id=user_id,
        platform_id=platform_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(RevokeUserV3)
def revoke_user_v3(user_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = RevokeUserV3.create(
        user_id=user_id,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(TokenGrantV3)
def token_grant_v3(grant_type: str, device_id: Optional[str] = None, code: Optional[str] = None, code_verifier: Optional[str] = None, client_id: Optional[str] = None, redirect_uri: Optional[str] = None, refresh_token: Optional[str] = None):
    request = TokenGrantV3.create(
        grant_type=grant_type,
        device_id=device_id,
        code=code,
        code_verifier=code_verifier,
        client_id=client_id,
        redirect_uri=redirect_uri,
        refresh_token=refresh_token,
    )
    return run_request(request)


@same_doc_as(TokenIntrospectionV3)
def token_introspection_v3(token: str):
    request = TokenIntrospectionV3.create(
        token=token,
    )
    return run_request(request)


@same_doc_as(TokenRevocationV3)
def token_revocation_v3(token: str):
    request = TokenRevocationV3.create(
        token=token,
    )
    return run_request(request)
