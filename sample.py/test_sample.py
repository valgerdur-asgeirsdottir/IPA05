import unittest
from sample import Fizzbuzz

class FirstTest(unittest.TestCase):

    def test(self):
        self.assertEqual(Fizzbuzz(15), 'FizzBuzz')
        self.assertEqual(Fizzbuzz(30), 'FizzBuzz')
        self.assertEqual(Fizzbuzz(60), 'FizzBuzz')
        self.assertEqual(Fizzbuzz(90), 'FizzBuzz')
        self.assertEqual(Fizzbuzz(150), 'FizzBuzz')
        
if __name__ == '__main__':
    unittest.main()
    