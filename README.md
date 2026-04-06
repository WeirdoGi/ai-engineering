# Document Q&A — RAG System

> Ask questions about any document in plain English and get accurate, context-aware answers.

## What is it?

A Retrieval Augmented Generation (RAG) system built in Python that lets you load any text document and query it conversationally. Instead of reading through an entire contract, handbook, or report manually, you ask it a question and it finds the relevant section and answers you accurately.

Supports multiple documents — choose which file to query at runtime without touching the code.

## Demo

```
Which file do you want to query?: software_contract.txt
Creating embeddings...
Stored 12 chunks in vector database

Ask a question: what happens if the client terminates early?

Answer:
Based on Article 8.2, if the Client terminates the agreement early "for convenience":

Financial Obligations
- Client must provide 60 days written notice to the Developer
- Client must pay for all work completed through the termination date
- Client must pay a termination fee of 15% of the remaining contract value

Important Note: If termination is "for cause" due to a Developer breach (Article 8.1),
the termination fee and 60-day notice requirement may not apply.
```

## How it works

```
Document → chunk into sections → embed with sentence-transformers
                                          ↓
                                     ChromaDB (vector store)
                                          ↓
User question → embed question → find closest chunks → send to Claude API
                                                               ↓
                                                        Natural language answer
```

## Tech stack

| Layer | Technology |
|---|---|
| LLM | Claude API (Anthropic) |
| Embeddings | sentence-transformers (all-MiniLM-L6-v2) |
| Vector store | ChromaDB |
| Language | Python |

## Getting started

```bash
# Clone the repo
git clone https://github.com/WeirdoGi/ai-engineering.git
cd ai-engineering

# Create virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows
source venv/bin/activate      # Mac/Linux

# Install dependencies
pip install anthropic chromadb sentence-transformers

# Set your API key
export ANTHROPIC_API_KEY="your-key-here"

# Run
python rag.py
```

## Usage

When prompted, enter the filename you want to query — any `.txt` file in the same directory works. Then ask questions in plain English.

```
Which file do you want to query?: acme_company_handbook.txt
Ask a question: what is the parental leave policy?
```

## Use cases

- **Legal** — query contracts for specific clauses, obligations, and deadlines
- **HR** — let employees ask questions about company policies
- **Research** — extract specific information from long reports
- **Onboarding** — new hires can query internal documentation instead of reading everything

## What's next

- PDF support
- Persistent vector storage so embeddings don't regenerate on every run
- Multi-document querying — ask across several files at once
- Simple web UI

---

Built by Tobin | Part of the [ai-engineering](https://github.com/WeirdoGi/ai-engineering) repo
