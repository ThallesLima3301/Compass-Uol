# Caminho do diretório de backup
BACKUP_DIR="/home/ubuntu/ecommerce/vendas/backup"

# Arquivo final consolidado
OUTPUT_FILE="/home/ubuntu/ecommerce/relatorio_final.txt"

# Cria o arquivo final consolidado (vazio)
> $OUTPUT_FILE

# Adiciona um cabeçalho ao arquivo final
echo "Relatório Consolidado de Vendas" > $OUTPUT_FILE
echo "------------------------------" >> $OUTPUT_FILE

# Itera sobre todos os arquivos de relatório dentro do diretório de backup
for RELATORIO in $BACKUP_DIR/relatorio-*.txt; do
	echo "Processando: $RELATORIO" >> $OUTPUT_FILE
	cat $RELATORIO >> $OUTPUT_FILE
	echo -e "\n------------------------------\n" >> $OUTPUT_FILE
done

# Exibe uma mensagem de conclusão
echo "Consolidação concluída. Relatório final gerado em $OUTPUT_FILE"
