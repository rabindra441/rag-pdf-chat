from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-l6-v2')

sentences = [
    "I love dogs",
    "Puppies are amazing",
    "The stock market crashed today"
]

embeddings = model.encode(sentences)
similarity_1 = util.cos_sim(embeddings[0], embeddings[1])
print("Similarity (dogs vs puppies):", similarity_1)

similarity_2 = util.cos_sim(embeddings[0], embeddings[2])
print("Similarity (dogs vs stock market):", similarity_2)

# print(embeddings.shape)
# print(embeddings[0][:5])