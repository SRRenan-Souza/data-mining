### Como montar as consultas no SIDRA

No site do [SIDRA - Acervo](https://sidra.ibge.gov.br/acervo), selecione os **Filtros** desejados e, em seguida, acesse a **Visualização** da tabela de dados agregados gerada. 

No código da página, copie o atributo `data-selection`, excluindo as configurações de formatação localizadas após o caractere `/l`. Em seguida, inclua o segmento copiado em `src/data/queries.json`.

Para finalizar a consulta, podem ser adicionados outros marcadores conforme descrito na [documentação da API SIDRA](https://apisidra.ibge.gov.br/home/ajuda#Introducao).

Por fim, complete `src/data/queries.json` definindo as características (*features*) mais importantes para a análise, utilizando como referência o **dicionário de índices**.

> **Observação:** pretende-se automatizar futuramente a construção das buscas. Neste momento, o objetivo é apenas estabelecer uma base sólida para a codificação das funcionalidades de análise de dados. O desacoplamento entre a extração, formatação e análise permite alterar esse procedimento sem propagar mudanças para o restante do código.



### ROADMAP
- Escolher no entre 4-6 *features* (atributos) usados na composição e análise das tabelas
- Popular **src/data/queries.JSON** com as consultas na **API do IBGE (PIB) e SIDRA**
- Filtrar os atributos úteis para cada consulta em **src/data/queries.JSON**
- Juntar as tabelas pela chave: **Região ou Município**
- Utilizar técnicas de normalização adequadas para cada tipo de dado
- Efetuar análise de associação/correlação entre os dados agrupados
- Construir diferentes meios de visualização gráfica dos resultados
- Estruturar o código/análise em um documento **Jupyter (.ipynb)** 
