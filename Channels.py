from flask_restful import Resource
from src.db.channels_db import *
from flask import jsonify

class Channels(Resource):
    
    def get(self, channel_id=None):
        if channel_id != None:
            return jsonify(list_all_channel_messages(channel_id))
        return jsonify(list_all_channels())
    
