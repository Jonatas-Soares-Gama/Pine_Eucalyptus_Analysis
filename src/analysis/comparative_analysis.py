
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_path = '/home/jonatas-gama/Área de trabalho/projects/Pine_Eucalyptus_Analysis-main/data/silver/especie_pinus_eucalipto.csv'

df = pd.read_csv(data_path, sep=';', encoding='utf-8')

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

comparative_analysis = df[['UF', 'Ano', 'Especie', 'Grupo', 'Uso', 'Quantidade', 'Valor_Corrigido_IPCA_Mil_R$', 'Preco_Medio_Corrigido_IPCA']]

def convert_to_float(df):

    df = df.copy()

    df['Valor_Corrigido_IPCA_Mil_R$'] = df['Valor_Corrigido_IPCA_Mil_R$'].apply(limpar_valor)
    df['Preco_Medio_Corrigido_IPCA'] = df['Preco_Medio_Corrigido_IPCA'].apply(limpar_valor)

    return df

comparative_analysis = convert_to_float(comparative_analysis)

def update_values(column1: float, column2: float) -> float:

    df = comparative_analysis.copy()

    if 'Valor_Corrigido_IPCA_Mil_R$' in df.columns and 'Preco_Medio_Corrigido_IPCA' in df.columns:
        df['Valor_Corrigido_IPCA_Mil_R$'] = df['Valor_Corrigido_IPCA_Mil_R$'] * column1
        df['Preco_Medio_Corrigido_IPCA'] = df['Preco_Medio_Corrigido_IPCA'] * column2
    return df

comparative_analysis = update_values(1.0506, 1.0506)

table_comparative_analysis = comparative_analysis.to_csv('/home/jonatas-gama/Área de trabalho/projects/Pine_Eucalyptus_Analysis-main/data/gold/update_values_comparative_analysis_2025.csv', encoding='utf-8',sep=';', index=False)



