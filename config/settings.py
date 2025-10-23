from pathlib import Path
from config.dirs import DIR_PDF, DIR_OUTPUT

PDF_LIST = list(DIR_PDF.glob('*.pdf'))
DADOS_LIST = []
EXCEL_PATH = DIR_OUTPUT / 'vendas.xlsx'
CSV_PATH = DIR_OUTPUT / 'vendas.csv'