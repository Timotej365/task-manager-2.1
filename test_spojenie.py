from db_spojenie import vytvor_spojenie
import os
from dotenv import load_dotenv

load_dotenv()
print("Heslo z .env:", os.getenv("DB_PASSWORD"))

spojenie = vytvor_spojenie()
print("Spojenie úspešné:", spojenie.is_connected())
