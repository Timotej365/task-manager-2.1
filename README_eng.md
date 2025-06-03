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
REACT_APP_API_URL=http://localhost:5000
```

---

### 🚀 Run Backend

```bash
cd backend
pip install -r requirements.txt
python API.py
```

### 🚀 Run Frontend

```bash
cd frontend
npm install
npm start
```



## 🧪Testing Examples

# Playwright E2E Tests

This project includes end-to-end tests written with Playwright in Python. Tests verify key frontend functionality like login, registration, task creation, and task editing.

# How to run tests locally


## 1. Activate virtual environment (venv):
```bash
source venv/bin/activate       # for Linux / MacOS
.\venv\Scripts\Activate.ps1    # for Windows PowerShell
```
## 2. Install dependencies and Playwright:
```bash
pip install -r requirements.txt
playwright install
```
## 3. Run tests:
```bash
pytest tests/E2E -v
```
I have registered a test user. Manual testing has verified that the following features work:
-registration
-subsequent login
-adding a task
-updating task status
-deleting a task
-The JWT token is stored in localStorage, and requests are authorized.

---

## 🎯 Project Goals

This project was created as a portfolio showcase for a junior tester or QA automation position, with the goals of:

-Practicing frontend/backend API integration
-Learning to work with a database
-Understanding the basics of CI/CD and cloud deployment

---

### 🌐 Public Deployment

The application is fully functional online and split into:

- 🔙 **Backend (Flask API):** hosted on [Render](https://render.com)
- 🖥️ **Frontend (React):** hosted on [Vercel](https://vercel.com)

#### 🔗 Direct Links:

- 🧠 **Frontend (React):** [task-manager-2-1.vercel.app](https://task-manager-2-1.vercel.app)
- 🔧 **Backend (Flask API):** REST API accessible via the React frontend (on Render)

The application is connected via API – registration, login, task management, JWT token authorization.

A presentable version of the project intended for GitHub portfolio and HR.

## 👤 Contact

**Timotej Šebest**  
GitHub: [@Timotej365](https://github.com/Timotej365)  
LinkedIn: [linkedin.com/in/timotej-šebest-94b513356](https://linkedin.com/in/timotej-šebest-94b513356)
