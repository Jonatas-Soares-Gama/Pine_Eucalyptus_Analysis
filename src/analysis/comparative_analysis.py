#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_path = '/home/jonatasgama/Desktop/project_silvicultura/data/silver/especie_pinus_eucalipto.csv'

df = pd.read_csv(data_path, sep=';', encoding='utf-8')

df.columns.to_list()
#%%

df['Grupo'].unique()

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

comparative_analysis = df[['UF', 'Ano', 'Especie', 'Grupo', 'Uso', 'Quantidade', 'Valor_Corrigido_IPCA_Mil_R$', 'Preco_Medio_Corrigido_IPCA']]

comparative_analysis.head()

def convert_to_float(df):

    df = df.copy()

    df['Valor_Corrigido_IPCA_Mil_R$'] = df['Valor_Corrigido_IPCA_Mil_R$'].apply(limpar_valor)
    df['Preco_Medio_Corrigido_IPCA'] = df['Preco_Medio_Corrigido_IPCA'].apply(limpar_valor)

    return df

comparative_analysis = convert_to_float(comparative_analysis)

comparative_analysis.head()

# %%





