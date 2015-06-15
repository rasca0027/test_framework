import unittest
import add

class multiplyTest(unittest.TestCase):
    def test_multiply_0(self):
        args = [1, 2]
 
        self.assertEqual( add.multiply(*args), 2 )

if __name__ == '__main__':
    unittest.main()
    