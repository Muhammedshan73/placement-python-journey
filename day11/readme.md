# 🎫 TicketRiser – Ticket Management System

## 📌 Project Overview

**TicketRiser** is a web-based ticket management system developed as part of the **PEP (Professional Enhancement Program) – Day 11**.
The application allows users to create, track, and manage tickets for issues such as electricity, maintenance, complaints, etc.

The system is built using **Django** and follows REST principles for handling ticket data.

---

## 🚀 Features

* ✅ Create new tickets with title, description, category, and priority
* ✅ View all submitted tickets
* ✅ Update ticket details
* ✅ Delete tickets
* ✅ REST API support using Django REST Framework
* ✅ Backend database integration

---

## 🛠️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Database:** SQLite (default)
* **Language:** Python
* **Tools:** Git, GitHub, VS Code

---

## 📂 Project Structure

```
ticketriser/
│
├── manage.py
├── ticketriser/
├── tickets/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│
└── db.sqlite3
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/ticketriser.git
cd ticketriser
```

### 2️⃣ Create virtual environment

```bash
python -m venv env
env\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run server

```bash
python manage.py runserver
```

---

## 🔗 API Endpoints (Sample)

* `GET /tickets/` → Get all tickets
* `POST /tickets/` → Create ticket
* `PUT /tickets/{id}/` → Update ticket
* `DELETE /tickets/{id}/` → Delete ticket

---

## 🎯 Learning Outcomes

* Django project structure understanding
* CRUD operations using REST API
* Model–Serializer–View workflow
* Migration handling
* Debugging database errors

---

## 👨‍💻 Author

**Muhammed Shan ST**
B.Tech CSE – Lovely Professional University

---

## 📅 PEP Progress

* ✅ Day 11 – TicketRiser basic CRUD + API implementation
