import time
from typing import Optional

import jwt

from accelbyte_py_sdk.core import MyConfigRepository as _DefaultConfigRepository
from accelbyte_py_sdk.core import EnvironmentConfigRepository as _EnvConfigRepository
from accelbyte_py_sdk.core import initialize as _initialize
from gpp.metric import send_metric_async as _send_metric_async

_INITIALIZED: bool = False
_NAMESPACE: Optional[str] = None
send_metric = _send_metric_async


def initialize(
        base_uri: str = None,
        client_id: str = None,
        client_secret: str = None,
        namespace: str = None,
):
    global _INITIALIZED, _NAMESPACE

    if base_uri and client_id and client_secret:
        config = _DefaultConfigRepository(base_uri, client_id, client_secret, namespace)
    else:
        config = _EnvConfigRepository()

    options = {
        'http': 'HttpxHttpClient',
        'config': config,
    }
    _initialize(options=options)
    _NAMESPACE = namespace
    _INITIALIZED = True


def initialized() -> bool:
    return _INITIALIZED


def ns() -> str:
    return _NAMESPACE


def valid_access_token(access_token):
    if not access_token:
        return False
    parsed = jwt.decode(access_token, options={"verify_signature": False})
    return int(time.time()) > parsed['exp']
