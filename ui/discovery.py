import streamlit as st

from core.discovery.feature_engine import FeatureEngine

from core.discovery.discovery_engine import DiscoveryEngine

from core.discovery.report_engine import ReportEngine

from services.data_service import obtener_historico_procesado


def render_discovery():

    st.title("🧠 Discovery Engine")

    df = obtener_historico_procesado()

    fe = FeatureEngine()

    features = fe.build(df)

    de = DiscoveryEngine()

    summary = de.summary(features)

    ReportEngine.render(summary)

    st.subheader("State Vector")

    st.dataframe(features)
