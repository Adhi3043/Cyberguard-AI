# 🛡️ CyberGuard AI – Phishing Detection Assistant

[![Live Demo](https://img.shields.io/badge/Live%20Demo-online-green?style=flat-square&logo=render)](https://cyberguard-ai.onrender.com)

A real-time, AI-powered phishing detection platform that scans suspicious URLs, uses machine learning to identify threats, and integrates threat intelligence feeds — all accessible from a clean web interface.

---

## 🚀 Features

- 🔍 Real-time phishing URL scanning
- 🧠 ML model with custom feature extraction
- 🌐 Threat feed scanning and logging
- 📦 Flask REST API + Web UI
- 📊 Confidence score output
- 🧪 Unit-tested and production-ready structure
- 🌍 Deployed on Render for public use

---

## 🌐 Live Demo

👉 [Click to Try the Web App](https://cyberguard-ai.onrender.com)

---

## 📂 Project Structure
CyberGuard-AI/
├── app/ # Flask web app
├── phishing_detector/ # Model, features, ML logic
├── feeds/ # Threat intelligence URL feed scanner
├── templates/ # Web UI HTML
├── logs/ # Phishing scan logs
├── data/ # CSV dataset
├── tests/ # Unit tests
├── requirements.txt
└── README.md


---

## 🧠 Tech Stack

- Python 3
- Flask
- Scikit-learn
- Pandas
- Requests
- Joblib

---

## 🧪 Run Locally

```bash
git clone https://github.com/Adhi3043/Cyberguard-AI.git
cd Cyberguard-AI
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 phishing_detector/train_model.py
python3 app/main.py

## 📄 License
---

## 👨‍💻 Author

**Jhansi Aditya Akula**  
Cybersecurity + AI Engineer  
[GitHub Profile](https://github.com/Adhi3043)  
[Live Web App](https://cyberguard-ai.onrender.com)
