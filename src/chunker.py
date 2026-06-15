def chunk_text(
    text,
    page_number,
    chunk_size=500,
    min_chunk_size=100
):
    chunks = []

    paragraphs = [
        p.strip()
        for p in text.split("\n")
        if p.strip()
    ]

    current_chunk = ""

    for paragraph in paragraphs:

        if len(current_chunk) + len(paragraph) + 1 <= chunk_size:

            current_chunk += paragraph + "\n"

        else:

            if len(current_chunk.strip()) >= min_chunk_size:

                chunks.append(
                    {
                        "document_id": "j_0060",
                        "source":"j_0060.pdf",
                        "page": page_number,
                        "chunk_id": len(chunks),
                        "char_count": len(current_chunk.strip()),
                        "text": current_chunk.strip()
                    }
                )

            current_chunk = paragraph + "\n"

    if len(current_chunk.strip()) >= min_chunk_size:

        chunks.append(
            {
                "document_id": "j_0060",
                "source":"j_0060.pdf",
                "page": page_number,
                "chunk_id": len(chunks),
                "char_count": len(current_chunk.strip()),
                "text": current_chunk.strip()
            }
        )

    return chunks


def chunk_pages(
    pages,
    chunk_size=500
):
    all_chunks = []

    for page in pages:

        page_chunks = chunk_text(
            text=page["text"],
            page_number=page["page"],
            chunk_size=chunk_size
        )

        all_chunks.extend(page_chunks)

    return all_chunks