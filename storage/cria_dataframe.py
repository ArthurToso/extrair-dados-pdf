import pandas as pd
from config.settings import EXCEL_PATH, CSV_PATH
from pathlib import Path

def cria_csv_xlsx (EXCEL_PATH : Path, CSV_PATH: Path, DADOS_LIST: list):
    try:
        if EXCEL_PATH.exists() and CSV_PATH.exists():
            df_antigo = pd.read_excel(EXCEL_PATH)
            df_novo = pd.DataFrame(DADOS_LIST)
            df = pd.concat([df_antigo, df_novo], ignore_index=True)
        else:
            df = pd.DataFrame(DADOS_LIST)
    except Exception as e:
        print(f'Erro na função cria_dataframe: {e}')
    try:    
        df.to_csv(CSV_PATH, index=False, encoding="utf-8-sig")
        df.to_excel(EXCEL_PATH, index=False, engine="openpyxl")
    except Exception as e:
        print(f'Erro na hora de criar o csv e xlsx: {e}') 