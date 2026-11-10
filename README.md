# NOTE2BRAINS

An AI-powered learning platform that turns uploaded documents into summaries, quizzes, and flashcards.

**[Frontend demo](https://note2brains.vercel.app)** · **[Source code](https://github.com/Looks0ng/note2brains)**

The frontend demo is separate from the Python backend. Document processing and learning features require a running backend, a configured database, and access to the external AI services. Some frontend requests currently target `http://localhost:8000`, so the hosted frontend alone does not demonstrate the complete workflow.

## What the application does

- Upload learning documents for text extraction and summarization.
- Review documents and their extracted content.
- Generate quizzes and flashcards from learning materials.
- Submit quiz answers and review results and learning history.
- Register and sign in to access user-associated learning data.

## Team project

NOTE2BRAINS is a collaborative project combining frontend development, backend services, document processing, and AI integrations. This README describes the application and the team's shared implementation.

## Technology stack

| Layer | Technologies |
| --- | --- |
| Frontend | React, JavaScript, CSS, React Router, Lucide React |
| Backend | Python, FastAPI, Uvicorn |
| Database | PostgreSQL, Prisma Client Python |
| Document and AI processing | Typhoon OCR/LLM integration, PyPDF2 |
| Frontend hosting | Vercel |

## Application flow

1. A user uploads a learning document through the React frontend.
2. FastAPI handles the document-processing request and calls the document/AI services.
3. Document data and generated learning content are stored through Prisma in PostgreSQL.
4. The frontend displays document content, quizzes, flashcards, and quiz results through backend API calls.

## Repository structure

```text
note2brains/
├── frontend/
│   ├── public/
│   ├── src/                 # React screens, components, styles, API calls
│   └── package.json
└── backend/
    ├── app.py               # FastAPI entry point; includes application routers
    ├── main.py              # Account and related routes
    ├── quiz.py              # Quiz generation and attempts
    ├── flashCard.py         # Flashcard generation
    ├── db.py                # Prisma client
    ├── prisma/schema.prisma # PostgreSQL schema
    └── requirements.txt
```

## Local development

These instructions describe the current repository structure. A complete local run requires your own database and AI-service configuration; the application has not been freshly runtime-tested as part of this documentation update.

### 1. Get the source

```bash
git clone https://github.com/Looks0ng/note2brains.git
cd note2brains
```

### 2. Configure and start the backend

Use a Python virtual environment, then install the backend dependencies:

```bash
cd backend
python -m venv .venv
```

Activate the environment using `.venv\Scripts\activate` on Windows Command Prompt, `.\.venv\Scripts\Activate.ps1` on PowerShell, or `source .venv/bin/activate` on macOS/Linux.

```bash
python -m pip install -r requirements.txt
```

Configure `DATABASE_URL` for a development PostgreSQL database. Configure your own Typhoon credentials for the OCR and language-model integrations; check `app.py`, `quiz.py`, and `flashCard.py` for the configuration expected by each integration. Keep credentials outside version control.

Generate the Prisma client and apply the schema to your development database:

```bash
prisma generate
prisma db push
python -m uvicorn app:app --reload --port 8000
```

The backend API documentation is available at `http://localhost:8000/docs` when the server is running.

### 3. Start the frontend

In another terminal, from the repository root:

```bash
cd frontend
npm install
npm start
```

The frontend normally starts at `http://localhost:3000`.

### Current development notes

- Several frontend components use `http://localhost:8000` directly. Update those URLs when connecting to a remote backend.
- `frontend/src/api.js` imports Axios, but Axios is not currently listed in `frontend/package.json`. If that module is used, add the dependency or align the module with the Fetch API used elsewhere.
- A hosted frontend does not imply that the backend or external AI services are available.

