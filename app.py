"""
=========================================================
SignalMap Research Lab
APP PRINCIPAL
=========================================================
"""

import os
import pandas as pd

from core.state_vector import StateVectorEngine


# ============================================
# CONFIGURACIÓN
# ============================================

DATA_FILE = "data/historico.csv"

OUTPUT_FOLDER = "output"

OUTPUT_FILE = "output/state_vectors.csv"


# ============================================
# CREAR CARPETA OUTPUT
# ============================================

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


print("=" * 60)
print(" SIGNALMAP RESEARCH LAB ")
print("=" * 60)


# ============================================
# CARGAR HISTÓRICO
# ============================================

print("\nCargando histórico...")

df = pd.read_csv(DATA_FILE)

print(f"Registros encontrados: {len(df)}")


# ============================================
# GENERAR STATE VECTORS
# ============================================

print("\nGenerando State Vectors...")

engine = StateVectorEngine()

state_vectors = engine.build_dataset(df)


# ============================================
# GUARDAR CSV
# ============================================

state_vectors.to_csv(

    OUTPUT_FILE,

    index=False,

    encoding="utf-8-sig"

)

print("\nState Vectors generados correctamente.")

print(f"Variables creadas: {len(state_vectors.columns)}")

print(f"Registros procesados: {len(state_vectors)}")

print(f"\nArchivo generado:")

print(OUTPUT_FILE)

print("\nProceso terminado.")
