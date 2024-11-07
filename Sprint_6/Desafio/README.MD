# Desafio da Sprint 

1. Objetivo
O propósito deste desafio é praticar e consolidar o que foi aprendido até agora sobre diversas tecnologias e ferramentas, integrando-as em um projeto robusto. A tarefa consiste na construção de um Data Lake que organize, armazene e possibilite o consumo de dados de filmes e séries, com foco em comédia e animação. Esse Data Lake possui uma estrutura de armazenamento em camadas, incluindo a ingestão de dados em um formato bruto, processamento dos dados com Apache Spark, e consumo final através de dashboards analíticos.

Este é um projeto de ponta a ponta, no qual aplico conhecimentos de Python, Docker, AWS, manipulação de dados e visualização, além de explorar uma API para enriquecer as análises. Em resumo, o desafio oferece uma excelente oportunidade de experimentar como as diferentes tecnologias se complementam na construção de um pipeline completo de dados.

2. Implementação da Ingestão Batch (Entrega 1)

Configuração do Ambiente e Organização dos Dados
Para essa primeira entrega, precisei configurar um ambiente local com Docker para executar um script Python que realiza o upload dos dados para o Amazon S3. Utilizei arquivos CSV contendo dados de filmes e séries, os quais serão processados e analisados nas etapas seguintes. Esta camada de dados brutos é a "RAW Zone" do Data Lake, onde os dados permanecem sem qualquer tipo de processamento, servindo como fonte confiável de informações.

Uma das principais considerações foi estruturar os dados no S3 de forma organizada para facilitar futuras consultas e análises. Segui o padrão de nomenclatura abaixo para armazenar os arquivos no S3:

    ´# Configurar caminhos para os arquivos´

    ´base_path = f"Raw/Local/CSV"´

    ´movies_key = f"{base_path}/Movies/{data_formatada}/movies.csv"´
    
    ´series_key = f"{base_path}/Series/{data_formatada}/series.csv"´

    
    








# Tipo de analise 

Para minha análise, pensei em começar com analytics descritiva Análise de Filmes e Séries de Comédia/Animação


Objetivo: Analisar a evolução e as tendências de filmes e séries de Comédia/Animação ao longo dos anos. O projeto busca entender as avaliações desse gênero, destacando fatores que possam influenciar a popularidade e qualidade percebida, com insights que auxiliem em uma visão preditiva e diagnóstica.

Principais Análises:

Média de Notas por Ano:

Análise: Calcular a média de notas para filmes e séries de Comédia/Animação ao longo dos anos, identificando tendências de aumento ou queda na popularidade.
Visualização: Gráfico de linha mostrando a média de notas por ano, facilitando a visualização das mudanças de avaliação ao longo do tempo.
Objetivo: Responder "como as avaliações de Comédia/Animação evoluíram ao longo dos anos?".

Análise Preditiva (Simples):

Análise: Aplicar uma previsão simples de notas futuras para o gênero Comédia/Animação, utilizando técnicas básicas de Machine Learning.

Métricas: Mean Squared Error (MSE) e Mean Absolute Error (MAE) serão usados para medir a precisão do modelo.

Visualização: Exibir as métricas em cards no dashboard e usar um scatter plot para visualizar a relação entre previsões e valores reais.

Objetivo: Identificar possíveis tendências futuras e avaliar a precisão do modelo preditivo.

Análise Diagnóstica:
Análise: Utilizar MSE e MAE para verificar a presença de erros significativos ou outliers que possam estar impactando a precisão das previsões.

Visualização: Gráfico de distribuição dos erros residuais, mostrando onde o modelo pode estar errando mais.

Objetivo: Diagnosticar problemas e entender o comportamento do modelo para prever notas de Comédia/Animação.

Evolução Temporal de Popularidade e Qualidade:

Análise: Examinar como a produção e popularidade de Comédia/Animação mudaram ao longo dos anos, com uma análise da quantidade de lançamentos e avaliações.

Visualização: Gráfico de linha para a quantidade de lançamentos por ano e a evolução das notas médias.
Objetivo: Oferecer uma visão ampla da presença e aceitação do gênero ao longo do tempo.


**Nota: Ainda não tenho certeza sobre isso preciso ter api para ter uma ideia melhor sobre, mas gostaria muito de poder usar ML no meu desafio, tenho bastante interesse na área**
