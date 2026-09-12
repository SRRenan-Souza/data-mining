from dataclasses import dataclass
from pathlib import Path

import pandas as pd
import requests, json

DIR : Path = Path(__file__).parent if "__file__" in locals() else Path.cwd()
DATA: Path = DIR / "data"

IBGE : str = "https://servicodados.ibge.gov.br/api/v3/agregados/"
SIDRA: str = "https://apisidra.ibge.gov.br/"

def load_queries(file_path: Path) -> dict:
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)["queries"]

@dataclass
class API:
    queries: Path = DATA/"queries.json"

    # Consulta uma API e retorna uma tabela nomeada e formatada
    def query(self, name: str) -> pd.DataFrame:

        """ Consulta as APIs do IBGE/SIDRA conforme predefinido em queries.JSON. """

        queries = load_queries(self.queries)

        if name not in queries:
            raise KeyError(f"Consulta não encontrada: {name}")

        query = queries[name]
        url   = query["api"] + query["url"]
    
        response = requests.get(url, timeout = 15)
        response.raise_for_status()

        data = response.json()

        # Tratamento das tabelas brutas para cada API
        if   IBGE == query["api"]:
            table = self._unnest(data)

        elif SIDRA == query["api"]:
            table = pd.DataFrame(data)


        # Seleciona os atributos desejados nas tabelas extraídas da API
        features = query.get("features")

        if features:
            table = table[list(features)]
            table = table.rename(columns = features)

        # DEBUG
        print(table)

        return table


    def _unnest(self, data: list) -> pd.DataFrame:

        """  Desaninha os dados serializados pela API de Agregados do IBGE. """

        tuples = []

        # Percorre os dados aninhados para extrair atributos específicos
        for variable in data:
            for result in variable.get("resultados", []):
                for serie in result.get("series", []):

                    tuples.append(
                        {
                            "codigo": serie.get("localidade", {}).get("id"),
                            "localidade": serie.get("localidade", {}).get("nome"),
                            **serie.get("serie", {}),
                        }
                    )

        return pd.DataFrame(tuples)

api: API = API()
dataset: list[pd.DataFrame] = []

try:
    # Armazena as tabelas extraídas da API em uma lista
    dataset.append(api.query("PIB por região"))
    dataset.append(api.query("PIB por município"))
    dataset.append(api.query("Alfabetização por município"))
    # OUTRAS CONSULTAS...
   

except FileNotFoundError as error:
    print(f"Arquivo de configuração não encontrado: {error}")

except json.JSONDecodeError as error:
    print(f"Erro ao decodificar JSON: {error}")

except KeyError as error:
    print(f"Consulta ou coluna não encontrada: {error}")

except requests.exceptions.RequestException as error:
    print(f"Erro de requisição de API/HTTP: {error}")

except Exception as error:
    print(f"Erro inesperado: {error}")