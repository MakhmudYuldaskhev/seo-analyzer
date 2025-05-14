import os
import sqlite3
from flask import Flask, request, jsonify, abort
from dotenv import load_dotenv

# .env faylni yuklash
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
DB_PATH = os.getenv("DB_PATH")


# 📌 SQL injectiondan himoyalangan query
def get_user_by_name(username):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, username FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    return result


# 🛡 Foydalanuvchi inputni xavfsiz ishlatish
@app.route('/user', methods=['GET'])
def get_user():
    username = request.args.get('username')
    if not username:
        abort(400, "Username kerak")

    user = get_user_by_name(username)
    if user:
        return jsonify({'id': user[0], 'username': user[1]})
    else:
        return jsonify({'message': 'Topilmadi'}), 404


# ❌ Debugni o'chiring
if __name__ == '__main__':
    app.run(debug=False)  # Productionda debug=False BO‘LISHI SHART!
