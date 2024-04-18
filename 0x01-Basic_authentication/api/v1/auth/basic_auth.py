#!/usr/bin/env python3
"""
Basic authentication inheriting from the main Auth class
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic authentication Base class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Extract base 64 authorization header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startwith("Basic "):
            return None
        return authorization_header[6:]
