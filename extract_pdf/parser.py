import re
from config.regex_patterns import ID_CLIENTE_RE, NOME_CLIENTE_RE, DATA_FATURA_RE, VALOR_TOTAL_RE, DETALHES_RE

def obter_dados (texto_pdf : str) -> dict:
    dados_dict = {}
    try:    
        match = re.search(ID_CLIENTE_RE, texto_pdf)
        if match:
            dados_dict['id_cliente'] = match.group(1)
        else:
            dados_dict['id_cliente'] = "Erro ao extrair ID_CLIENTE"
        match = re.search(NOME_CLIENTE_RE, texto_pdf)
        if match:
            dados_dict['nome_cliente'] = match.group(1)
        else:
            dados_dict['nome_cliente'] = "Erro ao extrair NOME_CLIENTE"
        match = re.search(DATA_FATURA_RE, texto_pdf)
        if match:
            dados_dict['data_fatura'] = match.group(1)
        else:
            dados_dict['data_fatura'] = "Erro ao extrair DATA_FATURA"
        match = re.search(VALOR_TOTAL_RE, texto_pdf)
        if match:
            dados_dict['valor_total'] = match.group(1)
        else:
            dados_dict['valor_total'] = "Erro ao extrair VALOR_TOTAL"
        match = re.search(DETALHES_RE, texto_pdf)
        if match:
            texto_aux = match.group(1).strip()
            detalhes_list = texto_aux.split("\n")
            dados_dict['detalhes'] = detalhes_list
        else:
            dados_dict['detalhes'] = "Erro ao extrair DETALHES"
    except Exception as e:
        print(f"Erro funcao obter_dados: {e}")
    return dados_dict