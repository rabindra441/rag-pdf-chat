import chromadb
from groq import Groq
import os

client_db = chromadb.PersistentClient(path="./chroma_db")
collection = client_db.get_or_create_collection("pdf_chunks")

client_ai = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def ask_question(question):
    results = collection.query(
        query_texts=[question],
        n_results=3
    )

    relevant_chunks = results["documents"][0]

    print("DEBUG - Retrieved chunks:", relevant_chunks)

    context = "\n".join(relevant_chunks)

    prompt = f"""Answer the question based only on the context provided below. If the exact wording isn't a perfect match, but do not use any information outside the context.

    Context:
    {context}

    Question: {question}
    Answer:"""

    print("DEBUG - Prompt sent to AI model:", prompt)

    response = client_ai.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
        )
    return response.choices[0].message.content

#
# print("Q1:", "How much does the monitoring service cost?")
# print("A1:", ask_question("How much does the monitoring service cost?"))
# print()
# print("Q2:", "What is the company's return policy?")
# print("A2:", ask_question("What is the company's return policy?"))
# print()
# print("Q3:", "Do you sell smartphones?")
# print("A3:", ask_question("Do you sell smartphones?"))
print("Q4:", "How many years AI is working in industry?")
print("A4:", ask_question("How many years AI is working in industry?"))