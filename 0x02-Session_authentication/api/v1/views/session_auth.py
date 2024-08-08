#!/usr/bin/env python3
from api.v1.views import app_views
from flask import request, jsonify
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['post'], strict_slashes=False)
def retrieve_email_pwd() -> str:
    """ Retrieve email and password of user"""
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400
    pwd = request.form.get('pwd')
    if not pwd:
        return jsonify({"error": "password missing"}), 400
    user = User.search({'email': email})
    if len(user) <= 0:
        return jsonify({"error": "no user found for this email"}), 404
    if user[0].is_valid_password(pwd):
        from api.v1.app import auth
        sessiond_id = auth.create_session(getattr(user[0], 'id'))
        res = jsonify(user[0].to_json())
        res.set_cookie(os.getenv("SESSION_NAME"), sessiond_id)
        return res
    return jsonify({"error": "wrong password"}), 401
