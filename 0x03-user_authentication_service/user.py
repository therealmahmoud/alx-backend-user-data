#!/usr/bin/env python3
""" User module."""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, column, String
import flask

Base = declarative_base()


class User(Base):
    """ Define the user class."""
    __tablename__ = 'users'
    id = column(Integer, primary_key=True)
    email = column(String, nullable=False)
    hashed_password = column(String, nullable=False)
    session_id = column(String, nullable=True)
    reset_token = column(String, nullable=True)
