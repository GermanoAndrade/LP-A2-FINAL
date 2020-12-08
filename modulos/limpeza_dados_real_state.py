from classe_RS_limp import RS_limp
import conexao_base as cb

df_real_state = cb.df_rs

real_state = RS_limp(df_real_state)

#Troca booleans por inteiros na coluna 'CHAS'
real_state.trocar_bools_para_int('CHAS')

#Retira valores nulos
real_state.drop_na()

#Escrevendo o dataframe em um csv
real_state.escrever_csv('../dataframes/df_real_state.csv')