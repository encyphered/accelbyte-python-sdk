# Auto-generated at 2021-09-21T14:10:39.091329+08:00
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

from ...models import CreditRequest
from ...models import ErrorEntity
from ...models import ValidationErrorEntity


class CheckTransactionCreditLimit(Operation):
    """Check credit transaction limit (checkTransactionCreditLimit)

    Properties:
        url: /platform/admin/namespaces/{namespace}/users/{userId}/wallets/{currencyCode}/checkTransactionCreditLimit

        method: POST

        tags: Wallet

        consumes: ["application/json"]

        produces: ["application/json"]

        security: bearer

        body: (body) OPTIONAL CreditRequest in body

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

        currency_code: (currencyCode) REQUIRED str in path

    Responses:
        204: No Content - (check successfully and not limited)

        400: Bad Request - ErrorEntity (ErrorCode: 35121 | ErrorMessage: Transaction amount [{actualAmount}] exceed max amount [{maxAmount}] per day)

        409: Conflict - ErrorEntity (ErrorCode: 20006 | ErrorMessage: optimistic lock)

        422: Unprocessable Entity - ValidationErrorEntity (ErrorCode: 20002 | ErrorMessage: validation error)
    """

    # region fields

    _url: str = "/platform/admin/namespaces/{namespace}/users/{userId}/wallets/{currencyCode}/checkTransactionCreditLimit"
    _method: str = "POST"
    _consumes: List[str] = ["application/json"]
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    body: CreditRequest                                                                            # OPTIONAL in [body]
    namespace: str                                                                                 # REQUIRED in [path]
    user_id: str                                                                                   # REQUIRED in [path]
    currency_code: str                                                                             # REQUIRED in [path]

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
            "user_id",
            "currency_code",
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
        if hasattr(self, "user_id"):
            result["userId"] = self.user_id
        if hasattr(self, "currency_code"):
            result["currencyCode"] = self.currency_code
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "user_id") or self.user_id is None:
            return False
        if not hasattr(self, "currency_code") or self.currency_code is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_body(self, value: CreditRequest) -> CheckTransactionCreditLimit:
        self.body = value
        return self

    def with_namespace(self, value: str) -> CheckTransactionCreditLimit:
        self.namespace = value
        return self

    def with_user_id(self, value: str) -> CheckTransactionCreditLimit:
        self.user_id = value
        return self

    def with_currency_code(self, value: str) -> CheckTransactionCreditLimit:
        self.currency_code = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "body") and self.body:
            result["body"] = self.body.to_dict(include_empty=include_empty)
        elif include_empty:
            result["body"] = CreditRequest()
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "user_id") and self.user_id:
            result["userId"] = str(self.user_id)
        elif include_empty:
            result["userId"] = str()
        if hasattr(self, "currency_code") and self.currency_code:
            result["currencyCode"] = str(self.currency_code)
        elif include_empty:
            result["currencyCode"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, HttpResponse], Union[None, ErrorEntity, ValidationErrorEntity]]:
        """Parse the given response.

        204: No Content - (check successfully and not limited)

        400: Bad Request - ErrorEntity (ErrorCode: 35121 | ErrorMessage: Transaction amount [{actualAmount}] exceed max amount [{maxAmount}] per day)

        409: Conflict - ErrorEntity (ErrorCode: 20006 | ErrorMessage: optimistic lock)

        422: Unprocessable Entity - ValidationErrorEntity (ErrorCode: 20002 | ErrorMessage: validation error)
        """
        if code == 204:
            return HttpResponse.create(code, "No Content"), None
        if code == 400:
            return None, ErrorEntity.create_from_dict(content)
        if code == 409:
            return None, ErrorEntity.create_from_dict(content)
        if code == 422:
            return None, ValidationErrorEntity.create_from_dict(content)
        return None, HttpResponse.create_unhandled_error()

    # endregion response methods

    # region static methods

    @classmethod
    def create(
        cls,
        namespace: str,
        user_id: str,
        currency_code: str,
        body: Optional[CreditRequest] = None,
    ) -> CheckTransactionCreditLimit:
        instance = cls()
        instance.namespace = namespace
        instance.user_id = user_id
        instance.currency_code = currency_code
        if body is not None:
            instance.body = body
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> CheckTransactionCreditLimit:
        instance = cls()
        if "body" in dict_ and dict_["body"] is not None:
            instance.body = CreditRequest.create_from_dict(dict_["body"], include_empty=include_empty)
        elif include_empty:
            instance.body = CreditRequest()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "userId" in dict_ and dict_["userId"] is not None:
            instance.user_id = str(dict_["userId"])
        elif include_empty:
            instance.user_id = str()
        if "currencyCode" in dict_ and dict_["currencyCode"] is not None:
            instance.currency_code = str(dict_["currencyCode"])
        elif include_empty:
            instance.currency_code = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "body": "body",
            "namespace": "namespace",
            "userId": "user_id",
            "currencyCode": "currency_code",
        }

    # endregion static methods