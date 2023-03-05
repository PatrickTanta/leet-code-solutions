import unittest
from fizz_buzz import fizz_buzz_array

class TestClass(unittest.TestCase):
    def test_fizz_buzz(self):
        self.assertEqual(middle_of_the_linked_list(3), ["1","2","Fizz"])
        self.assertEqual(middle_of_the_linked_list(5), ["1","2","Fizz","4","Buzz"])
        self.assertEqual(middle_of_the_linked_list(15), ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"])

if __name__=='__main__':
	unittest.main()
