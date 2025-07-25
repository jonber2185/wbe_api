from flask_jwt_extended import (
    create_access_token, create_refresh_token
)
from . import module as auth_module
from . import error as e


def update_new_access_token(input_token, identity):
    try:
        if identity == "":
            raise ValueError
        identity = int(identity)
    except ValueError:
        raise e.SessionTokenError(f"Invalid identity")

    if input_token != "login":
        stored_token = auth_module.get_token_by_user_id(identity)
        if stored_token != input_token:
            raise e.SessionTokenError("Invalid refresh token")

    access_token = create_access_token(identity=str(identity))
    return access_token

def update_new_tokens(input_token, identity) -> list:
    access_token = update_new_access_token(
        input_token=input_token,
        identity=identity
    )
    refresh_token = create_refresh_token(identity=str(identity))
    auth_module.set_new_refresh_token(user_id=identity, token=refresh_token)
    return [access_token, refresh_token]