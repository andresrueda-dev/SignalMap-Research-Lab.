"""
=========================================================
SignalMap Research Lab
Dataset Builder v1.0
=========================================================
"""

import pandas as pd

from core.state_vector import StateVectorEngine


class DatasetBuilder:

    def __init__(self):

        self.engine = StateVectorEngine()

    def build(self, csv_file):

        print("\nLeyendo histórico...")

        df = pd.read_csv(csv_file)

        # Orden cronológico
        df = df.sort_values("CONCURSO").reset_index(drop=True)

        print(f"Registros: {len(df)}")

        registros = []

        for _, row in df.iterrows():

            numeros = [

                row["R1"],
                row["R2"],
                row["R3"],
                row["R4"],
                row["R5"],
                row["R6"]

            ]

            vector = self.engine.build_vector(numeros)

            vector["concurso"] = row["CONCURSO"]
            vector["fecha"] = row["FECHA"]
            vector["producto"] = row["NPRODUCTO"]
            vector["r7"] = row["R7"]
            vector["bolsa"] = row["BOLSA"]

            registros.append(vector)

        resultado = pd.DataFrame(registros)

        print("Dataset generado.")

        return resultado
