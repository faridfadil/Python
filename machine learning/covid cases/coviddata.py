import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('owid-covid-data.csv')
df['location'].hist(bins=20)
plt.title("Covid cases across continents")
plt.show()
