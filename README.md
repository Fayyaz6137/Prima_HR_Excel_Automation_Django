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

---


---

## ⚙️ Tech Stack

- **Python**
- **Django**
- **Pandas** (CSV processing)
- **HTML (Django Templates)**
- **CSS (Django Statics)**

---



