from src.db.swen344_db_utils import *
import secrets
import hashlib

def login(username, passwrd: str):
    hashed = hashlib.sha512(passwrd.encode('UTF-8')).hexdigest()
    session_key = secrets.token_hex(16)
    select = 'SELECT count(*) from users WHERE username=(%s) AND passwrd=(%s)'
    result = exec_get_one(select, (username, hashed))
    print(result)
    if result[0] == 1:
        sql = 'UPDATE users SET session_key=(%s) WHERE username=(%s) AND passwrd=(%s)'
        exec_commit(sql, (session_key, username, hashed,))
        return session_key
    return "Incorrect login info"

def logout(username):
    sql = 'UPDATE users SET session_key=NULL WHERE username=(%s)'
    result = exec_commit(sql, (username,))
    return result