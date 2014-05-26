"""
tests.py
Nitaino

Prueba que cosas funcionen.

"""

import unittest, libnitaino

        
class TestLibNitaino(unittest.TestCase):
    """
    Prueba que todo funcione en libtaino
    """
     
    def test_printea(self):
        """
        Prueba el alias para 
        """
        # prueba que regrese una cadena con los aguanta lugares remplacados
        self.assertEqual(libnitaino.printea('%s' % ('Testing print wrapper')), 'Testing print wrapper')
        
        # que functione con numeros
        self.assertEqual(libnitaino.printea('%s' % (1)), '1')
        self.assertEqual(libnitaino.printea('%d' % (1)), '1')
        
        # que funcione normal
        self.assertEqual(libnitaino.printea('Testing print wrapper'), 'Testing print wrapper')

    def test_collecion_a_numeros(self):
        """
        Prueba collecion a numeros
        """        
        # una collecion de numeros
        self.assertEqual(libnitaino.collecion_a_numeros(["1", "2", "3"]), 
                                                        [1, 2, 3])       
                                                        
        # collecion con solo un numero
        self.assertEqual(libnitaino.collecion_a_numeros(["123"]), 
                                                         [123])       

        # solo una cadena debe regresar una collecion de numeros 
        self.assertEqual(libnitaino.collecion_a_numeros("123"), 
                                                         [1, 2, 3])
         
        # negativos tambien funcionan
        self.assertEqual(libnitaino.collecion_a_numeros(["-1", "-2", "-3"]), 
                                                        [-1, -2, -3])
                                                         
        # vacio a vacio                                                                                        
        self.assertEqual(libnitaino.collecion_a_numeros([]), [])
         
        # numeros se quedan iqual
        self.assertEqual(libnitaino.collecion_a_numeros([1]), [1])
         
        # una cadena vacia es un error
        self.assertRaises(ValueError, libnitaino.collecion_a_numeros, [""])
         
        # letras son errores
        self.assertRaises(ValueError, libnitaino.collecion_a_numeros, ["a", 
                                                                       "b",
                                                                       "c"])
    
        self.assertRaises(ValueError, libnitaino.collecion_a_numeros, ["a"])
                                                                             
    def test_analiza_serie(self):
        """
        La funcion analiza_serie.
        
        """
        # que regresa una collecion con numeros n1-n2
        self.assertEqual(list(libnitaino.analiza_serie('0-10')), [0, 1, 2, 3, 4, 5,
                                                             6, 7, 8, 9])
                                                       
        # si se puede pasar un paso
        self.assertEqual(list(libnitaino.analiza_serie('0-10-2')), [0, 2, 4, 6, 8])
        
        # si el primero es menor, debe regresar una lista bacia
        self.assertEqual(list(libnitaino.analiza_serie('20-1')), [])
        
        # no se puede pasar nada sin '-'
        self.assertRaises(ValueError, libnitaino.analiza_serie, '') 
        
        # no se puede pasar algo que no se numeros, aparte de '-' 
        self.assertRaises(ValueError, libnitaino.analiza_serie, '19-19a')

        # solo letras error 
        self.assertRaises(ValueError, libnitaino.analiza_serie, 'a-a')
        self.assertRaises(ValueError, libnitaino.analiza_serie, 's')

        
        # se puede pasar solo un numero
        self.assertEqual(list(libnitaino.analiza_serie('10')), [10])
            
        # y es lo mismo que pasar n1-n1+1
        self.assertEqual(list(libnitaino.analiza_serie('10-11')), [10])

if __name__ == '__main__':
    unittest.main()
    
