import chromadb
from extractPdf import full_text, split_into_chunks

client = chromadb.PersistentClient(path="./chroma_db")

try:
    client.delete_collection("pdf_chunks")
    print("[DEBUG] Wiped old collection.")
except Exception:
    print("[DEBUG] No existing collection found. Creating a fresh one...")

collection = client.get_or_create_collection("pdf_chunks")

print("[DEBUG] Segmenting corporate_report.pdf text into chunks...")
real_chunks = split_into_chunks(full_text, chunk_size=500)

chunk_ids = [f"id_{i}" for i in range(len(real_chunks))]

collection.add(
    documents=real_chunks,
    ids=chunk_ids
)
print(f"Success! Fully indexed {len(real_chunks)} corporate chunks into database")

# results = collection.query(
#     query_texts=[questions],
#     n_results=2
# )

# print("Question:", questions)
# print("Most relevant chunks found:")
# for doc in results["documents"][0]:
#     print("-", doc)