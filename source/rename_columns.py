#%%
import pandas as pd
import chardet
import matplotlib.pyplot as plt


file_path = '/home/jonatasgama/Desktop/project_silvicultura/data/dados_ibge_94-23.csv'

with open(file_path, "rb") as f:
    result = chardet.detect(f.read())

print(result)


df = pd.read_csv(file_path, sep=';', encoding='ISO-8859-1', encoding_errors='replace')

df = df.rename(columns={'Valor corrigido (mil R$) (real - IPCA 2023)': 'Valor_Corrigido_IPCA',
                        'Tipo de floresta': 'Tipo_Floresta',
                        'Tipo de produto florestal': 'Tipo_Produto',
                        'Produto florestal (com código)': 'Produto_Florestal_Codigo',
                        'Parte da planta': 'Parte_Planta',
                        'Espécie': 'Especie',
                        'Unidade de medida PEVS': 'Unidade_Medida_PEVS',
                        'Valor da produção (mil R$) (nominal)': 'Valor_Producao_Nominal',
                        'Valor produção (mil R$) (nominal)': 'Valor_Producao',
                        'Fator de correção IPCA': 'Fator_Correcao_IPCA',
                        'Preço médio (R$/t) (nominal)': 'Preco_Medio_Nominal',
                        'Preço médio corrigido (R$/t) (real - IPCA 2023)': 'Preco_Medio_Corrigido_IPCA',
                        })

df_rename = df.to_csv('dados_ibge_rename_columns.csv', encoding='utf-8',sep=';', index=False)





