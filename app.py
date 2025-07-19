from flask import Flask, jsonify
import db


app = Flask(__name__)

@app.route('/create_user')
def create_user():
    try:
        db.user.create.create_user(
            user_id="jonber2185",
            password='qwert2846',
            username='jonber',
            vegan="none"
        )
        return jsonify({ "message": "유저가 생성되었습니다!" }), 201
    except db.user.error.UserError as e:
        return jsonify({ "error": str(e.message) }), e.status_code

if __name__ == '__main__':
    app.run(debug=True)
