import logging
from datetime import datetime
from pathlib import Path

LOG_DIR = Path(__file__).parent.parent /'logs'

data = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
nome_log = 'log_'+ data +'.txt'

logging.basicConfig(
    filename=LOG_DIR / nome_log,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    encoding='utf-8'
)

def cria_log(nome_modulo:str):
    return logging.getLogger(nome_modulo)
