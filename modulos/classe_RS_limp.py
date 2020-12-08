class RS_limp():
    """Classe responsável pelas funções que farão a limpeza do datrafame sujo.
    

    

    Attributes
    ----------
    dataframe : pandas.core.frame.dataframe
        Dataframe.

    Methods
    -------
    trocar_bools_para_int()
        Transforma os booleanos em inteiros.
    drop_na()
        Faz a mesma função de np.dropna.
    escrever_csv()
        Escreve o dataframe em um csv.
    """
    def __init__(self,dataframe):
        """Método construtor da classe.
        

        Parameters
        ----------
        dataframe : pandas.core.frame.dataframe
            Dataframe.

        

        """
        self.dataframe = dataframe

    def trocar_bools_para_int(self,columns):
        """Transforma os booleanos em inteiros
        

        Parameters
        ----------
        columns : pandas.core.series.Series
            Coluna específica do dataframe

        

        """
        self.dataframe[columns] = self.dataframe[columns].apply(lambda value : 1 if value == True else 0)

    def drop_na(self):
        """Dropa as colunas e linhas que possuem valores nulos.
        

        

        """
        self.dataframe.dropna(inplace=True)
        
    def escrever_csv(self, caminho_arquivo):
        """Escreve o dataframe em um arquivo csv.
        
        
        Parameters
        ----------
        caminho_arquivo : str
        Path do arquivo.
    
        
    
        """
        self.dataframe.to_csv(caminho_arquivo)