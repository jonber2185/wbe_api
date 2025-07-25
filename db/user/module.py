import re
from datetime import datetime
import bcrypt
from db.module import run_sql


allowed_id_pattern = r'^[A-Za-z0-9._-]+$'
def is_valid_user_id(user_id: str) -> bool:
    if len(user_id) < 4:
        return False
    if len(user_id) > 30:
        return False
    if ' ' in user_id:
        return False
    if not re.match(allowed_id_pattern, user_id):
        return False
    return True

def is_unique_user_id(user_id: str) -> bool:
    result = run_sql(
        "SELECT user_id FROM users WHERE user_id = %s",
        (user_id,),
        fetchone=True
    )
    if result is not None:
        return False
    return True

allowed_pw_pattern = r'^[A-Za-z0-9!@#$%^&*()\-_+=\[\]{}:;,.?]+$'
def is_valid_password(password: str) -> bool:
    if len(password) < 8:
        return False
    if ' ' in password:
        return False
    if not re.match(allowed_pw_pattern, password):
        return False
    return True

def hash_valid_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')  # DB에 저장할 문자열

def is_valid_username(username: str) -> bool:
    if len(username) == 0:
        return False
    if len(username) > 30:
        return False
    return True

def is_valid_date(date) -> bool:
    if date is None:
        return True
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def is_valid_vegan(vegan: str) -> bool:
    if vegan in ["none", "vegan", "lacto", "ovo", "lacto-ovo", "pesco", "pollo"]:
        return True
    else: return False

def get_id_by_input_id(input_id: str) -> str:
    result = run_sql(
        "SELECT id FROM users WHERE user_id = %s",
        (input_id,),
        fetchone=True
    )
    return result.get("id", "")