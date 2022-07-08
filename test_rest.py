import unittest
from tests.test_utils import *
from src.db.db import rebuild_tables
from src.db.users_db import *


class TestRest(unittest.TestCase):

    def setUp(self):
        rebuild_tables()

    def test_list_all_users(self):
        result = get_rest_call(self, 'http://localhost:5000/users')
        self.assertEqual(7, len(result))

    def test_list_all_communities(self):
        result = get_rest_call(self, 'http://localhost:5000/communities')
        self.assertEqual(2, len(result))

    def test_list_all_channels(self):
        result = get_rest_call(self, 'http://localhost:5000/channels')
        self.assertEqual(4, len(result))

    def test_list_all_channel_messages(self):
        result = get_rest_call(self, 'http://localhost:5000/channels/1')
        self.assertEqual([], result)

    def test_create_user(self):
       params = dict(username='Lauren', email='lauren@gmail.com', passwrd='password123', created_on= '2022-03-15')
       result = post_rest_call(self, 'http://localhost:5000/users', params)
       users = get_rest_call(self, 'http://localhost:5000/users')
       self.assertEqual(8, len(users))

    def test_delete_user(self):
        result = delete_rest_call(self,'http://localhost:5000/users/7')
        users = get_rest_call(self, 'http://localhost:5000/users/7')
        self.assertEqual(None, users)
        
    def test_edit_user_password(self):
        params = dict(passwrd='newpassword!')
        put_rest_call(self, 'http://localhost:5000/users/3', params)
        result = get_rest_call(self, 'http://localhost:5000/users/3')
        self.assertEqual('newpassword!', result[3])

    # def test_login(self):
    
    # def test_create_dm(self):
    #     params = dict(sender_id=1, reciever_id=2, message="test message")
    #     result = post_rest_call(self, 'http://localhost:5000/messages', params)
    #     messages = get_rest_call(self, 'http://localhost:5000/messages/1')
    #     self.assertEqual(3, len(messages))
