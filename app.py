import streamlit as st
import pandas as pd

st.title("SignalMap Research Lab")

archivo = "data/historico.csv"

with open(archivo, "rb") as f:
    datos = f.read(200)

st.subheader("Primeros bytes del archivo")
st.code(datos)

st.write("Tamaño del archivo (bytes):", len(open(archivo, "rb").read()))

try:

    df = pd.read_csv(
        archivo,
        sep=None,
        engine="python"
    )

    st.success("CSV leído correctamente")

    st.write(df.head())

    st.write(df.columns.tolist())

except Exception as e:

    st.error(e)
