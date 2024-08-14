#!/usr/bin/env python3
""" The authentcation module."""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """ Hashing and encrypting the password"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _uuid() -> str:
    """ Generate a unique id."""
    unique = str(uuid4)
    return unique


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initializes a new Auth instance.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Register a new user."""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """Credentials validation."""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        if bcrypt.checkpw(password.encode("utf-8"),
                          _hash_password(password)) is True:
            return True
        else:
            return False
