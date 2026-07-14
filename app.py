import streamlit as st
import pandas as pd

from core.state_vector import StateVectorEngine
from core.experiment_engine import ExperimentEngine

st.set_page_config(page_title="SignalMap Research Lab", layout="wide")

st.title("🧪 SignalMap Research Lab")

archivo = "data/historico.csv"

# ==========================
# CARGAR HISTÓRICO
# ==========================

dataset = pd.read_csv(
    archivo,
    sep=None,
    engine="python"
)

st.success(f"Histórico cargado correctamente ({len(dataset)} sorteos)")

st.dataframe(dataset.head())

# ==========================
# GENERAR STATE VECTORS
# ==========================

st.header("State Vector Engine")

engine = StateVectorEngine()

state_vectors = engine.build_dataset(dataset)

st.success(f"State Vectors generados: {len(state_vectors)}")

st.dataframe(state_vectors.head())

# ==========================
# EXPERIMENTO 001
# ==========================

st.header("Experimento 001")

exp = ExperimentEngine(state_vectors)

state_vectors = exp.add_target()

resultado = exp.experiment_sum(150)

st.json(resultado)
