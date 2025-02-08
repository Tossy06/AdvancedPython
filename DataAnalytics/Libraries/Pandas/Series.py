import pandas as pd 

serie = pd.Series([30, 35, 40], ['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(serie.iloc[1:])