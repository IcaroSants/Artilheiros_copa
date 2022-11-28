# Artilheiros Copa

A copa do mundo é o principal tornei de futebol exitente. Uma das grandes expectativas é ver quem será artilheiro. Esse projeto consiste em extrair dados do site de estatisticas *ogol*(https://www.ogol.com.br/edition_stats.php?v=jt1&id_edicao=132894) e adicionar ao banco de dados. Para não precisarmos nos preucuparmos em rodar o codigo manualmente de tempo em tempo. Usamos o Apache Airflow para automatiza esse processo.

## arquivos

* **SQL/table.sql**: Arquivo sql que gera a base de dados e a tabela onde será salva os registros que serão extraídos.

* **DAG/src/extract.py**: Arquivo que possuia classe para extrair os dados do site.

* **DAG/src/connectPostgres.py**: Arquivo de conexao com o banco de dados.

* **DAG/copa.py**: Arquivo que cria a DAG que contem 2 tarefas: Extração e Inserção. A DAG foi escalonada para executar a cada 4 dias, pois é quando todas as seleções atingem o mesmo número de jogos.

## Execução
Primeiro passo é executar o arquivo **table.sql** que irá criar a tabela onde os dados serão salvos. Apos isso, adicione os Arquivos da pasta DAG ao diretorio onde airflow busca as DAGs criadas, depois e so acessar a interface do airflow e triiggar a DAG *copa*. 