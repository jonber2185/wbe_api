

class UserError(Exception):
    def __init__(self, message: str, status_code: int = 400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


class UserValidationError(UserError):
    def __init__(self, message: str):
        super().__init__(message)


class UserUniqueError(UserError):
    def __init__(self):
        super().__init__("이미 존재하는 ID입니다.", status_code=409)