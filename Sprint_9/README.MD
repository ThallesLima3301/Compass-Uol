
Durante a Sprint 9, aprendi bastante e foi muito bom revisar os modelos relacionais. Desta vez, achei mais fácil trabalhar com eles e, de certa forma, gostei bastante dessa etapa.

Em relação ao AWS Glue, tive bastante dificuldade no início e cometi muitos erros, mas consegui aprender bastante ao longo do processo. Se precisasse realizar uma tarefa similar no futuro, acredito que faria de forma muito mais fácil e eficiente.

No geral, considero que foi uma ótima sprint!


# Certificados

 [Pasta vazio Certificados](../Sprint_9/certificados/img/texto.txt)

# Exercícios

1. [Pasta vazio exercicios](../Sprint_9/exercicios/texto.txt)


# Desafios

[Desafio 9](../Sprint_9/Desafio/README.MD)


# Evidências

Minha lógica ja esta documentada nos aquivos, vou usar imagens colocando que funcionou dentro da plataforma. A ideia é mostrar de forma clara e direta os resultados.



# Feedback


Durante o desenvolvimento da camada Refined, enfrentei alguns desafios.

Tive que revisar e testar várias vezes a lógica de join entre os arquivos CSV e JSON, pois a combinação de dados dependia do tratamento das colunas, como normalização de textos com trim e upper, para garantir que títulos fossem comparados corretamente.

Outro ponto complicado foi lidar com os possiveis dados duplicados e ambíguos. Precisei usar a função coalesce para unificar valores de diferentes fontes e definir quais dados teriam prioridade, o que exigiu um cuidado extra para não perder informações importantes. A deduplicação com base em colunas específicas, como titulo_principal e release_date, também foi uma etapa crítica para garantir a qualidade do resultado.

Por fim, os regex utilizados para filtrar gêneros "comedy" e "animation" também me deram trabalho, pois precisei testar várias abordagens até encontrar a expressão correta que funcionasse de forma case-insensitive.


MSE and MAE 
fora bem tranquilos pra mim eu ja tinha feito tudo no pandas desda sprint 6 eu so fui mudando com base oq eu foi necesario, eu cheguei no resultado que eu esperava, agora tenho que aprender a gerar no grafico no quicksight e ver se o resultado sai igual o meu feio no pandas.


# Feedback ápos monitoria


modifiquei bastante coisa, Código atualizado:

```sql
 
# Criar Tabela Fato (Filtrar apenas os anos e gêneros relevantes)
fato_comedia_animacao = common_movies.withColumn("release_date", to_date(F.col("release_date"), "yyyy-MM-dd")) \
    .select(
        F.col("titulo_principal"),
        "vote_average",
        "vote_count",
        "popularity",
        "genero",
        "release_date"
    ) \
    .withColumn("ano", F.year(F.col("release_date"))) \
    .filter((F.col("ano") >= 2000) & (F.col("ano") <= 2020)) \
    .filter(
        F.col("genero").rlike("(?i)(comedy|animation)")  # Regex para filtrar gêneros
    )

# Remover registros com valores nulos ou vazios
fato_comedia_animacao = fato_comedia_animacao.filter(
    (F.col("titulo_principal").isNotNull()) & 
    (F.trim(F.col("titulo_principal")) != "") & 
    (F.col("release_date").isNotNull())
)

# Simulação de previsões (adicionando variação aleatória de 10%)
fato_comedia_animacao = fato_comedia_animacao.withColumn(
    "vote_predicted",
    F.col("vote_average") * (1 + F.rand() * 0.2 - 0.1)  # 10% de variação para mais ou menos
)

# Adicionar MSE e MAE como colunas constantes no fato
fato_comedia_animacao = fato_comedia_animacao.withColumn("mse", lit(mse)) \
                                             .withColumn("mae", lit(mae))

# Salvar com particionamento por ano e gênero
fato_comedia_animacao.write.mode("overwrite") \
    .partitionBy("ano", "genero") \
    .parquet(f"{output_base_path}/fato_comedia_animacao")

# Criar DataFrames com os valores MSE e MAE e salvar separadamente
mse_df = glueContext.spark_session.createDataFrame([("MSE", mse)], ["Metric", "Value"])
mae_df = glueContext.spark_session.createDataFrame([("MAE", mae)], ["Metric", "Value"])

# Salvar os arquivos MSE e MAE em pastas separadas
mse_df.write.mode("overwrite").parquet(f"{output_base_path}/fato_comedia_animacao/mse")
mae_df.write.mode("overwrite").parquet(f"{output_base_path}/fato_comedia_animacao/mae")

# Dimensão Filme com particionamento
dim_filme = common_movies.select(
    F.col("csv_id").alias("id"),
    F.col("titulo_principal"),
    F.col("titulooriginal").alias("titulo_original"),
    F.col("release_date"),
    F.col("popularity")
).distinct() \
    .withColumn("ano", F.year(to_date(F.col("release_date"), "yyyy-MM-dd"))) \
    .filter((F.col("ano") >= 2000) & (F.col("ano") <= 2020))

dim_filme.write.mode("overwrite").partitionBy("ano").parquet(f"{output_base_path}/dim_filme")

# Dimensão Tempo com particionamento
dim_tempo = common_movies.withColumn("release_date", to_date(F.col("release_date"), "yyyy-MM-dd")) \
    .select("release_date").distinct() \
    .withColumn("ano", F.year(F.col("release_date"))) \
    .withColumn("mes", F.month(F.col("release_date"))) \
    .filter((F.col("ano") >= 2000) & (F.col("ano") <= 2020))

dim_tempo.write.mode("overwrite").partitionBy("ano", "mes").parquet(f"{output_base_path}/dim_tempo")

```

