import pyodbc
import pandas as pd
import numpy as np
from sklearn import datasets, linear_model, metrics, model_selection
import statsmodels.api as sm
import matplotlib.pyplot as plt

df_fifa = pd.read_csv('../dataframes/df_fifa.csv')

#Construção do modelo estatístico
df_fifa_2 = df_fifa[["Overall","Value","Wage","Release_Clause"]]
df_fifa_2.dropna(inplace=True)

# variável preditora : Value
# variável alvo : Release_Clause

X_sm = sm.add_constant(df_fifa_2["Value"])
results = sm.OLS(df_fifa_2["Release_Clause"], X_sm).fit()

print(results.summary())

#Gráfico de correlação
plt.scatter(df_fifa_2["Value"], df_fifa_2["Release_Clause"])
plt.xlabel("Valor de mercado do jogador")
plt.ylabel("Valor da quebra do contrato do jogador")
plt.title("Valor de mercado \n x \n Valor da quebra do contrato")
plt.show()




