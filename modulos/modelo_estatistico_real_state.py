import statsmodels.api as sm
import pandas as pd
from sklearn import datasets, linear_model, metrics, model_selection
import matplotlib.pyplot as plt
import scipy as sp
import seaborn as sns

df_real_state = pd.read_csv('../dataframes/df_real_state.csv')

#Análise descritiva dos dados
print(df_real_state.head(),"\n")
print(df_real_state.columns,"\n")
print(df_real_state.describe(),"\n")


#Construção do modelo estatístico 
# variável preditora : NOX
# variável alvo : INDUS

X_sm = sm.add_constant(df_real_state["NOX"])
results = sm.OLS(df_real_state["INDUS"], X_sm).fit()

print(results.summary())
print(results.params[0])
print(results.params[1])

#Gráfico de correlação
sns.lmplot(x = "NOX", y = "INDUS",data=df_real_state)
plt.xlabel("nitric oxides concentration")
plt.ylabel("proportion of non-retail business")
plt.title("nitric oxides concentration \n x \n proportion of non-retail business")
plt.show()


# Observa-se um alto grau de correlação entre a concentração de óxidos nítricos
# e a proporção de negócios não varejistas, com um R² de 0,582

##############################

independentes = df_real_state.drop("TAX", axis = 1)
dependente = df_real_state["TAX"]

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
plt.xlabel("Taxa de Imposto")
plt.ylabel("Taxa de Imposto Prevista")
plt.title("Taxa de Imposto \n x \n Taxa de Imposto Prevista")
plt.show()

plt.scatter(model.predict(X_treino), model.predict(X_treino) - Y_treino, color = "green", s = 10, label = "Treino")
plt.scatter(model.predict(X_teste), model.predict(X_teste) - Y_teste, color = "blue", s = 10, label = "Teste")
plt.show()

print("\n####################################\n")
print(model.score(X_treino, Y_treino))
print("Intercept:", model.intercept_)
print("Coefs:", model.coef_)

print("\n####################################\n")

