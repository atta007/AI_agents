
# 🤖 AI Agents Project

This project is an AI-powered automation framework designed to work with agent-like systems. It includes tools for reading documents, interacting with APIs, and processing user input with intelligent agents.

---

## 📦 Features

- Modular AI agent system
- Environment config with `.env`
- Document reading (e.g. LinkedIn profiles, resumes)
- Integration with OpenAI, Grok, and more
- Gradio-based UI

---

## 🚀 Getting Started

Follow these steps to set up the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/atta007/AI_agents.git
cd AI_agents
```

### 2. Create Assets Folder

```bash
mkdir assets
```

> Used for uploading PDF files or other input data.

### 3. Create & Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Required Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Set Up Environment Variables

Copy the example `.env` file and fill in the required values:

```bash
cp .env.example .env
```

Edit the `.env` file:

```bash
nano .env
```

> Make sure to include your API keys and other necessary credentials.

---

### 6. Run the Application

```bash
python main.py
```

---

## 🛠 Troubleshooting

- Make sure you are using **Python 3.9+**
- Activate the virtual environment before running any scripts
- Check `.env` values carefully (API keys, etc.)
- If `main.py` is slow or stalls, test API latency or inspect logs

---

## 📁 Project Structure

```
AI_agents/
│
├── assets/             # Store input PDFs and data files
├── agents/             # Agent logic and tools
├── .env.example        # Environment variable example
├── main.py             # Entry point
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## 📬 Contact

Maintainer: [@atta007](https://github.com/atta007)