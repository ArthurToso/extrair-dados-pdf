import os
from config.dirs import DIR_OUTPUT
from shutil import move

def mover_pdf(pdf:str ,data_fatura: str):
    data_fatura_aux = data_fatura.replace('/', '_')
    pasta = DIR_OUTPUT / data_fatura_aux
    print(pasta)
    os.makedirs(pasta, exist_ok=True)
    move(pdf, pasta)