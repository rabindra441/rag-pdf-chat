
import chromadb
from groq import Groq
import os

# 1. Connect directly to existing vector database
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("pdf_chunks")
client_ai = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# 2. Initialize  Groq client (Make sure  API key environment variable is set!)
# groq_client = Groq()

def query_corporate_rag(user_question: str) -> str:
    # A. Search ChromaDB for the closest 3 matching chunks
    results = collection.query(
        query_texts=[user_question],
        n_results=3
    )

    # B. Extract the matching text blocks
    retrieved_chunks = results['documents'][0]
    context = "\n---\n".join(retrieved_chunks)

    # C.Professional corporate prompt
    system_prompt = (
        "You are an advanced Enterprise Financial and Compliance AI Assistant. "
        "Answer the user's question using ONLY the provided document context below. "
        "If the context does not contain the answer, respond exactly with: "
        "'I am sorry, but the provided corporate documentation does not contain sufficient data to answer this query.' "
        "Maintain an objective, institutional, and professional tone. Do not speculate."
    )

    user_prompt = f"Context:\n{context}\n\nQuestion: {user_question}"

    # D. Fire the request to Groq LLM
    try:
        completion = client_ai.chat.completions.create(
            model="llama-3.3-70b-versatile", # or your preferred llama3/mixtral model
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.0
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error calling Groq API: {str(e)}"

# Quick local test loop
if __name__ == "__main__":
    test_query = "What company is this report filed for and what is the document type?"
    print(f"Testing Query: {test_query}\n")
    print(query_corporate_rag(test_query))