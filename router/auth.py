from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
import db


AuthRouter = Blueprint('auth', __name__)

@AuthRouter.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        input_id = data.get('id')
        input_password = data.get('password')

        if not all([input_id, input_password]):
            raise db.auth.error.AuthError("잘못된 형식입니다.")
        db.auth.sign.login(input_id=input_id, input_password=input_password)
        # 로그인 성공

        user_id = db.user.module.get_id_by_input_id(input_id)
        [access_token, refresh_token] = db.auth.token.update_new_tokens(
            input_token="login",
            identity=user_id
        )
        return jsonify(access_token=access_token, refresh_token=refresh_token), 200
    except db.auth.error.AuthError as e:
        return jsonify({
            "error": str(type(e).__name__),
            "message": str(e.message)
        }), e.status_code

@AuthRouter.route('/refresh', methods=['GET'])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    auth_header = request.headers.get("Authorization", "")
    input_token = auth_header.replace("Bearer ", "").strip()

    try:
        new_access_token = db.auth.token.update_new_access_token(
            input_token=input_token,
            identity=identity
        )
        return jsonify(access_token=new_access_token), 200
    except db.auth.error.AuthError as e:
        return jsonify({
            "error": str(type(e).__name__),
            "message": str(e.message),
        }), e.status_code

@AuthRouter.route('/update-refresh', methods=['GET'])
@jwt_required(refresh=True)
def update_refresh():
    identity = get_jwt_identity()
    auth_header = request.headers.get("Authorization", "")
    input_token = auth_header.replace("Bearer ", "").strip()

    try:
        [access_token, refresh_token] = db.auth.token.update_new_tokens(
            input_token=input_token,
            identity=identity
        )
        return jsonify(access_token=access_token, refresh_token=refresh_token), 200
    except db.auth.error.AuthError as e:
        return jsonify({
            "error": str(type(e).__name__),
            "message": str(e.message)
        }), e.status_code
