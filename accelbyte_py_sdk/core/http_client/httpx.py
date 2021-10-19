from json import dumps as json_dumps
from typing import Any, Union

import httpx

from .._header import Header
from .._http_client import HttpClient
from .._http_client import Response
from .._operation import Operation


class HttpxHttpClient(HttpClient):
    def __init__(self, allow_redirects: bool = True):
        self.allow_redirects = allow_redirects
        self._client = httpx.AsyncClient()

    def create_request(self, operation: Operation, base_url: Union[None, str] = None,
                       headers: Union[None, Header] = None, **kwargs) -> Any:
        if not operation.is_valid():
            raise Exception("Missing required values.")

        headers = headers if headers is not None else operation.get_headers()

        body_params = operation.get_body_params()
        form_data_params = operation.get_form_data_params()

        if body_params:
            data, json = None, body_params
        else:
            data, json = form_data_params, None

        request = httpx.Request(
            method=operation.method,
            url=operation.get_full_url(base_url=base_url),
            headers=headers,
            data=data,
            json=json,
        )

        return request

    async def send_request(self, request: Any, **kwargs) -> Any:
        return await self._client.send(request)

    def handle_response(
            self, raw_response: Any, **kwargs
    ) -> Response:
        status_code = raw_response.status_code
        content_type = raw_response.headers.get('Content-Type')
        content = None

        if raw_response.is_redirect:
            content_type = "location"
            content = raw_response.headers["location"]
        elif raw_response.history:
            content_type = "location"
            history = next(filter(lambda h: "location" in h.headers, raw_response.history))
            if history:
                status_code = history.status_code
                content = history.headers["location"]
        elif content_type:
            if content_type == "application/json":
                content = raw_response.json()
            elif content_type.startswith("text/"):
                content = raw_response.text
        else:
            content = raw_response.content
        return status_code, content_type, content
