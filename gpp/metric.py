from datetime import datetime
from datetime import timezone
from typing import Any
from typing import Dict
from typing import Union

import gpp
from accelbyte_py_sdk.api.amalgam_game_telemetry import TelemetryBody
from accelbyte_py_sdk.api.amalgam_game_telemetry import \
    protected_save_events_game_telemetry_v1_protected_events_post_async as _send_protected_events
from accelbyte_py_sdk.api.iam import token_grant_v3_async
from accelbyte_py_sdk.core import get_access_token as _get_access_token


async def send_metric_async(
        event_name: str,
        payload: Dict[str, Any],
        event_id: str = None,
        event_timestamp: Union[str, float, datetime] = None,
):
    assert gpp.initialized(), 'SDK should be initialized first'

    access_token, _ = _get_access_token()
    if not gpp.valid_access_token(access_token):
        await token_grant_v3_async('client_credentials')

    if not event_timestamp:
        event_timestamp = _utc()
    elif isinstance(event_timestamp, datetime):
        event_timestamp = _utc(dt=event_timestamp)
    elif isinstance(event_timestamp, int) or isinstance(event_timestamp, float):
        event_timestamp = datetime.fromtimestamp(event_timestamp)
    telemetry = TelemetryBody.create(event_name, gpp.ns(), payload, event_id, event_timestamp)

    _, e = await _send_protected_events(telemetry)
    if e is None:
        return True
    return False


def _utc(dt: datetime = None):
    if not dt:
        dt = datetime.utcnow()
    else:
        dt = dt.astimezone(timezone.utc)
    return "%s:%sZ" % (
        dt.strftime('%Y-%m-%dT%H:%M'),
        ("%06.3f" % (dt.second + dt.microsecond / 1e6))
    )
