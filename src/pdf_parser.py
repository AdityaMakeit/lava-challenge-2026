import fitz


def open_pdf(pdf_path):
    return fitz.open(str(pdf_path))


def get_page_count(document):
    return len(document)


def get_page(document, page_number):
    return document[page_number]


def extract_page_text(page):
    return page.get_text()


def extract_all_pages(document):
    pages = []

    for page_number in range(len(document)):
        page = document[page_number]

        pages.append({
            "page": page_number + 1,
            "text": extract_page_text(page)
        })

    return pages