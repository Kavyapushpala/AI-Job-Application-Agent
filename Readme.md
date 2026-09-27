# 🤖 AI Job Application Agent

An AI-powered job application assistant that analyzes resumes and job descriptions, identifies matching and missing skills, and performs semantic resume-to-job matching using **LLMs, embeddings, and vector search**.

---

## 🎯 Project Goal

The goal of this project is to build an **AI-powered job application assistant** that helps candidates understand how well their resume matches a job description, identify skill gaps, and receive AI-based recommendations for improving their applications.

---

## 🚀 Features

* 📄 Resume PDF upload & text extraction
* 🤖 AI-powered resume parsing
* 💼 Job description analysis
* 🧠 Semantic resume-to-job matching
* 🔎 Vector similarity search using ChromaDB
* 📊 Skill matching & gap analysis
* 🗄️ PostgreSQL database integration
* ⚡ FastAPI REST APIs
* 🔗 LangChain / LangGraph workflow support
* 🌐 Frontend integration ready

---

## 🏗️ Architecture

```text
                 ┌─────────────────────┐
                 │      Frontend       │
                 │   React / Web App   │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │      FastAPI        │
                 │     Backend         │
                 └──────────┬──────────┘
                            │
            ┌───────────────┼───────────────┐
            │               │               │
            ▼               ▼               ▼
     ┌────────────┐  ┌────────────┐  ┌────────────┐
     │ PostgreSQL │  │  ChromaDB  │  │    LLM     │
     │  Database  │  │ Vector DB  │  │ AI Engine  │
     └────────────┘  └────────────┘  └────────────┘
            │               │               │
            └───────────────┼───────────────┘
                            ▼
                 ┌─────────────────────┐
                 │ Resume ↔ Job Match   │
                 │ Skill Gap Analysis   │
                 └─────────────────────┘
```

---

## 🔄 Workflow

```text
Resume PDF
    ↓
PDF Text Extraction
    ↓
Resume Parsing
    ↓
Generate Embeddings
    ↓
Store in ChromaDB
    ↓
Job Description
    ↓
Semantic Matching
    ↓
Skill Matching
    ↓
Skill Gap Analysis
    ↓
AI Recommendations
```

---

## 🛠️ Tech Stack

| Category        | Technologies             |
| --------------- | ------------------------ |
| Backend         | Python, FastAPI          |
| AI/LLM          | LLMs, Prompt Engineering |
| Embeddings      | Sentence Transformers    |
| RAG / Agents    | LangChain, LangGraph     |
| Vector Database | ChromaDB                 |
| Database        | PostgreSQL               |
| PDF Processing  | PyPDF                    |
| API Server      | Uvicorn                  |
| Frontend        | React.js                 |

---

## ⚙️ Setup

### Clone Repository

```bash
git clone https://github.com/Kavyapushpala/AI-Job-Application-Agent.git
cd AI-Job-Application-Agent
```

### Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```


### Run FastAPI

```bash
uvicorn main:app --reload
```

### API Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

---

## 🔮 Future Scope

* AI resume optimization
* Personalized cover letter generation
* Automated job discovery
* Agentic job application workflow
* Application tracking
* React frontend dashboard

---

## 👩‍💻 Author

**Kavya Varshitha Pushpala**
B.Tech – Artificial Intelligence & Data Science
SRKR Engineering College

**GitHub:** https://github.com/Kavyapushpala
**LinkedIn:** https://www.linkedin.com/in/kavya-varshitha-pushpala-2et32/
