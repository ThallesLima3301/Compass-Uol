--1

E01
select  *
FROM livro

--Apresente a query para listar todos os livros publicados após 2014. Ordenar pela coluna cod, em ordem crescente, as linhas.  Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma
select   cod, titulo, autor, editora, valor, publicacao, edicao, idioma
FROM livro
WHERE publicacao > '2014-12-31'
ORDER BY cod ASC;


E02
-- Apresente a query para listar os 10 livros mais caros. Ordenar as linhas pela coluna valor, em ordem decrescente.  Atenção às colunas esperadas no resultado final:  titulo, valor.

SELECT titulo, valor
FROM livro
ORDER BY valor DESC
LIMIT 10;

--3
--  Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.

SELECT COUNT(livro.cod) AS quantidade, editora.nome, endereco.estado, endereco.cidade
FROM livro
JOIN editora ON livro.editora = editora.codEditora
JOIN endereco ON editora.endereco = endereco.codEndereco
GROUP BY editora.nome, endereco.estado, endereco.cidade
ORDER BY quantidade DESC
LIMIT 5;


--4
--Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).
SELECT
    autor.codAutor,
    autor.nome,
    autor.nascimento,
    COUNT(livro.cod) AS quantidade
FROM
    autor
LEFT JOIN
    livro ON autor.codAutor = livro.autor
GROUP BY
    autor.codAutor, autor.nome, autor.nascimento
ORDER BY
    autor.nome ASC;



--5Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.
/*Bom esse aqui eu sou obrigado a contar uma historia sobre oq eu passei
estava fazendo oq exercicios de boa, batendo um pouco a cabeça mas sempre conseguindo resolver de forma rapida
ATE CHEGAR NESSA BELEZINHA AQUI. O meu primeiro codigo foi esse aqui. 

SELECT DISTINCT autor.nome
FROM autor
JOIN livro ON autor.codAutor = livro.autor
JOIN editora ON livro.editora = editora.codEditora
JOIN endereco ON editora.endereco = endereco.codEndereco
WHERE endereco.estado NOT IN ('PR', 'SC', 'RS')
ORDER BY autor.nome ASC;

como podem ver igual o que deu certo  porem estaav dando errado e me retornando autores do PARANÁ

E comecei a ir atas do pq estava acontecendo isso. utilziei ´JOIN livro ON autor.codAutor = livro.autor
    JOIN editora ON livro.editora = editora.codEditora
    JOIN endereco ON editora.endereco = endereco.codEndereco´ para ver se ia 
    usei o ´HAVING SUM(CASE WHEN endereco.estado IN ('PR', 'SC', 'RS') THEN 1 ELSE 0 END) = 0´
e nada
usei o `LEFT JOIN` e nada 
 indiguinado aprendi o comando PRAGMA e comecei a ver as tabelas do q estava acontecendo 
 `--estrutura das tabelas
--PRAGMA table_info(autor);
--PRAGMA table_info(livro);
--PRAGMA table_info(editora);
--PRAGMA table_info(endereco);`
usei o ´SELECT * FROM autor LIMIT 10;
SELECT * FROM livro LIMIT 10;
SELECT * FROM editora LIMIT 10;
SELECT * FROM endereco LIMIT 10;´ pra ver as tabelas e nada 
usei ´WHERE endereco.estado IN ('PR', 'SC', 'RS')
)
AND endereco.estado NOT IN ('PR', 'SC', 'RS')´ pra ter certeza e mas o AADNOY, Bernt continuava
usei GROUP BY autor.nome
`HAVING SUM(CASE WHEN endereco.estado IN ('PR', 'SC', 'RS') THEN 1 ELSE 0 END) = 0`
e nada
depois de quase 1H eu dessiti e fui para os proximos depois q eu fiz o 6 e 0 7  eu voltei e decidi Testar mudar o  PR para PARANÁ 🤡🤡🤡 enfim deu certo

ENFIM, a logica ficou assim
A query faz um JOIN entre as tabelas autor, livro, editora, e endereco para conectar os autores aos livros e editoras, e finalmente ao endereço da editora.

Filtra as editoras cujo estado (endereco.estado) não está entre os estados da região Sul (PARANÁ, SC, RS).

Usei o DISTINCT para garantir que não haja autores duplicados no resultado.
Ordena o resultado em ordem crescente pelo nome dos autores (ORDER BY autor.nome ASC).

*/
SELECT DISTINCT autor.nome
FROM autor
JOIN livro ON autor.codAutor = livro.autor
JOIN editora ON livro.editora = editora.codEditora
JOIN endereco ON editora.endereco = endereco.codEndereco
WHERE endereco.estado NOT IN ('PARANÁ', 'SC', 'RS')
ORDER BY autor.nome ASC;


--- 6
--Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.

/*COUNT(livro.cod): Contamos o número de livros associados a cada autor.
GROUP BY autor.codAutor, autor.nome: Agrupei por código e nome do autor para garantir que cada autor tenha sua contagem de publicações calculada corretamente.
ORDER BY quantidade_publicacoes DESC:  Resultados em ordem decrescente para que o autor com o maior número de publicações apareça primeiro.
LIMIT 1: Limitei o resultado para exibir apenas o autor com o maior número de publicações.
*/
SELECT autor.codAutor, autor.nome, COUNT(livro.cod) AS quantidade_publicacoes
FROM autor
JOIN livro ON autor.codAutor = livro.autor
GROUP BY autor.codAutor, autor.nome
ORDER BY quantidade_publicacoes DESC
LIMIT 1;


--7
--Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.
LEFT JOIN: Usei um LEFT JOIN para garantir que todos os autores sejam incluídos, mesmo aqueles que não têm nenhum livro.

WHERE livro.cod IS NULL: Isso garante que filtrei apenas os autores que não têm nenhum livro associado a eles (nenhuma publicação).

ORDER BY autor.nome ASC: Coloquei o resultado em ordem alfabética crescente, conforme solicitado.

SELECT autor.nome
FROM autor
LEFT JOIN livro ON autor.codAutor = livro.autor
WHERE livro.cod IS NULL
ORDER BY autor.nome ASC;


biblioteca2

SELECT 
    l.cod AS CodLivro,
    l.titulo AS Titulo,
    a.codAutor AS CodAutor,
    a.nome AS NomeAutor,
    l.valor AS Valor,
    e.codEditora AS CodEditora,
    e.nome AS NomeEditora
FROM 
    LIVRO l
JOIN 
    AUTOR a ON l.autor = a.codAutor
JOIN 
    EDITORA e ON l.editora = e.codEditora
ORDER BY 
    l.valor DESC
LIMIT 10;


SELECT 
    e.codEditora AS CodEditora,
    e.nome AS NomeEditora,
    COUNT(l.cod) AS QuantidadeLivros
FROM 
    LIVRO l
JOIN 
    EDITORA e ON l.editora = e.codEditora
GROUP BY 
    e.codEditora, e.nome
ORDER BY 
    QuantidadeLivros DESC
LIMIT 5;
