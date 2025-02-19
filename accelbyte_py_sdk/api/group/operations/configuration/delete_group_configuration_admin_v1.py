# Auto-generated at 2021-09-27T17:01:30.814833+08:00
# from: Justice Group Service (2.4.0)

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

from ...models import ModelsGetGroupConfigurationResponseV1
from ...models import ResponseErrorResponse


class DeleteGroupConfigurationAdminV1(Operation):
    """Delete group configuration (deleteGroupConfigurationAdminV1)

    Properties:
        url: /group/v1/admin/namespaces/{namespace}/configuration/{configurationCode}

        method: DELETE

        tags: Configuration

        consumes: []

        produces: ["application/json"]

        security: bearer

        namespace: (namespace) REQUIRED str in path

        configuration_code: (configurationCode) REQUIRED str in path

    Responses:
        201: Created - ModelsGetGroupConfigurationResponseV1 (Created)

        400: Bad Request - ResponseErrorResponse (errorCode: 20002 | errorMessage: validation error)

        401: Unauthorized - ResponseErrorResponse (errorCode: 20001 | errorMessage: unauthorized access)

        403: Forbidden - ResponseErrorResponse (errorCode: 20013 | errorMessage: insufficient permissions)

        404: Not Found - ResponseErrorResponse (errorCode: 73131 | errorMessage: global configuration not found)

        500: Internal Server Error - ResponseErrorResponse (Internal Server Error)
    """

    # region fields

    _url: str = "/group/v1/admin/namespaces/{namespace}/configuration/{configurationCode}"
    _method: str = "DELETE"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    namespace: str                                                                                 # REQUIRED in [path]
    configuration_code: str                                                                        # REQUIRED in [path]

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
            "configuration_code",
        ]

    # endregion get methods

    # region get_x_params methods

    def get_all_params(self) -> dict:
        return {
            "path": self.get_path_params(),
        }

    def get_path_params(self) -> dict:
        result = {}
        if hasattr(self, "namespace"):
            result["namespace"] = self.namespace
        if hasattr(self, "configuration_code"):
            result["configurationCode"] = self.configuration_code
        return result

    # endregion get_x_params methods

    # region is/has methods

    def is_valid(self) -> bool:
        if not hasattr(self, "namespace") or self.namespace is None:
            return False
        if not hasattr(self, "configuration_code") or self.configuration_code is None:
            return False
        return True

    # endregion is/has methods

    # region with_x methods

    def with_namespace(self, value: str) -> DeleteGroupConfigurationAdminV1:
        self.namespace = value
        return self

    def with_configuration_code(self, value: str) -> DeleteGroupConfigurationAdminV1:
        self.configuration_code = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "namespace") and self.namespace:
            result["namespace"] = str(self.namespace)
        elif include_empty:
            result["namespace"] = str()
        if hasattr(self, "configuration_code") and self.configuration_code:
            result["configurationCode"] = str(self.configuration_code)
        elif include_empty:
            result["configurationCode"] = str()
        return result

    # endregion to methods

    # region response methods

    # noinspection PyMethodMayBeStatic
    def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, ModelsGetGroupConfigurationResponseV1], Union[None, ResponseErrorResponse]]:
        """Parse the given response.

        201: Created - ModelsGetGroupConfigurationResponseV1 (Created)

        400: Bad Request - ResponseErrorResponse (errorCode: 20002 | errorMessage: validation error)

        401: Unauthorized - ResponseErrorResponse (errorCode: 20001 | errorMessage: unauthorized access)

        403: Forbidden - ResponseErrorResponse (errorCode: 20013 | errorMessage: insufficient permissions)

        404: Not Found - ResponseErrorResponse (errorCode: 73131 | errorMessage: global configuration not found)

        500: Internal Server Error - ResponseErrorResponse (Internal Server Error)
        """
        if code == 201:
            return ModelsGetGroupConfigurationResponseV1.create_from_dict(content), None
        if code == 400:
            return None, ResponseErrorResponse.create_from_dict(content)
        if code == 401:
            return None, ResponseErrorResponse.create_from_dict(content)
        if code == 403:
            return None, ResponseErrorResponse.create_from_dict(content)
        if code == 404:
            return None, ResponseErrorResponse.create_from_dict(content)
        if code == 500:
            return None, ResponseErrorResponse.create_from_dict(content)
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
        configuration_code: str,
    ) -> DeleteGroupConfigurationAdminV1:
        instance = cls()
        instance.namespace = namespace
        instance.configuration_code = configuration_code
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> DeleteGroupConfigurationAdminV1:
        instance = cls()
        if "namespace" in dict_ and dict_["namespace"] is not None:
            instance.namespace = str(dict_["namespace"])
        elif include_empty:
            instance.namespace = str()
        if "configurationCode" in dict_ and dict_["configurationCode"] is not None:
            instance.configuration_code = str(dict_["configurationCode"])
        elif include_empty:
            instance.configuration_code = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "namespace": "namespace",
            "configurationCode": "configuration_code",
        }

    # endregion static methods
