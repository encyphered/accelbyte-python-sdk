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

from ..models import OrderSyncResult

from ..operations.order_dedicated import SyncOrders


@same_doc_as(SyncOrders)
def sync_orders(start: str, end: str, next_evaluated_key: Optional[str] = None):
    request = SyncOrders.create(
        start=start,
        end=end,
        next_evaluated_key=next_evaluated_key,
    )
    return run_request(request)
