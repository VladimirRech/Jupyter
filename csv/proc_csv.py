# Processamento de arquivo CSV
import pandas as pd
tb = pd.read_csv("~/git/Jupyter/csv/test.csv")
# Visualizar a estrutura
tb.info()
print("\n\n")
# Mostrar alguns dados
# print(tb)
# Quantas compras por banco
# print(tb['Banco'].value_counts())
# Quantas compras por categoria?
#print('Quantas compras por categoria?')
# print(tb['Categoria'].value_counts())

# Agrupando por categoria e mostrando os totais
# https://datatofish.com/replace-character-pandas-dataframe/
tb['Valor'] = tb['Valor'].str.replace('.', '')
tb['Valor'] = tb['Valor'].str.replace(',', '.')
tb['Val'] = tb['Valor'].astype(float)
print(tb.groupby('Categoria')['Val'].sum())
