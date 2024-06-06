from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DATABASE = 'teacher_data.db'

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    firstName, lastName = query.split(' ')

    cur.execute("SELECT * FROM teachers WHERE first_name LIKE ? AND last_name LIKE ?", ('%' + firstName + '%', '%' + lastName + '%'))
    teachers = cur.fetchall()
    conn.close()
    return jsonify(teachers)

if __name__ == '__main__':
    app.run(debug=True)