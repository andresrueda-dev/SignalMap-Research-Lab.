"""
=========================================================
SignalMap Research Lab
Experiment Engine v1.0
=========================================================
"""

import pandas as pd


class ExperimentEngine:

    def __init__(self, dataset):
        self.df = dataset.copy()

    def add_target(self):

        objetivos = []

        for i in range(len(self.df) - 1):

            actual = {
                self.df.loc[i, "R1"],
                self.df.loc[i, "R2"],
                self.df.loc[i, "R3"],
                self.df.loc[i, "R4"],
                self.df.loc[i, "R5"],
                self.df.loc[i, "R6"],
            }

            siguiente = {
                self.df.loc[i + 1, "R1"],
                self.df.loc[i + 1, "R2"],
                self.df.loc[i + 1, "R3"],
                self.df.loc[i + 1, "R4"],
                self.df.loc[i + 1, "R5"],
                self.df.loc[i + 1, "R6"],
            }

            objetivos.append(len(actual.intersection(siguiente)))

        objetivos.append(None)

        self.df["TARGET"] = objetivos

        return self.df

    def experiment_sum(self, limit=150):

        datos = self.df.dropna(subset=["TARGET"])

        grupo1 = datos[datos["suma"] < limit]

        grupo2 = datos[datos["suma"] >= limit]

        return {

            "experimento": "Low Sum",

            "limite": limit,

            "casos_bajos": len(grupo1),

            "casos_altos": len(grupo2),

            "media_bajos": round(grupo1["TARGET"].mean(),3),

            "media_altos": round(grupo2["TARGET"].mean(),3)

        }
