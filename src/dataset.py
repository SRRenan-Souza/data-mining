from dataclasses import dataclass
from pathlib import Path
from enum import Enum

import pandas as pd
import requests, json

DIR : Path = Path(__file__).parent if "__file__" in locals() else Path.cwd()
DATA: Path = DIR / "data"


class Provider(Enum):
    IBGE = "https://servicodados.ibge.gov.br/api/v3/agregados/"
    SIDRA = "https://apisidra.ibge.gov.br/"


def load_queries(file_path: Path) -> dict:
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)["queries"]

@dataclass
class API:
    queries: Path = DATA / "queries.json"

    # Consulta uma API e retorna uma tabela nomeada e formatada
    def query(self, provider: Provider, info: str) -> pd.DataFrame:
        """ Implementação das APIs do IBGE/SIDRA conforme
            as consultas predefinidas em queries.json. """

        queries: dict = load_queries(self.queries)

        try:
            query = queries[provider.name][info]
        except KeyError:
            raise KeyError(f"Consulta '{info}' do provedor '{provider.name}' não foi encontrada.")

        url = provider.value + query["params"]

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        data = response.json()

        table = self._unnest(data) if provider == Provider.IBGE else pd.DataFrame(data)

        if features := query.get("features"):
            table = table[features]
            table.columns = table.iloc[0]
            table = table.iloc[1:].reset_index(drop = True)

        # DEBUG
        print(table)
        return table

    def _unnest(self, data: list) -> pd.DataFrame:

        """  Desaninhamento os dados serializados 
             pela API de dados agregados do IBGE. """

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

