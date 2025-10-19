# FlowRAG: Agentic RAG Workflow Platform (FastAPI + Inngest + Qdrant)

FlowRAG is a powerful, event-driven platform for **Retrieval-Augmented Generation (RAG)** that uses a modern Python stack to ingest documents, generate embeddings, store them in a vector database, and provide grounded answers.

This project showcases a complete, production-ready RAG architecture orchestrated as reliable workflows and served through a clean user interface.

---

## 📺 Video Demo

[Watch the video on YouTube](https://youtu.be/eunl83jkD_8)

<p align="center">
  <a href="https://youtu.be/eunl83jkD_8" target="_blank">
    <img src="https://i9.ytimg.com/vi_webp/eunl83jkD_8/mqdefault.webp?v=68f55d68&sqp=CIi61ccG&rs=AOn4CLDQa8y0Oo_E_8eh8kTu7mYtZ0p47g" alt="Project Demo" width="60%">
  </a>
</p>


---

## 🚀 Key Features

* **User Interface (UI):** A simple, interactive Streamlit front-end for uploading PDFs and asking questions.
* **Event-Driven Ingestion:** Uses Inngest to define reliable workflows for ingesting new PDFs, ensuring chunking, embedding, and storage are handled idempotently and with retries.
* **Vector Storage:** Leverages Qdrant for high-performance vector indexing and retrieval.
* **High-Quality Context:** Utilizes LlamaIndex for intelligent PDF loading and chunking, optimized for RAG.
* **Modern API Backbone:** Built on FastAPI to expose the ingestion and querying endpoints, while Inngest manages asynchronous execution.
* **LLM Grounding:** Employs OpenAI (specifically `gpt-4o-mini`) for generating concise, context-aware answers with source attribution.

---

## ⚙️ Technology Stack

| Component           | Technology                   | Role                                                                         |
| ------------------- | ---------------------------- | ---------------------------------------------------------------------------- |
| **Language**        | Python 3.11+                 | Primary development language                                                 |
| **Front-End**       | Streamlit                    | Simple, interactive web interface for users                                  |
| **Web Server**      | FastAPI                      | High-performance API layer                                                   |
| **Workflow Engine** | Inngest                      | Event-driven orchestration of RAG pipelines                                  |
| **Vector DB**       | Qdrant                       | Vector indexing and retrieval                                                |
| **Embedding/LLM**   | OpenAI API                   | Generating embeddings (`text-embedding-3-large`) and answers (`gpt-4o-mini`) |
| **Data Loader**     | LlamaIndex Readers/Splitters | Processing and splitting PDF files                                           |

---

## 📐 Architecture Overview

The system defines two main asynchronous workflows managed by Inngest, triggered by events sent from the Streamlit UI:

### **1. rag/ingest_pdf (Ingestion Workflow)**

* **Trigger:** User uploads a PDF via Streamlit.
* **Steps:** Load → Chunk → Embed → Upsert to Qdrant.

### **2. rag/query_pdf_ai (Query Workflow)**

* **Trigger:** User asks a question via Streamlit.
* **Steps:** Embed Question → Search Qdrant for Context → Construct LLM Prompt → Generate Answer.

---

## 🛠️ Installation and Local Setup

To run this project locally, you will need to start three main components: the Qdrant vector database, the Inngest Development Server, and the Python application servers (FastAPI and Streamlit).

### **Prerequisites**

* **Docker:** Required to run the Qdrant vector database.
* **Python 3.11+**
* **OpenAI API Key:** Set in your environment or `.env` file.

---

### **Step 1: Clone and Install Dependencies**

```bash
git clone https://github.com/syedshahidashiqali/document-rag-ai-agent.git
cd document-rag-ai-agent

# Install dependencies using uv
uv sync
```

If you add new packages later:

```bash
uv add <package-name>
```

To run your app in an isolated environment:

```bash
uv run python main.py
```

---

### **Step 2: Start Qdrant**

Run Qdrant via Docker:

```bash
docker run -p 6333:6333 -d qdrant/qdrant
```

---

### **Step 3: Configure Environment Variables**

Create a file named `.env` in the root directory:

```bash
# Required for embedding and LLM calls
OPENAI_API_KEY="sk-..."

# Optional: Configuration for Qdrant
QDRANT_URL="http://localhost:6333"
```

---

### **Step 4: Run the Services**

You must run the **Inngest Dev Server**, **FastAPI**, and **Streamlit UI** in separate terminals.

#### **Terminal 1: Start the Inngest Dev Server (Main)**

This runs the local Inngest development engine.

```bash
npx inngest-cli@latest dev
```

#### **Terminal 2: Start the Inngest Dev Server (Linked to FastAPI)**

This connects the Inngest Dev Server to your FastAPI backend.

```bash
npx inngest-cli@latest dev -u http://127.0.0.1:8000/api/inngest --no-discovery
```

#### **Terminal 3: Start the Streamlit UI**

This is the user interface where you can upload files and ask questions.

```bash
uv run streamlit run ./streamlit_app.py
```

Then open your browser to the URL provided by Streamlit (usually `http://localhost:8501`) to start interacting with **FlowRAG**!

---

## 🧠 Author

Developed by [**Shahid Ali**](https://github.com/syedshahidashiqali) — Full Stack Developer & n8n Automation Specialist.

---

## 🧩 Future Improvements

* ✅ Add document versioning and metadata filters.
* ✅ Support multi-file ingestion and multi-turn question answering.
* ✅ Integrate local embeddings (e.g., SentenceTransformers) for offline mode.
* ✅ Add Docker Compose setup for one-click deployment.

---

## 📜 License

This project is open-source under the **MIT License**.
