# utils.py

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

def load_data(file_path, delimiter='|'):
    r"""Carrega o arquivo CSV e substitui valores '\N' por NaN."""
    df = pd.read_csv(file_path, delimiter=delimiter, dtype={'anoLancamento': str}, low_memory=False)
    df.replace('\\N', np.nan, inplace=True)
    return df


#def plot_top_ratings(df, title, output_dir='resultado'):
def plot_top_ratings(df, title, output_dir='/app/resultado'):
    """Cria um gráfico de barras para as 10 produções com nota máxima."""
    top_10 = df[df['notaMedia'] == 10].drop_duplicates(subset=['tituloPincipal']).head(10)
    os.makedirs(output_dir, exist_ok=True)
    plt.figure(figsize=(12, 6))
    plt.barh(top_10['tituloPincipal'], top_10['anoLancamento'], color='skyblue')
    for index, value in enumerate(top_10['anoLancamento']):
        plt.text(value, index, "10.0", va='center')
    plt.xlabel("Ano de Lançamento")
    plt.ylabel("Produções")
    plt.title(f"Top 10 {title} com Nota Máxima - Ano de Lançamento")
    plt.tight_layout()
    plt.savefig(f'{output_dir}/top_10_{title}_nota_maxima.png')
    plt.close()

import os
import matplotlib.pyplot as plt

def plot_top_genre_ratings(df, title, output_dir='notaComediaanimacao'):
    """Cria um gráfico de barras horizontal com foco na nota média, mostrando o ano de lançamento apenas como referência."""
    
    top_10 = df.drop_duplicates(subset=['tituloPincipal']).head(10)
    os.makedirs(output_dir, exist_ok=True)  # Cria o diretório de saída se não existir

    plt.figure(figsize=(12, 6))
    plt.barh(top_10['tituloPincipal'], top_10['notaMedia'], color='skyblue')
    
    # Adicionando rótulos com o ano de lançamento ao lado da nota
    for index, (nota, ano) in enumerate(zip(top_10['notaMedia'], top_10['anoLancamento'])):
        plt.text(nota, index, f"{nota:.1f} ({ano})", va='center')

    plt.xlabel("Nota Média")
    plt.ylabel("Produções")
    plt.title(f"Top 10 {title} - Focado na Nota Média")
    plt.tight_layout()
    plt.savefig(f'{output_dir}/top_10_{title.replace(" ", "_")}_focado_na_nota.png')
    plt.close()


