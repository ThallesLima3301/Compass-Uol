import logging
import os
from s3_operations import download_file_s3, upload_file_s3
from data_processing import process_dataframe

# Configurando o logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def main():
    bucket_name = 'sprint-5'
    file_key = 'relatorio_inabilitado_s3.csv'
    download_path = 'relatorio_inabilitado_s3.csv'
    output_file = 'resultado_sprint_5.csv'

    # Criar a pasta 'resultados' se não existir
    os.makedirs('resultados', exist_ok=True)

    # Download do arquivo do S3
    download_file_s3(bucket_name, file_key, download_path)

    # Processamento do DataFrame
    df, df_filtrado = process_dataframe(download_path)
    df.to_csv(output_file, index=False, sep=';', encoding='latin1')


    # Verificar se há registros "Expirado"
    df_expirado = df[df['Status'] == 'Expirado']
    if not df_expirado.empty:
        logging.info(f"Encontrados {len(df_expirado)} registros com status 'Expirado'.")
        registros_expirados = df_expirado.head().to_string(index=False)
    else:
        registros_expirados = "Nenhum registro 'Expirado' encontrado."

    # Consolidação de todas as informações em uma única resposta
    resultado_consolidado = f"""
    ========== RESULTADO CONSOLIDADO ==========
    Primeiras linhas após a substituição de datas ausentes:
    {df.head().to_string(index=False)}

    Primeiras linhas do DataFrame filtrado:
    {df_filtrado.head().to_string(index=False)}

    Primeiras linhas após a criação da coluna 'Status':c
    {df[['Data Final', 'Status']].head().to_string(index=False)}

    Primeiras linhas com CPF Limpo e Nome em Maiúsculas:
    {df[['CPF Limpo', 'Nome em Maiúsculas']].sample(5).to_string(index=False)} 

    Registros Expirados:
    {registros_expirados}
    ============================================
    """

    # Imprimir o resultado consolidado sample(5)
    print(resultado_consolidado)

    # Salvar os DataFrames como CSVs locais dentro da pasta 'resultados'
    df.to_csv('resultados/tabela_original.csv', index=False, sep=';', encoding='latin1')
    df_filtrado.to_csv('resultados/tabela_filtrada.csv', index=False, sep=';', encoding='latin1')
    df_expirado.to_csv('resultados/tabela_expirados.csv', index=False, sep=';', encoding='latin1')

    # Fazer o upload dos arquivos CSV para o bucket S3
    upload_file_s3(bucket_name, 'resultados/tabela_original.csv', 'resultados/tabela_original.csv')
    upload_file_s3(bucket_name, 'resultados/tabela_filtrada.csv', 'resultados/tabela_filtrada.csv')
    upload_file_s3(bucket_name, 'resultados/tabela_expirados.csv', 'resultados/tabela_expirados.csv')
    upload_file_s3(bucket_name, output_file, output_file)


    # Mensagem final indicando que todas as etapas foram concluídas
    print("\nTodas as etapas foram concluídas com sucesso, e os arquivos de tabelas foram enviados para o bucket S3.")

if __name__ == "__main__":
    main()
