import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Načítaj environment premenné z .env (ak testuješ lokálne)
load_dotenv()

try:
    spojenie = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        ssl_ca="./ca.pem",  # predpokladáme, že máš ca.pem v rovnakom priečinku
        ssl_verify_cert=True
    )
    if spojenie.is_connected():
        print("✅ Spojenie s databázou je úspešné.")
except Error as e:
    print("❌ Chyba pri pripájaní k databáze:")
    print(e)
