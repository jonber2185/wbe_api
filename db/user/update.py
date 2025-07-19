from db.module import run_sql
from . import module as user_model
from . import error as e


def update_user_id(user_id, new_user_id):
    if not user_model.is_valid_user_id(new_user_id):
        raise e.UserValidationError("ID 형식이 잘못되었습니다.")
    if not user_model.is_unique_user_id(new_user_id):
        raise e.UserUniqueError("이미 존재하는 ID입니다.")

    run_sql(
        "UPDATE users SET user_id = %s WHERE id = %s",
        (new_user_id, user_id)
    )

def update_user_password(user_id, new_password):
    if not user_model.is_valid_password(new_password):
        raise e.UserValidationError("비밀번호 형식이 잘못되었습니다.")
    password = user_model.hash_valid_password(new_password)

    run_sql(
        "UPDATE users SET password = %s WHERE id = %s",
        (password, user_id)
    )

def update_user_username(user_id, new_username):
    username = new_username.strip()
    if not user_model.is_valid_username(username):
        raise e.UserValidationError("이름 형식이 잘못되었습니다.")

    run_sql(
        "UPDATE user_profiles SET username = %s WHERE user_id = %s",
        (username, user_id)
    )

def update_user_vegan(user_id, vegan):
    if not user_model.is_valid_vegan(vegan):
        raise e.UserValidationError("비견 형식이 잘못되었습니다.")

    run_sql(
        "UPDATE user_profiles SET vegan = %s WHERE user_id = %s",
        (vegan, user_id)
    )