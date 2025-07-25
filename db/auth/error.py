

class AuthError(Exception):
    def __init__(self, message: str, status_code: int = 401):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


class LoginDisagreementError(AuthError):
    def __init__(self):
        super().__init__("ID 또는 PW가 일치하지 않습니다.")


class SessionTokenError(AuthError):
    def __init__(self, message: str):
        super().__init__(message)


class UnAuthorizedError(AuthError):
    def __init__(self):
        super().__init__("인증이 필요합니다.")


class ForbiddenError(AuthError):
    def __init__(self):
        super().__init__("접근 권한이 없습니다.", status_code=403)