import pandas as pd
from sklearn import datasets, linear_model, metrics, model_selection
import statsmodels.api as sm
import matplotlib.pyplot as plt

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

#Gráfico de correlação
plt.scatter(df_real_state["NOX"], df_real_state["INDUS"],color='green')
plt.xlabel("nitric oxides concentration")
plt.ylabel("proportion of non-retail business")
plt.title("nitric oxides concentration \n x \n proportion of non-retail business")
plt.show()

# Observa-se um alto grau de correlação entre a concentração de óxidos nítricos
# e a proporção de negócios não varejistas, com um R² de 0,582


