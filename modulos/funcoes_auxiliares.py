import numpy as np

def pes_para_cm(height):   
            if height not in [None]:
                height_pes = float(height.replace("'","."))
                height_cm = round(height_pes * 30.48,0)
                return height_cm
            else:
                return np.NaN  

def lbs_para_kg(weight):
        if weight not in [None]:
            weight_lbs = float(weight.replace("lbs",""))
            weight_kg = round(weight_lbs * 0.453592,1)
            return weight_kg
        else:
            return np.NaN

def preco_str_p_int(value):
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
        dicio = {'GK':'Goleiro','LS':'Ponta Esquerda','ST':'Atacante','RS':'Ponta Direita','LW':'Ala Esquerdo','LF':'Atacante Esquerdo','CF':'Centro Avante','RF':'Atacante Direito','RW':'Ala Direito','LAM':'Meia Atacante Esquerdo','CAM':'Armador','RAM':'Meia Atacante Direiro','LM':'Meia Esquerda','LCM':'Meia Ala Esquerdo','CM':'Meia Central','RCM':'Meia Ala Direito','RM':'Meia Direita','LWB':'Lateral Esquerdo','LDM':'Volante Esquerdo','CDM':'Volante Central','RDM':'Volante Direito', 'RWB':'Lateral Direito', 'LB':'Zagueiro Esquerdo', 'LCB':'Zagueiro Central Esquerdo', 'CB':'Zagueiro Central', 'RCB':'Zagueiro Central Direito', 'RB':'Zagueiro Direito'} 
        if position in [None]:
            return np.NaN
        else:
            return dicio[position]