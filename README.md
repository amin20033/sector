# 📊 Sector Analysis API (Django + DRF + LLM)

## 🚀 Project Overview

The **Sector Analysis API** is a backend service that analyzes Indian market sectors and generates structured trade opportunity reports.

The API accepts a sector name (e.g., *technology, pharmaceuticals, agriculture*), fetches relevant market/news data, processes it using an LLM (Llama 3.2 via Ollama), and returns a **structured markdown report** containing insights such as trends, opportunities, and risks.

---

## 🎯 Key Features

* 🔐 JWT Authentication (login & token-based access)
* ⚡ DRF Throttling (rate limiting per user)
* 🧠 AI-powered analysis using Llama 3.2 (Ollama)
* 🌐 Real-time data fetching using newsdata.io
* 🧾 Markdown report generation
* 🗂️ Session tracking for user activity
* 👤 Custom User Model (without username field)

---

## 🏗️ Architecture Overview

```
Client → API View → Services → External API → AI Model → Response
```

### Components

* **Views**
  Handles request/response lifecycle and orchestrates the workflow.

* **Serializers**
  Validates and sanitizes input data.

* **Services Layer**

  * Handles external API calls (news data)
  * Handles AI-based analysis (LLM processing)

* **Authentication**

  * JWT-based authentication using SimpleJWT

* **Throttling**

  * Implemented using DRF built-in throttling

* **Session Management**

  * Tracks user activity (e.g., last searched sector)

---

## ⚙️ Tech Stack

* Django
* Django REST Framework
* JWT (SimpleJWT)
* httpx (async HTTP client)
* Ollama (Llama 3.2)
* newsdata.io API

---

## 📦 Installation & Setup

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd sector
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup Ollama (LLM)

```bash
ollama run llama3.2:1b
```

---

### 5. Configure News API

* Get API key from: https://newsdata.io
* Add it in your service file as:

```python
API_KEY = "your_api_key_here"
```

---

### 6. Run Migrations
```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

### 7. Create Superuser

```bash
python manage.py createsuperuser
```

---

### 8. Run Server

```bash
python manage.py runserver
```

---

## 🔐 Authentication Flow (JWT)

### Login

* Endpoint: `/api/login/`
* Method: POST
* Description: Returns access and refresh tokens

### Refresh Token

* Endpoint: `/api/refresh/`
* Method: POST

### Authorization Header

```
Authorization: Bearer <access_token>
```

---

## 📡 API Endpoints

### Analyze Sector

* Endpoint: `/api/analyze/{sector}/`
* Method: GET
* Description: Returns AI-generated market analysis report

---

### Register User

* Endpoint: `/api/register/`
* Method: POST

---

### Logout User

* Endpoint: `/api/logout/`
* Method: POST

---

## 🧾 Sample Response

```json
{
  "sector": "technology",
  "report": "## Overview\n...\n## Trends\n...\n## Opportunities\n...\n## Risks\n...\n## Conclusion\n..."
}
```

---

## 🧠 How It Works

1. User sends a sector name
2. JWT authentication is verified
3. Input is validated
4. News data is fetched from newsdata.io
5. Data is processed using Llama 3.2
6. A structured markdown report is generated
7. Response is returned to the user
8. Session stores the last searched sector

---

## ⚠️ Error Handling

* **400** → Invalid input
* **401** → Unauthorized
* **429** → Too many requests
* **500** → Internal server error

---

## 👤 Author

**Sk Aminur Rahman**

---

## 📌 Conclusion

This project demonstrates building a secure and scalable API using Django REST Framework, integrating real-time data and AI-based analysis to generate meaningful trade insights for different market sectors.
