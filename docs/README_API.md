
# 📘 API Documentation – Shuttle Tracking System

This document describes the available endpoints in the REST API for managing trips in the University Shuttle Tracking System.

---

## ▶️ How to Run the API

1. Make sure you have **FastAPI** and **uvicorn** installed:
   ```bash
   pip install fastapi uvicorn
   ```

2. Run the API server:
   ```bash
   uvicorn main:app --reload
   ```

3. Visit the interactive API docs:
   ```
   http://127.0.0.1:8000/docs
   ```

---

## 🚏 Trip Endpoints

| Method | Endpoint         | Description             |
|--------|------------------|-------------------------|
| POST   | `/trips/`        | Create a new trip       |
| GET    | `/trips/`        | Get all trips           |
| GET    | `/trips/{id}`    | Get a trip by ID        |
| DELETE | `/trips/{id}`    | Delete a trip by ID     |

---

### ✅ Example Request (POST /trips/)
```
/trips/?trip_id=T001&status=Scheduled&start_time=08:00&end_time=09:00&route_id=R1&shuttle_id=S1
```

---

📌 **Tip:** Use `/docs` in your browser to test endpoints interactively.

---

Prepared by: **Luyolo Batyi**
