#!/usr/bin/env python3
""" The authentcation module."""
import bcrypt
import base64


def _hash_password(password: str) -> bytes:
    """ Hashing and encrypting the password"""
    encoded = password.encode('utf8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(encoded, salt)
