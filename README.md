 CivicFix AI – Smart Civic Issue Management Platform

Turning citizen complaints into smarter, faster civic solutions with Artificial Intelligence.

CivicFix AI is an AI-powered civic issue management platform designed to bridge the gap between citizens and local authorities. It enables citizens to report public infrastructure and community problems while using AI to analyze, classify, prioritize, and organize reported issues.

Our goal is to make cities safer, cleaner, and smarter through technology-driven civic participation.

---

Problem Statement

Citizens frequently face civic problems such as:

- Damaged roads and potholes
- Garbage accumulation
- Water leakage
- Drainage and sewage issues
- Broken streetlights
- Damaged footpaths

Traditional complaint systems can make it difficult to categorize, prioritize, and track these problems efficiently.

 Our Solution

CivicFix AI provides a centralized platform where citizens can submit civic complaints and authorities can manage them through an organized dashboard.

The AI engine analyzes complaint descriptions and generates structured insights to support faster decision-making.

 Key Features

- Citizen Reporting: Submit civic complaints with descriptions, locations, and supporting images.
- AI-Powered Classification: Automatically identify the category of reported issues.
- Department Assignment: Suggest the appropriate department for each complaint.
- AI-Generated Summaries: Convert complaint descriptions into concise summaries.
- Priority Recommendations: Explain why an issue should receive attention.
- Admin Dashboard: View, monitor, and manage submitted complaints.
- Issue Tracking: Update complaint status from reported to resolved.

 How It Works

1. A citizen submits a complaint with a description and location.
2. The Flask backend receives the submitted information.
3. The AI engine analyzes the complaint.
4. The system identifies the issue category, severity, safety risk, and responsible department.
5. The analysis is stored in the database.
6. Administrators can view complaints and update their status through the dashboard.

 Technology Stack

Technology| Purpose
Python| Backend programming
Flask| Web application framework
OpenAI API| AI-powered complaint analysis
SQLite| Database management
HTML5| Frontend structure
CSS3| User interface styling
JavaScript| Frontend interactions

📂 Project Structure

CivicFix_AI/
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
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── app.js
    └── uploads/

Installation and Setup

1. Clone the repository

git clone https://github.com/saichandanahari/CivicFix-AI-Civic-Issue-Management.git

2. Navigate to the project directory

cd CivicFix-AI

3. Create a virtual environment

py -m venv venv

4. Install dependencies

Windows:

.\venv\Scripts\python.exe -m pip install -r requirements.txt

5. Configure environment variables

Create a ".env" file in the project root using ".env.example" as a template.

Add your OpenAI API key:

OPENAI_API_KEY=your_actual_api_key
OPENAI_MODEL=gpt-5-mini

Important: Never upload your ".env" file or expose your API key publicly.

6. Run the application

.\venv\Scripts\python.exe app.py

7. Open in your browser

http://127.0.0.1:5000

 Environment Variables

Variable| Description
OPENAI_API_KEY| API key used for AI analysis
OPENAI_MODEL| OpenAI model used for complaint analysis

If the API key is not configured or AI analysis fails, the application uses its fallback rule-based analyzer.

      Developed For
HackDevengers 2.0 – Open Innovation Hackathon
Project: CivicFix AI
Category: Artificial Intelligence | Smart Cities | Civic Technology
 Our Vision
"Better cities begin with better communication between citizens and authorities."
CivicFix AI aims to transform everyday civic complaints into actionable insights and help build cleaner, safer, and smarter communities.
