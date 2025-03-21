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

group_type = df[['UF', 'Ano', 'Especie', 'Grupo', 'Uso', 'Quantidade', 'Valor_Corrigido_IPCA_Mil_R$', 'Preco_Medio_Corrigido_IPCA']]

group_type.head()





