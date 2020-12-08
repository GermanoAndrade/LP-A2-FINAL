import unittest
import solucao_fifa as sf


class Testes_SolucaoFIFA(unittest.TestCase):
    
    def teste_melhores(self):
        self.assertEqual(sf.melhores("Goleiro",sf.df_fifa),"De Gea")
        self.assertEqual(sf.melhores("Atacante",sf.df_fifa),['Cristiano Ronaldo', 'L. Messi', 'Neymar Jr'])
        self.assertEqual(sf.melhores("Zagueiro",sf.df_fifa),['Sergio Ramos', 'G. Chiellini'])
        self.assertEqual(sf.melhores("Oi!",sf.df_fifa),"Essa posição não existe!")
        self.assertEqual(sf.melhores("Meia",sf.df_fifa),['A. Griezmann', 'K. De Bruyne', 'David Silva'])
 
    def teste_melhores_time_atual(self):
        self.assertEqual(sf.melhor_time_atual(),['De Gea',
                                                 'Sergio Ramos',
                                                 'G. Chiellini',
                                                 'Azpilicueta',
                                                 'Marcelo',
                                                 'A. Griezmann',
                                                 'K. De Bruyne',
                                                 'David Silva',
                                                 'Cristiano Ronaldo',
                                                 'L. Messi',
                                                 'Neymar Jr'])
    
    def teste_porcentagem_canhotos(self):
        #self.assertRaises(TypeError,sf.porcentagem_canhoto("string kkk",sf.df_fifa))
        #Correção do Raise com tratamento de exceções:
        self.assertEqual(sf.porcentagem_canhoto("Teste",sf.df_fifa),"A variável num precisa ser do tipo int!")
        self.assertEqual(sf.porcentagem_canhoto(50,sf.df_fifa),"A porcentagem dos canhotos em relação aos 50 mais bem avaliados é de 28.0%")
                         
if __name__ == '__main__':
    unittest.main()