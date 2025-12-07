import os
import re
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.chat_models import ChatOpenAI
from pinecone import Pinecone

# Load environment variables
load_dotenv()

# Initialize global variables
_vector_store = None
_llm = None


def get_vector_store():
    global _vector_store
    if _vector_store is None:
        print("Connecting to Pinecone...")

        embeddings = OpenAIEmbeddings(
            model="text-embedding-3-small",
            openai_api_key=os.getenv("OPENAI_API_KEY"),
        )

        # Initialize Pinecone
        pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        index_name = "podcast-rag"  # Make sure this matches your Pinecone index name

        _vector_store = PineconeVectorStore(
            index_name=index_name,
            embedding=embeddings
        )
    return _vector_store


def get_llm():
    global _llm
    if _llm is None:
        _llm = ChatOpenAI(
            model_name="gpt-4o-mini",
            temperature=1,
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            verbose=False,
            streaming=False,
        )
    return _llm


def ask_podcast_rag(question: str):
    vector_store = get_vector_store()
    llm = get_llm()

    # 1. Try to extract an episode number for metadata filtering
    search_kwargs = {"k": 10}

    # Regex to find "episode <number>"
    match = re.search(r"episode\s+(\d+)", question, re.IGNORECASE)
    filter_used = None
    if match:
        ep_num = match.group(1)
        # Construct the ID format used in your metadata (e.g., "ep-462")
        filter_dict = {"episode": f"ep-{ep_num}"}
        search_kwargs["filter"] = filter_dict
        filter_used = filter_dict

    # 2. Retrieve documents
    docs = vector_store.similarity_search(question, **search_kwargs)

    # 3. Format context
    context = ""
    for i, doc in enumerate(docs):
        context += f"\nDocument {i + 1} (Episode {doc.metadata.get('episode')}):\n{doc.page_content}\n"

    # 4. Build prompt
    prompt = f"""You are a helpful assistant that answers questions strictly based on podcast transcripts.

You will be given a set of retrieved transcript excerpts as context.  
Use ONLY this context to answer the question.  
If the answer cannot be found or inferred from the context, say:  
"I do not have enough information from the provided context to answer."

Guidelines:
- Cite or reference relevant parts of the context in your reasoning.
- Do NOT invent facts, add details not in the context, or rely on prior general knowledge.
- If the question asks for something outside the given context, acknowledge the limitation.
- Provide concise, factual, and direct answers.
Context:
{context}

Question: {question}
"""

    # 5. Get answer
    response = llm.predict(prompt)

    return response, docs, filter_used
