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

### 4. Run the server
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```
| Method | Endpoint                                                   | Description                      |
| ------ | ---------------------------------------------------------- | -------------------------------- |
| POST   | `/api/signup/`                                             | Register a new user              |
| POST   | `/api/login/`                                              | Login and get JWT token          |
| GET    | `/api/expenses/`                                           | List all user expenses           |
| POST   | `/api/expenses/`                                           | Add a new expense                |
| GET    | `/api/expenses/?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD` | Filter expenses by date          |
| GET    | `/api/expenses/analytics/`                                 | Get total, category-wise, trends |

