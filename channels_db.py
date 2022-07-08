from src.db.swen344_db_utils import *

def list_all_channels():
    sql = 'SELECT * FROM channels'
    result = exec_get_all(sql)
    return result

def list_all_channel_messages(channel_id):
    sql = 'SELECT * FROM channel_messages WHERE channel_id = (%s)'
    result = exec_get_all(sql, (channel_id,))
    return result

