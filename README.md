# 🗂️ Task Manager 2.1 – Fullstack Web App (React + Flask + MySQL)

Plne funkčný online správca úloh s registráciou, prihlásením a CRUD operáciami. Táto aplikácia je nasadená na **Vercel (frontend)** a **Render (backend)** s cloudovou databázou **MySQL (Aiven)**.

> ℹ️ **Poznámka:** Backend beží na platforme Render v rámci bezplatného plánu. Po cca 15 minútach nečinnosti môže dôjsť k jeho uspatiu, čo môže spôsobiť pomalšie načítanie pri prvom prístupe. Frontend (Vercel) zostáva stále dostupný.
> 
> 🔗 [Vyskúšaj aplikáciu online](https://task-manager-2-1.vercel.app)

---

🧪 V repozitári je prítomný testovací skript `test_spojenie.py` a `db_spojenie`, ktorý slúži na overenie funkčnosti pripojenia k databáze počas vývoja.


## 🔧 Použité technológie

- **Frontend:** React.js (Vercel)
- **Backend:** Flask (Render)
- **Databáza:** MySQL (Aiven)
- **Autentifikácia:** JWT Tokeny
- **Šifrovanie hesiel:** Werkzeug
- **CORS + REST API**
- **Deployment:** CI/CD z GitHubu

---

## 🔐 Funkcionality

- ✅ Registrácia a prihlásenie používateľa
- ✅ Bezpečné šifrovanie hesiel (bcrypt)
- ✅ CRUD operácie pre úlohy (vlastné pre každého používateľa)
- ✅ Filtrovanie úloh podľa stavu (Nezahájená, Prebieha, Hotová)
- ✅ Prívetivé rozhranie a ikony pre prehľadnosť

---

### 🛠️ Lokálne spustenie (voliteľné)

1. Naklonuj si repozitár:
```bash
git clone https://github.com/Timotej365/task-manager-2.1
cd task-manager-2.1
```

2. Vytvor `.env` súbory (nie sú súčasťou repozitára):

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

# 2. Nainštaluj závislosti a Playwright:
pip install -r requirements.txt
playwright install

# 3. Spusti testy:
pytest tests/E2E -v

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

## 📂 Screenshoty priebehu

Nájdeš v priečinku [`/screenshots`](./screenshots) – obsahuje priebeh spustenia a testovania aplikácie.

---

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


