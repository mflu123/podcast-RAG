# Project Title: Podcast RAG Chatbot for "This American Life"

A Retrieval-Augmented Generation (RAG) chatbot designed to answer detailed questions about "This American Life" podcast episodes by retrieving and synthesizing information from transcripts.

## What it Does

This project implements a specialized AI assistant that helps users explore the vast archive of "This American Life" podcast transcripts. Instead of relying on general knowledge which often hallucinates specific episode details, the system uses a RAG pipeline to retrieve exact transcript segments relevant to a user's query. It features an intelligent router that distinguishes between casual greetings, general knowledge questions, and specific podcast queries. The system is accessible via a user-friendly Streamlit web interface where users can chat with the bot and view the exact source documents used to generate each answer. The llm used for this project is gpt-4o mini and the data is stored in on pinecone cloud. 

## Quick Start

This project is deployed on the internet and can be accessed at this link:

https://podcast-rag-2kvzffxnrjnzmfqbbcb6rf.streamlit.app/


If you want to set this project up locally, follow these instructions:

1. **Download Data**: The data for the RAG was too big for github, instead it can be accessed at this link: https://duke.box.com/s/to632zn4o0pdfezhubtj0kkoc5rfi8kj
Once data is downloaded, store it in the data folder.

2.  **Install Dependencies**: Ensure you have Python 3.8+ and install requirements:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure Keys**: Create a `.env` file with your `OPENAI_API_KEY` and `PINECONE_API_KEY`.
4. **Load Database**: To create the database for the RAG, go to the create_database.ipynb notebook and run the notebook. This will create a local database in models/tal_chroma which can be used for testing locally and also will create the cloud database in pinecone which is needed to deploy the streamlit app. 

5.  **Run the App**:
    ```bash
    streamlit run app.py
    ```
    The application will open in your browser at `http://localhost:8501`.

*For detailed installation and setup instructions, please refer to [SETUP.md](SETUP.md).*

## Video Links

*   **Demo Video**: https://duke.box.com/s/55wqjksxg02lwkptcspwmvl4ztwwja89
*   **Technical Walkthrough**: https://duke.box.com/s/d8d9n5mptkhcp2yglltu5m3vrw0u0gt2


## Evaluation

The system was evaluated using a "Golden Set" of 25 diverse questions in the json.ipynb notebook ranging from specific episode titles to detailed content queries. We compared the performance of the RAG system against a "Vanilla" LLM (GPT-4o-mini without context).

**Results:**
*   **RAG Accuracy**: 72%
*   **Vanilla LLM Accuracy**: 24%


The evaluation demonstrates that the RAG pipeline significantly outperforms the base model on domain-specific queries. While the Vanilla model struggled with specific episode numbers and obscure details (often hallucinating or refusing to answer), the RAG system successfully retrieved the correct transcripts to provide accurate, grounded answers.

**Qualitative Analysis:**
After analyzing the type of questions that the chatbot often gets incorrect, it often does not have the information to answer questions regarding exact episode name. This is due to the fact that the documents that are retrieved by the chatbot do not list the episode title name, instead they only list the episode number. Therefore, a limitation for this chatbot are queries that inquire about specific episode names. Instead, users must specify the episode number to use the chatbot to its full capabilities. This utilizes a episode metadata filter, if a user asks a question about a specific episode number, the chatbot will only retrieve documents with the episode metadata filter, improving accuracy. 

## Individual Contributions

This project was completed individually by Matthew Lu. All components, including data processing, RAG pipeline implementation, frontend development, and evaluation, were designed and built by the author.
