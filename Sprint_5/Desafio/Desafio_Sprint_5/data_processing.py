import pandas as pd
from datetime import datetime

def process_dataframe(file_path):

    """Processa o DataFrame com as manipulações necessárias."""
    df = pd.read_csv(file_path, delimiter=';', encoding='latin1')

    # Substituindo valores "-" por NaT (Not a Time) para tratar como datas ausentes
    df['Trânsito em Julgado'] = df['Trânsito em Julgado'].replace('-', pd.NaT)

    # Convertendo colunas de data para o formato datetime
    df['Data Final'] = pd.to_datetime(df['Data Final'], format='%d/%m/%Y', errors='coerce')
    df['Trânsito em Julgado'] = pd.to_datetime(df['Trânsito em Julgado'], format='%d/%m/%Y', errors='coerce')
    df['Data do acórdão'] = pd.to_datetime(df['Data do acórdão'], format='%d/%m/%Y', errors='coerce')

    # Aplicando a cláusula com dois operadores lógicos
    df_filtrado = df[(df['Data Final'] > '2025-01-01') & (df['Trânsito em Julgado'] < '2023-11-11')]

    # Extraindo o ano da "Data do acórdão" para facilitar a agregação
    df['Ano do Acórdão'] = df['Data do acórdão'].dt.year

    # Calculando o ano da "Data Final" e a diferença de anos até a data final
    df['Ano Final'] = df['Data Final'].dt.year
    df['Anos Restantes'] = df['Ano Final'] - df['Ano do Acórdão']

    # Criando a função condicional para determinar o status
    data_atual = pd.to_datetime(datetime.now().strftime('%Y-%m-%d'))
    df['Status'] = df['Data Final'].apply(lambda x: 'Válido' if x > data_atual else 'Expirado')

    # Manipulação de strings e formatação de colunas
    df['Data Final String'] = df['Data Final'].dt.strftime('%d-%m-%Y')
    df['CPF Limpo'] = df['CPF'].str.replace('.', '', regex=False).str.replace('-', '', regex=False)
    df['Nome em Maiúsculas'] = df['Nome do Responsável'].str.upper()

    return df, df_filtrado
