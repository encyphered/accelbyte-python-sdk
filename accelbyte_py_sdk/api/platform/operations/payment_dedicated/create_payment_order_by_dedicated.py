# Auto-generated at 2021-09-27T17:01:29.912701+08:00
# from: Justice Platform Service (3.24.0)

# Copyright (c) 2018 - 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

# pylint: disable=duplicate-code
# pylint: disable=line-too-long
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

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Union

from .....core import Operation
from .....core import HttpResponse

from ...models import ErrorEntity
from ...models import ExternalPaymentOrderCreate
from ...models import PaymentOrderCreateResult
from ...models import ValidationErrorEntity


class CreatePaymentOrderByDedicated(Operation):
    """Create payment order by dedicated server (createPaymentOrderByDedicated)

    Properties:
        url: /platform/admin/namespaces/{namespace}/payment/orders

        method: POST

        tags: Payment(Dedicated)

        consumes: ["application/json"]

        produces: ["application/json"]

        security: bearer

        body: (body) OPTIONAL ExternalPaymentOrderCreate in body

        namespace: (namespace) REQUIRED str in path

    Responses:
        201: Created - PaymentOrderCreateResult (successful operation)

        400: Bad Request - ErrorEntity (ErrorCode: 33121 | ErrorMessage: Recurring payment failed with code: [{errorCode}] and message: [{errorMessage}])

        403: Forbidden - ErrorEntity (ErrorCode: 20016 | ErrorMessage: action is banned)

        404: Not Found - ErrorEntity (ErrorCode: 36141 | ErrorMessage: Currency [{currencyCode}] does not exist in namespace [{namespace}])

        409: Conflict - ErrorEntity (ErrorCode: 20006 | ErrorMessage: optimistic lock)

        422: Unprocessable Entity - ValidationErrorEntity (ErrorCode: 20002 | ErrorMessage: validation error)
    """

    # region fields

    _url: str = "/platform/admin/namespaces/{namespace}/payment/orders"
    _method: str = "POST"
    _consumes: List[str] = ["application/json"]
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    body: ExternalPaymentOrderCreate                                                               # OPTIONAL in [body]
    namespace: str                                                                                 # REQUIRED in [path]

    # endregion fields

    # region properties

    @property
    def url(self) -> str:
        return self._url

    @property
    def method(self) -> str:
        return self._method

    @property
    def consumes(self) -> List[str]:
        return self._consumes

    @property
    def produces(self) -> List[str]:
        return self._produces

    @property
    def security(self) -> Optional[str]:
        return self._security

    @property
    def location_query(self) -> str:
        return self._location_query

    # endregion properties

    # region get methods

    def get_full_url(self, base_url: Union[None, str] = None) -> str:
        result = base_url if base_url is not None else ""

        # path params
        url = self.url
        for k, v in self.get_path_params().items():
            url = url.replace(f"{{{k}}}", v)
        result += url

        return result

    # noinspection PyMethodMayBeStatic
    def get_all_required_fields(self) -> List[str]:
        return [
            "namespace",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "body": self.get_body_params(),
            "path": self.get_path_params(),
        }

    def get_body_params(self) -> Any:
        return self.body.to_dict()

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_body(self, value: ExternalPaymentOrderCreate) -> CreatePaymentOrderByDedicated:
        self.body = value
        return self

    def with_namespace(self, value: str) -> CreatePaymentOrderByDedicated:
        self.namespace = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "body") and self.body:
            result["body"] = self.body.to_dict(include_empty=include_empty)
        elif include_empty:
            result["body"] = ExternalPaymentOrderCreate()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, PaymentOrderCreateResult], Union[None, ErrorEntity, ValidationErrorEntity]]:
        """Parse the given response.

        201: Created - PaymentOrderCreateResult (successful operation)

        400: Bad Request - ErrorEntity (ErrorCode: 33121 | ErrorMessage: Recurring payment failed with code: [{errorCode}] and message: [{errorMessage}])

        403: Forbidden - ErrorEntity (ErrorCode: 20016 | ErrorMessage: action is banned)

        404: Not Found - ErrorEntity (ErrorCode: 36141 | ErrorMessage: Currency [{currencyCode}] does not exist in namespace [{namespace}])

        409: Conflict - ErrorEntity (ErrorCode: 20006 | ErrorMessage: optimistic lock)

        422: Unprocessable Entity - ValidationErrorEntity (ErrorCode: 20002 | ErrorMessage: validation error)
        """
        if code == 201:
            return PaymentOrderCreateResult.create_from_dict(content), None
        if code == 400:
            return None, ErrorEntity.create_from_dict(content)
        if code == 403:
            return None, ErrorEntity.create_from_dict(content)
        if code == 404:
            return None, ErrorEntity.create_from_dict(content)
        if code == 409:
            return None, ErrorEntity.create_from_dict(content)
        if code == 422:
            return None, ValidationErrorEntity.create_from_dict(content)
        was_handled, undocumented_response = HttpResponse.try_create_undocumented_response(code, content)
        if was_handled:
            return None, undocumented_response
        return None, HttpResponse.create_unhandled_error()

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        namespace: str,
        body: Optional[ExternalPaymentOrderCreate] = None,
    ) -> CreatePaymentOrderByDedicated:
        instance = cls()
        instance.namespace = namespace
        if body is not None:
            instance.body = body
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> CreatePaymentOrderByDedicated:
        instance = cls()
        if "body" in dict_ and dict_["body"] is not None:
            instance.body = ExternalPaymentOrderCreate.create_from_dict(dict_["body"], include_empty=include_empty)
        elif include_empty:
            instance.body = ExternalPaymentOrderCreate()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "body": "body",
            "namespace": "namespace",
        }

    # endregion static methods
