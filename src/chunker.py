def chunk_text(text, chunk_size=500):

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunk = text[i:i + chunk_size]

        chunks.append(chunk)

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