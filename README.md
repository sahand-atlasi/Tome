# Tome
Enterprise knowledge assistant (RAG over reports, meetings, docs)
# Tome

[![CI](https://github.com/sahand-atlasi/Tome/actions/workflows/ci.yml/badge.svg)](https://github.com/sahand-atlasi/Tome/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.12%20%7C%203.13-blue)
[![License](https://img.shields.io/badge/license-Apache--2.0-green)](LICENSE)

Tome is an enterprise knowledge assistant. Ask a question about a company's own documents
(reports, meeting notes, policies, project docs) and get an answer grounded in those documents,
with citations to the exact passages it used.

> Status: early development. See the [roadmap](#roadmap).

## How it works

1. **Ingest:** load PDF and Markdown files, split them into chunks, embed them with Gemini and
   store them in a local Chroma vector database.
2. **Ask:** embed the question, retrieve the most relevant chunks, and ask Gemini to answer
   using only those chunks.
3. **Cite:** every claim points to a source chunk; the server verifies the citations and refuses
   when the documents do not contain the answer.

## Getting started

Requirements: Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/sahand-atlasi/Tome.git
cd Tome
uv sync                       # create .venv and install locked dependencies
cp .env.example .env          # then add your GEMINI_API_KEY
uv run pytest                 # run the tests
```

## Development

```bash
uv run pre-commit install     # run formatting and lint checks before every commit
uv run ruff format .          # format
uv run ruff check .           # lint
uv run mypy                   # type check
uv run pytest                 # tests with coverage
```

Workflow: short-lived feature branches, pull requests into `main`, CI must pass,
squash merge with a [Conventional Commit](https://www.conventionalcommits.org/) title.

## Roadmap

- [x] v0.0.1 Foundations: project setup, tooling, CI
- [ ] v0.0.2 Ingestion: loaders, chunking, idempotent indexing
- [ ] v0.0.3 Retrieval: Gemini embeddings, Chroma, `/api/v1/search`
- [ ] v0.0.4 Grounded answers: cited answers, refusals, `/api/v1/ask`
- [ ] v0.0.5 Evaluation: golden question set and published metrics
- [ ] v0.1.0 Docker, demo UI, hosted demo

## License

[Apache-2.0](LICENSE)
