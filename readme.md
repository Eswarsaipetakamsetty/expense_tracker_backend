# 💸 Expense Tracker Backend (Django + DRF + JWT)

A simple Expense Tracker API built with Django, Django REST Framework (DRF), and JWT authentication.

---

## ⚙️ Features

- 🔐 JWT Authentication (Login & Signup)
- 📤 Create new expenses
- 📊 View and filter expenses by date
- 📈 Expense analytics (total, category-wise, monthly trends)

---

## 🏗️ Tech Stack

- Python 3.12+
- Django 4.x
- Django REST Framework
- djangorestframework-simplejwt
- PostgreSQL

---

## 🚀 Getting Started

## Deployed link

Here is the deployed link, and can directly access the api from here
https://expense-tracker-backend-iqtm.onrender.com

## Self Host

### 1. Clone the repository

```bash
git clone https://github.com/Eswarsaipetakamsetty/expense-tracker-backend.git
cd expense-tracker-backend

```
### 2. Create virtual env(optional)
```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install requirements.txt
```bash
pip install -r requirements.txt
```

### 4. Configure the database
To configure JWT lifetime or switch DB to PostgreSQL, edit your settings.py.
Example for PostgreSQL:

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'expense_db',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Run the server
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```
POST /api/signup/

Request Body
```bash
{
  "email": "user@example.com",
  "username": "user123",
  "password": "yourpassword"
}
```
POST /api/login/

Request Body
```bash
{
  "email": "user@example.com",
  "password": "yourpassword"
}
```

All /expenses/ endpoints require JWT Authorization header:
```bash
Authorization: Bearer <access_token>
```


| Method | Endpoint                                                   | Description                      |
| ------ | ---------------------------------------------------------- | -------------------------------- |
| POST   | `/api/signup/`                                             | Register a new user              |
| POST   | `/api/login/`                                              | Login and get JWT token          |
| GET    | `/api/expenses/`                                           | List all user expenses           |
| POST   | `/api/expenses/`                                           | Add a new expense                |
| GET    | `/api/expenses/?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD` | Filter expenses by date          |
| GET    | `/api/expenses/analytics/`                                 | Get total, category-wise, trends |
