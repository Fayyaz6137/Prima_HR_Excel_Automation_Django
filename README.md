# 📊 Excel Calculation Replacement – Django PoC

This project is a **Django-based Proof of Concept** that replaces an existing **Excel calculation model** with a backend system.

The application accepts **CSV input files**, applies the same calculation logic programmatically (without using Excel), generates **downloadable output CSV files**, and maintains a **history of executions**.

---

## 🚀 Features

- Upload CSV files following a predefined input structure  
- Persist uploaded input files  
- Replicate Excel calculation logic using Python  
- Generate and store output CSV files  
- Download input and output files  
- View execution history with status and metadata  
- Simple and functional Django-based UI  

---

## ⚙️ Tech Stack

- **Python**
- **Django**
- **Pandas** (CSV processing)
- **HTML (Django Templates)**
- **CSS (Django Statics)**

---

## ▶️ Run Locally (Recommended)

```bash
git clone [https://github.com/Fayyaz6137/Ping_Pong_Game_Python.git](https://github.com/Fayyaz6137/Prima_HR_Excel_Automation_Django.git)

pip install -r requirements.txt

python manage.py migrate --> Only if running for the first time

python manage.py runserver
```

---

## 🐳 Run With Docker

```bash
docker compose up --build
```
⚠️ Since this is a GUI application, running inside Docker requires an X server (e.g., VcXsrv on Windows).

---

## 🖼️ UI 
![Upload FIle](https://github.com/user-attachments/assets/faac7e66-ed0a-4102-aed2-3a1f1480c6fa)

![History](https://github.com/user-attachments/assets/278d8045-2244-446d-9896-4af74e4d9694)


## 🧠 Development Approach (Phased)

The application was built incrementally to ensure clarity, correctness, and testability.

### Phase 1 – UI & Navigation
- Landing (upload) page
- History page
- Basic navigation between pages

### Phase 2 – File Upload
- CSV file upload using Django forms
- Backend receives files successfully (no storage yet)

### Phase 3 – Persistence & History
- Uploaded files stored on disk
- Execution metadata stored in database
- History page displays uploaded input files

### Phase 4 – Processing & Output
- Excel formulas replicated in Python
- CSV processed without Excel dependency
- Output CSV generated and stored
- Execution status and row counts recorded



