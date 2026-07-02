# 📧 Enterprise AI Email Agent

An AI-powered Enterprise Email Assistant built using **Langflow**, **Google Gemini**, **Gmail API**, and **SQLite**.

The agent understands natural language requests, intelligently calls custom tools, drafts professional emails, retrieves recipients from a company database, and sends emails using Gmail.

---

# 🚀 Features

- 🤖 AI-powered Email Agent using Google Gemini
- 🧠 Natural Language Understanding
- 🏢 Employee Database Lookup
- ✉️ AI Email Draft Generation
- 📤 Gmail API Integration
- 🔧 Custom Langflow Components
- 🗃 SQLite Employee Database
- 🎯 Autonomous Tool Calling
- 💬 Interactive Langflow Playground

---

# 🏗 Project Architecture

```
                           User
                             │
                             ▼
                     Gemini AI Agent
                  ┌────────┼────────┐
                  ▼        ▼        ▼
         Database Tool  Draft Tool  Gmail Tool
                  │        │        │
                  ▼        ▼        ▼
             SQLite DB   Gemini    Gmail API
```

---

# 📁 Project Structure

```
email-agent/
│
├── src/
│   └── email_agent/
│       ├── database/
│       ├── gmail/
│       ├── tools/
│       └── app.py
│
├── tests/
│
├── langflow/
│   └── workflow.json
│
├── requirements.txt
├── pyproject.toml
├── README.md
└── .env.example
```

---

# 🛠 Technologies Used

- Python 3.13+
- Langflow
- Google Gemini API
- Gmail API
- SQLite
- Google OAuth
- Google Generative AI SDK

---

# ⚙ Prerequisites

Install:

- Python 3.13+
- Git
- Google Chrome (recommended)
- Google Cloud Account
- Gemini API Key

---

# 📥 Installation

## 1. Clone Repository

```bash
git clone <repository-url>

cd email-agent
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install -e .
```

---

# 🔑 Gemini API Setup

Create a Gemini API Key from:

https://aistudio.google.com/

Create a file named:

```
.env
```

Example:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

# 📧 Gmail API Setup

## Step 1

Go to Google Cloud Console

https://console.cloud.google.com/

---

## Step 2

Create a new Project

---

## Step 3

Enable APIs

Enable:

- Gmail API
- Google People API

---

## Step 4

Configure OAuth Consent Screen

Choose:

External

Add your Gmail account as a Test User.

---

## Step 5

Create OAuth Client

Application Type:

Desktop App

Download:

```
credentials.json
```

---

## Step 6

Copy

```
credentials.json
```

into

```
src/email_agent/gmail/
```

---

# 🔐 Gmail Authentication

Run

```bash
python -m email_agent.app
```

Browser opens.

Login using your Gmail account.

Permission screen appears.

Allow Gmail permissions.

Token gets stored automatically inside

```
src/email_agent/gmail/tokens/
```

Future logins reuse the stored token.

---

# 🗄 Database Setup

Create Database

```bash
python src/email_agent/database/init_db.py
```

Populate Sample Data

```bash
python src/email_agent/database/seed.py
```

---

# ▶ Running the CLI Application

```bash
python -m email_agent.app
```

Example:

```
Send email to everyone in Marketing saying tomorrow is Work From Home.
```

---

# 🌊 Langflow Setup

Install Langflow

```bash
pip install langflow
```

---

Run Langflow

```bash
langflow run
```

Open

```
http://localhost:7860
```

---

# 📂 Import Langflow Flow

Inside Langflow

Import

```
langflow/workflow.json
```

The following components will load automatically:

- Gemini Agent
- Database Lookup Tool
- Email Draft Tool
- Gmail Sender Tool

---

# ▶ Testing the Agent

Example prompts:

```
Find all employees in Marketing.
```

```
Draft an email saying tomorrow is Work From Home.
```

```
Send an email to everyone in Marketing saying tomorrow is Work From Home.
```

---

# 🧰 Custom Components

The project contains three custom Langflow tools.

## DATABASE_LOOKUP

Purpose

Retrieves employee email addresses.

Inputs

- recipient_type
- recipient_value

Output

- email addresses

---

## EMAIL_DRAFT_TOOL

Purpose

Generates professional email drafts.

Input

- instruction

Output

- subject
- body

---

## GMAIL_SENDER_TOOL

Purpose

Sends email using Gmail API.

Inputs

- recipients
- subject
- body

Output

- success status

---

# 🧪 Running Tests

Intent Extraction

```bash
python -m tests.test_intent
```

Database

```bash
python -m tests.test_database
```

Database Tool

```bash
python -m tests.test_database_tool
```

Draft Tool

```bash
python -m tests.test_draft
```

Login

```bash
python -m tests.test_login
```

Send Email

```bash
python -m tests.test_send
```

---

# 📌 Future Enhancements

- CC Support
- BCC Support
- Email Attachments
- HTML Emails
- Schedule Emails
- Reply / Reply All
- Email Templates
- Multi-User Authentication
- Microsoft Outlook Integration
- Slack Integration
- Audit Logging
- Approval Workflow

---

# 📜 Workflow

```
User Request

↓

Gemini Agent

↓

Database Lookup

↓

Email Draft

↓

Gmail Sender

↓

Email Delivered
```

---

# 👨‍💻 Author

**Sarthak Bhardwaj**

B.Tech Computer Science & Engineering (Cloud Computing)

Enterprise AI & Agentic AI Enthusiast

---

# 📄 License

This project is intended for educational and demonstration purposes.