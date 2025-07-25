from flask import Blueprint, request, jsonify
import db

UserRouter = Blueprint('user', __name__)


@UserRouter.route('/create', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        password = data.get('password')
        username = data.get('username')
        vegan = data.get('vegan', 'none')  # 기본값 설정
        birth = data.get('birth', None)

        if not all([user_id, password, username]):
            raise db.user.error.UserValidationError("잘못된 형식입니다.")

        db.user.create.create_user(
            user_id=user_id,
            password=password,
            username=username,
            vegan=vegan,
            birth=birth
        )
        return jsonify({"message": "유저가 생성되었습니다!"}), 201
    except db.user.error.UserError as e:
        return jsonify({
            "error": str(type(e).__name__),
            "message": str(e.message)
        }), e.status_code
