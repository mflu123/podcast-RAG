# Podcast RAG Project

This project implements a Retrieval-Augmented Generation (RAG) system for "This American Life" podcast transcripts. It allows users to ask questions about episodes and retrieves relevant context from the transcripts to generate accurate answers.

## Project Structure

- `src/`: Source code (if any non-notebook code exists).
- `data/`: Data files (transcripts, speaker maps).
- `models/`: Vector database and other model artifacts.
- `notebooks/`: Jupyter notebooks for exploration and analysis.
- `videos/`: Demo and walkthrough videos.
- `docs/`: Additional documentation.

## Features

- **Ingestion**: Chunks and embeds podcast transcripts.
- **Retrieval**: Uses ChromaDB for semantic search with metadata filtering.
- **Generation**: Uses OpenAI's GPT models to answer questions based on retrieved context.
- **Evaluation**: Includes a "Golden Set" evaluation loop with deterministic scoring.
