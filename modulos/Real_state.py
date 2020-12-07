import pyodbc
import pandas as pd
import numpy as np
from sklearn import datasets, linear_model, metrics, model_selection
import statsmodels.api as sm
import matplotlib.pyplot as plt


params = '''DRIVER={ODBC Driver 17 for SQL Server};
            SERVER=tcp:fgv-db-server.database.windows.net,1433;
            DATABASE=fgv-db;Persist Security Info={False};
            UID={student};
            PWD=@dsInf123;
            MultipleActiveResultSets=False;
            Encrypt =True;
            TrustServerCertificate =False;
            Connection Timeout=30;'''
            
cnxn = pyodbc.connect(params)

sql = """SELECT * FROM real_state.real_state_values"""
df_real_state = pd.read_sql(sql, cnxn)

#Análise descritiva dos dados
print(df_real_state.head(),"\n")
print(df_real_state.columns,"\n")
print(df_real_state.describe(),"\n")

#Limpeza dos dados
df_real_state.dropna(inplace=True)

def trocar_valores_str_p_int(value):
    if value == True:
        return 1
    else:
        return 0
    
df_real_state["CHAS"] = df_real_state["CHAS"].apply(trocar_valores_str_p_int)
print(df_real_state.head())



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


