


8

estava escrevendo "concluída"
dei um 

SELECT DISTINCT status

FROM tbvendas;

e entendi oq estava acontecendo 

SELECT v.cdvdd, vd.nmvdd
FROM tbvendas v
JOIN tbvendedor vd ON v.cdvdd = vd.cdvdd
WHERE v.status = 'Concluído'
GROUP BY v.cdvdd
ORDER BY COUNT(v.cdven) DESC
LIMIT 1;

9

SELECT v.cdpro, v.nmpro
FROM tbvendas v
WHERE v.status = 'Concluído'
AND v.dtven BETWEEN '2014-02-03' AND '2018-02-02'
GROUP BY v.cdpro, v.nmpro
ORDER BY SUM(v.qtd) DESC
LIMIT 1;



utilizei o comando para fazer a verificacao dos nomes
PRAGMA table_info(tbvendedor);

10

SELECT 
    vd.nmvdd AS vendedor,
    SUM(v.qtd * v.vrunt) AS valor_total_vendas,
    ROUND(SUM(v.qtd * v.vrunt) * vd.perccomissao / 100, 2) AS comissao
FROM tbvendas v
JOIN tbvendedor vd ON v.cdvdd = vd.cdvdd
WHERE v.status = 'Concluído'
GROUP BY vd.nmvdd
ORDER BY comissao DESC;



11

SELECT 
    v.cdcli, 
    v.nmcli, 
    SUM(v.qtd * v.vrunt) AS gasto
FROM tbvendas v
WHERE v.status = 'Concluído'
GROUP BY v.cdcli, v.nmcli
ORDER BY gasto DESC
LIMIT 1;

12

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

da pra fazer fazem utilziando o  IS NOT NULL

HAVING SUM(v.qtd * v.vrunt) IS NOT NULL

13

usei ocomando, pois escrevendo E-Commerce
SELECT DISTINCT nmcanalvendas
FROM tbvendas;

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

14

SELECT 
    v.estado, 
    ROUND(AVG(v.qtd * v.vrunt), 2) AS gastomedio
FROM tbvendas v
WHERE v.status = 'Concluído'
GROUP BY v.estado
ORDER BY gastomedio DESC;


15

usei o para  verificando se "1" realmente indica uma venda deletada 
SELECT DISTINCT deletado
FROM tbvendas;


SELECT v.cdven
FROM tbvendas v
WHERE v.deletado = '1'
ORDER BY v.cdven ASC;


16

SELECT 
    v.estado, 
    v.nmpro, 
    ROUND(AVG(v.qtd), 4) AS quantidade_media
FROM tbvendas v
WHERE v.status = 'Concluído'
GROUP BY v.estado, v.nmpro
ORDER BY v.estado ASC, v.nmpro ASC;
