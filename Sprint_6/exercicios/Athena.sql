CREATE DATABASE meubanco

CREATE EXTERNAL TABLE IF NOT EXISTS meubanco.nomes ( nome STRING, sexo STRING, ano INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES ( 'serialization.format' = ',', 'field.delim' = ','
)
LOCATION 's3://ex-labawss3/dados/'


SELECT * FROM meubanco.nomes LIMIT 10

SELECT nome, COUNT(*) AS total, FLOOR(ano / 10) * 10 AS decada
FROM meubanco.nomes
WHERE ano >= 1950
GROUP BY nome, FLOOR(ano / 10) * 10
ORDER BY decada, total DESC
LIMIT 3

SELECT nome 
FROM meubanco.nomes 
WHERE ano = 1999 
ORDER BY nome 
LIMIT 15;
