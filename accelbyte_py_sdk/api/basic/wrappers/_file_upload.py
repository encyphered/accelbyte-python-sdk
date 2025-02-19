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

from ..models import ErrorEntity
from ..models import FileUploadUrlInfo
from ..models import ValidationErrorEntity

from ..operations.file_upload import GeneratedUploadUrl
from ..operations.file_upload import GeneratedUserUploadContentUrl
from ..operations.file_upload import PublicGeneratedUploadUrl
from ..operations.file_upload import PublicGeneratedUserUploadContentUrl


@same_doc_as(GeneratedUploadUrl)
def generated_upload_url(folder: str, file_type: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GeneratedUploadUrl.create(
        folder=folder,
        file_type=file_type,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(GeneratedUserUploadContentUrl)
def generated_user_upload_content_url(user_id: str, file_type: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GeneratedUserUploadContentUrl.create(
        user_id=user_id,
        file_type=file_type,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicGeneratedUploadUrl)
def public_generated_upload_url(folder: str, file_type: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicGeneratedUploadUrl.create(
        folder=folder,
        file_type=file_type,
        namespace=namespace,
    )
    return run_request(request)


@same_doc_as(PublicGeneratedUserUploadContentUrl)
def public_generated_user_upload_content_url(user_id: str, file_type: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = PublicGeneratedUserUploadContentUrl.create(
        user_id=user_id,
        file_type=file_type,
        namespace=namespace,
    )
    return run_request(request)
