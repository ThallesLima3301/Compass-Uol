
Durante a Sprint 5, aprendi bastante, especialmente sobre AWS, uma área que me interessou muito. O ponto mais positivo foi a introdução prática aos serviços da AWS, que me permitiu aprender de forma simples e envolvente. Outro destaque foi a oportunidade de aprender a fazer a conexão com o S3 por meio do desafio proposto, o que foi uma experiência valiosa.

De forma geral, considerei a sprint fácil e, como terminei as atividades com bastante tempo livre, acabei explorando mais do que o necessário. Aproveitei para pesquisar possíveis bônus e aprimorar ainda mais meus conhecimentos.
e fiz um curso sobre AWS chamado "Master AWS with Python and Bot03" achei bem legal ele
Atualmente, já concluí os  cursos e estou gostando bastante da trilha. Estou ansioso pela próxima sprint e pelos novos aprendizados que ela trará 😊.

# Certificados

 [ Certificados](../Sprint_5/certificados/img/AWS%20Skill%20Builder%20Course%20Completion%20Certificate.pdf)

  [ Link publico](https://www.credly.com/badges/8f42540e-33ce-4e93-b419-5f825c0b4111/public_url)

  
 [ Certificados](../Sprint_5/certificados/img/AWS_Cloud_Quest_Badge.png)

# Exercícios

1. [Resposta Ex1](../Sprint_5/exercicios/index.html)

Documentação do Exercício de Hospedagem de Site Estático no AWS S3
Bom exercício, eu gostei de fazer, de certo modo. Aqui eu vou documentar um pouco melhor sobre. Achei o enunciado muito grande para coisas algo tão simples.

Passo 1: Criar um Bucket no S3
O primeiro passo foi acessar o console do AWS S3 e criar um bucket para hospedar o site. Defini o nome e a região do bucket, escolhendo us-east-1 para facilitar a configuração e deixar no padrão.

![Img 17 EX](../Sprint_5/evidencias/img_resposta/img_resposta17.png)


Passo 2: Habilitar a Hospedagem Estática
Depois de criar o bucket, eu habilitei a hospedagem de site estático. Defini o index.html como o documento de índice e o 404.html como o documento de erro. Foi simples, mas achei que poderia ser mais direto no enunciado.


Passo 3: Upload dos Arquivos
Fiz o upload dos arquivos necessários:

![Img 18 EX](../Sprint_5/evidencias/img_resposta/img_resposta18.png)

index.html: Página inicial do site com um link para download do CSV.
404.html: Página de erro personalizada.
nomes.csv: O arquivo de dados que será baixado pelo usuário.

Passo 4: Configurar Permissões e Política de Bucket
Para garantir que o site funcionasse, precisei ajustar as permissões:

![Img 19 EX](../Sprint_5/evidencias/img_resposta/img_resposta19.png)

Editei a Política do Bucket para permitir acesso público de leitura a todos os objetos.
Verifiquei as permissões individuais de cada arquivo, garantindo que todos tivessem a leitura pública habilitada.

Passo 5: Testar o Endpoint do Site
Com tudo configurado, testei o endpoint do site. O index.html carregou corretamente, e o link para download do CSV estava funcionando após ajustar as permissões.

![Img 20 EX](../Sprint_5/evidencias/img_resposta/img_resposta20.png)

![Img 20 EX](../Sprint_5/evidencias/img_resposta/img_resposta21.png)

Conclusão
Achei interessante explorar o AWS S3 para hospedar um site estático, mas percebi que, apesar de ser um processo simples, o enunciado poderia ser mais objetivo. No geral, foi um bom exercício para entender as configurações básicas de permissões e políticas no S3.



# Desafios

[Desafio 1](../Sprint_5/Desafio/README.md)

# Evidências

Vou documentar aqui a lógica por trás das minhas ideas, usando imagens. A ideia é mostrar de forma clara e direta o que eu fiz e por que tomei certas decisões, facilitando o entendimento do processo.

Procurei um arquivo CSV ou JSON no portal de dados públicos do Governo Brasileiro e verifiquei se ele está dentro do limite permitido no S3.
link do arquivo:

https://dados.gov.br/dados/conjuntos-dados/inabilitados-para-funcao-publica-segundo-tcu

![Img 1 EX](../Sprint_5/evidencias/img_resposta/img_resposta16.png)

Vou explicar um pouco sobre o meu diretório:

__pycache__:



No meu projeto, o diretório __pycache__ é onde o Python armazena os arquivos compilados (.pyc) dos módulos que utilizo. No meu caso, ele contém os arquivos compilados dos scripts data_processing e s3_operations.

Arquivos .py:
data_processing.py: Este é o script onde defini as funções para processar o DataFrame, incluindo tarefas como limpar, manipular e analisar dados.
main.py: Esse é o arquivo principal do meu projeto, onde coordeno as operações entre os diferentes módulos e scripts que criei.
s3_operations.py: Esse script contém funções específicas para operações no S3, como download e upload de arquivos usando a biblioteca boto3.
Arquivos .csv:
relatorio_inabilitado_s3.csv: Este é o arquivo que baixei do S3 e que utilizo para manipulações e análises no meu projeto.
resultado_sprint_5.csv: Este é o arquivo gerado após o processamento realizado pelo meu script, onde aplico transformações e agregações com o Pandas.
.env:
O arquivo .env é onde armazeno minhas variáveis de ambiente, como credenciais e configurações sensíveis que não quero expor diretamente no código. Utilizo a biblioteca dotenv para carregar essas variáveis de maneira segura.

Eu decidi usar o arquivo .env porque não gostava de ver as senhas aparecendo diretamente no código. Por isso, pesquisei uma maneira de escondê-las e proteger essas informações, e encontrei essa solução.

Além disso, importei o módulo logging após fazer uma pesquisa sobre ele e achei interessante adicioná-lo ao meu código como um bônus. Ele é uma forma eficiente de registrar eventos e informações úteis, o que ajuda a monitorar o comportamento do programa e a identificar problemas de maneira mais profissional.
Vamos fala do desafio. 

# Documentação do Desafio AWS S3

1. Objetivo
Meu objetivo com esse desafio foi praticar os conhecimentos adquiridos sobre AWS, especificamente com o serviço S3. A ideia era manipular arquivos diretamente no S3 usando scripts em Python com a biblioteca boto3 e pandas.

2. Entregáveis
Para concluir o desafio, preparei os seguintes entregáveis:

Um arquivo Markdown com evidências (prints) e documentação explicando cada etapa executada.
Arquivos .py contendo os códigos para download, processamento, e upload dos arquivos no S3.
Um arquivo CSV com os resultados processados e salvos.
3. Preparação
Primeiramente, certifiquei-me de que minha conta da Compass AWS estava configurada e que eu tinha as permissões necessárias para criar e manipular buckets e arquivos no S3.

4. Desafio
O desafio consistiu em trabalhar com dados de um CSV baixado do portal de dados públicos do Governo Brasileiro. Escolhi o arquivo relatorio_inabilitado.csv e segui os passos abaixo:

4.1 AWS S3
1. Escolha do arquivo
Escolhi o arquivo relatorio_inabilitado.csv porque ele se encaixava nos critérios exigidos pelo desafio. Garanti que ele era único na turma.

2. Análise dos dados
Analisei o conteúdo do arquivo localmente usando um editor de texto para conhecer os dados e planejar as manipulações necessárias.



3. Carregamento no S3
Utilizei um script Python para carregar o arquivo relatorio_inabilitado_s3.csv para um bucket no S3, utilizando a biblioteca boto3. Fiz a configuração das credenciais no arquivo .env para manter as informações sensíveis fora do código.

4. Manipulação do DataFrame
Em outro script, carreguei o arquivo diretamente do S3 e criei um DataFrame usando pandas para aplicar as seguintes manipulações:

![Img 1 EX](../Sprint_5/evidencias/img_resposta/img_resposta7.png)

Usei uma cláusula que filtra dados com dois operadores lógicos: selecionei registros onde a "Data Final" era posterior a 2025 e o "Trânsito em Julgado" era anterior a 2023.

![Img 9 EX](../Sprint_5/evidencias/img_resposta/img_resposta9.png)

Apliquei funções de agregação, como calcular a diferença de anos entre duas colunas de data.

![Img 10 EX](../Sprint_5/evidencias/img_resposta/img_resposta10.png)

Utilizei uma função condicional para determinar se um registro estava "Válido" ou "Expirado" com base na data atual.

![Img 11 EX](../Sprint_5/evidencias/img_resposta/img_resposta11.png)

Fiz conversões de colunas para strings formatadas, incluindo a limpeza de CPFs e transformação de nomes para maiúsculas.

![Img 12 EX](../Sprint_5/evidencias/img_resposta/img_resposta12.png)

Fiz algumas mudanças no meu código para deixá-lo mais prático e organizado. Primeiro, adicionei um comando que cria a pasta resultados automaticamente, garantindo que os arquivos CSV sejam salvos sem erro, independente de onde o script rode. Também usei variáveis para deixar mais fácil mudar o nome dos arquivos no futuro, sem precisar mexer em várias partes do código.

Além disso, troquei o método .head() pelo .sample() para mostrar amostras aleatórias dos dados(somente para o video), dando uma visão mais variada dos registros. Estruturei o upload dos arquivos para o S3 de forma mais organizada, colocando tudo em pastas. E, por fim, implementei o logging para registrar mensagens e monitorar a execução, facilitando a identificação de problemas.

Essas mudanças tornaram o código mais flexível e fácil de ajustar para diferentes cenários, deixando o fluxo mais automatizado e eficiente.

![Img 9 EX](../Sprint_5/evidencias/img_resposta/Desafio_resultados_23.png)

![Img 9 EX](../Sprint_5/evidencias/img_resposta/Desafio_resultados_24.png)

5. Salvando e enviando o arquivo

    # Fazer o upload dos arquivos CSV para o bucket S3
    upload_file_s3(bucket_name, 'resultados/tabela_original.csv', 'resultados/tabela_original.csv')
    upload_file_s3(bucket_name, 'resultados/tabela_filtrada.csv', 'resultados/tabela_filtrada.csv')
    upload_file_s3(bucket_name, 'resultados/tabela_expirados.csv', 'resultados/tabela_expirados.csv')
    upload_file_s3(bucket_name, output_file, output_file)

6. Documentação no Git
Documentei todo o processo em um arquivo Markdown, incluindo prints das execuções e os códigos utilizados. Armazenei os arquivos .csv e .py, juntamente com as evidências, no meu repositório Git.


# Melhor detalhes sobre o desafio 

![Desafio 5](../Sprint_5/Desafio/README.md)

# Feedback

Durante a Sprint 6, tive uma experiência bastante positiva, especialmente em relação à implementação do código, que achei relativamente fácil e direta. Não enfrentei grandes dificuldades técnicas nessa parte. Contudo, o maior desafio foi realmente desenvolver uma análise que fosse sólida e envolvente. Confesso que ainda me sinto um pouco incerto sobre qual caminho seguir para criar uma análise que traga insights realmente interessantes e aprofundados.

De modo geral, aprendi muito e aproveitei bem a oportunidade para expandir meus conhecimentos, especialmente na prática. Inclusive, fiz alguns cursos adicionais por fora para complementar meu aprendizado. No entanto, senti que a sprint foi um pouco superficial em termos de conteúdo. Consegui finalizar todas as atividades com bastante antecedência, e isso acabou me levando a procrastinar um pouco, pois não havia tanto a explorar além do que foi proposto. Apesar disso, me esforcei para buscar maneiras de enriquecer o que foi entregue.

Minha avaliação para essa sprint é 6/10. Foi uma experiência produtiva e enriquecedora em certos aspectos, mas eu gostaria que houvesse mais profundidade em algumas áreas. Ter um conteúdo mais desafiador e um escopo mais amplo permitiria que eu me envolvesse ainda mais e realmente me aprofundasse na análise de dados.