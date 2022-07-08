from src.db.swen344_db_utils import *

def list_all_communities():
    sql = 'SELECT * FROM communities'
    result = exec_get_all(sql)
    return result

