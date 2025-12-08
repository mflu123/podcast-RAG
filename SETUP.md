# Setup Instructions

## Prerequisites

- Python 3.8+
- OpenAI API Key
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

### 1. Run the Chatbot Application (Recommended)
The main interface is a Streamlit web app.
```bash
streamlit run app.py
```
This will launch the chatbot in your default web browser.

### 2. Run Notebooks
For data ingestion, analysis, or evaluation:
1. Navigate to the `notebooks/` directory.
2. Open `create_database.ipynb` to process transcripts and create the vector database (Local ChromaDB or Pinecone).
3. Open `json.ipynb` to run the evaluation suite and test the RAG pipeline programmatically.

## Testing for Graders
To verify the system functionality:
1. Ensure `.env` is set up with valid keys.
2. Run `streamlit run app.py`.
3. Ask a specific question like: *"In episode 462, what did Ira Glass and Steve Blass talk about?"*
4. Verify that the bot answers correctly and cites the source.
