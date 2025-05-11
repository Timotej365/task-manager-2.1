import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def vytvor_spojenie():
    return mysql.connector.connect(
        host=os.environ['DB_HOST'],
        port=int(os.environ['DB_PORT']),
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        database=os.environ['DB_NAME'],
        ssl_ca=os.path.join(os.path.dirname(__file__), 'ca.pem'),
        ssl_verify_cert=True
    )
