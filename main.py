from config.settings import PDF_LIST, DADOS_LIST, EXCEL_PATH, CSV_PATH
from extract_pdf.extract_text import extrair_texto
from extract_pdf.parser import obter_dados
from storage.cria_dataframe import cria_csv_xlsx
from config.logger import cria_log
from storage.cria_pastas import mover_pdf

def processa_lista_pdf (pdf_list):
    log = cria_log(__name__) 
    if len(pdf_list) > 0:
        log.info(f"Iniciando o processamento")
        for pdf in pdf_list:
            try:
                texto = extrair_texto(pdf)
                log.info(f'Extraindo o texto do PDF: {pdf}')
                dados_pdf = obter_dados(texto)
                log.info(f'Extraindo os dados do PDF: {pdf}')
                DADOS_LIST.append(dados_pdf)
                log.info(f'PDF: {pdf} Processado com sucesso!')
                mover_pdf(pdf, dados_pdf.get('data_fatura'))
            except Exception as e:
                log.error(f'Erro no processamento do PDF: {e}')
        try:
            cria_csv_xlsx(EXCEL_PATH, CSV_PATH, DADOS_LIST)
            log.info(f'CSV e XLSX atualizados com sucesso!')
        except Exception as e:
            log.error(f'Erro ao criar csv e xlsx: {e}')
    else:
        log.info("Não foram encontrados PDF's para processar")

if __name__ == "__main__":
    processa_lista_pdf(PDF_LIST)
