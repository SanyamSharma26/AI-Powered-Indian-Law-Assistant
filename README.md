# ⚖️ LegalAI – AI-Powered Legal Document Summarization & Translation System

> An AI-driven web platform that helps lawyers, researchers, and citizens **summarize, analyze, and translate legal documents** in multiple Indian languages.

---

## 🧠 Overview

**LegalAI** automates the reading and interpretation of legal texts using modern NLP models.  
Users can upload judgments, petitions, or legal acts, and receive:
- **Concise summaries** using state-of-the-art Transformer models  
- **Extracted legal citations** (Sections, Articles, Case Laws, Acts)  
- **Multilingual translations** (Hindi, Tamil, Punjabi, Gujarati, Bengali, etc.)  
- **Chat-based interaction** with uploaded documents (LLM integration-ready)  

---

## 🚀 Features

- 🗂️ **Upload & Extract** – Upload PDFs, DOCX, or TXT files and extract clean text using `PyPDF2` and `python-docx`.  
- 🧾 **AI Summarization** – Summarize legal content via Hugging Face’s `distilbart-cnn-12-6` model.  
- ⚖️ **Citation Extraction** – Detect Acts, Articles, and IPC/CrPC sections via regex-based parsing.  
- 🌐 **Multilingual Translation** – Translate summaries into 10+ Indian languages using `googletrans`.  
- 💬 **Chat Sessions (LLM-Ready)** – Attach documents and chat contextually (OpenRouter API integration point).  
- 🔐 **User Management** – OTP-based signup, profile pictures, document history, and session tracking.  

---

## 🧩 Tech Stack

| Layer | Technologies |
|-------|---------------|
| **Frontend** | HTML, CSS, Bootstrap |
| **Backend** | Django 5 |
| **AI / NLP** | Hugging Face Transformers, PyTorch |
| **Utilities** | PyPDF2, python-docx, googletrans, langdetect |
| **Database** | SQLite (default) |
| **Deployment** | Localhost / Render / Docker (optional) |

---

## 🗃️ Project Architecture

```
legalAI/
├── mainApp/                  # Authentication, dashboard, chat, translator
│   ├── utils/                # Text extraction, translation, IP lookup
│   ├── templates/            # UI pages
│   └── static/css/           # Styling for login, dashboard, etc.
├── summarizer/               # Summarization & citation extraction
│   └── utils/                # summarize.py, translator.py, extract_citations.py
├── law_data/                 # Indian Acts & Sections data
├── legalAI/                  # Project settings & URL routing
├── requirements.txt
└── manage.py
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/legalAI.git
cd legalAI
```

### 2️⃣ Create & activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate      # (Linux/Mac)
.venv\Scripts\activate       # (Windows)
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables  
Create a `.env` file in the project root:
```bash
DEBUG=True
SECRET_KEY=your_django_secret
OPENROUTER_API_KEY=your_openrouter_key
```

### 5️⃣ Apply migrations & run server
```bash
python manage.py migrate
python manage.py runserver
```

### 6️⃣ Access the app  
Open your browser at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧮 Example Workflow

1. **Sign Up** → Verify OTP → Log In  
2. **Upload Document** → Text extracted & summarized  
3. **View Summary** → Translate if needed  
4. **Extract Citations** → View IPC/CrPC/Act references  
5. **Chat with Document** (optional)  

---

## 🔐 Security & Privacy

- OTP verification for users  
- Per-user document storage  
- `.env` for API keys and secret values  
- Future scope for **RAG-based** retrieval on Indian legal databases  

---

## 🎯 Future Enhancements

- 🧩 Retrieval-Augmented Generation (RAG) for grounded Q&A  
- 📚 FAISS/Qdrant vector database integration  
- 🤖 Advanced LLM summarization (Mistral / Llama 3)  
- 🔍 Named Entity Recognition for legal citations  
- ☁️ Docker & cloud deployment with Gunicorn/Nginx  

---

## 🧑‍💻 Author

**Sanyam Sharma**  
B.E. Computer Engineering – Thapar Institute of Engineering & Technology (TIET), Patiala  
📫 [GitHub](https://github.com/SanyamSharma26) • [LinkedIn](https://linkedin.com/in/sanyamsharma26)  

---

> ⚖️ *“Empowering justice through intelligent automation.”*

