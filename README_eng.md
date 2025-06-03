# 🗂️ Task Manager 2.1 – Fullstack Web App (React + Flask + MySQL)

A fully functional online task manager with user registration, login, and CRUD operations. This application is deployed on **Vercel (frontend)** and **Render (backend)** with a cloud **MySQL (Aiven)** database.

> ℹ️ **Note:** The backend runs on Render's free plan. After about 15 minutes of inactivity, it may go into sleep mode, which could cause a slight delay on the first request.  
> 🔗 [Try the app online](https://task-manager-2-1.vercel.app)

---

🧪 The repository contains a test script `test_spojenie.py` and `db_spojenie`, which serve to verify the functionality of the database connection during development.


## 🔧 Technologies Used

- **Frontend:** React.js (Vercel)
- **Backend:** Flask (Render)
- **Database:** MySQL (Aiven)
- **Authentication:** JWT Tokens
- **Password Hashing:** Werkzeug
- **CORS + REST API**
- **Deployment:** CI/CD from GitHub

---

## 🔐 Features

- ✅ User registration and login
- ✅ Secure password hashing (bcrypt)
- ✅ CRUD operations for tasks (per user)
- ✅ Task filtering by status (Not Started, In Progress, Completed)
- ✅ User-friendly interface and icons for clarity

---

### 🛠️ Local Setup (Optional)

1. Clone the repository:  
   ```bash
   git clone https://github.com/Timotej365/task-manager-2.1
   cd task-manager-2.1
   
```

2. Create .env files (not included in the repository):

#### 📁 `backend/.env`
```
DB_HOST=...
DB_PORT=...
DB_USER=...
DB_PASSWORD=...
DB_NAME=...
SECRET_KEY=...
```

#### 📁 `frontend/.env`
```
REACT_APP_API_URL=https://tvoj-render-backend-url.onrender.com
```

---

### 🚀 Spustenie backendu

```bash
cd backend
pip install -r requirements.txt
python API.py
```

### 🚀 Spustenie frontendu

```bash
cd frontend
npm install
npm start
```



## 🧪 Príklady testovania

# Playwright E2E testy

Tento projekt obsahuje end-to-end testy napísané pomocou Playwright v Pythone. Testy overujú základné funkcie frontendu, ako je prihlasovanie, registrácia, pridávanie a úprava úloh.

## Ako spustiť testy lokálne

```bash
# 1. Aktivuj virtuálne prostredie (venv):
source venv/bin/activate       # pre Linux / MacOS
.\venv\Scripts\Activate.ps1    # pre Windows PowerShell
```
# 2. Nainštaluj závislosti a Playwright:
```bash
pip install -r requirements.txt
playwright install
```
# 3. Spusti testy:
```bash
pytest tests/E2E -v
```
Registroval som testovacieho používateľa. Manuálnym testovaním som overil, že Funguje:

- registrácia  
- následné prihlásenie  
- pridanie úlohy  
- zmena stavu úlohy  
- odstránenie úlohy  

JWT token sa ukladá do `localStorage`, požiadavky sa autorizujú.

---

## 🎯 Ciele projektu

Tento projekt bol vytvorený ako portfólio ukážka pre pozíciu **junior testera** alebo **QA automation**, pričom cieľom bolo:

- precvičiť si **frontend/backend prepojenie cez API**
- naučiť sa prácu s **databázou**
- pochopiť základy **CI/CD** a **nasadenia do cloudu**

---

### 🌐 Verejné nasadenie

Aplikácia je plne funkčná online a rozdelená na:

- 🔙 **Backend (Flask API):** hostovaný na [Render](https://render.com)
- 🖥️ **Frontend (React):** hostovaný na [Vercel](https://vercel.com)

#### 🔗 Priame odkazy:

- 🧠 **Frontend (React):** [task-manager-2-1.vercel.app](https://task-manager-2-1.vercel.app)
- 🔧 **Backend (Flask API):** REST API dostupné cez React frontend (na Renderi)

Aplikácia je prepojená cez API – registrácia, login, správa úloh, autorizácia cez JWT token.

> Prezentovateľná verzia projektu určená pre GitHub portfólio a HR.


## 👤 Kontakt

**Timotej Šebest**  
GitHub: [@Timotej365](https://github.com/Timotej365)  
LinkedIn: [linkedin.com/in/timotej-šebest-94b513356](https://linkedin.com/in/timotej-šebest-94b513356)
