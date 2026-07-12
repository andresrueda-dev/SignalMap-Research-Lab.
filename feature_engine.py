import numpy as np
import pandas as pd


class FeatureEngine:

    def __init__(self):
        pass


    def build(self, df):

        rows = []

        columnas = ["F1","F2","F3","F4","F5","F6"]

        for _,row in df.iterrows():

            nums = sorted(
                row[columnas].astype(int).tolist()
            )

            gaps = np.diff(nums)

            pares = sum(n%2==0 for n in nums)

            impares = 6-pares

            vector = {

                "suma":np.sum(nums),

                "media":np.mean(nums),

                "mediana":np.median(nums),

                "std":np.std(nums),

                "var":np.var(nums),

                "max":max(nums),

                "min":min(nums),

                "rango":max(nums)-min(nums),

                "pares":pares,

                "impares":impares,

                "consecutivos":np.sum(gaps==1),

                "gap_medio":np.mean(gaps),

                "gap_std":np.std(gaps),

                "gap_max":np.max(gaps),

                "gap_min":np.min(gaps),

            }

            rows.append(vector)

        return pd.DataFrame(rows)
