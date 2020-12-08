import numpy as np

def pes_para_cm(height):   
    """Função que transforma uma string com a altura medida em pés em um float com essa altura convertida para centímetros.
    

    Parameters
    ----------
    height : str
        String contendo a altura, em pés, dos jogadores.

    Returns
    -------
    float
        Float contendo a altura, em centímetros, dos jogadores.

    """
    if height not in [None]:
        height_pes = float(height.replace("'","."))
        height_cm = round(height_pes * 30.48,0)
        return height_cm
    else:
        return np.NaN  


def lbs_para_kg(weight):
    """Função que transforma uma string com o peso, em libras, em um float com esse peso convertido para quilogramas.
    

    Parameters
    ----------
    weight : str
        String contendo o peso, em libras, dos jogadores.

    Returns
    -------
    float
        Float contendo o peso, em quilogramas, dos jogadores.

    """
    if weight not in [None]:
        weight_lbs = float(weight.replace("lbs",""))
        weight_kg = round(weight_lbs * 0.453592,1)
        return weight_kg
    else:
        return np.NaN

def preco_str_p_int(value):
    """Função que transforma uma string contendo o valor, na forma MK(M = Milhões, K = Milhares), em um float com o valor real.
    

    Parameters
    ----------
    value : str
        String da forma '€x(MK)', que representa o preço x em M = Milhões ou K = Milhares de Euros.

    Returns
    -------
    int
        Int com o preço real do jogador.

    """
    if value in [None,np.NaN]:
        return 0
    elif 'M' in value:
        value_str = value.replace("M","")
        value_int = float(value_str.replace("€",""))*1000000
        return int(value_int)
    elif 'K' in value:
        value_str = value.replace("K","")
        value_int = float(value_str.replace("€",""))*1000
        return int(value_int)

def traduz_posicao(position):
    """Função que traduz a string com a sigla da posição em uma string com nome da posição.
    

    Parameters
    ----------
    position : str
        String que contém a sigla que representa a posição do jogador.

    Returns
    -------
    str
        String que contém a posição do jogador.

    """
    dicio = {'GK':'Goleiro','LS':'Ponta Esquerda','ST':'Atacante','RS':'Ponta Direita','LW':'Ponta Esquerdo','LF':'Ponta Esquerdo','CF':'Meia Atacante','RF':'Ponta Direita','RW':'Ponta Direita','LAM':'Meia','CAM':'Meia Atacante','RAM':'Meia Direita','LM':'Meia Esquerda','LCM':'Meia Esquerda','CM':'Meia Atacante','RCM':'Meia Direita','RM':'Meia Direita','LWB':'Lateral Esquerdo','LDM':'Volante','CDM':'Volante','RDM':'Volante', 'RWB':'Lateral Direito', 'LB':'Lateral Esquerdo', 'LCB':'Zagueiro Esquerdo', 'CB':'Zagueiro Direito', 'RCB':'Zagueiro Direito', 'RB':'Lateral Direito'}
    if position in [None]:
        return np.NaN
    else:
        return dicio[position]