# CivicFix AI Connected MVP

1. Create venv: `py -m venv venv`
2. Install: `./venv/Scripts/python.exe -m pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add your OpenAI API key.
4. Run: `./venv/Scripts/python.exe app.py`
5. Open `http://127.0.0.1:5000`

If no API key is configured, CivicFix automatically uses a fallback analyzer.
Never upload `.env` to GitHub.
