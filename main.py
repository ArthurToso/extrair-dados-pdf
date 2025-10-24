from config.settings import PDF_LIST, DADOS_LIST, EXCEL_PATH, CSV_PATH
from extract_pdf.extract_text import extrair_texto
from extract_pdf.parser import obter_dados
from storage.cria_dataframe import cria_csv_xlsx

def processa_lista_pdf (pdf_list): 
    if len(pdf_list) > 0:
        for pdf in pdf_list:
            try:
                texto = extrair_texto(pdf)
                print(texto)
                dados_pdf = obter_dados(texto)
                DADOS_LIST.append(dados_pdf)
            except Exception as e:
                print(f"Erro na execução: {e}")
        cria_csv_xlsx(EXCEL_PATH, CSV_PATH, DADOS_LIST)
    else:
        print("Não foram encontrados PDF's para processar")

if __name__ == "__main__":
    processa_lista_pdf(PDF_LIST)
