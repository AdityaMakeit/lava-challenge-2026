import re


def clean_text(text):

    text = text.strip()

    text = re.sub(
        r"\n\d+\s*$",
        "",
        text
    )

    return text


def clean_pages(pages):

    cleaned_pages = []

    for page in pages:

        cleaned_pages.append(
            {
                "page": page["page"],
                "text": clean_text(
                    page["text"]
                )
            }
        )

    return cleaned_pages