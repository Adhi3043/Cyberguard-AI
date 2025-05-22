# 🛡️ CyberGuard AI – Threat Intelligence & Phishing Detection Assistant

A powerful, AI-powered cybersecurity tool that detects phishing URLs in real time, scans live phishing feeds, and logs threat intelligence for analysis.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Machine Learning](https://img.shields.io/badge/ML-RandomForest-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🚀 Features

- 🔍 Real-time phishing URL detection using custom features
- 🌐 Live phishing feed scanner (auto scans 20 latest links)
- 🧠 Trained with RandomForest model for 90%+ confidence
- 🧪 Unit tests included
- 🧾 Logs results to `phish_feed_scan_log.csv`
- 📦 Built using Flask, Scikit-learn, Pandas

---

## 🧠 Tech Stack

- Python 3.10+
- Flask (REST API)
- Scikit-learn (ML)
- Pandas (Data handling)
- Requests (Threat feed pulling)

---

## 📂 Project Structure

```bash
CyberGuard-AI/
├── app/                    # Flask API
├── phishing_detector/      # ML model + detection logic
├── feeds/                  # Live feed collector
├── logs/                   # Logged results
├── tests/                  # Unit tests
├── data/                   # CSV phishing dataset
├── README.md
├── requirements.txt
