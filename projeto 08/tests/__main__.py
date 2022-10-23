
# assert

soma = sum([1,2,3])

assert soma == 6, 'Era para ser 6'
# print('passou no test!')



# Teste unitario
import unittest

class Teste01(unittest.TestCase):
    
    def test_soma(self):
        self.assertEqual(sum([1,2,3]), 7, 'Era para ser 6 na classe')
        


#rodar todos os testes
#unittest.main()

from ipdb import set_trace 

# IPDB

nome = 'julio'

set_trace()

nome = 'Cezar'

set_trace()


        


