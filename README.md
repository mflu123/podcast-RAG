# Podcast RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot designed to answer detailed questions about "This American Life" podcast episodes by retrieving and synthesizing information from transcripts.

## What it Does

This project implements a specialized AI assistant that helps users explore the vast archive of "This American Life" podcast transcripts. Instead of relying on general knowledge which often hallucinates specific episode details, the system uses a RAG pipeline to retrieve exact transcript segments relevant to a user's query. It features an intelligent router that distinguishes between casual greetings, general knowledge questions, and specific podcast queries. The system is accessible via a user-friendly Streamlit web interface where users can chat with the bot and view the exact source documents used to generate each answer.

## Quick Start

1.  **Install Dependencies**: Ensure you have Python 3.8+ and install requirements:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Configure Keys**: Create a `.env` file with your `OPENAI_API_KEY` and `PINECONE_API_KEY`.
3.  **Run the App**:
    ```bash
    streamlit run app.py
    ```
    The application will open in your browser at `http://localhost:8501`.

*For detailed installation and setup instructions, please refer to [SETUP.md](SETUP.md).*

## Video Links

*   **Demo Video**: [Link to Demo Video]
*   **Technical Walkthrough**: [Link to Technical Walkthrough]

*(Please update these links with your actual video URLs)*

## Evaluation

The system was evaluated using a "Golden Set" of 11 diverse questions ranging from specific episode titles to detailed content queries. We compared the performance of the RAG system against a "Vanilla" LLM (GPT-4o-mini without context).

**Results:**
*   **RAG Accuracy**: 100.0%
*   **Vanilla LLM Accuracy**: 45.5%

The evaluation demonstrates that the RAG pipeline significantly outperforms the base model on domain-specific queries. While the Vanilla model struggled with specific episode numbers and obscure details (often hallucinating or refusing to answer), the RAG system successfully retrieved the correct transcripts to provide accurate, grounded answers.

## Individual Contributions

This project was completed individually by Matthew Lu. All components, including data processing, RAG pipeline implementation, frontend development, and evaluation, were designed and built by the author.
