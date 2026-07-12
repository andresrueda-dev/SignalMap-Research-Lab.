import streamlit as st


class ReportEngine:

    @staticmethod

    def render(summary):

        st.metric(

            "Variables",

            summary["variables"]

        )

        st.metric(

            "Registros",

            summary["registros"]

        )

        st.subheader("Mapa de correlaciones")

        st.dataframe(

            summary["correlaciones"]

        )
