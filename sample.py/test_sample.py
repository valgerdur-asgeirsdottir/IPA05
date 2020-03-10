import unittest
from sample import Fizzbuzz

class FirstTest(unittest.TestCase):

    def test(self):
        self.assertEqual(Fizzbuzz(15), 'FizzBuzz')
        self.assertEqual(Fizzbuzz(30), 'FizzBuzz')
        self.assertEqual(Fizzbuzz(60), 'FizzBuzz')
        self.assertEqual(Fizzbuzz(90), 'FizzBuzz')
        self.assertEqual(Fizzbuzz(150), 'FizzBuzz')
        self.assertEqual(Fizzbuzz(5), 'Buzz')
        self.assertEqual(Fizzbuzz(10), 'Buzz')
        self.assertEqual(Fizzbuzz(20), 'Buzz')
        self.assertEqual(Fizzbuzz(25), 'Buzz')
        self.assertEqual(Fizzbuzz(35), 'Buzz')
        
if __name__ == '__main__':
    unittest.main()
    