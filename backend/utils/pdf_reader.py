import fitz


def extract_text_from_pdf(file_path: str):

    document = fitz.open(file_path)

    extracted_text = ""

    for page in document:
        extracted_text += page.get_text()

    page_count = len(document)

    document.close()

    return extracted_text, page_count