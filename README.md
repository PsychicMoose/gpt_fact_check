# 🧠 GPT Fact Checker – Chrome Extension

A right-click fact-checking Chrome extension powered by GPT-4. Highlight any text on a webpage, right-click, and instantly get a verdict on whether it's true, false, or uncertain—plus a short explanation, all via OpenAI.

---

## ⚙️ Features

- ✅ Right-click on any selected text to fact-check it
- 🧠 GPT-4 evaluates claims based on public knowledge
- 🖥️ Local Flask backend processes the request securely
- 🔐 Keeps your OpenAI API key private with `.env` setup
- 🔔 Results delivered via Chrome notification

---
Demo:

![image](https://github.com/user-attachments/assets/bf87ef38-48b7-49da-9cb4-cc7b2b4149fe)


## 🚀 Setup Instructions

### 🔧 Extension (Frontend)
1. Clone or download this repo
2. Go to `chrome://extensions/` in Chrome
3. Enable **Developer Mode**
4. Click **Load unpacked** → select the extension folder
5. Right-click any text on a webpage → “**Fact Check with GPT**”

---

### 🧠 Flask Backend (Python)

#### 1. Install dependencies:

pip install flask openai python-dotenv flask-cors

#### 2. set up api key
create a .env file with your API key
OPENAI_API_KEY=sk-...
