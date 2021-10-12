from abc import ABC, abstractmethod
from typing import Any, Tuple, Union

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
