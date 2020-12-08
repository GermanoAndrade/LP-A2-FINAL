# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import solucao_fifa as sf

df_fifa = pd.read_csv("../dataframes/df_fifa.csv")


time_dos_sonhos = sf.melhor_time_atual()

print(time_dos_sonhos)

df_time_dos_sonhos = df_fifa[df_fifa["Name"].isin(time_dos_sonhos)][:-2].reset_index()
print(df_time_dos_sonhos)
df_time_dos_sonhos["Time"] = "Time dos Sonhos"

def plot_skills(index_player, dataframe, single_player = True, goalkeeper = False, title = False):
    index = index_player
    if single_player:
        if dataframe["Position"].iloc[index] == "Goleiro":
            skills = ["KIC", "HAN", "DIV", "POS", "PAC", "REF"]
        else:
            skills = ["PAS", "SHO", "PAC", "PHY", "DEF", "DRI"]
    else:
        if goalkeeper:
            skills = ["KIC", "HAN", "DIV", "POS", "PAC", "REF"]
        else:
            skills = ["PAS", "SHO", "PAC", "PHY", "DEF", "DRI"]
    
    skills.append(skills[0])
    values = list(dataframe[skills].iloc[index])
    
    fig = plt.figure()    
    fig.set_size_inches(6, 6)
    ax = fig.add_subplot(111,polar=True)
    plt.polar([skill+" "+str(value) for skill, value in zip(skills, values)], values,'b-p')

    if not title:
        title = dataframe["Name"].iloc[index]

    plt.title('{} Skills'.format(title), fontweight ="bold", va='bottom', y=1.1)
    ax.fill([skill+" "+str(value) for skill, value in zip(skills, values)], values, color="mediumseagreen", alpha = .4)
    return plt



#print(df_time_dos_sonhos.groupby("Time").mean())

#for i in df_time_dos_sonhos.index:
 #   plot_skills(i, df_time_dos_sonhos)
 
#Sem goleiro 
agrupado = np.round(df_time_dos_sonhos[df_time_dos_sonhos["Position"]!= "Goleiro"].groupby("Time").mean()) 
figura = plot_skills(0, agrupado, single_player=False, title = "Time dos Sonhos")
name = "../galeria/{}/Time_dos_sonhos_Inteiro.{}"
plt.savefig(name.format("PNG", "png"))
plt.savefig(name.format("PDF", "pdf"))
figura.show()

#Só o goleiro
agrupado = np.round(df_time_dos_sonhos[df_time_dos_sonhos["Position"]== "Goleiro"].groupby("Time").mean()) 
figura = plot_skills(0, agrupado, single_player=False, goalkeeper = True, title = "Goleiro")
name = "../galeria/{}/Time_dos_sonhos_Goleiro.{}"
plt.savefig(name.format("PNG", "png"))
plt.savefig(name.format("PDF", "pdf"))
figura.show()


cinquenta_melhores = df_fifa.sort_values(by = "Overall", ascending= False).iloc[:50].reset_index()


print(cinquenta_melhores["Preferred_Foot"].value_counts(normalize=True).index)
dir_esq = cinquenta_melhores["Preferred_Foot"].value_counts(normalize=True)

sns.barplot(x = dir_esq.index, y = list(dir_esq), order=["Left", "Right"], palette=["#000000", "#7F7F7F"])
plt.title("Porcentagem de canhotos\nentre os 50 mais bem avaliados", fontweight='bold')
plt.ylabel("Porcentagem")
plt.xlabel("Pé Dominante")

name = "../galeria/{}/Canhotos_entre_os_melhores.{}"
plt.savefig(name.format("PNG", "png"))
plt.savefig(name.format("PDF", "pdf"))
plt.show()










