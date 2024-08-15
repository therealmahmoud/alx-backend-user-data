#!/usr/bin/env python3
""" The authentcation module."""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User
from uuid import uuid4
from typing import Union


def _hash_password(password: str) -> bytes:
    """ Hashing and encrypting the password"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ Generate a unique id."""
    return str(uuid4())


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
        user = None
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                return bcrypt.checkpw(
                    password.encode("utf-8"),
                    user.hashed_password,
                )
        except NoResultFound:
            return False
        return False

    def create_session(self, email: str) -> str:
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id) -> Union[User, None]:
        """ Finding user by session id."""
        user = None
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return user

    def destroy_session(self, user_id) -> None:
        """ Updates the corresponding user’s session ID to None."""
        if not user_id:
            return None
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email) -> str:
        """Generate reset password token."""
        user = self._db.find_user_by(email=email)
        if not user:
            raise ValueError()
        user_id = _generate_uuid()
        self._db.update_user(user.id, reset_token=user_id)
        return user_id
