# 🧠 FlowRAG: Agentic RAG Workflow Platform

**FlowRAG** is a powerful, event-driven platform for **Retrieval-Augmented Generation (RAG)** built with a modern Python stack. It processes unstructured documents (like PDFs), generates embeddings, stores them in a vector database, and provides grounded, context-aware answers via a large language model.

This project demonstrates a **production-ready RAG architecture** orchestrated as a series of reliable, event-driven workflows.

---

## 🚀 Key Features

- **Event-Driven Ingestion**  
  Uses **Inngest** to define reliable workflows for ingesting new PDFs, ensuring chunking, embedding, and storage are handled *idempotently* and with retries.

- **Vector Storage**  
  Leverages **Qdrant** for high-performance vector indexing and retrieval.

- **High-Quality Context**  
  Utilizes **LlamaIndex** for intelligent PDF loading and chunking, optimized for RAG performance.

- **Modern API Backbone**  
  Built on **FastAPI**, exposing clean ingestion and querying endpoints.

- **LLM Grounding**  
  Employs **OpenAI’s `gpt-4o-mini`** for generating concise, context-aware answers grounded in retrieved content.

---

## ⚙️ Technology Stack

| Component        | Technology                  | Role                                           |
|------------------|-----------------------------|------------------------------------------------|
| **Language**     | Python 3.11+                | Primary development language                   |
| **Web Server**   | FastAPI                     | High-performance API layer                     |
| **Workflow Engine** | Inngest                 | Event-driven orchestration of RAG pipelines    |
| **Vector DB**    | Qdrant                      | Vector indexing and retrieval                  |
| **Embedding / LLM** | OpenAI API              | Embeddings (`text-embedding-3-large`) and LLM (`gpt-4o-mini`) |
| **Data Loader**  | LlamaIndex Readers/Splitters | PDF loading, processing, and chunking          |

---

## 📐 Architecture Overview

FlowRAG defines two main asynchronous workflows powered by **Inngest**:

### 🧩 `rag/ingest_pdf` — *Ingestion Workflow*
**Input:** Path to a PDF file  
**Steps:**  
`Load → Chunk → Embed → Upsert to Qdrant`

### 💬 `rag/query_pdf_ai` — *Query Workflow*
**Input:** User question  
**Steps:**  
`Embed Question → Search Qdrant → Construct LLM Prompt → Generate Answer`

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/flowrag.git
cd flowrag
