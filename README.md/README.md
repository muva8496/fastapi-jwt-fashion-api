# FastAPI Authentication API

A FastAPI project demonstrating authentication and authorization using JWT tokens and Argon2 password hashing.

## 🚀 Features

- User Registration
- User Login
- JWT Authentication
- Argon2 Password Hashing
- FastAPI REST API
- Swagger Documentation
- Fashion Sales Dataset Integration

## 🛠️ Tech Stack

- Python 3.12
- FastAPI
- Uvicorn
- Argon2
- Python-JOSE
- Pandas
- OpenPyXL

## 📁 Project Structure

```text
fastapi-jwt-fashion-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── auth.py
│   ├── security.py
│   ├── schemas.py
│   ├── fake_db.py
│   ├── models.py
│   └── dataset.py
│
├── data/
├── requirements.txt
└── README.md
```

## ⚙️ Installation

```bash
conda create -n fastapi_auth python=3.12
conda activate fastapi_auth
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the API

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

## 🔐 Authentication Flow

```text
Register
   ↓
Argon2 Hashing
   ↓
Login
   ↓
JWT Token
   ↓
Protected Routes
```

## 📌 Endpoints

| Method | Endpoint | Description |
|----------|----------|----------|
| GET | `/` | Home Route |
| POST | `/register` | Register User |
| POST | `/login` | Login User |
| GET | `/sales` | Sales Data |
| GET | `/summary` | Dataset Summary |

## 🎯 Learning Goals

- FastAPI Fundamentals
- Authentication & Authorization
- JWT Tokens
- Password Hashing
- Data APIs
- Backend Development

## 🔮 Future Improvements

- SQLite Database
- PostgreSQL Integration
- OAuth2
- Role-Based Access Control (RBAC)
- Protected Dataset Endpoints
- Cloud Deployment

## 👨‍💻 Author

**Musa**

Data Engineering • Analytics 