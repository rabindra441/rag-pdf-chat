from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import chromadb
import os
from groq import Groq

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Setup
client_db = chromadb.PersistentClient(path="./chroma_db")
collection = client_db.get_or_create_collection("kundalini_collection")

client_ai = Groq(api_key=os.environ.get("GROQ_API_KEY"))

class Question(BaseModel):
    question:str

@app.get("/")
def home():
    return {"message":"RAG API is running"}

@app.post("/ask")
def ask_question(data:Question):
    question = data.question

    results = collection.query(query_texts=[question], n_results=3)
    relevant_chunks = results["documents"][0]
    context = "\n".join(relevant_chunks)

    prompt = f"""Answer the question using the context below. Use reasonable inference if the exact wording isn't a perfect match, but do not use any information outside the context.

Context:{context}

Question:{question}
Answer."""

    response = client_ai.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role":"user", "content":prompt}]
    )

    return{"answer": response.choices[0].message.content}