import pandas as pd
'''
data = pd.read_excel("https://docs.google.com/uc?export=download&id=1bqVTtpAF50QSlrtB6DjfeHx1w9UKT7O3")
print(data)
'''

df_exel = pd.read_excel("https://docs.google.com/uc?export=download&id=1RjyFp3seXXSwjJMVwT6FBs3lNniDxsNN", index_col='ID_Producto')
#print(df_exel.head())

#print(df_exel.loc["SKU172"])

#print(df_exel.loc[["SKU172", "SKU126"], ["Cantidad", "Precio"]])

#print(df_exel.iloc[10:])
print(df_exel.iloc[[0, 5, 7]])
dtA = df_exel.iloc[[0, 4, 7], 0:-1]
print(dtA)

dtB = df_exel.Precio.iloc[:7]
print(dtB)

print(df_exel.shape)

