import os
import pdfplumber
import re
import shutil

def ler_dados_pdf (dir_pdf):
    with pdfplumber.open(dir_pdf) as pdf:
        dados_pdf = {}
        pdf_page = pdf.pages[0]
        texto_pdf = pdf_page.extract_text().lower()
        id_cliente_regex = r"id\s+do\s+cliente:\s+(.*)"
        nome_cliente_regex = r"nome\s+do\s+cliente:\s+(.*)"
        data_fatura_regex = r"data\s+da\s+fatura:\s+(.*)"
        valor_total_regex = r"valor\s+total:\s+(.*)"
        detalhes_regex = r"detalhes:(.*)----------------------------------------"
    
        #Match id_cliente
        match = re.search(id_cliente_regex, texto_pdf)
        if match:
            dados_pdf["id_cliente"] = match.group(1)
        else:
            dados_pdf["id_cliente"] = "Id do Cliente Não Encontrado"
        #Match nome_cliente
        match = re.search(nome_cliente_regex, texto_pdf)
        if match:
            dados_pdf["nome_cliente"] = match.group(1)
        else:
            dados_pdf["nome_cliente"] = "Nome do Cliente Não Encontrado"
        #Match data_fatura
        match = re.search(data_fatura_regex, texto_pdf)
        if match:
            dados_pdf["data_fatura"] = match.group(1)
        else:
            dados_pdf["data_fatura"] = "Data da Fatura Não Encontrada"
        #Match valor_total
        match = re.search(valor_total_regex, texto_pdf)
        if match:
            dados_pdf["valor_total"] = match.group(1)
        else:
            dados_pdf["valor_total"] = "Valor Total Não Encontrado"
        #Match detalhes
        match = re.search(detalhes_regex, texto_pdf, re.DOTALL)
        if match:
            texto_aux = match.group(1).strip()
            detalhes_list = texto_aux.split("\n")
            dados_pdf["detalhes"] = detalhes_list
        else:
            dados_pdf["detalhes"] = "Detalhes Não Encontrado"
    return dados_pdf

dir_pdf = os.path.dirname(__file__)

pdf_list = [f for f in os.listdir(dir_pdf) if f.endswith(".pdf") or f.endswith(".PDF")]

for arquivo in pdf_list:
    try:
        dados_pdf = ler_dados_pdf(arquivo)
        print(dados_pdf.get("detalhes"))
        nome_pasta = str(dados_pdf.get("data_fatura"))
        nome_pasta = nome_pasta.replace("/","-")
        dir_pasta = os.path.join(dir_pdf, nome_pasta)
        if not os.path.exists(dir_pasta):
            os.makedirs(dir_pasta, exist_ok=True)
        shutil.move(arquivo, dir_pasta)
        print(nome_pasta)
    except Exception as e:
        print(f"Erro: {e}")