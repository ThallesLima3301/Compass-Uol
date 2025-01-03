


--8 
--Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.
--estava escrevendo "concluída" e estava dando errado dei um

SELECT DISTINCT status

FROM tbvendas;

--e entendi oq estava acontecendo 
--JOIN:  uni as tabelas tbvendas e tbvendedor com base no campo cdvvdd
--WHERE: Filtrei as vendas que têm o status "Concluído".
--GROUP BY: Agrupei as vendas por cdvvdd para contar quantas vendas cada vendedor fez.
--ORDER BY COUNT(v.cdven) DESC: Ordenei os resultados pela contagem de vendas em ordem decrescente (maior número de vendas primeiro).
-- e coloquei limit 1 linha
SELECT v.cdvdd, vd.nmvdd
FROM tbvendas v
JOIN tbvendedor vd ON v.cdvdd = vd.cdvdd
WHERE v.status = 'Concluído'
GROUP BY v.cdvdd
ORDER BY COUNT(v.cdven) DESC
LIMIT 1;

--

--9
--Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.
--WHERE: Filtra as vendas que têm o status "Concluído" e que ocorreram entre as datas especificadas.
--GROUP BY: Agrupei por cdpro (código do produto) e nmpro (nome do produto) para contar as vendas de cada produto.
--ORDER BY SUM(v.qtd) DESC: Ordena os resultados pela quantidade total de vendas, de forma decrescente (produto mais vendido primeiro).
--LIMIT 1: Limita o resultado ao produto mais vendido.

SELECT v.cdpro, v.nmpro
FROM tbvendas v
WHERE v.status = 'Concluído'
AND v.dtven BETWEEN '2014-02-03' AND '2018-02-02'
GROUP BY v.cdpro, v.nmpro
ORDER BY SUM(v.qtd) DESC
LIMIT 1;


--10
--A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 
--Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.
--As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.
--utilizei o comando para fazer a verificacao dos nomes pois etsva escrevendo errado

PRAGMA table_info(tbvendedor);

--SUM(v.qtd * v.vrunt): Calcula o total de vendas por vendedor (quantidade * valor unitário).
--ROUND(SUM(v.qtd * v.vrunt) * vd.perccomissao  / 100, 2): Calcula a comissão para cada vendedor, arredondada para duas casas decimais.
--JOIN: Conecta a tabela de vendas (tbvendas) com a tabela de vendedores (tbvendedor) usando a chave cdvdd.
--WHERE: Filtra as vendas com o status "Concluído".
--GROUP BY vd.nmvdd: Agrupa os resultados por vendedor para calcular a soma das vendas e da comissão.
--ORDER BY comissao DESC: Ordena os vendedores pela maior comissão.

SELECT 
    vd.nmvdd AS vendedor,
    SUM(v.qtd * v.vrunt) AS valor_total_vendas,
    ROUND(SUM(v.qtd * v.vrunt) * vd.perccomissao / 100, 2) AS comissao
FROM tbvendas v
JOIN tbvendedor vd ON v.cdvdd = vd.cdvdd
WHERE v.status = 'Concluído'
GROUP BY vd.nmvdd
ORDER BY comissao DESC;



--11
--Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.
--SUM(v.qtd * v.vrunt): Calcula o gasto total de cada cliente (quantidade * valor unitário).
--WHERE: Filtra apenas as vendas com o status "Concluído".
--GROUP BY v.cdcli, v.nmcli: Agrupa os resultados por cliente, tanto pelo código quanto pelo nome.
--ORDER BY gasto DESC: Ordena os resultados em ordem decrescente pelo gasto total.
--LIMIT 1: Retorna apenas o cliente com o maior gasto.
SELECT 
    v.cdcli, 
    v.nmcli, 
    SUM(v.qtd * v.vrunt) AS gasto
FROM tbvendas v
WHERE v.status = 'Concluído'
GROUP BY v.cdcli, v.nmcli
ORDER BY gasto DESC
LIMIT 1;

--12
--Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.
--Observação: Apenas vendas com status concluído.

--JOIN tbdependente: Faz a junção entre tbvendedor e tbdependente para trazer os dependentes dos vendedores.
--SUM(v.qtd * v.vrunt): Calcula o valor total de vendas para cada dependente (considerando as vendas do vendedor associado).
--WHERE v.status = 'Concluído': Filtra apenas as vendas concluídas.
--GROUP BY d.cddep, d.nmdep, d.dtnasc: Agrupa os resultados por dependente.
--HAVING valor_total_vendas > 0: Garante que apenas dependentes com valor total de vendas maior que zero sejam considerados.
--ORDER BY valor_total_vendas ASC: Ordena os dependentes pelo menor valor total de vendas.
--LIMIT 1: Retorna apenas o  menor valor total de vendas.

SELECT 
    d.cddep, 
    d.nmdep, 
    d.dtnasc, 
    SUM(v.qtd * v.vrunt) AS valor_total_vendas
FROM tbvendas v
JOIN tbvendedor vd ON v.cdvdd = vd.cdvdd
JOIN tbdependente d ON vd.cdvdd = d.cdvdd
WHERE v.status = 'Concluído'
GROUP BY d.cddep, d.nmdep, d.dtnasc
HAVING valor_total_vendas > 0
ORDER BY valor_total_vendas ASC
LIMIT 1;


--13
--Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.
--usei comando , pois estava escrevendo E-Commerce
SELECT DISTINCT nmcanalvendas
FROM tbvendas;

--WHERE v.nmcanalvendas IN ('Ecommerce', 'Matriz'): Filtra as vendas feitas pelos canais de Ecommerce ou Matriz.
--SUM(v.qtd): Soma a quantidade vendida de cada produto.
--GROUP BY v.cdpro, v.nmcanalvendas, v.nmpro: Agrupa os resultados por produto e canal de vendas.
--ORDER BY quantidade_vendas ASC: Ordena os resultados pela quantidade vendida em ordem crescente (menos vendidos primeiro).
--LIMIT 10: Limita os resultados aos 10 produtos menos vendidos.

SELECT 
    v.cdpro, 
    v.nmcanalvendas, 
    v.nmpro, 
    SUM(v.qtd) AS quantidade_vendas
FROM tbvendas v
WHERE v.status = 'Concluído'
AND v.nmcanalvendas IN ('Ecommerce', 'Matriz')
GROUP BY v.cdpro, v.nmcanalvendas, v.nmpro
ORDER BY quantidade_vendas ASC
LIMIT 10;

--14
--Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.

--Observação: Apenas vendas com status concluído.
--ROUND(AVG(v.qtd * v.vrunt), 2): Calcula o gasto médio por estado, multiplicando a quantidade pelo valor unitário e arredondando o resultado para duas casas decimais.
--GROUP BY v.estado: Agrupa os resultados por estado da federação.
--ORDER BY gastomedio DESC: Ordena os estados em ordem decrescente de gasto médio.
SELECT 
    v.estado, 
    ROUND(AVG(v.qtd * v.vrunt), 2) AS gastomedio
FROM tbvendas v
WHERE v.status = 'Concluído'
GROUP BY v.estado
ORDER BY gastomedio DESC;


--15
--Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.
--WHERE v.deletado = '1': Filtra as vendas que foram marcadas como deletadas. Suponho que o valor '1' indique que a venda foi deletada, baseado no campo "deletado" do diagrama.
--ORDER BY v.cdven ASC: Ordena os resultados pelo código da venda (cdven) em ordem crescente.
--usei o para  verificando se "1" realmente indica uma venda deletada 
SELECT DISTINCT deletado
FROM tbvendas;

SELECT v.cdven
FROM tbvendas v
WHERE v.deletado = '1'
ORDER BY v.cdven ASC;


--16
--Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º).
--Obs: Somente vendas concluídas.

--ROUND(AVG(v.qtd), 4): Calcula a quantidade média de produtos vendidos, arredondada para quatro casas decimais.
--WHERE v.status = 'Concluído': Filtra apenas as vendas que estão com o status "Concluído".
--GROUP BY v.estado, v.nmpro: Agrupa os resultados por estado e produto.
--ORDER BY v.estado ASC, v.nmpro ASC: Ordena os resultados primeiro por estado (crescente) e depois por nome do produto (crescente).
SELECT 
    v.estado, 
    v.nmpro, 
    ROUND(AVG(v.qtd), 4) AS quantidade_media
FROM tbvendas v
WHERE v.status = 'Concluído'
GROUP BY v.estado, v.nmpro
ORDER BY v.estado ASC, v.nmpro ASC;
