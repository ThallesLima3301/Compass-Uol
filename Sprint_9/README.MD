
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