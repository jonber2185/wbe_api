from . import module as auth_model
from ..user import module as user_model
from . import error as e


def login(input_id: str, input_password: str):
    if not user_model.is_valid_user_id(input_id):
        raise e.LoginDisagreementError()
    if not user_model.is_valid_password(input_password):
        raise e.LoginDisagreementError()

    user_password = auth_model.get_password_by_input_id(input_id)
    if user_password is None:
        raise e.LoginDisagreementError()
    user_password = user_password.get("password")
    if not auth_model.check_valid_password(input_password, user_password):
        raise e.LoginDisagreementError()

    # 로그인 성공