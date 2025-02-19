import json
from abc import ABC, abstractmethod
from typing import Any, Tuple, Union

import requests

from ._header import Header
from ._http_response import HttpResponse
from ._operation import Operation


# NOTE(elmer): convert into a class if needed
Response = Tuple[int, str, Any]  # code, content-type, content


class HttpClient(ABC):

    @abstractmethod
    def create_request(
            self,
            operation: Operation,
            base_url: Union[None, str] = None,
            headers: Union[None, Header] = None,
            **kwargs
    ) -> Tuple[Any, Union[None, HttpResponse]]:
        pass

    @abstractmethod
    def send_request(
            self,
            request: Any,
            **kwargs
    ) -> Tuple[Any, Union[None, HttpResponse]]:
        pass

    @abstractmethod
    def handle_response(
            self,
            raw_response: Any,
            **kwargs
    ) -> Tuple[Union[None, Response], Union[None, HttpResponse]]:
        pass

    def run_request(
            self,
            operation: Operation,
            base_url: Union[None, str] = None,
            headers: Union[None, Header] = None,
            **kwargs
    ) -> Tuple[Union[None, Response], Union[None, HttpResponse]]:
        request, error = self.create_request(operation, base_url, headers, **kwargs)
        if error:
            return None, error

        raw_response, error = self.send_request(request, **kwargs)
        if error:
            return None, error

        response, error = self.handle_response(raw_response, **kwargs)
        if error:
            return None, error

        return response, None


# TODO(elmer): move to a separate file once it gets too big
class RequestsHttpClient(HttpClient):

    def __init__(self, allow_redirects: bool = True):
        self.allow_redirects = allow_redirects
        self.session = requests.Session()

    def create_request(
            self,
            operation: Operation,
            base_url: Union[None, str] = None,
            headers: Union[None, Header] = None,
            **kwargs
    ) -> Tuple[Any, Union[None, HttpResponse]]:
        if not operation.is_valid():
            raise Exception("Missing required values.")

        headers = headers if headers is not None else operation.get_headers()

        body_params = operation.get_body_params()
        form_data_params = operation.get_form_data_params()

        if body_params:
            files, data, json_ = None, json.dumps(body_params), None
        else:
            files, data, json_ = None, form_data_params, None

        prepared_request = requests.Request(
            method=operation.method,
            url=operation.get_full_url(base_url=base_url),
            headers=headers,
            files=files,
            data=data,
            json=json_,
        ).prepare()

        return prepared_request, None

    def send_request(
            self,
            request: Any,
            **kwargs
    ) -> Tuple[Any, Union[None, HttpResponse]]:
        if "allow_redirects" not in kwargs:
            kwargs["allow_redirects"] = self.allow_redirects
        raw_response = self.session.send(request, **kwargs)
        return raw_response, None

    def handle_response(
            self,
            raw_response: Any,
            **kwargs
    ) -> Tuple[Union[None, Response], Union[None, HttpResponse]]:
        status_code = raw_response.status_code

        if raw_response.is_redirect:
            content_type = "location"
            content = raw_response.headers["location"]
        elif raw_response.history:
            content_type = "location"
            content = None
            for history in raw_response.history:
                if "location" in history.headers:
                    status_code = history.status_code
                    content = history.headers["location"]
                    break
            if content is None:
                return None, HttpResponse.create_unhandled_error()
        elif "Content-Type" in raw_response.headers:
            content_type = raw_response.headers["Content-Type"]
            if content_type == "application/json":
                content = raw_response.json()
            elif content_type.startswith("text/"):
                content = raw_response.text
            else:
                return None, HttpResponse.create_unhandled_error()
        else:
            content_type = None
            content = None

        return (status_code, content_type, content), None
