from flask_restful import Resource
from src.db.messages_db import *
from flask import jsonify, request
import requests
import datetime
from src.api import check_auth

class Messages(Resource):

    def get(self, sender_id=None):
        if sender_id != None:
            return jsonify(get_direct_messages(sender_id))
        return jsonify(get_all_messages())
    
    def post(self):
        if check_auth(request.headers.get('Authorization')):
            json_data = request.get_json(force=True)
            data = create_new_message(
                json_data['sender_id'],
                json_data['reciever_id'],
                json_data['message'],
                datetime.datetime.now()
            )
            return data
        else:
            return "Not authed", 401
    
