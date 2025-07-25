import bcrypt
from db.module import run_sql


def get_password_by_input_id(input_id: str) -> dict:
    result = run_sql(
        "SELECT password FROM users WHERE user_id = %s",
        (input_id,),
        fetchone=True
    )
    return result

def get_token_by_user_id(user_id: int) -> str:
    result = run_sql(
        "SELECT token FROM refresh_tokens WHERE user_id = %s",
        (user_id,),
        fetchone=True
    )
    return result.get('token', "")

def set_new_refresh_token(user_id: int, token: str):
    run_sql(
        "UPDATE refresh_tokens SET token = %s WHERE user_id = %s",
        (token, user_id)
    )

def check_valid_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
