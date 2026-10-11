# Google GenAI Python Mini Bot

A simple, interactive, terminal-based conversational AI bot built with Python and Google's `google-genai` SDK. Developed as part of a learning course to explore multi-turn conversational AI sessions.

## Features

- **Continuous Multi-Turn Chat:** Maintains conversational history throughout the session.
- **Minimal Implementation:** Built with fewer than 20 lines of clean, readable Python code.
- **Graceful Exit:** Type `exit` to end the conversation.
- **Google Gemini Integration:** Uses Google's GenAI SDK to interact with a Gemini model.

## Tech Stack

- Python
- Google GenAI SDK (`google-genai`)
- Google Gemini API

## Getting Started

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
cd Google-GenAI-Python-Mini-Bot
```

### 2. Install Dependencies

```bash
pip install google-genai
```

### 3. Configure Your API Key

Get an API key from [Google AI Studio](https://aistudio.google.com/apikey).

Set it as an environment variable named `GEMINI_API_KEY`.

**Windows PowerShell:**
```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

** macOS / Linux:**
```bash
export GEMINI_API_KEY="your_api_key_here"
```

Keep your API key private. Never commit it to GitHub.

### 4. Run the Bot

```bash
python main.py
```

Replace `main.py` with your actual Python filename if it differs.

## Learning Objectives

- Understand how to integrate Google's GenAI SDK with Python.
- Explore multi-turn conversational sessions.
- Learn the basics of terminal-based AI applications.
- Practice writing minimal and readable Python code.

## Developer

**Rudra**

Built as a hands-on learning project while exploring generative AI and Python development.
