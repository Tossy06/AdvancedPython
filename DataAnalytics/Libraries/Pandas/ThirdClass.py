import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_artist = pd.read_excel("https://docs.google.com/uc?export=download&id=1bqVTtpAF50QSlrtB6DjfeHx1w9UKT7O3")

grafico_Barra = df_artist.plot.barh(x = "Artista", y = "Spotify streams (millones)", color= 'g')

grafico_torta = df_artist.plot.pie(x = "Artista", y = "Spotify streams (millones)", 
                                   labels = df_artist.Artista, 
                                   legend = False)



