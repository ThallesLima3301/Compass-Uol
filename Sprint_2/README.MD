
Durante a Sprint 2, aprendi muita coisa, 


Atualmente, já concluí os dois cursos (SQL e AWS) e estou gostando bastante da trilha. Estou ansioso pela próxima sprint e pelos novos aprendizados que ela trará 😊.

# Certificados

 [ Certificados](../Sprint_2/certificados/img/AWS%20Partner%20Sales%20Accreditation%20(Business)(Portuguese).png)

# Exercícios

1. [Resposta Caso de Estudo Biblioteca](../Sprint_2/exercicios/Caso_de_Estudo_Biblioteca/biblioteca/Exercicio_1_ao_7.sql)

2. [Resposta Caso de Estudo Loja](../Sprint_2/exercicios/Caso_de_Estudo_Loja/loja/Exercicio_8_ao_16.sql)

3. [exportacao_Biblioteca Ex3](../Sprint_2/exercicios/exportacao_Biblioteca/biblioteca2/query.sql)



# Desafios

[Desafio 2](../Sprint_2/Desafio/README.MD)


# Evidências

Minha lógica ja esta documentada nos aquivos, vou usar imagens colocando que funcionou dentro da plataforma. A ideia é mostrar de forma clara e direta os resultados

1. [Resposta Caso de Estudo Biblioteca](../Sprint_2/exercicios/Caso_de_Estudo_Biblioteca/biblioteca/Exercicio_1_ao_7.sql)

2. [Resposta Caso de Estudo Loja](../Sprint_2/exercicios/Caso_de_Estudo_Loja/loja/Exercicio_8_ao_16.sql)

Bom ja esse exercicios eu vou documentar aqui o meu passo a passo

3. [exportacao_Biblioteca Ex3](../Sprint_2/exercicios/exportacao_Biblioteca/biblioteca2/query.sql)

    # Seção 6: Linguagem SQL - Exercícios II


fiz as instalações na base de dados chamada "Biblioteca"

Baixei a extensão SQL Tools no VSCode

![Texto alternativo](../Sprint_2/evidencias/exportacao_Biblioteca/SQL_Tools_1.png)

fazendo a conexão

![Texto alternativo](../Sprint_2/evidencias/exportacao_Biblioteca/SQL_Tools_2.png)
Eu tive uns probleminhas, mas resolvi

![Texto alternativo](../Sprint_2/evidencias/exportacao_Biblioteca/SQL_Tools_3.png)

![Texto alternativo](../Sprint_2/evidencias/exportacao_Biblioteca/SQL_Tools_4.png)

confirmando se foi:

![Texto alternativo](../Sprint_2/evidencias/exportacao_Biblioteca/SQL_Tools_5.png)


fazendo A Exportar os 10 livros mais caros (Etapa 1):
SELECT * FROM sqlite_master WHERE type='table';

![Texto alternativo](../Sprint_2/evidencias/exportacao_Biblioteca/exportacao_Biblioteca_image1.png)

Para a Etapa 1, use o caractere ; (ponto e vírgula) como separador.

**10 livros mais caros**

   ```sql
SELECT
	l.cod AS CodLivro, 
    l.titulo AS Titulo,
	a.codAutor AS CodAutor,
	a.nome AS NomeAutor,
	l.valor AS Valor,
	e.codEditora AS CodEditora,
	e.nome AS NomeEditora`
`FROM
	livro l
JOIN
	autor a ON l.autor = a.codAutor
JOIN
	editora e ON l.editora = e.codEditora
ORDER BY
	l.valor DESC
LIMIT 10;
```
Essa query realiza:

Um JOIN entre as tabelas LIVRO, AUTOR e EDITORA para obter os detalhes do livro, autor e editora.
Os resultados são ordenados pelo valor (l.valor) de forma decrescente e limitados aos 10 livros mais caros.
Resultado

![Texto alternativo](../Sprint_2/evidencias/exportacao_Biblioteca/exportacao_Biblioteca_image2.png)

Após rodar a query, opção Save Results As, depois selecionei CSV e usei o caractere ; como separador.

![Texto alternativo](../Sprint_2/evidencias/exportacao_Biblioteca/exportacao_Biblioteca_image3.png)

Resultado

![Texto alternativo](../Sprint_2/evidencias/exportacao_Biblioteca/exportacao_Biblioteca_image4.png)

**Nota: A extensão Rainbow CSV que apareceu na notificação é útil para visualização e edição de arquivos CSV, pois ela destaca automaticamente os campos. Eu optei por instalar essa extensão para facilitar o trabalho com arquivos CSV no VSCode, mas isso é opcional.**

Abri o arquivo no Excel:

No Excel, fui para Dados > Obter Dados Externos > Do Texto/CSV.
Selecione o arquivo CSV que eu exportei.

Abri o assistente de importação, olhei:
`O delimitador está definido como ponto e vírgula (;).`
E
`A codificação está definida como UTF-8.`

![Texto alternativo](../Sprint_2/evidencias/exportacao_Biblioteca/exportacao_Biblioteca_image5.png)

![Texto alternativo](../Sprint_2/evidencias/exportacao_Biblioteca/exportacao_Biblioteca_image6.png)

Resultado da minha tabela

![Texto alternativo](../Sprint_2/evidencias/exportacao_Biblioteca/exportacao_Biblioteca_image7.png)

[Resultado](exercicios/exportacao_Biblioteca/biblioteca2/livros_caros.csv)

Beleza deu tudo certo com a Modelagem de Dados.

Proximo:
**A query para listar as editoras com a maior quantidade de livros.**

Para a Etapa 2, use o caractere | (pipe) como separador.


Essa query realiza:

Um JOIN entre LIVRO e EDITORA para contar a quantidade de livros associados a cada editora.
O resultado é agrupado por codEditora e nome e ordenado pela contagem (QuantidadeLivros) de forma decrescente, mostrando apenas as 5 editoras com mais livros.

   ```sql  
   SELECT 
    e.codEditora AS CodEditora,
    e.nome AS NomeEditora,
    COUNT(l.cod) AS QuantidadeLivros
FROM 
    livro l
JOIN 
    editora e ON l.editora = e.codEditora
GROUP BY 
    e.codEditora, e.nome
ORDER BY 
    QuantidadeLivros DESC
LIMIT 5;`
```
![Texto alternativo](../Sprint_2/evidencias/exportacao_Biblioteca/exportacao_Biblioteca_image8.png)

![Texto alternativo](../Sprint_2/evidencias/exportacao_Biblioteca/exportacao_Biblioteca_image9.png)

Mesmo esquema para tranformar em arquivo.csv


![Texto alternativo](../Sprint_2/evidencias/exportacao_Biblioteca/exportacao_Biblioteca_image5.png)

![Texto alternativo](../Sprint_2/evidencias/exportacao_Biblioteca/exportacao_Biblioteca_image6.png)

[Resultado](exercicios/exportacao_Biblioteca/biblioteca2/maiores_editoras.csv)

[Meu banco de dados](../../Sprint2.session.sql)

# Desafios

Vou falar sobre o desafio agora
    Fiz a normalização  
    **Resultado da normalização:**
tb_cliente: contém informações do cliente.
tb_carro: contém informações do carro, evitando redundâncias.
tb_combustivel: armazena os tipos de combustível.
tb_vendedor: guarda os dados do vendedor.
tb_locacao: armazena as informações sobre as locações, com as referências às outras tabelas.

vale resaltar que 

Modelo Relacional: Focado em eliminar redundâncias, os dados são organizados em tabelas normalizadas, divididos em várias entidades, com relações estabelecidas por chaves estrangeiras. É usado principalmente para transações (OLTP).

![Texto alternativo](../Sprint_2/evidencias/Img_Desafio/Relacional.png)

Já o 
Modelo Dimensional: É otimizado para consultas analíticas (OLAP). Os dados são organizados em uma tabela fato (contendo medidas) e várias tabelas dimensão (descritores). Ele é menos normalizado, facilitando a análise de grandes volumes de dados.

![Texto alternativo](../Sprint_2/evidencias/Img_Desafio/Dimensão.png)

criei as tabelas no sql apenas para mostrar

![Texto alternativo](../Sprint_2/evidencias/Img_Desafio/Desafio0.png)

Agora sobre as view eu tive difciduldade no data mas pesquisando bastante eu consegui fazer funcionar, fiquei bem feliz com o resultado.

# Estudando sobre view
eu  estudei bastante sobre. 

"As views geralmente são usadas para simplificar consultas complexas, fornecer uma exibição personalizada dos dados ou limitar acesso a dados das tabelas reais."

"As views servem como tabelas virtuais que são baseadas no resultado de uma query. Elas permitem simplificar consultas complexas, encapsulando-as em uma única estrutura, e ajudam a fornecer uma camada de segurança, pois você pode restringir o acesso a determinadas colunas ou dados específicos. Além disso, views facilitam a manutenção de consultas frequentes, oferecendo uma forma conveniente de reutilizar consultas sem precisar reescrever o código toda vez. Elas não armazenam dados por si mesmas, mas sim referências aos dados em outras tabelas."

Tirando a parte de  de fazer o dim_data (foi complciado), o processo foi bem tranquilo. Criei várias views que considero importantes no desenvolvimento, com perguntas que provavelmente são comuns no dia a dia. Alguns exemplos incluem: uma view para mostrar informações de locações feitas por vendedores de um estado específico e outra para calcular o valor total pago em uma locação (multiplicando o número de dias pelo valor da diária).

Ainda me sinto um pouco inseguro em relação ao SQL, mas acredito que essa sprint está me ajudando bastante a aprender. Mesmo assim, ainda tenho muitas dúvidas, especialmente em relação aos modelos. Consegui fazer, mas não foi algo fácil. Espero que esteja tudo certo.

# Feedback

Gostaria de compartilhar meu feedback sobre a Sprint de forma geral e meu desempenho. Embora eu tenha desejado ser mais organizado, isso não aconteceu. Os exercícios foram tranquilos, mas no desafio eu me perdi nas tabelas, cometendo erros bobos. Entendi as formas de normalização, mas tive dificuldade em aplicá-las corretamente. O modelo dimensional foi complicado, mas consegui finalizar a tempo. Tive dificuldades com as views, criei várias para testar e entender suas funcionalidades, mas ainda preciso praticar mais. Comparada à primeira Sprint, esta foi relativamente fácil, mas estou feliz com o que aprendi.

Um ponto positivo foi que ajudei muitas pessoas, o que me deu uma perspectiva diferente, pois as dúvidas delas ampliaram minha compreensão. Isso me fez evoluir bastante.

Este resumo de Sprint foi menos detalhado e mais direto do que o anterior. Para a próxima, vou experimentar uma abordagem diferente resultado 3 tipos. Após o feedback da terceira Sprint, decidirei qual modelo de resumo vou adotar daqui em diante com base o feedback de voces.
