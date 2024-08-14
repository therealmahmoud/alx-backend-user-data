#!/usr/bin/env python3
""" The authentcation module."""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """ Hashing and encrypting the password"""
    return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        if User.email == email:
            raise ValueError(f'User {email} already exists')
        _hash_password(password)
        user = self._db.add_user(email, password)
        return user
