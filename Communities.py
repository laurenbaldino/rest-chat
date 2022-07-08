from flask_restful import Resource
from src.db.communities_db import *
from flask import jsonify

class Communities(Resource):
    def get(self):
        return jsonify(list_all_communities())