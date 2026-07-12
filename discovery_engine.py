import pandas as pd


class DiscoveryEngine:

    def summary(self,features):

        return {

            "variables":

            len(features.columns),

            "registros":

            len(features),

            "correlaciones":

            features.corr(numeric_only=True)

        }
