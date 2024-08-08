#!/usr/bin/env python3
""" Module of Session_auth. """
from .auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """SessionAuth class."""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a Session ID for a user_id. """
        if not user_id or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Retrieves the user id of the user"""
        if type(session_id) is str:
            return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Retrieves the user associated with the request."""
        self.session_cookie(request)
        self.user_id_for_session_id(self.user_id_by_session_id)
        return User.get(User.load_from_file())
