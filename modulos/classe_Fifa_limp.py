import funcoes_auxiliares as fa


class Fifa_limp():
    """Classe responsável pelas funções que farão a limpeza do datrafame sujo.
    

    

    Attributes
    ----------
    dataframe : pandas.core.frame.dataframe
        dataframe.

    Methods
    -------
    trocar_pes_para_cm()
        Transforma uma string com a altura medida em pés em um float com essa altura convertida para centímetros.
    trocar_lbs_para_kg()
        Transforma uma string com o peso, em libras, em um float com esse peso convertido para quilogramas.
    trocar_valores_str_p_int()
        Transforma uma string contendo o valor, na forma MK(M = Milhões, K = Milhares), em um float com o valor real.
    traduzir_posicoes()
        Traduz a string com a sigla da posição em uma string com nome da posição.
    colunas_desejadas()
        Seleciona uma lista de colunas do dataframe.
    porcentagem_overall_potential()
        Adiciona uma nova coluna que calcula a porcentagem da diferença de potencial e overall.
    escrever_csv()
        Escreve o dataframe em um csv.
    arredondar_valores()
        Arredonda valores.
    """
    
    def __init__(self, dataframe):
        """Método construtor da classe.
        

        Parameters
        ----------
        dataframe : pandas.core.frame.dataframe
            dataframe.

        

        """
        self.dataframe = dataframe
      
    def trocar_pes_para_cm(self,column):
        """Aplica a função trocar_pes_para_cm() -> módulo [limpeza_dados_fifa.py]- na coluna especificada.
        

        Parameters
        ----------
        column : pandas.core.series.Series
            Coluna do dataframe.

    

        """
        self.dataframe[column] = self.dataframe[column].apply(fa.pes_para_cm)
       
    def trocar_lbs_para_kg(self,column):
        """Aplica a função trocar_lbs_para_kg() -> módulo [limpeza_dados_fifa.py]- na coluna especificada.
        

        Parameters
        ----------
        column : pandas.core.series.Series
            Coluna do dataframe.


        """
        self.dataframe[column] = self.dataframe[column].apply(fa.lbs_para_kg)
    
    def trocar_valores_str_p_int(self,column):
        """Aplica a função trocar_valores_str_p_int() -> módulo [limpeza_dados_fifa.py]- na coluna especificada.
        

        Parameters
        ----------
        column : pandas.core.series.Series
            Coluna do dataframe.


        """
        self.dataframe[column] = self.dataframe[column].apply(fa.preco_str_p_int)
    
    def traduzir_posicoes(self,column):
        """Aplica a função traduzir_posicoes() -> módulo [limpeza_dados_fifa.py]- na coluna especificada.
        

        Parameters
        ----------
        column : pandas.core.series.Series
            Coluna do dataframe.


        """
        self.dataframe[column] = self.dataframe[column].apply(fa.traduz_posicao)
    
    def colunas_desejadas(self, list_colunas):
        """Seleciona uma lista de colunas desejadas do dataframe.
        

        Parameters
        ----------
        list_colunas : list
            Lista com as colunas desejadas.


        """
        self.dataframe = self.dataframe[list_colunas]
        
    def porcentagem_overall_potential(self, potential,overall,new_column):
        """Adiciona uma nova coluna que calcula a porcentagem da diferença de potencial e overall.
        

        Parameters
        ----------
        potential : str
            String com o nome da coluna.
        overall : str
            String com o nome da coluna.
        new_column : str
            String com o nome da nova coluna.

      

        """
        self.dataframe[new_column] = 100*((self.dataframe[potential]-self.dataframe[overall])/self.dataframe[overall])
        
    def escrever_csv(self, caminho_arquivo):
        """Escreve o dataframe em um arquivo csv.
        

        Parameters
        ----------
        caminho_arquivo : str
            Path do arquivo.

        

        """
        self.dataframe.to_csv(caminho_arquivo)
    
    def arredondar_valores(self, column, precisao):
        """Arredonda valores da coluna desejada com a precisão desejada.
        

        Parameters
        ----------
        column : pandas.core.series.Series
            Coluna do dataframe.
        precisao : int
            Quantas casas decimais se quer arredondar.

       

        """
        self.dataframe[column] = self.dataframe[column].apply(lambda x : round(x,precisao))
        
    def cria_skills(self):
        
        PAC = ["Acceleration", "SprintSpeed"]
        SHO = ["Positioning", "Finishing", "ShotPower", "LongShots", "Volleys", "Penalties"]
        PAS = ["Vision", "Crossing", "FKAccuracy", "ShortPassing", "LongPassing", "Curve"]
        DRI = ["Agility", "Balance", "Reactions", "BallControl", "Dribbling", "Composure"]
        DEF = ["Interceptions", "HeadingAccuracy", "Marking", "StandingTackle", "SlidingTackle"]
        PHY = ["Jumping", "Stamina", "Strength", "Aggression"]
        GOALKEEPING = ["GKDiving", "GKHandling", "GKKicking", "GKPositioning", "GKReflexes"]
        
        
        self.dataframe["PAC"] = round(self.dataframe[PAC].mean(axis=1))
        self.dataframe["SHO"] = round(self.dataframe[SHO].mean(axis=1)) 
        self.dataframe["PAS"] = round(self.dataframe[PAS].mean(axis=1)) 
        self.dataframe["DRI"] = round(self.dataframe[DRI].mean(axis=1)) 
        self.dataframe["DEF"] = round(self.dataframe[DEF].mean(axis=1)) 
        self.dataframe["PHY"] = round(self.dataframe[PHY].mean(axis=1)) 
        self.dataframe["DIV"] = self.dataframe[GOALKEEPING[0]] 
        self.dataframe["HAN"] = self.dataframe[GOALKEEPING[1]] 
        self.dataframe["KIC"] = self.dataframe[GOALKEEPING[2]] 
        self.dataframe["POS"] = self.dataframe[GOALKEEPING[3]] 
        self.dataframe["REF"] = self.dataframe[GOALKEEPING[4]]

