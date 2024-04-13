#!/usr/bin/env python3
"""
Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Returns an encoded password with salt
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Return True if the hashed passowrd matches the original
    one """
    encoded = password.encode()
    return True if bcrypt.checkpw(encoded, hashed_password) else False
