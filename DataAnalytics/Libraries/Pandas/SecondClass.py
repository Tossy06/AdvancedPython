import pandas as pd


df_exel = pd.read_excel("https://docs.google.com/uc?export=download&id=1RjyFp3seXXSwjJMVwT6FBs3lNniDxsNN", index_col='ID_Producto')

'''
print(df_exel.head(5))

print(df_exel.describe())
print(df_exel.Precio.max())

condicion = df_exel[(df_exel["Cantidad"]> 100) & (df_exel["Precio"] < 200000)]
print(condicion)

ordenado = df_exel.sort_values(by="Precio", ascending= False).head(5)
print(ordenado)
'''

'''
df_artist = pd.read_excel("https://docs.google.com/uc?export=download&id=1bqVTtpAF50QSlrtB6DjfeHx1w9UKT7O3")
print(df_artist.isna().sum())

df_filtrado = df_artist.dropna()
print(df_filtrado)

df_llenado = df_artist.fillna(10200)
print(df_llenado)
'''

#Add columns and Drop Columns

new_column =df_exel["Valor Inventario"] = df_exel.Precio * df_exel["Cantidad"]
print(df_exel.head(5))

print('Columna borrada')

df_prdouctos_borrado = df_exel.drop("Valor Inventario", axis= 1)
print(df_prdouctos_borrado.head(5))

