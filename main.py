import os
import shutil
import pandas as pd
from config.dirs import DIR_OUTPUT, DIR_PDF
from config.settings import PDF_LIST, DADOS_LIST, EXCEL_PATH, CSV_PATH
from extract_pdf.extract_text import extrair_texto
from extract_pdf.parser import obter_dados

def processa_lista_pdf (pdf_list):
    if len(pdf_list) > 0:
        for pdf in pdf_list:
            try:
                texto = extrair_texto(pdf)
                print(texto)
                dados_pdf = obter_dados(texto)
                print(dados_pdf)
            except Exception as e:
                print(f"Erro na execução: {e}")
    else:
        print("Não foram encontrados PDF's para processar")

if __name__ == "__main__":
    processa_lista_pdf(PDF_LIST)


excel_path = DIR_OUTPUT / "vendas.xlsx"
csv_path = DIR_OUTPUT / "vendas.csv"
if excel_path.exists() and csv_path.exists():
    df_antigo = pd.read_excel(excel_path)
    df_novo = pd.DataFrame(DADOS_LIST)
    df = pd.concat([df_antigo, df_novo], ignore_index=True)
else:
    df = pd.DataFrame(DADOS_LIST)

df.to_csv(CSV_PATH, index=False, encoding="utf-8-sig")
df.to_excel(EXCEL_PATH, index=False, engine="openpyxl")