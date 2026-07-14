"""
=========================================================
SignalMap Research Lab
Memory Engine v1.0
=========================================================
"""

import pandas as pd


class MemoryEngine:

    def __init__(self):
        pass


    def get_memory(self,
                   similarity_matrix,
                   state_vectors,
                   top=20):

        current = state_vectors.iloc[-1]["concurso"]

        scores = similarity_matrix.loc[current]

        scores = scores.drop(current)

        scores = scores.sort_values(
            ascending=False
        )

        similares = scores.head(top)

        memoria = []

        for concurso in similares.index:

            idx = state_vectors[
                state_vectors["concurso"] == concurso
            ].index[0]

            siguiente = idx + 1

            if siguiente >= len(state_vectors):
                continue

            memoria.append({

                "estado": concurso,

                "similitud":
                    round(similares.loc[concurso],4),

                "siguiente":
                    state_vectors.iloc[siguiente]["concurso"]

            })

        return pd.DataFrame(memoria)
