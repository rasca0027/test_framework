import unittest
from test_framework.add import *

class addTest(unittest.TestCase):
    def test_add_0(self):
        args = [u'1', 2]
        try:
             add(*args) 
        except Exception, inst:
            self.assertEqual( str(inst.message), "coercing to Unicode: need string or buffer, int found" )
    def test_add_1(self):
        args = [2, 3]
 
        self.assertEqual( add(*args), 5 )
    def test_add_2(self):
        args = [3, 4]
 
        self.assertEqual( add(*args), 7 )

if __name__ == '__main__':
    unittest.main()
    