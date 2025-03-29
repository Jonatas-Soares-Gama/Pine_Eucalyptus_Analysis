#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "/home/jonatas-gama/Área de trabalho/projects/Pine_Eucalyptus_Analysis-main/data/raw/dados_ibge_rename_columns.csv"

df = pd.read_csv(file_path, sep=";", encoding="utf-8")

# Filtrar as espécies de interesse
df_filtered = df[df['Especie'].isin(['Eucalipto', 'Pinus'])]

#%%
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

#%%

def convert_to_float(df):

    df = df_filtered.copy()

    df['Valor_Corrigido_IPCA_Mil_R$'] = df['Valor_Corrigido_IPCA_Mil_R$'].apply(limpar_valor)
    df['Preco_Medio_Corrigido_IPCA'] = df['Preco_Medio_Corrigido_IPCA'].apply(limpar_valor)
    df['Fator_Correcao_IPCA'] = df['Fator_Correcao_IPCA'].apply(limpar_valor)

    return df

df_filtered = convert_to_float(df_filtered)

#%%

def update_values(column1: float, column2: float, column3: float) -> float:

    df = df_filtered.copy()

    if 'Valor_Corrigido_IPCA_Mil_R$' in df.columns and 'Preco_Medio_Corrigido_IPCA' in df.columns:
        df['Valor_Corrigido_IPCA_Mil_R$'] = df['Valor_Corrigido_IPCA_Mil_R$'] * column1
        df['Preco_Medio_Corrigido_IPCA'] = df['Preco_Medio_Corrigido_IPCA'] * column2
        df['Fator_Correcao_IPCA'] = df['Fator_Correcao_IPCA'] * column3
    return df

df_filtered = update_values(1.0506, 1.0506, 1.0506)
df_filtered['Quantidade'] = df_filtered['Quantidade'].astype(int)

df_filtered['Quantidade'].dtype 
df_filtered.head()

#%%



df_filtered.to_csv('/home/jonatas-gama/Área de trabalho/projects/Pine_Eucalyptus_Analysis-main/data/silver/especie_pinus_eucalipto.csv', encoding='utf-8', sep=';', index=False)

df_filtered.columns

#%%

df_filtered.head()

