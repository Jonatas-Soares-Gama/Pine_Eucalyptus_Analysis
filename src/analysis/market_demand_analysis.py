
#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_path = '/home/jonatas-gama/Área de trabalho/projects/Pine_Eucalyptus_Analysis-main/data/silver/especie_pinus_eucalipto.csv'

df = pd.read_csv(data_path, sep=';', encoding='utf-8')

df['Preco_Medio_Corrigido_IPCA']
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

def analisar_precos(df):

    df = df.copy()

    precos_anuais = df.groupby(['Ano', 'Especie']).agg({
        'Quantidade' : 'sum',
        'Valor_Corrigido_IPCA_Mil_R$': 'sum'
    }).reset_index()
    
    return precos_anuais

precos_anuais = analisar_precos(df)
precos_anuais.to_csv('/home/jonatas-gama/Área de trabalho/projects/Pine_Eucalyptus_Analysis-main/data/gold/precos_anuais.csv', encoding='utf-8', sep=';', index=False)

print(precos_anuais.head())
#%%
def analisar_producao_regional_pinus(df):
    # Cria uma cópia do dataframe para evitar modificações no original
    df = df.copy()
    producao_regional = df.groupby(['Ano', 'UF', 'Especie', 'Grupo', 'Uso'])['Quantidade'].sum().reset_index()

    return producao_regional

producao_regional = analisar_producao_regional_pinus(df)

producao_regional = producao_regional.sort_values(by=['Quantidade'], ascending=False)

producao_regional = producao_regional[producao_regional['Especie'] == 'Pinus']


producao_regional.to_csv('/home/jonatas-gama/Área de trabalho/projects/Pine_Eucalyptus_Analysis-main/data/gold/producao_regional_pinus.csv', encoding='utf-8', sep=';', index=False)

#%%
def analisar_producao_regional_eucalipto(df):
    # Cria uma cópia do dataframe para evitar modificações no original
    df = df.copy()
    producao_regional = df.groupby(['Ano', 'UF', 'Especie', 'Grupo', 'Uso'])['Quantidade'].sum().reset_index()

    return producao_regional

producao_regional_eucalipto = analisar_producao_regional_eucalipto(df)

producao_regional_eucalipto = producao_regional_eucalipto.sort_values(by=['Quantidade'], ascending=False)

producao_regional_eucalipto = producao_regional_eucalipto[producao_regional_eucalipto['Especie'] == 'Eucalipto']


producao_regional.to_csv('/home/jonatas-gama/Área de trabalho/projects/Pine_Eucalyptus_Analysis-main/data/gold/producao_regional_Eucalipto.csv', encoding='utf-8', sep=';', index=False)


# %%
def analisar_evolucao_producao_regional(df):
    # Cria uma cópia do dataframe para evitar modificações no original
    df = df.copy()
    # Limpa e converte valores monetários em string para float.
    df['Quantidade'] = df['Quantidade'].apply(limpar_valor)

    producao_anuais = df.groupby(['Ano', 'Especie'])['Quantidade'].sum().reset_index()

    return producao_anuais

producao_anuais = analisar_evolucao_producao_regional(df)

producao_anuais.to_csv('/home/jonatas-gama/Área de trabalho/projects/Pine_Eucalyptus_Analysis-main/data/gold/producao_anuais.csv', encoding='utf-8', sep=';', index=False)

print(producao_anuais.head())
#%%

plt.figure(figsize=(10, 6))
sns.lineplot(data=analisar_evolucao_producao_regional(df), x='Ano', y='Quantidade', hue='Especie')
plt.title('Evolução da Produção por Ano e Espécie')
plt.xlabel('Ano')
plt.ylabel('Produção')
plt.legend(title='Espécie')
plt.show()

#%%