/*
1. Objetivos
Objetivo da Sprint 2 é o nivelamento de conhecimento entre todos os bolsistas dcs conteúdos envolvidos ra
sprint.
2. Conteúdos
Nesta Sprint abordaremos conceitos muito importantes para qualquer profissional de tecnologia, mais ainda para
profissionais que trabalham com dados que é Linguagem SQL e Modelagem de Dados.
3. Atividades
Extrair dados de uma base e exportá-los em diferentes formatos é atividade recorrente em projetos de dados.
Nesta atividade você terá uma experiência introdutória de como este processo funciona.
Considerando a base de dadcs Biblioteca apresentada na Seção 3, realize a exportação de dados (em formato
.CSV) através do cliente SQL de sua preferência (DBeaver, VSCode...). O layout dos arquivos, bem como os
critérios de coleta de dados estão definidos em cada uma das etapas da atividade.
3.1. Etapa 1

Exportar o resultado da query que obtém os 10 livros mais caros para um arquivo CSV. Utilizar 0 caractere ;
(ponto e vírgula) como separador. Lembre-se que o conteúdo do seu arquivo deverd respeitar a sequência de
colunas e seus respectivos nomes de cabeçalho que listamos abaixo:
CodLivro
Titulo
CodAutor
NomeAutor
Valor
CodEditorc
NomeEditora
Observação: O arquivo exportado, conforme as especificações acima, deve ser disponibilizado no GitHub.

*/
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


/*3.2. Etapa 2
Exportar o resultado da query que obtém as 5 editoras com maior quantidade de livros na biblioteca para um
arquivo CSV. Utilizar o caractere I (pipe) como separador. Lembre-se que o conteúdo do seu arquivo deverá
respeitar a sequência de colunas e seus respectivos nomes de cabeçalho que listamos abaixo:
CodEditorc
NomeEditora
QuantidadeLivros
Observação: O arquivo exportado, conforrne as especificações acirna, deve ser disponibilizado no GitHub.
*/
--A query para listar as editoras com a maior quantidade de livros.


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


