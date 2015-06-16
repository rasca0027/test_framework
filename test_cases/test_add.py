import unittest
from test_framework.add import *

class addTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.file = open('add_report', 'w')
    
    @classmethod
    def tearDownClass(self):
        self.file.close()

    def test_add_0(self):
        args = [u'1', 2]
        try:
             add(*args) 
        except Exception, inst:
            self.assertEqual( str(inst.message), "coercing to Unicode: need string or buffer, int found" )
            self.file.write('''add( [u'1', 2] ) => error coercing to Unicode: need string or buffer, int found\n''')
    def test_add_1(self):
        args = [2, 3]
 
        self.assertEqual( add(*args), 5 )
        self.file.write('''add( [2, 3] ) = 5\n''')
    def test_add_2(self):
        args = [3, 4]
 
        self.assertEqual( add(*args), 7 )
        self.file.write('''add( [3, 4] ) = 7\n''')

if __name__ == '__main__':
    unittest.main()
    