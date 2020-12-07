import funcoes_auxiliares as fa


class Fifa_limp():
    def __init__(self, dataframe):
        self.dataframe = dataframe
      
    def trocar_pes_para_cm(self,column):
       self.dataframe[column] = self.dataframe[column].apply(fa.pes_para_cm)
       
    def trocar_lbs_para_kg(self,column):
       self.dataframe[column] = self.dataframe[column].apply(fa.lbs_para_kg)
    
    def trocar_valores_str_p_int(self,column):    
        self.dataframe[column] = self.dataframe[column].apply(fa.preco_str_p_int)
    
    def traduzir_posicoes(self,column):    
        self.dataframe[column] = self.dataframe[column].apply(fa.traduz_posicao)
    
    def colunas_desejadas(self, list_colunas):
        self.dataframe = self.dataframe[list_colunas]
        
    def porcentagem_overall_potential(self, potential,overall,new_column):
        self.dataframe[new_column] = 100*((self.dataframe[potential]-self.dataframe[overall])/self.dataframe[overall])
        
    def escrever_csv(self, caminho_arquivo):
        self.dataframe.to_csv(caminho_arquivo)
    
    def arredondar_valores(self, column, precisao):
        self.dataframe[column] = self.dataframe[column].apply(lambda x : round(x,precisao))
        

