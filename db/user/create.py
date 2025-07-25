from db.module import run_sql
from . import module as user_model
from . import error as e


def create_user(user_id, password, username, vegan, birth=None):
    if not user_model.is_valid_user_id(user_id):
        raise e.UserValidationError("ID 형식이 잘못되었습니다.")
    if not user_model.is_unique_user_id(user_id):
        raise e.UserUniqueError()
    if not user_model.is_valid_password(password):
        raise e.UserValidationError("비밀번호 형식이 잘못되었습니다.")
    password = user_model.hash_valid_password(password)
    username = username.strip()
    if not user_model.is_valid_username(username):
        raise e.UserValidationError("이름 형식이 잘못되었습니다.")
    if not user_model.is_valid_vegan(vegan):
        raise e.UserValidationError("비견 형식이 잘못되었습니다.")
    if not user_model.is_valid_date(birth):
        raise e.UserValidationError("날짜 형식이 잘못되었습니다.")

    return_id = run_sql(
        "INSERT INTO users (user_id, password) VALUES (%s, %s)",
        (user_id, password),
        return_id=True
    )
    run_sql(
        "INSERT INTO user_profiles (user_id, username, birth, vegan) VALUES (%s, %s, %s, %s)",
        (int(return_id), username, birth, vegan)
    )
    run_sql(
        "INSERT INTO refresh_tokens (user_id, token) VALUES (%s, %s)",
        (int(return_id), "new_refresh_token")
    )
