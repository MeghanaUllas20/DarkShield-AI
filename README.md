# 🛡️ DarkShield AI

## AI-Powered Dark Pattern Detection & Ethical UX Auditor

DarkShield AI is an intelligent platform designed to identify, analyze, and explain dark patterns used in websites and digital products. The system leverages Generative AI to detect manipulative user experience practices and provide ethical redesign recommendations.

## 🚀 Problem Statement

Many websites use deceptive design techniques, commonly known as **Dark Patterns**, to influence user behavior. These patterns often pressure users into actions such as:

* Accepting unnecessary cookies
* Making unintended purchases
* Subscribing to unwanted services
* Sharing personal information
* Remaining trapped in difficult cancellation flows

Most users are unable to recognize these manipulative tactics.

DarkShield AI helps users, designers, and organizations identify such practices and promote ethical digital experiences.

---

## 🔗 Project Links

- 🌐 Live Application: https://darksheild-ai.netlify.app/
- 📚 API Documentation: https://darksheild-ai.onrender.com/docs

## ✨ Features

### 🔍 Dark Pattern Detection

Detects common dark patterns including:

* Confirmshaming
* Forced Action
* Hidden Costs
* Interface Interference
* Obstruction
* Scarcity & Urgency Tactics

### 🤖 AI-Powered Analysis

Uses Google Gemini AI to:

* Analyze webpage content
* Identify manipulative language
* Explain why content is harmful
* Generate ethical alternatives

### 📊 Risk Assessment

Provides:

* Risk Score
* Severity Level
* Detailed Explanation
* Pattern Classification

### 🌐 Website Scanning

Analyze website content through:

* URL input
* Text input
* Screenshot-based inspection

### 🧩 Browser Extension

Real-time dark pattern detection while browsing websites.

### 💡 Ethical Recommendations

Suggests user-friendly and transparent alternatives to manipulative design practices.

---

## 🏗️ System Architecture

```text
User Input / Browser Extension
            │
            ▼
Frontend (React + Vite)
            │
            ▼
Backend API (FastAPI)
            │
            ▼
Google Gemini AI
            │
            ▼
Risk Analysis Engine
            │
            ▼
Results Dashboard
```

---

## 🛠️ Tech Stack

### Frontend

* React
* Vite
* JavaScript
* HTML5
* CSS3

### Backend

* Python
* FastAPI
* Uvicorn

### AI Layer

* Google Gemini API

### Deployment

* Netlify (Frontend)
* Render (Backend)

---

## 📂 Project Structure

```text
DarkShield-AI/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── services/
│   │   ├── models/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── render.yaml
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/MeghanaUllas20/DarkShield-AI.git
cd DarkShield-AI
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend will run on:

```text
http://localhost:5173
```

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Backend will run on:

```text
http://127.0.0.1:8000
```

---

## 🎯 Use Cases

### Consumers

Identify manipulative websites before making decisions.

### UX Designers

Audit products and create ethical user experiences.

### Businesses

Evaluate products for transparency and compliance.

### Regulators

Support digital consumer protection initiatives.

---

## 🔮 Future Enhancements

* Computer Vision based dark pattern detection
* Browser extension marketplace release
* Real-time website auditing
* Regulatory compliance reporting
* Enterprise dashboard
* Multi-language support

---

## 🏆 Hackathon Highlights

* AI-Powered Detection Engine
* Explainable AI Analysis
* Ethical UX Recommendations
* Browser Extension Support
* Scalable API Architecture
* Real-World Social Impact

---

## 👥 Team

Built during a Hackathon to promote ethical and transparent digital experiences.

### Team DarkShield AI

* Meghana Ullas
* Team Members 

---

## 📜 License

This project is developed for educational, research, and innovation purposes.

---

### "Building a safer and more transparent digital world through AI-powered ethical UX analysis."
