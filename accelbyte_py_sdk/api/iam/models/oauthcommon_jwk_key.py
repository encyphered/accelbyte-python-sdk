# Auto-generated at 2021-09-27T17:12:31.694558+08:00
# from: Justice Iam Service (4.1.0)

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

from ....core import Model


class OauthcommonJWKKey(Model):
    """Oauthcommon JWK key

    Properties:
        alg: (alg) OPTIONAL str

        e: (e) OPTIONAL str

        kid: (kid) OPTIONAL str

        kty: (kty) REQUIRED str

        n: (n) OPTIONAL str

        use: (use) OPTIONAL str
    """

    # region fields

    alg: str                                                                                       # OPTIONAL
    e: str                                                                                         # OPTIONAL
    kid: str                                                                                       # OPTIONAL
    kty: str                                                                                       # REQUIRED
    n: str                                                                                         # OPTIONAL
    use: str                                                                                       # OPTIONAL

    # endregion fields

    # region with_x methods

    def with_alg(self, value: str) -> OauthcommonJWKKey:
        self.alg = value
        return self

    def with_e(self, value: str) -> OauthcommonJWKKey:
        self.e = value
        return self

    def with_kid(self, value: str) -> OauthcommonJWKKey:
        self.kid = value
        return self

    def with_kty(self, value: str) -> OauthcommonJWKKey:
        self.kty = value
        return self

    def with_n(self, value: str) -> OauthcommonJWKKey:
        self.n = value
        return self

    def with_use(self, value: str) -> OauthcommonJWKKey:
        self.use = value
        return self

    # endregion with_x methods

    # region to methods

    def to_dict(self, include_empty: bool = False) -> dict:
        result = {}
        if hasattr(self, "alg") and self.alg:
            result["alg"] = str(self.alg)
        elif include_empty:
            result["alg"] = str()
        if hasattr(self, "e") and self.e:
            result["e"] = str(self.e)
        elif include_empty:
            result["e"] = str()
        if hasattr(self, "kid") and self.kid:
            result["kid"] = str(self.kid)
        elif include_empty:
            result["kid"] = str()
        if hasattr(self, "kty") and self.kty:
            result["kty"] = str(self.kty)
        elif include_empty:
            result["kty"] = str()
        if hasattr(self, "n") and self.n:
            result["n"] = str(self.n)
        elif include_empty:
            result["n"] = str()
        if hasattr(self, "use") and self.use:
            result["use"] = str(self.use)
        elif include_empty:
            result["use"] = str()
        return result

    # endregion to methods

    # region static methods

    @classmethod
    def create(
        cls,
        kty: str,
        alg: Optional[str] = None,
        e: Optional[str] = None,
        kid: Optional[str] = None,
        n: Optional[str] = None,
        use: Optional[str] = None,
    ) -> OauthcommonJWKKey:
        instance = cls()
        instance.kty = kty
        if alg is not None:
            instance.alg = alg
        if e is not None:
            instance.e = e
        if kid is not None:
            instance.kid = kid
        if n is not None:
            instance.n = n
        if use is not None:
            instance.use = use
        return instance

    @classmethod
    def create_from_dict(cls, dict_: dict, include_empty: bool = False) -> OauthcommonJWKKey:
        instance = cls()
        if not dict_:
            return instance
        if "alg" in dict_ and dict_["alg"] is not None:
            instance.alg = str(dict_["alg"])
        elif include_empty:
            instance.alg = str()
        if "e" in dict_ and dict_["e"] is not None:
            instance.e = str(dict_["e"])
        elif include_empty:
            instance.e = str()
        if "kid" in dict_ and dict_["kid"] is not None:
            instance.kid = str(dict_["kid"])
        elif include_empty:
            instance.kid = str()
        if "kty" in dict_ and dict_["kty"] is not None:
            instance.kty = str(dict_["kty"])
        elif include_empty:
            instance.kty = str()
        if "n" in dict_ and dict_["n"] is not None:
            instance.n = str(dict_["n"])
        elif include_empty:
            instance.n = str()
        if "use" in dict_ and dict_["use"] is not None:
            instance.use = str(dict_["use"])
        elif include_empty:
            instance.use = str()
        return instance

    @staticmethod
    def get_field_info() -> Dict[str, str]:
        return {
            "alg": "alg",
            "e": "e",
            "kid": "kid",
            "kty": "kty",
            "n": "n",
            "use": "use",
        }

    # endregion static methods
