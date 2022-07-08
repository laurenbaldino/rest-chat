from flask_restful import Resource
from src.db.users_db import *
from flask import jsonify, request
import json
import hashlib
import requests

class Users(Resource):
    def get(self, user_id=None):
        if user_id is None:
            return jsonify(list_all_users())
        else:
            return jsonify(get_user_by_id(user_id))

    def post(self):
        json_data = request.get_json(force=True)
        try:
            data = create_new_user(
                json_data['email'],
                json_data['username'],
                hashlib.sha512(json_data['passwrd'].encode('UTF-8')).hexdigest(),
                json_data['created_on']
            )
            return data
        except psycopg2.errors.UniqueViolation:
            return "user already exists", 400

    def delete(self, user_id=None):
        if user_id:
            if get_user_by_id(user_id):
                data = delete_user(
                    user_id
                )
                return data
            else:
                return jsonify("No user found")
        else:
            return "Bad input", 200

    def put(self, user_id=None):
        if user_id:
            json_data = request.get_json(force=True)
            if get_user_by_id(user_id):
                data = edit_user_password(
                    json_data['passwrd'],
                    user_id
                )
                return data
            else:
                return "No user found"
        else:
            return "Bad input"