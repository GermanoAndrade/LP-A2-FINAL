# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import solucao_fifa as sf

##FIFA 19
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
    fig.set_size_inches(6, 6.5)
    ax = fig.add_subplot(111,polar=True)
    plt.polar([skill+" "+str(value) for skill, value in zip(skills, values)], values,'b-p')

    if not title:
        nome = dataframe["Name"].iloc[index]
        title = '{} Skills'.format(nome)

    plt.title(title, fontweight ="bold", va='bottom', y=1.1)
    ax.fill([skill+" "+str(value) for skill, value in zip(skills, values)], values, color="mediumseagreen", alpha = .4)
    return plt



#Sem goleiro 
jogs_linha = np.round(df_time_dos_sonhos[df_time_dos_sonhos["Position"]!= "Goleiro"].groupby("Time").mean()) 
figura = plot_skills(0, jogs_linha, single_player=False, title = "Jogadores de linha\ndo Time dos Sonhos")
name = "../galeria/{}/Time_dos_sonhos_Jogadores_de_linha.{}"
plt.savefig(name.format("PNG", "png"))
plt.savefig(name.format("PDF", "pdf"))
figura.show()

#Só o goleiro
goleiro = np.round(df_time_dos_sonhos[df_time_dos_sonhos["Position"]== "Goleiro"].groupby("Time").mean()) 
figura = plot_skills(0, goleiro, single_player=False, goalkeeper = True, title = "Goleiro\ndo Time dos Sonhos")
name = "../galeria/{}/Time_dos_sonhos_Goleiro.{}"
plt.savefig(name.format("PNG", "png"))
plt.savefig(name.format("PDF", "pdf"))
figura.show()

time_futuro = sf.melhor_time_futuro()
print(time_futuro)

df_time_futuro = df_fifa[df_fifa["Name"].isin(time_futuro)][:-1].reset_index()
print(df_time_futuro)
df_time_futuro["Time"] = "Time Futuro"

#Sem goleiro 
jogs_linha = np.round(df_time_dos_sonhos[df_time_dos_sonhos["Position"]!= "Goleiro"].groupby("Time").mean()) 
figura = plot_skills(0, jogs_linha, single_player=False, title = "Jogadores de linha\ndo Time Futuro")
name = "../galeria/{}/Time_Futuro_Jogadores_de_linha.{}"
plt.savefig(name.format("PNG", "png"))
plt.savefig(name.format("PDF", "pdf"))
figura.show()

#Só o goleiro
goleiro = np.round(df_time_dos_sonhos[df_time_dos_sonhos["Position"]== "Goleiro"].groupby("Time").mean()) 
figura = plot_skills(0, goleiro, single_player=False, goalkeeper = True, title = "Goleiro\ndo Time Futuro")
name = "../galeria/{}/Time_Futuro_Goleiro.{}"
plt.savefig(name.format("PNG", "png"))
plt.savefig(name.format("PDF", "pdf"))
figura.show()

#Comparando os dois times em relação à idade
sns.distplot(df_time_dos_sonhos["Age"], label="Time dos Sonhos", color="red")
sns.distplot(df_time_futuro["Age"], label="Time Futuro", color="blue")
plt.legend()
plt.title("Diferença de Idade entre o\nTime dos Sonhos e o Time Futuro", fontweight='bold')
plt.ylabel("Densidade")
plt.xlabel("Idade")
name = "../galeria/{}/Diferença_de_idade_entre_os_times.{}"
plt.savefig(name.format("PNG", "png"))
plt.savefig(name.format("PDF", "pdf"))
plt.show()
plt.show()

#Comparando os dois times em relação ao preço total
preco_dos_times = [df_time_dos_sonhos["Value"].sum(), df_time_futuro["Value"].sum()]
ax = sns.barplot(x = ["Time dos Sonhos", "Time Futuro"], y=preco_dos_times, palette=["#000000", "#7F7F7F"])
#total = float(len(cinquenta_melhores))
for p in ax.patches:
    ax.text(p.get_x()+p.get_width()/2,
            p.get_height()+6000000,
            #'{:1.0f}%'.format(p.get_height()*100),
            '€ {:1.0f}'.format(p.get_height()),
            ha="center")
plt.title("Comparação de preço total entre o\nTime dos Sonhos e o Time Futuro", fontweight='bold')
plt.ylabel("Preço (em Mi)")
name = "../galeria/{}/Comparação_entre_preço_dos_times.{}"
plt.savefig(name.format("PNG", "png"))
plt.savefig(name.format("PDF", "pdf"))
plt.show()

#Questão 3
cinquenta_melhores = df_fifa.sort_values(by = "Overall", ascending= False).iloc[:50].reset_index()


print(cinquenta_melhores["Preferred_Foot"].value_counts(normalize=True).index)
dir_esq = cinquenta_melhores["Preferred_Foot"].value_counts(normalize=True)

ax = sns.barplot(x = dir_esq.index, y = list(dir_esq), order=["Left", "Right"], palette=["#000000", "#7F7F7F"])
total = float(len(cinquenta_melhores))
for p in ax.patches:
    ax.text(p.get_x()+p.get_width()/2,
            p.get_height()+.006,
            '{:1.0f}%'.format(p.get_height()*100),
            ha="center")
plt.title("Porcentagem de canhotos\nentre os 50 mais bem avaliados", fontweight='bold')
plt.ylabel("Porcentagem")
plt.xlabel("Pé Dominante")

name = "../galeria/{}/Canhotos_entre_os_melhores.{}"
plt.savefig(name.format("PNG", "png"))
plt.savefig(name.format("PDF", "pdf"))
plt.show()


##REAL STATE VALUES
df_rs = pd.read_csv('../dataframes/df_real_state.csv')
#df_rs.sort_values(by ="CRIM", inplace=True,ascending= False)
print(df_rs)
sns.scatterplot(x = "CRIM", y="DIS", data = df_rs)
plt.title("Distância\nx\nTaxa de Crime", fontweight='bold')
plt.ylabel("Distância")
plt.xlabel("Taxa de crime")

name = "../galeria/{}/Distancia_vs_taxa_de_crime.{}"
plt.savefig(name.format("PNG", "png"))
plt.savefig(name.format("PDF", "pdf"))
plt.show()




