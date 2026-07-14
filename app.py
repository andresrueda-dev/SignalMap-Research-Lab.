import streamlit as st
import os

st.title("🧪 SignalMap Research Lab")

st.write("La app inició correctamente.")

st.write("Directorio actual:")

st.code(os.getcwd())

st.write("Archivos:")

st.write(os.listdir())

if os.path.exists("data"):
    st.success("Carpeta data encontrada")
    st.write(os.listdir("data"))
else:
    st.error("No existe la carpeta data")
