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

from core.similarity_engine import SimilarityEngine

print("\nCalculando similitud entre estados...")

sim = SimilarityEngine()

matrix = sim.build_similarity_matrix(state_vectors)

matrix.to_csv(
    "output/similarity_matrix.csv",
    encoding="utf-8-sig"
)

ultimo = state_vectors.iloc[-1]["concurso"]

print("\nEstados más parecidos al último sorteo:\n")

print(
    sim.most_similar(
        matrix,
        ultimo,
        top=10
    )
)

print("\nProceso terminado.")

from core.memory_engine import MemoryEngine

print("\nConstruyendo memoria histórica...")

memory = MemoryEngine()

history = memory.get_memory(
    matrix,
    state_vectors,
    top=20
)

history.to_csv(
    "output/memory_engine.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nMemoria creada.")

print(history)
