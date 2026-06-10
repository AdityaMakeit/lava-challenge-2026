def chunk_text(
    text,
    chunk_size=500,
    overlap=100
):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        if len(chunk.strip()) >= 100:
         chunks.append(chunk)

        start += chunk_size - overlap

    return chunks

def chunk_pages(pages, chunk_size=500):

    all_chunks = []

    for page in pages:

        text_chunks = chunk_text(
            page["text"],
            chunk_size
        )

        for chunk_id, chunk in enumerate(text_chunks):

            all_chunks.append(
                {
                    "page": page["page"],
                    "chunk_id": chunk_id,
                    "text": chunk
                }
            )

    return all_chunks

