#!/usr/bin/env python3
""" The authentcation module."""
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Hashing and encrypting the password"""
    encoded = password.encode('utf8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(encoded, salt)

from db import DB


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user():
        pass
