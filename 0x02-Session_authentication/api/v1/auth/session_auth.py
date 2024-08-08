#!/usr/bin/env python3
""" Module of Session_auth. """
from .auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """SessionAuth class."""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a Session ID for a user_id. """
        if not user_id or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id = {session_id: user_id}
        return session_id
