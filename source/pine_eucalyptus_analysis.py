
#%%

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "/home/jonatasgama/Desktop/project_silvicultura/data/dados_ibge_rename_columns.csv"

df = pd.read_csv(file_path, sep=";", encoding="utf-8")

# Filtrar as espécies de interesse
df_filtered = df[df['Especie'].isin(['Eucalipto', 'Pinus'])]

df_filtered.columns

def limpar_valor(valor):
    """
    Limpa e converte valores monetários em string para float.
    Remove separadores de milhar (pontos) e converte vírgulas para pontos decimais.
    """
    if isinstance(valor, str):
        # Remove todos os pontos (separadores de milhar)
        valor = valor.replace('.', '')
        # Substitui vírgula por ponto (separador decimal)
        valor = valor.replace(',', '.')
        try:
            return float(valor) # Converte o valor para float
        except ValueError:  # Se não for possível converter, retorna None
            print(f"Não foi possível converter o valor: {valor}")   
            return None
    return valor    

def analisar_precos(df):

    df = df.copy()

    df['Preco_Medio_Nominal'] = df['Preco_Medio_Nominal'].apply(limpar_valor)

    precos_anuais = df.groupby(['Ano', 'Especie'])['Preco_Medio_Nominal'].mean().reset_index()
    return precos_anuais

precos_anuais = analisar_precos(df_filtered)

print(precos_anuais.head())
#%%

plt.figure(figsize=(10, 6))
sns.lineplot(data=analisar_precos(df_filtered), x='Ano', y='Preco_Medio_Nominal', hue='Especie')
plt.title('Preço Médio Nominal por Ano e Espécie')
plt.xlabel('Ano')
plt.ylabel('Preço Médio Nominal')
plt.legend(title='Espécie')
plt.show()

#%%
def analisar_producao_regional(df):
    # Cria uma cópia do dataframe para evitar modificações no original
    df = df.copy()
    # Limpa e converte valores monetários em string para float.
    df['Quantidade'] = df['Quantidade'].apply(limpar_valor)
    # Agrupa a produção por ano e UF
    producao_regional = df.groupby(['Ano', 'UF'])['Quantidade'].sum().reset_index()

    return producao_regional

producao_regional = analisar_producao_regional(df_filtered)

print(producao_regional.head())
#%%

plt.figure(figsize=(10, 6))
sns.lineplot(data=analisar_producao_regional(df_filtered), x='Ano', y='Quantidade', hue='UF')
plt.title('Produção Regional por Ano e UF')
plt.xlabel('Ano')
plt.ylabel('Produção Regional')
plt.legend(title='UF')
plt.show()

# %%
def analisar_evolucao_producao_regional(df):
    # Cria uma cópia do dataframe para evitar modificações no original
    df = df.copy()
    # Limpa e converte valores monetários em string para float.
    df['Quantidade'] = df['Quantidade'].apply(limpar_valor)

    producao_anuais = df.groupby(['Ano', 'Especie'])['Quantidade'].sum().reset_index()

    return producao_anuais

producao_anuais = analisar_evolucao_producao_regional(df_filtered)

print(producao_anuais.head())
#%%

plt.figure(figsize=(10, 6))
sns.lineplot(data=analisar_evolucao_producao_regional(df_filtered), x='Ano', y='Quantidade', hue='Especie')
plt.title('Evolução da Produção por Ano e Espécie')
plt.xlabel('Ano')
plt.ylabel('Produção')
plt.legend(title='Espécie')
plt.show()

#%%