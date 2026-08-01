from pypdf import PdfReader

reader = PdfReader("corporate_report.pdf")

full_text = ""
for page in reader.pages:
    full_text += page.extract_text() + "\n"

print(full_text[:500])  # Print the first 500 characters of the extracted text
print("Total characters extracted:", len(full_text))

def split_into_chunks(text, chunk_size=500):
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        current_chunk.append(word)
        current_length += len(word) + 1  # +1 for the space
        if current_length >= chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_length = 0

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

chunks = split_into_chunks(full_text)
print("Number of chunks:", len(chunks))
print("First chunk:", chunks[0])  # Print the first 200 characters of the first chunk