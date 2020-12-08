import pandas as pd


df_fifa = pd.read_csv('../dataframes/df_fifa.csv')

#Início das soluções para a primeira base de dados

#Questão 1

df_fifa.sort_values(by = "Overall", ascending= False, inplace = True)

def melhores(p,df):
    if p == "Atacante":
        a = df[df["Position"]== "Atacante"]["Name"].iloc[0]
        b = df[df["Position"]== "Ponta Direita"]["Name"].iloc[0]
        c = df[df["Position"]== "Ponta Esquerdo"]["Name"].iloc[0]
        return [a, b, c]   
    elif p == "Meia":
        a = df[df["Position"]== "Meia Atacante"]["Name"].iloc[0]
        b = df[df["Position"]== "Meia Direita"]["Name"].iloc[0]
        c = df[df["Position"]== "Meia Esquerda"]["Name"].iloc[0]
        return [a, b, c]
    elif p == "Lateral":
        a = df[df["Position"]== "Lateral Direito"]["Name"].iloc[0]
        b = df[df["Position"]== "Lateral Esquerdo"]["Name"].iloc[0]
        return [a, b]
    elif p == "Zagueiro":
        a = df[df["Position"]== "Zagueiro Direito"]["Name"].iloc[0]
        b = df[df["Position"]== "Zagueiro Esquerdo"]["Name"].iloc[0]
        return [a, b]
    elif p == "Goleiro":
        a = df[df["Position"]== "Goleiro"]["Name"].iloc[0]
        return a

        
    
def melhor_time_atual():
    gol = melhores("Goleiro",df_fifa)
    zag1, zag2 = melhores("Zagueiro",df_fifa)
    lat1, lat2 = melhores("Lateral",df_fifa)
    mei1, mei2, mei3 = melhores("Meia",df_fifa)
    ata1, ata2, ata3 = melhores("Atacante",df_fifa)
    return [gol, zag1, zag2, lat1, lat2, mei1, mei2, mei3, ata1, ata2, ata3]
    

def print_melhor_time_atual():
    gol, zag1, zag2, lat1, lat2, mei1, mei2, mei3, ata1, ata2, ata3 = melhor_time_atual()
    return f"""O melhor time atual é formado por:
        -> Goleiro-O melhor goleiro será o {gol}
        -> Zagueiro-A melhor dupla de zagueiro será {zag1} e {zag2}
        -> Laterais-A melhor dupla de lateral será {lat1} e {lat2}
        -> Meias-O melhor meia será composto por {mei1}, {mei2} e {mei3}
        -> Atacantes->O melhor ataque será composto por {ata1}, {ata2} e {ata3}"""
        
 
#Questão 2
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
        

#Questão 3

def porcentagem_canhoto(num,df):
    a = df["Preferred_Foot"].iloc[0:num+1]
    s = 0
    for i in a:  
        if i == "Left":
            s += 1
    result = (s/num)*100
    return f"A porcentagem dos canhotos em relação aos {num} mais bem avaliados é de {round(result,2)}%"
        


if __name__ == '__main__':
    print(print_melhor_time_atual())
    print(melhor_time_futuro())
    print(porcentagem_canhoto(50,df_fifa))





































