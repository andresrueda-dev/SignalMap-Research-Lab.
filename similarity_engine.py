"""
=========================================================
SignalMap Research Lab
Similarity Engine v1.0
=========================================================
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity


class SimilarityEngine:

    def __init__(self):
        self.scaler = StandardScaler()

    def build_similarity_matrix(self, df):

        numeric = df.select_dtypes(include=["number"]).copy()

        if "concurso" in numeric.columns:
            numeric = numeric.drop(columns=["concurso"])

        scaled = self.scaler.fit_transform(numeric)

        similarity = cosine_similarity(scaled)

        return pd.DataFrame(
            similarity,
            index=df["concurso"],
            columns=df["concurso"]
        )

    def most_similar(self, similarity_matrix, contest, top=10):

        if contest not in similarity_matrix.index:
            return None

        scores = similarity_matrix.loc[contest]

        scores = scores.drop(contest)

        scores = scores.sort_values(ascending=False)

        return scores.head(top)
