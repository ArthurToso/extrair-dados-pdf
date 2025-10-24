# 🚀 Extrator de Faturas PDF 

## 📄 Descrição

Este projeto é um script de automação em Python focado em processar extratos de vendas em formato PDF.

O objetivo principal é ler múltiplos arquivos PDF de uma pasta de entrada, extrair dados-chave usando expressões regulares (regex), e consolidar todas as informações em um único arquivo `CSV` e `Excel (.xlsx)`. Este processo facilita o controle financeiro e a análise de vendas, eliminando a entrada manual de dados.

## ✨ Funcionalidades Principais

* **Extração de Dados de PDF:** Lê o texto de múltiplos arquivos `.pdf`.
* **Identificação de Padrões (Regex):** Localiza e extrai dados específicos:
    * `Id_cliente`
    * `nome_cliente`
    * `data_fatura`
    * `valor_total`
    * `detalhes_compra`
* **Processamento em Lote:** Processa todos os arquivos encontrados na pasta de entrada (.pdf).
* **Consolidação de Dados:** Utiliza `pandas` para carregar os dados antigos do `CSV` e `Excel`, concatenar (adicionar) os novos dados extraídos e salvar os arquivos atualizados. O script não sobrescreve os dados antigos, ele os acumula.
* **Organização de Arquivos:** Após o processamento bem-sucedido, cada PDF é movido para uma pasta de "processados", sendo organizado em subpastas com base na `data_fatura` (ex: `processados/2025-10-24/`).

## ⚙️ Como Funciona (Workflow)

1.  O script verifica a pasta de entrada (ex: `input_data/`) por novos arquivos `.pdf`.
2.  Para cada PDF, o texto é extraído.
3.  Os padrões de regex são aplicados para encontrar os dados-chave, que serão armazenados em um dicionário.
4.  Os dados extraídos são validados e organizados em um DataFrame `pandas`.
5.  O script lê os relatórios existentes (`relatorio_vendas.csv` e `relatorio_vendas.xlsx`) da pasta de saída (ex: `output_data/`).
6.  O novo DataFrame é concatenado ao DataFrame antigo.
7.  Os arquivos de relatório são salvos, substituindo os antigos pela versão atualizada e consolidada.
8.  O PDF original é movido para a pasta de arquivamento (ex: `processados/AAAA-MM-DD/`).

## 🛠️ Requisitos e Instalação

Este projeto foi desenvolvido em Python 3.12.6 e requer as seguintes bibliotecas:

* **pandas**: Para manipulação de dados e exportação para CSV/Excel.
* **openpyxl**: Dependência do `pandas` para escrever arquivos `.xlsx`.
* **pdfplumber**: para extração de texto em um PDF.
* **Consultar requirements.txt**

**Instalação:**

1.  Clone este repositório (ou baixe os arquivos).

2.  (Recomendado) Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
    
## 🚀 Como Usar

1.  **Configuração:**
    * Verifique os caminhos das pastas no arquivo `config/settings.py` (ou onde você definiu suas constantes) para garantir que apontam para os locais corretos (`PASTA_ENTRADA`, `PASTA_SAIDA`, etc.).

2.  **Entrada de Dados:**
    * Adicione seus arquivos PDF de extrato na pasta de entrada (ex: `entradas/`).

3.  **Execução:**
    * Execute o script principal pelo seu terminal:
    ```bash
    python main.py
    ```

4.  **Saída:**
    * Verifique a pasta de saída (ex: `saidas/`). Os arquivos `relatorio_vendas.csv` e `relatorio_vendas.xlsx` estarão atualizados com os novos dados.
    * Verifique a pasta de processados (ex: `processados/`) para confirmar que os PDFs foram movidos e organizados corretamente.

## 📈 Possíveis Melhorias (Para o Futuro)

* [ ] Adicionar um log mais robusto para arquivos que falharam na extração.
* [ ] Implementar uma GUI (Interface Gráfica) simples com Tkinter ou PySimpleGUI.
* [ ] Substituir o CSV/Excel por um banco de dados (SQLite) para melhor performance.