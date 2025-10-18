import os
import pdfplumber
import re

def ler_dados_pdf (dir_pdf):
    with pdfplumber.open(dir_pdf) as pdf:
        dados_pdf = {}
        pdf_page = pdf.pages[0]
        texto_pdf = pdf_page.extract_text().lower()
        id_cliente_regex = r"id\s+do\s+cliente:\s+.*"
        match = re.search(id_cliente_regex, texto_pdf)
        if match:
            dados_pdf["id_cliente"] = match.group(0)
        else:
            dados_pdf["id_cliente"] = "Id do Cliente Não Encontrado"

    return dados_pdf

dir_pdf = os.path.dirname(__file__)

pdf_list = [f for f in os.listdir(dir_pdf) if f.endswith(".pdf") or f.endswith(".PDF")]

for arquivo in pdf_list:
    print(arquivo)
    dados_pdf = ler_dados_pdf(arquivo)
    print(dados_pdf.get("id_cliente"))