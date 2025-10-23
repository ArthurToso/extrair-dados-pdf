import pdfplumber

def extrair_texto (pdf_path : str) -> str:
    with pdfplumber.open(pdf_path) as pdf:
        texto_extraido = pdf.pages[0].extract_text().lower()
    return texto_extraido