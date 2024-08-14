#!/usr/bin/env python3
""" The authentcation module."""
import bcrypt
import base64

def _hash_password(password: str) -> bytes:
    """ Hashing and encrypting the password"""
    hashed_pass = bcrypt.hashpw(base64.b64encode(password), bcrypt.gensalt())
    return hashed_pass
