import urllib.parse

from typing import Any, Dict

from ._http_status_codes import HTTP_STATUS_CODES
from ._model import Model


class HttpResponse(Model):
    """HTTP Error

    Properties:

        code: (code) OPTIONAL int

        content_type: (content_type) OPTIONAL str

        content: (content) OPTIONAL Any
    """

    code: int
    content_type: str
    content: Any

    def __str__(self):
        return f"[{self.code}] {self.content_type}: {str(self.content)}"

    def is_error(self) -> bool:
        return self.content_type == "error"

    def get_query_params(self) -> dict:
        if self.content_type == "location":
            return urllib.parse.parse_qs(urllib.parse.urlparse(self.content).query)
        return {}

    @classmethod
    def create(cls, code: int, message: str):
        instance = cls()
        instance.code = code
        instance.content_type = "message"
        instance.content = message
        return instance

    @classmethod
    def create_error(cls, code: int, error: str):
        instance = cls()
        instance.code = code
        instance.content_type = "error"
        instance.content = error
        return instance

    @classmethod
    def create_redirect(cls, code: int, location: str):
        instance = cls()
        instance.code = code
        instance.content_type = "location"
        instance.content = location
        return instance

    @classmethod
    def create_unhandled_error(cls):
        instance = cls()
        instance.code = -1
        instance.content_type = "error"
        instance.content = "Unhandled Error"
        return instance

    @classmethod
    def try_create_undocumented_response(cls, code: int, content: Any):
        if code not in HTTP_STATUS_CODES:
            return False, None
        instance = cls()
        instance.code = code
        instance.content_type = "error"
        instance.content = content
        return True, instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "code": "code",
            "content_type": "content_type",
            "content": "content",
        }
