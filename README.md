COMO MONTAR AS CONSULTAS NO SIDRA:
No site <https://sidra.ibge.gov.br/acervo>, selecione os Filtros desejados, em seguida siga para **Visualização** da tabela de dados agregados gerada. No cabeçalho da tabela, acesse **Funções/Página Web**, nela haverá um **código HTML**:

**EXEMPLO:**
<div data-selection="t/1278/n1/all/v/83/p/all/c10/0/c16/0/c11/0/c12/0/c27/0/l/v,p+c10+c16+c11,t+c12+c27" class="sidra-widget-table"></div>

No código, copie *data-selection*, excluindo quaisquer configurações de formatação da tabela localizadas após o **caractere /l**. Após isso, inclua o segmento copiado em **src/data/queries.JSON**:

**EXEMPLO:**
...
"nome da consulta": {
"api": <https://apisidra.ibge.gov.br/values/>
"url": "t/1278/n1/all/v/83/p/all/c10/0/c16/0/c11/0/c12/0/c27/0/"
}
...

Para finalização da consulta, pode-se adicionar outros marcadores conforme  descrito em <https://apisidra.ibge.gov.br/home/ajuda#Introducao>. Ademais, deve-se completar o **JSON**, projetando a tabela final com as características ou *features* mais importantes para análise. Para isso, utiliza-se o dicionário de índices <link indisponível>.



**OBSERVAÇÕES:**
Pretende-se refinar a construção das buscas futuramente. No presente momento é desejável apenas uma base de dados sólida para codificação da análise dos dados. Como essa parte dependerá apenas das tabelas extraídas, o desacoplamento permite alterar os métodos de extração e formatação dos conteúdos das APIs sem propagar mudanças no restante do código.


**ROADMAP**:
- Escolher no entre 4-6 *features* (atributos) usados na composição e análise das tabelas
- Popular **src/data/queries.JSON** com as consultas na **API do IBGE (PIB) e SIDRA**
- Filtrar os atributos úteis para cada consulta em **src/data/queries.JSON**
- Juntar as tabelas pela chave: **Região ou Município**
- Utilizar técnicas de normalização adequadas para cada tipo de dado
- Efetuar análise de associação/correlação entre os dados agrupados
- Construir diferentes meios de visualização gráfica dos resultados
- Estruturar o código/análise em um documento **Jupyter (.ipynb)** 
