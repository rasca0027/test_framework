import unittest
from test_framework.add import *

class multiplyTest(unittest.TestCase):
    def test_multiply_0(self):
        args = [1, 2]
 
        self.assertEqual( multiply(*args), 2 )

if __name__ == '__main__':
    unittest.main()
    