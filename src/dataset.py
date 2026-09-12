from dataclasses import dataclass
from pathlib import Path

import pandas as pd
import requests, json

DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
DATA = DIR / "data"


def load_queries(file_path: Path) -> dict:
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)["queries"]

@dataclass
class API:
    queries: Path = DATA/"queries.json"

    # Consulta uma API e retorna uma tabela nomeada e formatada
    def query(self, name: str) -> pd.DataFrame:
        queries = load_queries(self.queries)

        if name not in queries:
            raise KeyError(f"Consulta não encontrada: {name}")

        query = queries[name]
        response = requests.get(query["url"], timeout = 15)
        response.raise_for_status()

        table = pd.DataFrame(response.json())
        features = query.get("features")

        # Seleciona os atributos desejados nas tabelas extraídas da API
        if features:
            table = table[list(features)]
            table = table.rename(columns = features)

        return table

api: API = API()
dataset: list[pd.DataFrame] = []

try:
    # Armazena as tabelas extraídas da API em uma lista
    dataset.append(api.query("Alfabetização por município"))
    dataset.append(api.query("PIB por região"))


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