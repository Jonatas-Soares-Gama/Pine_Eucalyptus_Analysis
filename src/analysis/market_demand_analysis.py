
#%%
import pandas as pd

data_path = '/home/jonatas-gama/Área de trabalho/projects/Pine_Eucalyptus_Analysis-main/data/silver/especie_pinus_eucalipto.csv'

df = pd.read_csv(data_path, sep=';', encoding='utf-8')

print(df['Preco_Medio_Corrigido_IPCA'])

def clean_value(valor):
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

def price_analysis(df):

    df = df.copy()

    annual_price = df.groupby(['Ano', 'Especie']).agg({
        'Quantidade' : 'sum',
        'Valor_Corrigido_IPCA_Mil_R$': 'sum'
    }).reset_index()
    
    return annual_price

annual_price = price_analysis(df)


annual_price.to_csv('/home/jonatas-gama/Área de trabalho/projects/Pine_Eucalyptus_Analysis-main/data/gold/precos_anuais.csv', encoding='utf-8', sep=';', index=False)

print(annual_price.head())

def analyze_regional_pine_production(df):
    # Cria uma cópia do dataframe para evitar modificações no original
    df = df.copy()
    producao_regional = df.groupby(['Ano', 'UF', 'Especie', 'Grupo', 'Uso'])['Quantidade'].sum().reset_index()

    return producao_regional

regional_production_pinus = analyze_regional_pine_production(df)

regional_production_pinus = regional_production_pinus.sort_values(by=['Quantidade'], ascending=False)

regional_production_pinus = regional_production_pinus[regional_production_pinus['Especie'] == 'Pinus']


regional_production_pinus.to_csv('/home/jonatas-gama/Área de trabalho/projects/Pine_Eucalyptus_Analysis-main/data/gold/producao_regional_pinus.csv', encoding='utf-8', sep=';', index=False)

def analyze_regional_eucalyptus_production(df):
    # Cria uma cópia do dataframe para evitar modificações no original
    df = df.copy()
    producao_regional = df.groupby(['Ano', 'UF', 'Especie', 'Grupo', 'Uso'])['Quantidade'].sum().reset_index()

    return producao_regional

regional_production_eucalyptus = analyze_regional_eucalyptus_production(df)

regional_production_eucalyptus = regional_production_eucalyptus.sort_values(by=['Quantidade'], ascending=False)

regional_production_eucalyptus = regional_production_eucalyptus[regional_production_eucalyptus['Especie'] == 'Eucalipto']


regional_production_eucalyptus.to_csv('/home/jonatas-gama/Área de trabalho/projects/Pine_Eucalyptus_Analysis-main/data/gold/producao_regional_Eucalipto.csv', encoding='utf-8', sep=';', index=False)

def analyze_evolution_of_regional_production(df):
    # Cria uma cópia do dataframe para evitar modificações no original
    df = df.copy()
    # Limpa e converte valores monetários em string para float.
    df['Quantidade'] = df['Quantidade'].apply(clean_value)

    annual_production = df.groupby(['Ano', 'Especie'])['Quantidade'].sum().reset_index()

    return annual_production

annual_production = analyze_evolution_of_regional_production(df)

annual_production.to_csv('/home/jonatas-gama/Área de trabalho/projects/Pine_Eucalyptus_Analysis-main/data/gold/producao_anuais.csv', encoding='utf-8', sep=';', index=False)

print(annual_production.head())
