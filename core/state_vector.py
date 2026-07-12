"""
=========================================================
SignalMap Research Lab
State Vector Engine v1.0
=========================================================
Convierte cada sorteo en un vector de características
matemáticas listo para análisis.
"""

import numpy as np
import pandas as pd


class StateVectorEngine:

    def __init__(self):
        pass

    def _is_prime(self, n):

        if n < 2:
            return False

        for i in range(2, int(np.sqrt(n)) + 1):
            if n % i == 0:
                return False

        return True

    def build_vector(self, numbers):

        numbers = sorted([int(x) for x in numbers])

        gaps = np.diff(numbers)

        pares = sum(n % 2 == 0 for n in numbers)
        impares = len(numbers) - pares

        primos = sum(self._is_prime(n) for n in numbers)

        bajos = sum(n <= 28 for n in numbers)
        altos = len(numbers) - bajos

        consecutivos = int(np.sum(gaps == 1))

        vector = {

            "suma": np.sum(numbers),

            "media": np.mean(numbers),

            "mediana": np.median(numbers),

            "max": np.max(numbers),

            "min": np.min(numbers),

            "rango": np.max(numbers) - np.min(numbers),

            "std": np.std(numbers),

            "var": np.var(numbers),

            "pares": pares,

            "impares": impares,

            "primos": primos,

            "bajos": bajos,

            "altos": altos,

            "consecutivos": consecutivos,

            "gap_medio": np.mean(gaps),

            "gap_max": np.max(gaps),

            "gap_min": np.min(gaps),

            "gap_std": np.std(gaps)

        }

        return vector

    def build_dataset(self, df):

        registros = []

        columnas = ["F1", "F2", "F3", "F4", "F5", "F6"]

        for _, row in df.iterrows():

            numeros = row[columnas].tolist()

            vector = self.build_vector(numeros)

            if "CONCURSO" in row:
                vector["concurso"] = row["CONCURSO"]

            if "FECHA" in row:
                vector["fecha"] = row["FECHA"]

            registros.append(vector)

        resultado = pd.DataFrame(registros)

        columnas_finales = []

        if "concurso" in resultado.columns:
            columnas_finales.append("concurso")

        if "fecha" in resultado.columns:
            columnas_finales.append("fecha")

        resto = [c for c in resultado.columns if c not in columnas_finales]

        resultado = resultado[columnas_finales + resto]

        return resultado
