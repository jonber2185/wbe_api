from flask import Flask
from flask_jwt_extended import JWTManager
from datetime import timedelta

import db.user.module
from router.auth import AuthRouter
from router.user import UserRouter

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'test'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=1)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=1)

jwt = JWTManager(app)

app.register_blueprint(AuthRouter, url_prefix='/auth')
app.register_blueprint(UserRouter, url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True)
