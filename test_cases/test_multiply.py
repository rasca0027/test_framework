import unittest
from test_framework.add import *

class multiplyTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.file = open('multiply_report', 'w')
    
    @classmethod
    def tearDownClass(self):
        self.file.close()

    def test_multiply_0(self):
        args = [1, 2]
 
        self.assertEqual( multiply(*args), 2 )
        self.file.write('''multiply( [1, 2] ) = 2\n''')

if __name__ == '__main__':
    unittest.main()
    