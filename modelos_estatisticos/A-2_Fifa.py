import pyodbc
import pandas as pd
import numpy as np
from sklearn import datasets, linear_model, metrics, model_selection
import statsmodels.api as sm
import matplotlib.pyplot as plt

#Acessando a base de dados
params = '''DRIVER={ODBC Driver 17 for SQL Server};SERVER=tcp:fgv-db-server.database.windows.net,1433;DATABASE=fgv-db;Persist Security Info={False};UID={student};PWD=@dsInf123;MultipleActiveResultSets=False;Encrypt =True;TrustServerCertificate =False;Connection Timeout=30;'''
cnxn = pyodbc.connect(params)

cursor = cnxn.cursor()

sql = """SELECT * FROM fifa.fifa_players"""
df_fifa = pd.read_sql(sql, cnxn)

#Começando a limpeza dos dados
def trocar_para_unique(body_type):
    if body_type not in ["Lean", "Normal", "Stocky", None]:
        return "Unique"
    else:
        return body_type
    
df_fifa["Body_Type"] = df_fifa["Body_Type"].apply(trocar_para_unique)


def trocar_pes_para_cm(height):
    if height not in [None]:
        height_pes = float(height.replace("'","."))
        height_cm = round(height_pes * 30.48,0)
        return height_cm
    else:
        return np.NaN

df_fifa["Height"] = df_fifa["Height"].apply(trocar_pes_para_cm)

def trocar_lbs_para_kg(weight):
    if weight not in [None]:
        weight_lbs = float(weight.replace("lbs",""))
        weight_kg = round(weight_lbs * 0.453592,1)
        return weight_kg
    else:
        return np.NaN
df_fifa["Weight"] = df_fifa["Weight"].apply(trocar_lbs_para_kg)

def trocar_valores_str_p_int(value):
    if value in [None,np.NaN]:
        return 0
    elif 'M' in value:
        value_str = value.replace("M","")
        value_int = float(value_str.replace("€",""))*1000000
        return int(value_int)
    elif 'K' in value:
        value_str = value.replace("K","")
        value_int = float(value_str.replace("€",""))*1000
        return int(value_int)
    
df_fifa["Value"] = df_fifa["Value"].apply(trocar_valores_str_p_int)
df_fifa["Wage"] = df_fifa["Wage"].apply(trocar_valores_str_p_int)
df_fifa["Release_Clause"] = df_fifa["Release_Clause"].apply(trocar_valores_str_p_int)

def traduz_posicao(position):
    dicio = {'GK':'Goleiro','LS':'Ponta Esquerda','ST':'Atacante','RS':'Ponta Direita','LW':'Ala Esquerdo','LF':'Atacante Esquerdo','CF':'Centro Avante','RF':'Atacante Direito','RW':'Ala Direito','LAM':'Meia Atacante Esquerdo','CAM':'Armador','RAM':'Meia Atacante Direiro','LM':'Meia Esquerda','LCM':'Meia Ala Esquerdo','CM':'Meia Central','RCM':'Meia Ala Direito','RM':'Meia Direita','LWB':'Lateral Esquerdo','LDM':'Volante Esquerdo','CDM':'Volante Central','RDM':'Volante Direito', 'RWB':'Lateral Direito', 'LB':'Zagueiro Esquerdo', 'LCB':'Zagueiro Central Esquerdo', 'CB':'Zagueiro Central', 'RCB':'Zagueiro Central Direito', 'RB':'Zagueiro Esquerdo'} 
    if position in [None]:
        return np.NaN
    else:
        return dicio[position]
    
df_fifa['Position'] = df_fifa['Position'].apply(traduz_posicao)


#Limpeza dos dados que não são interresantes 
df_fifa = df_fifa[["Name","Age","Nationality","Overall","Potential","Club","Jersey_Number","Value","Wage","Release_Clause","Preferred_Foot","Height","Weight","Position"]]
print(df_fifa.head())
print(df_fifa.describe())

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


