-- Tabela de clientes (dimensão Cliente)
CREATE TABLE IF NOT EXISTS tb_dim_cliente (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(40),
    estadoCliente VARCHAR(40),
    paisCliente VARCHAR(40)
);

-- Tabela de carros (dimensão Carro)
CREATE TABLE IF NOT EXISTS tb_dim_carro (
    idCarro INT PRIMARY KEY,
    modeloCarro VARCHAR(80),
    marcaCarro VARCHAR(80),  -- Armazenando a marca diretamente como texto
    kmCarro INT,
    anoCarro INT,
    idTipoCombustivel INT
);

-- Tabela de vendedores (dimensão vendedor)
CREATE TABLE IF NOT EXISTS tb_dim_vendedor (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(15),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(40)
);

-- Tabela de tempo (dimensão Tempo)
CREATE TABLE IF NOT EXISTS tb_dim_tempo (
  idData INT PRIMARY KEY,
  data DATE,
  ano INT,
  mes INT,
  dia INT,
  diaSemana VARCHAR(10),
  trimestre INT
);


-- Inserção de dados distintos para a dimensão Cliente
INSERT INTO tb_dim_cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao;

-- Inserção de dados distintos para a dimensão Carro com marca incluída
INSERT INTO tb_dim_carro (idCarro, modeloCarro, marcaCarro, kmCarro, anoCarro, idTipoCombustivel)
SELECT DISTINCT idCarro, modeloCarro, classiCarro AS marcaCarro, kmCarro, anoCarro, idcombustivel
FROM tb_locacao;

-- Inserção de dados distintos para a dimensão Vendedor
INSERT INTO tb_dim_vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;

-- Verificando os dados inseridos
SELECT * FROM tb_dim_cliente;
SELECT * FROM tb_dim_carro;
SELECT * FROM tb_dim_vendedor;

-- Selecionar os dados de carros da tabela de locação
SELECT idCarro, modeloCarro, idcombustivel
FROM tb_locacao;

-- Inserindo dados na dimensão de Tempo (tb_dim_tempo) com a data separada
INSERT INTO tb_dim_tempo (idData, data, ano, mes, dia, diaSemana, trimestre)
SELECT DISTINCT 
    dataLocacao AS idData,  --  idData no formato YYYYMMDD
    SUBSTR(dataLocacao, 1, 4) || '-' || SUBSTR(dataLocacao, 5, 2) || '-' || SUBSTR(dataLocacao, 7, 2) AS data, 
    CAST(SUBSTR(dataLocacao, 1, 4) AS INT) AS ano,  -- Extraindo o ano
    CAST(SUBSTR(dataLocacao, 5, 2) AS INT) AS mes,  -- Extraindo o mês
    CAST(SUBSTR(dataLocacao, 7, 2) AS INT) AS dia,  -- Extraindo o dia
    CASE 
        WHEN STRFTIME('%w', SUBSTR(dataLocacao, 1, 4) || '-' || SUBSTR(dataLocacao, 5, 2) || '-' || SUBSTR(dataLocacao, 7, 2)) = '0' THEN 'Domingo'
        WHEN STRFTIME('%w', SUBSTR(dataLocacao, 1, 4) || '-' || SUBSTR(dataLocacao, 5, 2) || '-' || SUBSTR(dataLocacao, 7, 2)) = '1' THEN 'Segunda'
        WHEN STRFTIME('%w', SUBSTR(dataLocacao, 1, 4) || '-' || SUBSTR(dataLocacao, 5, 2) || '-' || SUBSTR(dataLocacao, 7, 2)) = '2' THEN 'Terça'
        WHEN STRFTIME('%w', SUBSTR(dataLocacao, 1, 4) || '-' || SUBSTR(dataLocacao, 5, 2) || '-' || SUBSTR(dataLocacao, 7, 2)) = '3' THEN 'Quarta'
        WHEN STRFTIME('%w', SUBSTR(dataLocacao, 1, 4) || '-' || SUBSTR(dataLocacao, 5, 2) || '-' || SUBSTR(dataLocacao, 7, 2)) = '4' THEN 'Quinta'
        WHEN STRFTIME('%w', SUBSTR(dataLocacao, 1, 4) || '-' || SUBSTR(dataLocacao, 5, 2) || '-' || SUBSTR(dataLocacao, 7, 2)) = '5' THEN 'Sexta'
        WHEN STRFTIME('%w', SUBSTR(dataLocacao, 1, 4) || '-' || SUBSTR(dataLocacao, 5, 2) || '-' || SUBSTR(dataLocacao, 7, 2)) = '6' THEN 'Sábado'
    END AS diaSemana,  -- Dia da semana
    CASE 
        WHEN CAST(SUBSTR(dataLocacao, 5, 2) AS INT) IN (1, 2, 3) THEN 1
        WHEN CAST(SUBSTR(dataLocacao, 5, 2) AS INT) IN (4, 5, 6) THEN 2
        WHEN CAST(SUBSTR(dataLocacao, 5, 2) AS INT) IN (7, 8, 9) THEN 3
        ELSE 4
    END AS trimestre  -- Trimestre do ano
FROM tb_locacao
WHERE dataLocacao IS NOT NULL;

--Contar o número de locações por ano:

SELECT t.ano, COUNT(*) AS total_locacoes
FROM vw_fato_locacao f
LEFT JOIN tb_dim_tempo t ON f.dataLocacao = t.idData
GROUP BY t.ano;

--Filtrar locações feitas em um trimestre específico (por exemplo, 1º trimestre de 2023):

SELECT *
FROM vw_fato_locacao f
LEFT JOIN tb_dim_tempo t ON f.dataLocacao = t.idData
WHERE t.ano = 2023 AND t.trimestre = 1;

--Obter locações feitas em dias específicos da semana, como segunda-feira:

SELECT *
FROM vw_fato_locacao f
LEFT JOIN tb_dim_tempo t ON f.dataLocacao = t.idData
WHERE t.diaSemana = 'Segunda';

--SELECT * FROM tb_dim_tempo;

-- Ajustando a View de Fato para usar apenas os IDs das dimensões
-- Não é necessário incluir os atributos (nomeCliente, modeloCarro, etc.) diretamente aqui, eles podem ser acessados por meio de junções com as dimensões quando necessário.
CREATE VIEW IF NOT EXISTS vw_fato_locacao AS
SELECT 
    loc.idLocacao,
    loc.idCliente,   -- Apenas o idCliente, sem os atributos como nomeCliente
    loc.idCarro,     -- Apenas o idCarro, sem os atributos como modeloCarro
    loc.idVendedor,  -- Apenas o idVendedor, sem os atributos como nomeVendedor
    loc.qtdDiaria,
    loc.vlrDiaria,
    loc.qtdDiaria * loc.vlrDiaria AS valorTotal,
    loc.dataLocacao,
    loc.dataEntrega
FROM 
    tb_locacao loc;

-- Agora a tabela fato só contém os IDs das dimensões e os valores numéricos.
-- Se eu precisar de mais informações, como nome do cliente ou modelo do carro, basta fazer um JOIN com as tabelas de dimensões (como mostrado abaixo).

-- Exemplo de junção com a dimensão cliente e carro para obter mais informações
SELECT 
    f.idLocacao,
    f.qtdDiaria,
    f.vlrDiaria,
    f.valorTotal,
    c.nomeCliente,  -- Atributo da dimensão cliente
    car.modeloCarro -- Atributo da dimensão carro
FROM 
    vw_fato_locacao f
LEFT JOIN tb_dim_cliente c ON f.idCliente = c.idCliente
LEFT JOIN tb_dim_carro car ON f.idCarro = car.idCarro;

-- Verificando a View criada
SELECT * FROM vw_fato_locacao;


-- Verificar clientes duplicados
SELECT idCliente, COUNT(*)
FROM tb_dim_cliente
GROUP BY idCliente
HAVING COUNT(*) > 1;

SELECT * FROM tb_dim_tempo;

-- Criação da View de Locações filtrando por datas entre 20150110 e 20180102
CREATE VIEW IF NOT EXISTS vw_locacoes_2015_2018 AS
SELECT 
    idLocacao,
    idCliente,
    idCarro,
    dataLocacao,
    qtdDiaria,
    vlrDiaria,
    (qtdDiaria * vlrDiaria) AS valorTotal
FROM 
    tb_locacao
WHERE 
    dataLocacao BETWEEN '20150110' AND '20180102';


-- Verificar os dados da View
SELECT * FROM vw_locacoes_2015_2018;

-- Caso eu não queira criar uma view e simplesmente rodar uma consulta com o filtro de datas:
--indignado de ter dado certo
SELECT 
    idLocacao,
    idCliente,
    idCarro,
    dataLocacao,
    qtdDiaria,
    vlrDiaria,
    (qtdDiaria * vlrDiaria) AS valorTotal
FROM 
    tb_locacao
WHERE 
    dataLocacao BETWEEN '20150110' AND '20180102';

-- View dimensões
    CREATE VIEW IF NOT EXISTS vw_dim_cliente AS
SELECT 
    idCliente,          -- ID único do cliente
    nomeCliente,        -- Nome do cliente
    cidadeCliente,      -- Cidade do cliente
    estadoCliente,      -- Estado do cliente
    paisCliente         -- País do cliente
FROM tb_dim_cliente;


SELECT * FROM vw_dim_cliente;  -- Consulta todos os clientes

CREATE VIEW vw_locacao_vendedor_estado AS
SELECT 
    nomeVendedor,
    sexoVendedor,
    estadoVendedor,
    nomeCliente,
    marcaCarro,
    modeloCarro,
    dataLocacao
FROM tb_locacao
WHERE estadoVendedor = 'São Paulo';


SELECT * FROM vw_locacao_vendedor_estado;