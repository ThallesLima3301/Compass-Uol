# Diretório base achei que fosse precisar
BASE_DIR="/home/ubuntu/ecommerce"

# Navegangando para o diretório base
cd $BASE_DIR

# Criando o diretório 'vendas' e copia o arquivo dados_de_vendas.csv para ele
mkdir -p vendas
cp dados_de_vendas.csv vendas/

# Navegando até o diretório 'vendas'
cd vendas

# Criando o subdiretório 'backup'
mkdir -p backup

# Define a data atual no formato yyyymmdd_hhmmss 
DATA_ATUAL=$(date +%Y%m%d_%H%M%S)

# Copiando o arquivo dados_de_vendas.csv para o diretório backup com a data no nome
cp dados_de_vendas.csv backup/dados-$DATA_ATUAL.csv

# mudandoo nome do arquivo no diretório backup
mv backup/dados-$DATA_ATUAL.csv backup/backup-dados-$DATA_ATUAL.csv

# Criando o arquivo relatorio-DATA_ATUAL.txt e adicionando a data do sistema
echo "Data do sistema: $(date '+%Y/%m/%d %H:%M')" > backup/relatorio-$DATA_ATUAL.txt

# Adiciona a data do primeiro e último registro de venda
FIRST_DATE=$(head -n 2 backup/backup-dados-$DATA_ATUAL.csv | tail -n 1 | cut -d',' -f5)
LAST_DATE=$(tail -n 1 backup/backup-dados-$DATA_ATUAL.csv | cut -d',' -f5)
echo "Data do primeiro registro de venda: $FIRST_DATE" >> backup/relatorio-$DATA_ATUAL.txt
echo "Data do último registro de venda: $LAST_DATE" >> backup/relatorio-$DATA_ATUAL.txt

# Conta a quantidade total de itens diferentes vendidos
TOTAL_ITENS=$(cut -d',' -f2 backup/backup-dados-$DATA_ATUAL.csv | tail -n +2 | sort | uniq | wc -l)
echo "Quantidade total de itens diferentes vendidos: $TOTAL_ITENS" >> backup/relatorio-$DATA_ATUAL.txt

# Inclui as primeiras 10 linhas do arquivo no relatorio-DATA_ATUAL.txt
echo -e "\nPrimeiras 10 linhas do arquivo:" >> backup/relatorio-$DATA_ATUAL.txt
head -n 10 backup/backup-dados-$DATA_ATUAL.csv >> backup/relatorio-$DATA_ATUAL.txt

# Compacta o arquivo CSV no formato .zip
zip backup/dados-$DATA_ATUAL.zip backup/backup-dados-$DATA_ATUAL.csv

# Remove o arquivo CSV original do diretório backup
rm backup/backup-dados-$DATA_ATUAL.csv

# Remove o arquivo dados_de_vendas.csv do diretório vendas


# Exibe uma mensagem de conclusão
echo "Processamento de vendas concluído."
