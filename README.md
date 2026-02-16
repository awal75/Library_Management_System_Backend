# 📚 Library Management System API

A professional, industry-standard RESTful API built with **Django** and **Django REST Framework (DRF)**. This system manages books, authors, members, and complex borrow/return workflows with a focus on data integrity and concurrency safety.

## 🚀 Key Features

*   **Full CRUD Support**: Manage Books, Authors, and Members seamlessly.
*   **Advanced Borrowing System**: Automated availability tracking and return workflows.
*   **🛡️ Double Borrow Prevention**: Logic-level checks to ensure a book cannot be borrowed twice.
*   **🔐 Transaction Safe**: Uses `transaction.atomic` to ensure all-or-nothing operations.
*   **⚡ Race Condition Protection**: Implements `select_for_update()` to handle high-concurrency borrowing scenarios safely.
*   **📦 Clean Architecture**: Built using ViewSets and Routers for scalable, maintainable code.

## 🏗 Tech Stack

*   **Language:** Python 3.x
*   **Framework:** [Django](https://www.djangoproject.com)
*   **API Toolkit:** [Django REST Framework (DRF)](https://www.django-rest-framework.org)
*   **Database:** SQLite (Default) / PostgreSQL compatible
*   **Architecture:** RESTful ViewSets & ModelSerializers

---

## 📘 API Documentation

**Base URL:** `http://127.0.0.1:8000/api/v1/`

### 📚 Endpoints Summary

| Entity | Method | Endpoint | Description |
| :--- | :--- | :--- | :--- |

| **Books** | `GET` | `/books/` | List all books |
|  | `POST` | `/books/` | Create a new book |
|  | `GET` | `/books/{id}/` | Retrieve single book |
|  | `PATCH` | `/books/{id}/` | Update book |
|  | `DELETE` | `/books/{id}/` | Delete book |

| **Members** | `GET` | `/members/` | List all members |
|  | `POST` | `/members/` | Register a new member |
|  | `GET` | `/members/{id}/` | Retrieve single member |
|  | `PATCH` | `/members/{id}/` | Update member |
|  | `DELETE` | `/members/{id}/` | Delete member |

| **Authors** | `GET` | `/authors/` | List all authors |
|  | `POST` | `/authors/` | Add a new author |
|  | `GET` | `/authors/{id}/` | Retrieve single author |
|  | `PATCH` | `/authors/{id}/` | Update author |
|  | `DELETE` | `/authors/{id}/` | Delete author |

| **Borrow Records** | `GET` | `/borrow-records/` | List all borrow records |
|  | `POST` | `/borrow-records/` | Borrow a book |
|  | `GET` | `/borrow-records/{id}/` | Retrieve borrow record |
|  | `PATCH` | `/borrow-records/{id}/` | Return a book |
|  | `DELETE` | `/borrow-records/{id}/` | Delete borrow record |

---

## 🔄 Borrow Workflow

### 1. Borrow a Book
**Endpoint:** `POST /borrow-records/`  
**Payload:**
```json
{
  "book": 1,
  "member": 2
}
