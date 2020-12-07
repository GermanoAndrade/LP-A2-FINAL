import conexao_base as cb
from classe_Fifa_limp import Fifa_limp


df_fifa = cb.df_fifa

fifa = Fifa_limp(df_fifa)

#Troca os valores da coluna Height para centímetros
fifa.trocar_pes_para_cm("Height")

#Troca os valores da coluna Weight para kilogramas
fifa.trocar_lbs_para_kg("Weight")

#Troca os valores nas respectivas colunas que estão em str para int
fifa.trocar_valores_str_p_int("Value")
fifa.trocar_valores_str_p_int("Wage")
fifa.trocar_valores_str_p_int("Release_Clause")

#Traduz as posições, para posições mais comuns entre os brasileiros
fifa.traduzir_posicoes("Position")

#Pegando as colunas interessantes para o trabalhho
list_colunas = ["Name","Age","Nationality","Overall","Potential","Club","Jersey_Number","Value","Wage","Release_Clause","Preferred_Foot","Height","Weight","Position"]

fifa.colunas_desejadas(list_colunas)

#Adicionando uma nova coluna, que calcula a porcentagem da diferença de potencial e overall
fifa.porcentagem_overall_potential('Potential','Overall','% Potential e Overall')
fifa.arredondar_valores("% Potential e Overall", 2)

#Escrevendo o dataframe em um csv
fifa.escrever_csv("../dataframes/df_fifa.csv")
