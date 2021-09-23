# AccelByte Python SDK

## Installation

```sh
pip install git+ssh://git@bitbucket.org/accelbyte/justice-codegen-sdk.git@feature/JSC-158-python-3.9-sdk-poc#egg=accelbyte_py_sdk&subdirectory=accelbyte-py-sdk
```

## Usage

## Initializing

You'll have to initialize the SDK using the `initialize()` function.

```python
import accelbyte_py_sdk

accelbyte_py_sdk.initialize()
```

you could also pass in options like so:

```python
import accelbyte_py_sdk

from accelbyte_py_sdk.core import MyConfigRepository

my_config_repository = MyConfigRepository(
    base_url=environ["ACB_DEV_BASE_URL"],
    client_id=environ["ACB_DEV_CLIENT_ID"],
    client_secret=environ["ACB_DEV_CLIENT_SECRET"],
    namespace=environ["ACB_DEV_PRODUCT_NAMESPACE"],
)
options = {
    "config": my_config_repository
}
accelbyte_py_sdk.initialize(options)

# you could still set some of these options after initializing.
# ex. accelbyte_py_sdk.core.set_config_repository(my_config_repository)
```

## Calling functions

All* functions follow the return value format of `result, error`.

```python
from os import environ

import accelbyte_py_sdk
from accelbyte_py_sdk.services.auth import login, logout

if __name__ == "__main__":
    accelbyte_py_sdk.initialize()

    username = environ["ACB_DEV_ADMIN_USERNAME"]
    password = environ["ACB_DEV_ADMIN_PASSWORD"]

    _, error = login(username, password)
    assert error is None

    _, error = logout()
    assert error is None

```

here `login(username, password)` and `logout()` are wrapper functions.

```python
import accelbyte_py_sdk
from accelbyte_py_sdk.api.iam import token_grant_v3

if __name__ == "__main__":
    accelbyte_py_sdk.initialize()

    token, error = token_grant_v3(
        grant_type="client_credentials"
    )
    assert error is not None
```

you could also write your own wrapper functions
by using the generated models and operations in `accelbyte_py_sdk.api.<service-name>`.

## Generated code

### Models

Each definition in `#/definitions/` is turned into a Model.


Example:

```yaml
---
UserProfileInfo:
  type: object
  properties:
    userId:
      type: string
    namespace:
      type: string
    firstName:
      type: string
    lastName:
      type: string
    avatarSmallUrl:
      type: string
    avatarUrl:
      type: string
    avatarLargeUrl:
      type: string
    status:
      type: string
      enum:
      - ACTIVE
      - INACTIVE
    language:
      type: string
    timeZone:
      type: string
    dateOfBirth:
      type: string
      format: date
    customAttributes:
      type: object
      additionalProperties:
        type: object
    zipCode:
      type: string
```

```python
# accelbyte_py_sdk/api/basic/models/user_profile_info.py

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Union

from ....core import Model


class UserProfileInfo(Model):
    """User profile info

    Properties:
        user_id: (userId) OPTIONAL str

        namespace: (namespace) OPTIONAL str

        first_name: (firstName) OPTIONAL str

        last_name: (lastName) OPTIONAL str

        avatar_small_url: (avatarSmallUrl) OPTIONAL str

        avatar_url: (avatarUrl) OPTIONAL str

        avatar_large_url: (avatarLargeUrl) OPTIONAL str

        status: (status) OPTIONAL str

        language: (language) OPTIONAL str

        time_zone: (timeZone) OPTIONAL str

        date_of_birth: (dateOfBirth) OPTIONAL str

        custom_attributes: (customAttributes) OPTIONAL Dict[str, Any]

        zip_code: (zipCode) OPTIONAL str
    """

    # region fields

    user_id: str                                                                                   # OPTIONAL
    namespace: str                                                                                 # OPTIONAL
    first_name: str                                                                                # OPTIONAL
    last_name: str                                                                                 # OPTIONAL
    avatar_small_url: str                                                                          # OPTIONAL
    avatar_url: str                                                                                # OPTIONAL
    avatar_large_url: str                                                                          # OPTIONAL
    status: str                                                                                    # OPTIONAL
    language: str                                                                                  # OPTIONAL
    time_zone: str                                                                                 # OPTIONAL
    date_of_birth: str                                                                             # OPTIONAL
    custom_attributes: Dict[str, Any]                                                              # OPTIONAL
    zip_code: str                                                                                  # OPTIONAL

    # endregion fields
```

there are also a number of utility functions generated with each model that should help in the ease of use.

```python
# accelbyte_py_sdk/api/basic/models/user_profile_info.py

def with_user_id(self, value: str) -> UserProfileInfo:
    self.user_id = value
    return self

# other with_x() methods too

def to_dict(self, include_empty: bool = False) -> dict:
    return  # ...

@classmethod
def create(
    cls,
    # ...,
) -> UserProfileInfo:
    return  # ...

@classmethod
def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> UserProfileInfo:
    return  # ...

@staticmethod
def get_field_info() -> Dict[str, str]:
    return  # ...
```

### Operations

Each path item in `#/paths` is turned into an Operation.


Example:

```yaml
---
"/v1/public/namespaces/{namespace}/users/{userId}/profiles":
  get:
    tags:
    - UserProfile
    summary: Get user profile
    description: 'Get user profile.<br>Other detail info: <ul><li><i>Required permission</i>:
      resource=<b>"NAMESPACE:{namespace}:USER:{userId}:PROFILE"</b>, action=2 <b>(READ)</b></li><li><i>Action
      code</i>: 11403</li><li><i>Returns</i>: user profile</li></ul>'
    operationId: publicGetUserProfileInfo
    produces:
    - application/json
    parameters:
    - name: namespace
      in: path
      description: namespace, only accept alphabet and numeric
      required: true
      type: string
    - name: userId
      in: path
      description: user's id, should follow UUID version 4 without hyphen
      required: true
      type: string
    responses:
      '200':
        description: Successful operation
        schema:
          "$ref": "#/definitions/UserProfileInfo"
      '400':
        description: "<table><tr><td>errorCode</td><td>errorMessage</td></tr><tr><td>20002</td><td>validation
          error</td></tr></table>"
        schema:
          "$ref": "#/definitions/ValidationErrorEntity"
      '401':
        description: "<table><tr><td>errorCode</td><td>errorMessage</td></tr><tr><td>20001</td><td>unauthorized</td></tr></table>"
        schema:
          "$ref": "#/definitions/ErrorEntity"
      '403':
        description: "<table><tr><td>errorCode</td><td>errorMessage</td></tr><tr><td>20013</td><td>insufficient
          permission</td></tr></table>"
        schema:
          "$ref": "#/definitions/ErrorEntity"
      '404':
        description: "<table><tr><td>errorCode</td><td>errorMessage</td></tr><tr><td>11440</td><td>user
          profile not found</td></tr></table>"
        schema:
          "$ref": "#/definitions/ErrorEntity"
    security:
    - authorization: []
    x-authorization:
      resource: NAMESPACE:{namespace}:USER:{userId}:PROFILE
      action: '2'
```

```python
# accelbyte_py_sdk/api/basic/operations/user_profile/get_user_profile_info.py

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Union

from .....core import Operation
from .....core import HttpResponse

from ...models import ErrorEntity
from ...models import UserProfilePrivateInfo
from ...models import ValidationErrorEntity


class GetUserProfileInfo(Operation):
    """Get user profile (getUserProfileInfo)

    Properties:
        url: /basic/v1/admin/namespaces/{namespace}/users/{userId}/profiles

        method: GET

        tags: UserProfile

        consumes: []

        produces: ["application/json"]

        security: bearer

        namespace: (namespace) REQUIRED str in path

        user_id: (userId) REQUIRED str in path

    Responses:
        200: OK - UserProfilePrivateInfo (successful operation)

        400: Bad Request - ValidationErrorEntity (errorCode: 20002 | errorMessage: validation error)

        401: Unauthorized - ErrorEntity (errorCode: 20001 | errorMessage: unauthorized)

        403: Forbidden - ErrorEntity (errorCode: 20013 | errorMessage: insufficient permission)

        404: Not Found - ErrorEntity (errorCode: 11440 | errorMessage: user profile not found)
    """

    # region fields

    _url: str = "/basic/v1/admin/namespaces/{namespace}/users/{userId}/profiles"
    _method: str = "GET"
    _consumes: List[str] = []
    _produces: List[str] = ["application/json"]
    _security: Optional[str] = "bearer"
    _location_query: str = None

    namespace: str                                                                                 # REQUIRED in [path]
    user_id: str                                                                                   # REQUIRED in [path]

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
```

same with the models there are also a number of utility functions generated with each operation that should help in the ease of use.

```python
# accelbyte_py_sdk/api/basic/operations/user_profile/get_user_profile_info.py

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
    ]

def get_all_params(self) -> dict:
    return  # ...

def get_path_params(self) -> dict:
    return  # ...

# there would also be: get_body_params(), get_form_data_params(), get_header_params, get_query_params() too if the operation has those.

def is_valid(self) -> bool:
    if not hasattr(self, "namespace") or self.namespace is None:
        return False
    if not hasattr(self, "user_id") or self.user_id is None:
        return False
    return True

def with_namespace(self, value: str) -> GetUserProfileInfo:
    self.namespace = value
    return self

# other with_x() methods too

def to_dict(self, include_empty: bool = False) -> dict:
    return  # ...

# noinspection PyMethodMayBeStatic
def parse_response(self, code: int, content_type: str, content: Any) -> Tuple[Union[None, UserProfilePrivateInfo], Union[None, ErrorEntity, ValidationErrorEntity]]:
    """Parse the given response.

    200: OK - UserProfilePrivateInfo (successful operation)

    400: Bad Request - ValidationErrorEntity (errorCode: 20002 | errorMessage: validation error)

    401: Unauthorized - ErrorEntity (errorCode: 20001 | errorMessage: unauthorized)

    403: Forbidden - ErrorEntity (errorCode: 20013 | errorMessage: insufficient permission)

    404: Not Found - ErrorEntity (errorCode: 11440 | errorMessage: user profile not found)
    """
    if code == 200:
        return UserProfilePrivateInfo.create_from_dict(content), None
    if code == 400:
        return None, ValidationErrorEntity.create_from_dict(content)
    if code == 401:
        return None, ErrorEntity.create_from_dict(content)
    if code == 403:
        return None, ErrorEntity.create_from_dict(content)
    if code == 404:
        return None, ErrorEntity.create_from_dict(content)
    return None, HttpResponse.create_unhandled_error()

# the return value of parse_response follows the format Tuple[Union[None, all successful return codes], Union[None, all failure return codes]]

@classmethod
def create(
    cls,
    # ...,
) -> UserProfileInfo:
    return  # ...

@classmethod
def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> UserProfileInfo:
    return  # ...

@staticmethod
def get_field_info() -> Dict[str, str]:
    return  # ...
```

### Creating

:bulb: there are 4 ways to create an instance of these models and operations.

```python
# 1. using the python __init__() function then setting the parameters manually:
model = ModelName()
model.param_a = "foo"
model.param_b = "bar"

# 2. using the python __init__() function together with the 'with_x' methods:
# # the 'with_x' functions are type annotated and will show warnings if a wrong type is passed.
model = ModelName() \
    .with_param_a("foo") \
    .with_param_b("bar")

# 3. using the ModelName.create(..) class method:
# # parameters here are also type annotated and will throw a TypeError if a required field was not filled out.
model = ModelName.create(
    param_a="foo",
    param_b="bar",
)

# 4. using the ModelName.create_from_dict(..) class method:
# # this method also has a 'include_empty' option that would get ignore values that evaluate to False, None, or len() == 0.
model_params = {
    "param_a": "foo",
    "param_b": "bar",
    "param_c": False,
    "param_d": None,
    "param_e": [],
    "param_f": {},
}
model = ModelName.create_from_dict(model_params)

# all of these apply to all operations too.
```

### Wrappers

To improve ergonomics the code generator also generates wrappers around the operations.
The purpose of these wrappers is to automatically fill up parameters that the SDK already knows.
(e.g. namespace, client_id, access_token, etc.)

They are located at `accelbyte_py_sdk.api.<service-name>.wrappers` but can be accessed like so:

```python
import accelbyte_py_sdk
from accelbyte_py_sdk.api.iam import token_grant_v3

if __name__ == "__main__":
    accelbyte_py_sdk.initialize()

    token, error = token_grant_v3(
        grant_type="client_credentials"
    )
    assert error is not None
```

The wrapper function `token_grant_v3` is a wrapper for the `TokenGrantV3` operation.
It automatically passes in the information needed like the Basic Auth Headers.
The values are gotten from the current `ConfigRepository`.

continuing from the previous examples, would be:

```python
# accelbyte_py_sdk/api/basic/wrappers/_user_profile.py

from typing import Any, Dict, List, Optional, Tuple, Union

from ....core import get_namespace as get_services_namespace
from ....core import run_request
from ....core import same_doc_as

from ..operations.user_profile import GetUserProfileInfo


@same_doc_as(GetUserProfileInfo)
def get_user_profile_info(user_id: str, namespace: Optional[str] = None):
    if namespace is None:
        namespace, error = get_services_namespace()
        if error:
            return None, error
    request = GetUserProfileInfo.create(
        user_id=user_id,
        namespace=namespace,
    )
    return run_request(request)
```

this wrapper function automatically fills up the required path parameter `namespace`.

now to use it only the `user_id` is now required.

```python
import accelbyte_py_sdk
from accelbyte_py_sdk.api.basic import get_user_profile_info

if __name__ == "__main__":
    accelbyte_py_sdk.initialize()

    user_profile_info, error = get_user_profile_info(user_id="lorem")
    assert error is not None

    print(f"Hello there {user_profile_info.first_name}!")
```