"""
=========================================================
Feature Discovery Engine
=========================================================
"""

import pandas as pd

class FeatureDiscovery:

    def analyze(self, df):

        numeric = df.select_dtypes(include="number")

        report = []

        for col in numeric.columns:

            report.append({

                "variable": col,

                "media": numeric[col].mean(),

                "std": numeric[col].std(),

                "min": numeric[col].min(),

                "max": numeric[col].max(),

                "nulos": numeric[col].isna().sum()

            })

        return pd.DataFrame(report)
