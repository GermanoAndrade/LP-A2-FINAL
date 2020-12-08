class RS_limp():
    def __init__(self,dataframe):
        self.dataframe = dataframe

    def trocar_bools_para_int(self,columns):
        self.dataframe[columns] = self.dataframe[columns].apply(lambda value : 1 if value == True else 0)

    def drop_na(self):
        self.dataframe.dropna(inplace=True)
        
    def escrever_csv(self, caminho_arquivo):
        """Escreve o dataframe em um arquivo csv.
        
        
        Parameters
        ----------
        caminho_arquivo : str
        Path do arquivo.
    
        
    
        """
        self.dataframe.to_csv(caminho_arquivo)