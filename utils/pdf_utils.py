from pypdf import PdfReader

def extract_text_from_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    content = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            content += text
    return content
