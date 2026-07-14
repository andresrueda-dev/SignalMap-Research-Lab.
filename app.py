import os

from core.dataset_builder import DatasetBuilder

OUTPUT = "output"

os.makedirs(OUTPUT, exist_ok=True)

print("=" * 60)
print("SIGNALMAP RESEARCH LAB")
print("=" * 60)

builder = DatasetBuilder()

dataset = builder.build("data/historico.csv")

dataset.to_csv(

    "output/state_vectors.csv",

    index=False,

    encoding="utf-8-sig"

)

print()

print(dataset.head())

print()

print("Variables:", len(dataset.columns))

print("Registros:", len(dataset))
