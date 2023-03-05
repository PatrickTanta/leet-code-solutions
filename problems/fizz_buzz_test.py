import unittest
from fizz_buzz import fizz_buzz_array

class TestClass(unittest.TestCase):
    def test_fizz_buzz(self):
        self.assertEqual(fizz_buzz_array(3), ["1","2","Fizz"])
        self.assertEqual(fizz_buzz_array(5), ["1","2","Fizz","4","Buzz"])
        self.assertEqual(fizz_buzz_array(15), ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"])

if __name__=='__main__':
	unittest.main()
