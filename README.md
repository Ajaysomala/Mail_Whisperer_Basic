[README.MD](https://github.com/user-attachments/files/21654119/README.MD)
# 📬 Mail Whisperer: Your AI Email Summarizer Assistant

> A voice-powered AI assistant that fetches Gmail messages, filters important ones, summarizes them using NLP, and reads them out loud — with PDF report generation. Built with ❤️ using Python, Flask, and Google APIs.

---

## 🚀 Features

- 🔐 Connects to your Gmail inbox using OAuth 2.0
- 🧠 NLP-based summarization using LSA (Latent Semantic Analysis)
- 🗣️ Converts summaries into human-like speech (`gTTS`)
- 📄 Automatically generates daily PDF report
- ☁️ Flask-powered backend (ready for frontend / voice assistant integration)
- 🎯 Modular, clean architecture ready for production
- 🧩 Designed for future character/voice interactivity

---

## 🏗️ Project Structure

mail_whisperer/
├── app/
│ ├── init.py # Flask app factory
│ ├── routes/ # REST API endpoints
│ ├── services/ # Gmail, summarizer, PDF, TTS logic
│ └── utils/ # Filters, helpers, cleaners
├── static/audio_output/ # Auto-saved TTS files
├── reports/ # Daily PDF reports
├── credentials.json # CREATE it IN your LOCAL FOLDER ⏪
├── token.json # CREATE it IN your LOCAL FOLDER ⏪
├── run.py # Main Flask entrypoint
├── .gitignore
└── README.md


---

## 🔐 Setup Google OAuth Credentials

> You need to enable Gmail API and create OAuth credentials.

### ✅ Step-by-step:

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project → APIs & Services → Enable Gmail API
3. Go to **Credentials** tab → "Create Credentials" → `OAuth Client ID`
4. Choose **Desktop App** or **Web Application**
5. Download `credentials.json`
6. Place it inside your project root:

7. The first time you run the app, it will ask for Gmail access and create `token.json`

---

## ⚙️ Install Dependencies

```bash
git clone https://github.com/YourUsername/Mail_Whisperer.git
cd Mail_Whisperer
pip install -r requirements.txt

🧠 Run Flask App (Backend API)
bash
Copy
Edit
python run.py
This will:

Fetch and summarize recent Gmail messages

Save TTS audio files in /static/audio_output/

Save PDF report in /reports/

✨ API Endpoints (To be implemented)
| Endpoint            | Method | Description                    |
| ------------------- | ------ | ------------------------------ |
| `/api/fetch-emails` | GET    | Fetch & summarize emails       |
| `/api/next-summary` | GET    | Get next email summary (audio) |
| `/api/pdf-report`   | GET    | Download the PDF report        |
| `/api/reset`        | POST   | Reset session (start over)     |


📦 Environment & Secrets
Never commit:

token.json

credentials.json

.env (if you add environment variables)

Your .gitignore should contain:

credentials.json
token.json
*.pdf
static/audio_output/
__pycache__/


📚 NLP Details
📄 Summarization done using sumy with LSA model

HTML cleaned using BeautifulSoup

Future: Replace with BART/T5 for advanced summarization

Keyword filtering is done using rule-based NLP

🧠 Credits
Developed by Ajay Somala
With guidance and tech alignment by Beru V2 (AI Assistant) 🦾

🛡️ Disclaimer
This project uses Google APIs. Keep your tokens and credentials secure. Do not upload sensitive files to GitHub or share them publicly.


---

## ✅ What You Should Do Now:

1. Copy the above and **replace your current `README.md`**
2. Edit:
   - Your GitHub URL
   - Any real names you want removed or changed
3. Push to GitHub **after removing secrets** (as discussed before)

Would you like me to also generate your `requirements.txt` now based on this setup?
