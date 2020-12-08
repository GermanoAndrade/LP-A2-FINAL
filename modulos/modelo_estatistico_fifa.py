import pyodbc
import pandas as pd
import numpy as np
from sklearn import datasets, linear_model, metrics, model_selection
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

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
sns.lmplot(x = "Value", y = "Release_Clause",data=df_fifa_2)
plt.xlabel("Valor de mercado do jogador")
plt.ylabel("Valor da quebra do contrato do jogador")
plt.title("Valor de mercado \n x \n Valor da quebra do contrato")
plt.show()

#Observa-se um alto grau de correlação entre a quebra do contrato
#de um jogador com o seu valor de mercado
#Que encontramos um R² do modelo feito aproximado de 0,935

##############################

independentes = df_fifa_2.drop("Value", axis = 1)
dependente = df_fifa_2["Value"]

#Dividir o conjunto de dados em treino e teste
X_treino, X_teste, Y_treino, Y_teste = model_selection.train_test_split(independentes, dependente, test_size = 0.4, random_state = 1)#40% separado para teste

print(X_treino.shape)
print(X_teste.shape)
print(Y_treino.shape)
print(Y_teste.shape)

model = linear_model.LinearRegression()
model.fit(X_treino, Y_treino)

Y_previsto = model.predict(X_teste)

plt.scatter(Y_teste, Y_previsto)
plt.xlabel("Valor do Jogador")
plt.ylabel("Valor do Jogador Previsto")
plt.title("Valor do Jogador \n x \n Valor do Jogador Previsto")
plt.show()

plt.scatter(model.predict(X_treino), model.predict(X_treino) - Y_treino, color = "green", s = 10, label = "Treino")
plt.scatter(model.predict(X_teste), model.predict(X_teste) - Y_teste, color = "blue", s = 10, label = "Teste")
plt.show()

print("\n####################################\n")
print(model.score(X_treino, Y_treino))
print("Intercept:", model.intercept_)
print("Coefs:", model.coef_)

print("\n####################################\n")







