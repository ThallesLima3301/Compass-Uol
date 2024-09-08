SELECT * FROM livro;


SELECT * FROM sqlite_master WHERE type='table';


SELECT 
    l.cod AS CodLivro,
    l.titulo AS Titulo,
    a.codAutor AS CodAutor,
    a.nome AS NomeAutor,
    l.valor AS Valor,
    e.codEditora AS CodEditora,
    e.nome AS NomeEditora
FROM 
    livro l
JOIN 
    autor a ON l.autor = a.codAutor
JOIN 
    editora e ON l.editora = e.codEditora
ORDER BY 
    l.valor DESC
LIMIT 10;



A query para listar as editoras com a maior quantidade de livros.


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
LIMIT 5;
