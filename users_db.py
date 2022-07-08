from src.db.swen344_db_utils import *
import datetime

def list_all_users():
    sql = 'SELECT * from users'
    result = exec_get_all(sql)
    return result

def get_user_by_id(user_id):
    sql = 'SELECT * from users where user_id=(%s)'
    result = exec_get_one(sql, (user_id,))
    return result

def get_user_by_username(username):
    sql = 'SELECT * from users where username=(%s)'
    result = exec_get_one(sql, (username,))
    return result

def create_new_user(email, username, passwrd, created_on):
    sql = 'INSERT INTO users (email, username, passwrd, created_on, changed_on, change_end) VALUES (%s, %s, %s, %s, NULL, NULL)'
    result = exec_commit(sql, (email, username, passwrd, created_on,))
    return result

def edit_user_password(passwrd, user_id):
    sql = 'UPDATE users SET passwrd=(%s) WHERE user_id=(%s)'
    result = exec_commit(sql, (passwrd, user_id,))
    return result

def delete_user(user_id):
    sql = 'DELETE FROM users WHERE user_id =(%s)'
    result = exec_commit(sql, (user_id,))
    return result
