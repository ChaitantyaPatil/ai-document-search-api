# 🚀 AI-Powered Document Search & Q&A API (RAG)

A production-style **FastAPI backend** that allows users to upload documents, perform **semantic search** using embeddings, and ask **natural language questions** answered via a **Retrieval-Augmented Generation (RAG)** pipeline using **Hugging Face LLMs (OpenAI-compatible SDK)**.

---

## ✨ Key Features

* 📄 Upload and process documents
* 🧠 Text extraction and chunking
* 🔢 Embedding generation for document chunks
* 🔍 Semantic search using cosine similarity
* 🤖 Context-aware Q&A using Hugging Face Router (Qwen LLM)
* ⚡ Async FastAPI APIs with Swagger UI
* 🧱 Clean, layered architecture (API, service, repository)

---

## 🧠 System Architecture (High Level)

```
User Query
   ↓
Generate Query Embedding
   ↓
Semantic Search (Cosine Similarity)
   ↓
Relevant Document Chunks
   ↓
Prompt Construction
   ↓
Hugging Face LLM (Qwen via Router)
   ↓
Final Answer + Sources
```

---

## 🛠️ Tech Stack

* **Backend:** FastAPI, Python
* **AI / NLP:** Sentence Embeddings, RAG
* **LLM:** Hugging Face Router (Qwen – OpenAI compatible)
* **Database:** SQLAlchemy (SQLite / PostgreSQL ready)
* **Vector Search:** In-memory cosine similarity (FAISS ready)
* **Docs:** Swagger / OpenAPI
* **Config:** python-dotenv

---

## 📁 Project Structure

```
app/
├── api/
│   ├── search.py        # Semantic search endpoint
│   ├── ask.py           # RAG-based Q&A endpoint
│
├── core/
│   └── config.py        # Environment configuration
│
├── models/
│   └── document_chunk.py
│
├── repositories/
│   └── chunk_repository.py
│
├── services/
│   ├── embedding_service.py
│   ├── search_service.py
│   └── llm_service.py
│
├── utils/
│   ├── similarity.py
│   └── prompt_builder.py
│
├── db/
│   └── session.py
│
└── main.py
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/<your-username>/ai-document-search-api.git
cd ai-document-search-api
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Environment Variables

Create a `.env` file:

```env
HF_TOKEN=hf_xxxxxxxxxxxxxxxxx
HF_MODEL=Qwen/Qwen3-Coder-Next:novita
```

⚠️ **Never commit `.env` to Git**

---

### 5️⃣ Run the Application

```bash
uvicorn app.main:app --reload
```

Access:

* API → [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Swagger → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🔍 Semantic Search API

**POST** `/search`

```json
{
  "query": "What is FastAPI?",
  "top_k": 3
}
```

Returns most relevant document chunks using embeddings.

---

## 🤖 Ask Question (RAG)

**POST** `/ask`

```json
{
  "question": "What is FastAPI used for?"
}
```

### Sample Response

```json
{
  "question": "What is FastAPI used for?",
  "answer": "FastAPI is a modern Python web framework used for building APIs...",
  "sources": [
    {
      "document_id": 1,
      "chunk_id": 12,
      "score": 0.91,
      "text": "FastAPI is a high-performance web framework..."
    }
  ]
}
```

---

## 🔐 LLM Integration Details

* Uses **Hugging Face Router**
* OpenAI-compatible SDK
* Easy model switching without code changes

```python
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN,
)
```

---

## 🧾 Resume Description

> Built an AI-powered document search and Q&A system using FastAPI and Retrieval-Augmented Generation (RAG). Implemented semantic search with embeddings and cosine similarity, and integrated Hugging Face LLMs (Qwen) via OpenAI-compatible APIs to generate context-aware answers from enterprise documents.

---

## 🚀 Future Enhancements

* 🔹 FAISS / Vector DB integration
* 🔹 Authentication & rate limiting
* 🔹 Docker & cloud deployment
* 🔹 Streaming LLM responses
* 🔹 Multi-document citation ranking

---

## 👤 Author

**Chaitanya Patil**
Software Developer | Backend & AI Enthusiast

---

Just say the word 🚀
