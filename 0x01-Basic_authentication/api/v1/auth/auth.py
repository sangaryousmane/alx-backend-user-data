#!/usr/bin/env python3
""" Handles the base authentication class
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Base authentication class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require authentication
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Handles authentication header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user
        """
        return None
