from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Dynamické CORS podľa origin
CORS(app, supports_credentials=True)

@app.after_request
def pridaj_cors_headers(response):
    origin = request.headers.get("Origin")
    allowed = ["http://localhost:3000", "https://task-manager-2-1.vercel.app"]
    if origin in allowed:
        response.headers["Access-Control-Allow-Origin"] = origin
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
    response.headers["Vary"] = "Origin"
    return response

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

def pripojenie_db():
    try:
        spojenie = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            ssl_ca=os.path.join(os.path.dirname(__file__), "ca.pem"),
            ssl_verify_cert=True
        )
        print("✅ Pripojenie k databáze úspešné.")
        return spojenie
    except Error as e:
        print("❌ Chyba pri pripájaní k databáze:")
        print(e)
        return None

def over_token(request):
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith("Bearer "):
        return None
    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        return payload["user_id"]
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

@app.route('/tasks-open', methods=['GET'])
def get_all_tasks_open():
    spojenie = pripojenie_db()
    if spojenie is None:
        return jsonify({"error": "Chyba pri pripájaní k databáze."}), 500
    cursor = spojenie.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ulohy")
    ulohy = cursor.fetchall()
    cursor.close()
    spojenie.close()
    return jsonify(ulohy), 200

@app.route('/tasks', methods=['GET'])
def get_tasks():
    user_id = over_token(request)
    if not user_id:
        return jsonify({"error": "Neautorizovaný prístup."}), 401
    spojenie = pripojenie_db()
    if spojenie is None:
        return jsonify({"error": "Chyba pri pripájaní k databáze."}), 500
    cursor = spojenie.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ulohy WHERE user_id = %s", (user_id,))
    ulohy = cursor.fetchall()
    cursor.close()
    spojenie.close()
    return jsonify(ulohy), 200

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    spojenie = pripojenie_db()
    if spojenie is None:
        return jsonify({"error": "Chyba pri pripájaní k databáze."}), 500
    cursor = spojenie.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ulohy WHERE id = %s", (id,))
    uloha = cursor.fetchone()
    cursor.close()
    spojenie.close()
    if uloha:
        return jsonify(uloha), 200
    else:
        return jsonify({"error": "Úloha neexistuje."}), 404

@app.route('/tasks', methods=['POST'])
def add_task():
    user_id = over_token(request)
    if not user_id:
        return jsonify({"error": "Neautorizovaný prístup."}), 401
    data = request.get_json()
    nazov = data.get("nazov")
    popis = data.get("popis")
    if not nazov or not popis:
        return jsonify({"error": "Názov a popis sú povinné."}), 400
    spojenie = pripojenie_db()
    if spojenie is None:
        return jsonify({"error": "Chyba pri pripájaní k databáze."}), 500
    cursor = spojenie.cursor()
    sql = "INSERT INTO ulohy (nazov, popis, stav, user_id) VALUES (%s, %s, 'Nezahájená', %s)"
    cursor.execute(sql, (nazov, popis, user_id))
    spojenie.commit()
    nove_id = cursor.lastrowid
    cursor.close()
    spojenie.close()
    return jsonify({"message": "Úloha bola pridaná.", "id": nove_id}), 201

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    user_id = over_token(request)
    if not user_id:
        return jsonify({"error": "Neautorizovaný prístup."}), 401
    data = request.get_json()
    novy_stav = data.get("stav")
    if novy_stav not in ['Prebieha', 'Hotová']:
        return jsonify({"error": "Neplatný stav."}), 400
    spojenie = pripojenie_db()
    if spojenie is None:
        return jsonify({"error": "Chyba pri pripájaní k databáze."}), 500
    cursor = spojenie.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ulohy WHERE id = %s AND user_id = %s", (id, user_id))
    uloha = cursor.fetchone()
    if not uloha:
        return jsonify({"error": "Úloha neexistuje alebo nie je tvoja."}), 404
    cursor.execute("UPDATE ulohy SET stav = %s WHERE id = %s", (novy_stav, id))
    spojenie.commit()
    cursor.close()
    spojenie.close()
    return jsonify({"message": f"Úloha {id} bola aktualizovaná na '{novy_stav}'."}), 200

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    user_id = over_token(request)
    if not user_id:
        return jsonify({"error": "Neautorizovaný prístup."}), 401
    spojenie = pripojenie_db()
    if spojenie is None:
        return jsonify({"error": "Chyba pri pripájaní k databáze."}), 500
    cursor = spojenie.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ulohy WHERE id = %s AND user_id = %s", (id, user_id))
    uloha = cursor.fetchone()
    if not uloha:
        return jsonify({"error": "Úloha neexistuje alebo nie je tvoja."}), 404
    cursor.execute("DELETE FROM ulohy WHERE id = %s", (id,))
    spojenie.commit()
    cursor.close()
    spojenie.close()
    return jsonify({"message": f"Úloha {id} bola odstránená."}), 200

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    meno = data.get("meno")
    heslo = data.get("heslo")
    if not meno or not heslo:
        return jsonify({"error": "Meno a heslo sú povinné."}), 400
    hash_hesla = generate_password_hash(heslo)
    spojenie = pripojenie_db()
    if spojenie is None:
        return jsonify({"error": "Chyba pri pripájaní k databáze."}), 500
    cursor = spojenie.cursor()
    try:
        cursor.execute("INSERT INTO users (meno, heslo) VALUES (%s, %s)", (meno, hash_hesla))
        spojenie.commit()
        return jsonify({"message": "Registrácia prebehla úspešne."}), 201
    except mysql.connector.IntegrityError:
        return jsonify({"error": "Používateľ s týmto menom už existuje."}), 409
    finally:
        cursor.close()
        spojenie.close()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    meno = data.get("meno")
    heslo = data.get("heslo")
    if not meno or not heslo:
        return jsonify({"error": "Meno a heslo sú povinné."}), 400
    spojenie = pripojenie_db()
    if spojenie is None:
        return jsonify({"error": "Chyba pri pripájaní k databáze."}), 500
    cursor = spojenie.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE meno = %s", (meno,))
    user = cursor.fetchone()
    cursor.close()
    spojenie.close()
    if not user or not check_password_hash(user["heslo"], heslo):
        return jsonify({"error": "Nesprávne meno alebo heslo."}), 401
    token = jwt.encode({
        "user_id": user["id"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }, app.config['SECRET_KEY'], algorithm="HS256")
    return jsonify({"token": token}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
