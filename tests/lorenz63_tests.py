import random
import unittest

from lorenz63 import model

class UnitTestFunctions(unittest.TestCase):
    def test_lgp_format_number_positive(self):
        self.assertEqual(model._lgp_format_number(123.4), '1234')
        self.assertEqual(model._lgp_format_number(5.6), '0056')
        self.assertEqual(model._lgp_format_number(30000), '300000')
        
    def test_lgp_format_number_negative(self):
        self.assertEqual(model._lgp_format_number(-123.4), '-1234')

        
class IntegrationTestFunctions(unittest.TestCase):
    def test_bounded(self):
        for i in range(2):
            X0, Y0, Z0 = random.random(), random.random(), random.random()
            lorenz_model = model.Lorenz63(nt=6000, dt=0.01, X0=X0, Y0=Y0, Z0=Z0)
            lorenz_model.run()
            self.assertTrue(-40 < lorenz_model.Xs.min() and lorenz_model.Xs.max() < 40)
            self.assertTrue(-40 < lorenz_model.Ys.min() and lorenz_model.Ys.max() < 40)
            self.assertTrue(-20 < lorenz_model.Zs.min() and lorenz_model.Zs.max() < 60)        
            
            
if __name__ == '__main__':
    unittest.main()