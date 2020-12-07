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

# variável preditora : Release_Clause
# variável alvo : Overall

X_sm = sm.add_constant(df_fifa_2["Release_Clause"])
results = sm.OLS(df_fifa_2["Value"], X_sm).fit()

print(results.summary())

#Gráfico de correlação
plt.scatter(df_fifa_2["Release_Clause"], df_fifa_2["Value"])
plt.xlabel("Valor da quebra de contrato do jogador")
plt.ylabel("Valor de mercado do jogador")
plt.title("Valor de mercado \n x \n Valor da quebra de contrato")
plt.show()

# plt.scatter(model.predict(X_treino), model.predict(X_treino) - Y_treino, color = "green", s = 10, label = "Treino")
# plt.scatter(model.predict(X_teste), model.predict(X_teste) - Y_teste, color = "blue", s = 10, label = "Teste")
# plt.show()


