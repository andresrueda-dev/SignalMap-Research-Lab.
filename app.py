import os

from core.dataset_builder import DatasetBuilder
from core.feature_discovery import FeatureDiscovery

os.makedirs("output", exist_ok=True)

print("="*60)
print(" SIGNALMAP RESEARCH LAB ")
print("="*60)

builder = DatasetBuilder()

dataset = builder.build("data/historico.csv")

dataset.to_csv(
    "output/state_vectors.csv",
    index=False,
    encoding="utf-8-sig"
)

fd = FeatureDiscovery()

report = fd.analyze(dataset)

report.to_csv(
    "output/feature_report.csv",
    index=False,
    encoding="utf-8-sig"
)

print()

print(report)

print()

print("Dataset:",dataset.shape)

print("Reporte:",report.shape)
