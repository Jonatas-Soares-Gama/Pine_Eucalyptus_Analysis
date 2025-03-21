#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "/home/jonatasgama/Desktop/project_silvicultura/data/raw/dados_ibge_rename_columns.csv"

df = pd.read_csv(file_path, sep=";", encoding="utf-8")

# Filtrar as espécies de interesse
df_filtered = df[df['Especie'].isin(['Eucalipto', 'Pinus'])]

df_filtered.to_csv('../data/silver/especie_pinus_eucalipto.csv', encoding='utf-8', sep=';', index=False)

df_filtered.columns

#%%

df_filtered.head()

