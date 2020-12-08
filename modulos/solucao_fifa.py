import pandas as pd
import numpy as np


df_fifa = pd.read_csv('../dataframes/df_fifa.csv')

#Início das soluções para a primeira base de dados

#Questão 1
print(40*"=-")
print("Questão 1")

df_fifa.sort_values(by = "Overall", ascending= False, inplace = True)

def melhores(p,df):
    if p == "Atacante":
        a = df[df["Position"]== "Atacante"]["Name"].iloc[0]
        b = df[df["Position"]== "Ponta Direita"]["Name"].iloc[0]
        c = df[df["Position"]== "Ponta Esquerdo"]["Name"].iloc[0]
        return f"O melhor ataque futuro será composto por {a},{b} e {c}"   
    elif p == "Meia":
        a = df[df["Position"]== "Meia Atacante"]["Name"].iloc[0]
        b = df[df["Position"]== "Meia Direita"]["Name"].iloc[0]
        c = df[df["Position"]== "Meia Esquerda"]["Name"].iloc[0]
        return f"O melhor meia futuro será composto por {a},{b} e {c}" 
    elif p == "Lateral":
        a = df[df["Position"]== "Lateral Direito"]["Name"].iloc[0]
        b = df[df["Position"]== "Lateral Esquerdo"]["Name"].iloc[0]
        return f"A melhor dupla de lateral futura será {a} e {b}"
    elif p == "Zagueiro":
        a = df[df["Position"]== "Zagueiro Direito"]["Name"].iloc[0]
        b = df[df["Position"]== "Zagueiro Esquerdo"]["Name"].iloc[0]
        return f"A melhor dupla de zagueiro será {a} e {b}"
    elif p == "Goleiro":
        a = df[df["Position"]== "Goleiro"]["Name"].iloc[0]
        return f"O melhor goleiro será o {a}"

        
    
def melhor_time_atual():
    a = melhores("Goleiro",df_fifa)
    b = melhores("Zagueiro",df_fifa)
    c = melhores("Lateral",df_fifa)
    d = melhores("Meia",df_fifa)
    e = melhores("Atacante",df_fifa) 
    return f"""O melhor time atual é formado por:
        -> Goleiro-{a}
        -> Zagueiro-{b}
        -> Laterais-{c}
        -> Meias-{d}
        -> Atacantes->{e}"""
        

print(melhor_time_atual())    
 
print(40*"=-")
#Questão 2
print("Questão 2")
df_fifa_novo = df_fifa[df_fifa["Age"] < 25]
df_fifa_novo = df_fifa_novo.sort_values(by = "Potential", ascending= False)

            
def melhor_time_futuro():
    a = melhores("Goleiro",df_fifa_novo)
    b = melhores("Zagueiro",df_fifa_novo)
    c = melhores("Lateral",df_fifa_novo)
    d = melhores("Meia",df_fifa_novo)
    e = melhores("Atacante",df_fifa_novo) 
    return f"""O melhor time do futuro será formado por:
        -> Goleiro-{a}
        -> Zagueiro-{b}
        -> Laterais-{c}
        -> Meias-{d}
        -> Atacantes->{e}"""
        

print(melhor_time_futuro())
print(40*"=-")
#Questão 3
print("Questão 3")

def porcentagem_canhoto(num,df):
    a = df["Preferred_Foot"].iloc[0:num+1]
    s = 0
    for i in a:  
        if i == "Left":
            s += 1
    result = (s/num)*100
    return f"A porcentagem dos canhotos em relação aos {num} mais bem avaliados é de {round(result,2)}%"

print(porcentagem_canhoto(50,df_fifa))
print(40*"=-")        








































