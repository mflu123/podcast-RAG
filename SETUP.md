# Setup Instructions

## Prerequisites

- Python 3.8+
- OpenAI API Key, this project ueses the gpt 4o mini llm
- Pinecone API Key (for cloud vector storage) 

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd podcast-RAG
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Configuration**:
   Create a `.env` file in the root directory and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   PINECONE_API_KEY=your_pinecone_api_key_here
   ```

## Running the Project
If you want to access this project and test apis, you can access it on the internet at this link:

https://podcast-rag-2kvzffxnrjnzmfqbbcb6rf.streamlit.app/

To run the project locally, make sure to read the Quick Start section in the README.md first. 



### 1. Run Notebooks

For data ingestion, analysis, or evaluation:
1. Navigate to the `notebooks/` directory.
2. Open `create_database.ipynb` to process transcripts and create the vector database (Local ChromaDB or Pinecone).
3. Open `json.ipynb` to run the evaluation suite and test the RAG pipeline programmatically.

### 2. Run the Chatbot Application 
Once database is created, if you want to run locally:
The main interface is a Streamlit web app.
```bash
streamlit run app.py
```
This will launch the chatbot in your default web browser.

## Testing for Graders
To verify the system functionality and API functionality:
Go to online website at: https://podcast-rag-2kvzffxnrjnzmfqbbcb6rf.streamlit.app/
OR to run locally:

1. Ensure `.env` is set up with valid keys.
2. After following quick start directions run `streamlit run app.py`.
3. Ask a specific question like: *"In episode 500, what did Ira Glass compare the milestone of reaching 500 episodes to?"*
4. Verify that the bot answers and cites the source.
