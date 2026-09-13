### Consultando o SIDRA

No site do [SIDRA - Acervo](https://sidra.ibge.gov.br/acervo), selecione os **Filtros** desejados e, em seguida, acesse a **Visualização** da tabela de dados agregados gerada. No rodapé da página, selecione **Comparilhar Links** e copie endereço **Parâmetros para a API**

Para formatar a consulta, podem ser adicionados outros marcadores conforme descrito na [documentação da API SIDRA](https://apisidra.ibge.gov.br/home/ajuda#Introducao).

Para finalizar, coloque essas informações em `src/data/queries.json` e defina as características (*features*) mais importantes para a análise, utilizando como referência o **dicionário de índices** presente na própria página em que a tabela foi gerada.

### ROADMAP
- Escolher no entre 3-6 *features* (atributos) usados na composição e análise das tabelas
- Popular **src/data/queries.json** com as consultas na **API do IBGE (PIB) e SIDRA**
- Filtrar os atributos úteis para cada consulta em **src/data/queries.JSON**
- Juntar as tabelas pela chave: **Região ou Município**
- Utilizar técnicas de normalização adequadas para cada tipo de dado
- Efetuar análise de associação/correlação entre os dados agrupados
- Construir diferentes meios de visualização gráfica dos resultados
- Estruturar o código/análise em um documento **Jupyter (.ipynb)** 
