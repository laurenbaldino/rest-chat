from src.db.swen344_db_utils import *
import datetime

def get_all_messages():
    sql = 'SELECT * FROM MESSAGES'
    result = exec_get_all(sql)
    return result

def get_direct_messages(sender_id):
    sql = 'SELECT * FROM messages WHERE sender_id = (%s)'
    result = exec_get_all(sql, (sender_id,))
    return result

def create_new_message(sender_id, reciever_id, message, sent_on):
    sql = 'INSERT INTO messages(sender_id, reciever_id, message,sent_on, is_read) VALUES (%s, %s, %s, %s, FALSE)'
    result = exec_commit(sql ,(sender_id, reciever_id, message, sent_on))
    return result