import pandas as pd


df_fifa = pd.read_csv('../dataframes/df_fifa.csv')

#Início das soluções para a primeira base de dados

#Questão 1

df_fifa.sort_values(by = "Overall", ascending= False, inplace = True)

def melhores(p,df):
    """Função que retorna os melhores jogadores de determinada posição.
    

    Parameters
    ----------
    p : str
        String contendo a posição desejada.
    df : pandas.core.frame.dataframe
        Dataframe.

    Returns
    -------
    list
        Lista com os melhores jogadores da posição desejada.

    """
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
    else:
        return "Essa posição não existe!"
    

    
def melhor_time_atual():
    """Função que retorna uma lista com o melhor time atual, de acordo com o overall e independente do preço. 
    

    Returns
    -------
    list
        Lista com os jogadores do time.

    """
    gol = melhores("Goleiro",df_fifa)
    zag1, zag2 = melhores("Zagueiro",df_fifa)
    lat1, lat2 = melhores("Lateral",df_fifa)
    mei1, mei2, mei3 = melhores("Meia",df_fifa)
    ata1, ata2, ata3 = melhores("Atacante",df_fifa)
    return [gol, zag1, zag2, lat1, lat2, mei1, mei2, mei3, ata1, ata2, ata3]
    

def print_melhor_time(funcao_atual_ou_futuro):
    gol, zag1, zag2, lat1, lat2, mei1, mei2, mei3, ata1, ata2, ata3 = funcao_atual_ou_futuro
    return f"""O melhor time é formado por:
        -> Goleiro-O melhor goleiro será o {gol}
        -> Zagueiro-A melhor dupla de zagueiro será {zag1} e {zag2}
        -> Laterais-A melhor dupla de lateral será {lat1} e {lat2}
        -> Meias-O melhor meia será composto por {mei1}, {mei2} e {mei3}
        -> Atacantes->O melhor ataque será composto por {ata1}, {ata2} e {ata3}"""
        
 
#Questão 2
df_fifa_novo = df_fifa[df_fifa["Age"] < 25]
df_fifa_novo = df_fifa_novo.sort_values(by = "Potential", ascending= False)

            
def melhor_time_futuro():
    """Função que retorna uma string com o melhor time atual, de acordo com o potencial.
    

    Returns
    -------
    str
        String com os jogadores do time.

    """
    gol = melhores("Goleiro",df_fifa_novo)
    zag1, zag2 = melhores("Zagueiro",df_fifa_novo)
    lat1, lat2 = melhores("Lateral",df_fifa_novo)
    mei1, mei2, mei3 = melhores("Meia",df_fifa_novo)
    ata1, ata2, ata3 = melhores("Atacante",df_fifa_novo)
    return [gol, zag1, zag2, lat1, lat2, mei1, mei2, mei3, ata1, ata2, ata3]
    
        

#Questão 3

def porcentagem_canhoto(num,df):
    """Esta função calcula a porcentagem de canhotos entre os num jogadores mais bem avaliados.
    

    Parameters
    ----------
    num : int
        Quantidade num de jogadores mais bem avaliados.
    df : pandas.core.frame.dataframe
        Dataframe.

    Returns
    -------
    str
        String com a porcentagem de jogadores canhotos entre os num melhores.

    """
    try:
        if num>len(df):
            print("Essa quuantidade de jogadores é maior do que a existente no dataframe!")
        a = df["Preferred_Foot"].iloc[0:num+1]
        s = 0
        for i in a:  
            if i == "Left":
                s += 1
        result = (s/num)*100
        return f"A porcentagem dos canhotos em relação aos {num} mais bem avaliados é de {round(result,2)}%"
    except TypeError:
        print("A variável num precisa ser do tipo int!")
   


if __name__ == '__main__':
    #Questão 1
    print(40*"=-")
    print("Questão 1")
    print(print_melhor_time(melhor_time_atual()))
    
    print(40*"=-")
    #Questão 2
    print("Questão 2")
    print(print_melhor_time(melhor_time_futuro()))
    
    print(40*"=-")
    #Questão 3
    print("Questão 3")
    print(porcentagem_canhoto(50,df_fifa))




































