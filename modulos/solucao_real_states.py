import pyodbc
import pandas as pd

df_rs = pd.read_csv('../dataframes/df_real_state.csv')

#Início das soluções para da segunda base de dados
#Questão 1

print(10*"=-")
print("Questão 1")
df_rs.sort_values(by ="CRIM", ascending= False)
print(df_rs["DIS"].iloc[0])
print(10*"=-")

#Questão 2


print("Questão 2")
df_rs_2 = df_rs[df_rs["PTRATIO"] < 15]
df_rs_2.sort_values(by ="CRIM", ascending= False)
print(df_rs_2["CRIM"].iloc[0])
print(10*"=-")

#Questão 3


print("Questão 1")
df_rs_3 = df_rs[df_rs["CHAS"] == 1]
df_rs_3.sort_values(by = "MEDV", ascending = False)
menor = df_rs_3["MEDV"].iloc[-1]
maior = df_rs_3["MEDV"].iloc[0]
print(f"A menor quantidade média de casas ocupadas é {menor} e a maior é {maior}")
print(10*"=-")













