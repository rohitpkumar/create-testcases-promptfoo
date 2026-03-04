# 🚀 AI-Powered Structured Test Case Generation Framework

### An AI QA framework that converts user stories into validated Positive, Negative, and Edge test cases with strict schema enforcement and automated LLM evaluation.
### Designed for production-ready AI systems where output consistency, traceability, and regression detection matter.

---

## Generate Structured Test Cases Automatically using LLM + Promptfoo

This project demonstrates how to use **LangChain, OpenAI GPT models, Pydantic schema validation, and Promptfoo** to automatically generate structured test cases from User Stories and Acceptance Criteria.

The system enforces strict JSON output and validates LLM responses using automated evaluation.

It follows a simple architecture:

User Story + Acceptance Criteria  
↓  
LangChain Prompt Template  
↓  
LLM (GPT-4o-mini)  
↓  
Pydantic Schema Validation  
↓  
Structured Test Cases (Positive, Negative, Edge)  
↓  
Evaluate Response using Promptfoo  

---

## 🔥 Features

- Convert any user story into structured test cases
- Enforce strict JSON output using Pydantic schema
- Generate exactly:
  - Positive test case
  - Negative test case
  - Edge test case
- Scenario-based test IDs (e.g., `SIGNUP_TC_001`, `LOGIN_TC_001`)
- Dataset-driven input using YAML
- Automated validation using Promptfoo
- CI/CD ready architecture

---

## 📂 Project Structure

```
ai-llm-testcase-generator/
│
├── dataset/
│   └── login.yaml
│
├── models.py
├── test_generator.py
├── helper.py
├── promptfooconfig.yaml
│
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

## 🧪 What It Generates

For each flow (e.g., Signup, Login), the system generates:

- 1 Positive test case
- 1 Negative test case
- 1 Edge test case

Example Test ID format:

```
SIGNUP_TC_001
LOGIN_TC_001
```

All outputs are validated against a strict schema before evaluation.

---

## ⚙️ Getting Started

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add OpenAI API Key

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_key_here
```

---

## ▶️ Run Test Case Generator Manually

```bash
python test_generator.py
```

---

## 🧪 Run Promptfoo Evaluation

```bash
npx promptfoo eval --no-cache
```

View detailed results:

```bash
npx promptfoo view
```

---

## 📌 Tech Stack

- Python
- LangChain
- OpenAI GPT models
- Pydantic
- Promptfoo
- YAML dataset inputs

---
