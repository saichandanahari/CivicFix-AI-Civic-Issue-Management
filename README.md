# CivicFix AI – Smart Civic Issue Management Platform

**Turning citizen complaints into smarter, faster civic solutions with Artificial Intelligence.**

CivicFix AI is an AI-powered civic issue management platform that connects citizens with local authorities. It allows citizens to report public infrastructure and community problems while using AI to analyze, classify, prioritize, and organize complaints.

## Problem Statement

Citizens frequently face civic issues such as:
- Damaged roads and potholes
- Garbage accumulation
- Water leakage
- Drainage and sewage problems
- Broken streetlights
- Damaged footpaths

Traditional complaint systems can make it difficult to categorize, prioritize, and track these issues efficiently.

## Our Solution

CivicFix AI provides a centralized platform for citizens to report civic issues and for administrators to manage complaints through an organized dashboard.

Its AI engine analyzes complaint descriptions and generates structured insights to support better decision-making.

## Key Features

- **Citizen Reporting:** Submit complaints with descriptions, locations, and images.
- **AI-Powered Classification:** Identify the category of reported issues.
- **Department Assignment:** Suggest the appropriate department.
- **AI-Generated Summaries:** Convert complaints into concise summaries.
- **Priority Recommendations:** Assess issue severity and safety risks.
- **Admin Dashboard:** Monitor and manage submitted complaints.
- **Issue Tracking:** Update complaint status from reported to resolved.

## How It Works

1. Citizens submit complaints with descriptions and locations.
2. The Flask backend receives the information.
3. The AI engine analyzes the complaint.
4. The system identifies its category, severity, safety risk, and responsible department.
5. The analysis is stored in the database.
6. Administrators manage complaints and update their status.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework |
| OpenAI API | AI-powered analysis |
| SQLite | Database management |
| HTML5 | Frontend structure |
| CSS3 | Interface styling |
| JavaScript | Frontend interactions |

## Project Structure

```text
CivicFix-AI-Civic-Issue-Management/
│
├── app.py
├── ai_engine.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── report.html
│   ├── success.html
│   └── dashboard.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
│
└── uploads/
```

*Note: This represents the intended Flask folder structure. Keep it synchronized with the actual files in your repository. The uploads folder may be created at runtime.*

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/saichandanahari/CivicFix-AI-Civic-Issue-Management.git
```

### 2. Navigate to the project directory

```bash
cd CivicFix-AI-Civic-Issue-Management
```

### 3. Create a virtual environment

```bash
py -m venv venv
```

### 4. Install dependencies

```bash
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root using `.env.example` as a template.

Add your API configuration:

```env
OPENAI_API_KEY=your_api_key
OPENAI_MODEL=gpt-5-mini
```

**Important:** Never upload your `.env` file or expose your API key publicly.

### 6. Run the application

```bash
.\venv\Scripts\python.exe app.py
```

### 7. Open in your browser

```text
http://127.0.0.1:5000
```

## Environment Variables

| Variable | Description |
|---|---|
| OPENAI_API_KEY | API key for AI analysis |
| OPENAI_MODEL | Model used for complaint analysis |

If the API key is unavailable or AI analysis fails, the application uses its rule-based fallback analyzer.

## Developed For

**HackDevengers 2.0 – Open Innovation Hackathon**

**Category:** Artificial Intelligence | Smart Cities | Civic Technology

## Our Vision

"Better cities begin with better communication between citizens and authorities."

CivicFix AI aims to transform everyday civic complaints into actionable insights and contribute to cleaner, safer, and smarter communities.

## License

This project is available under the MIT License.
