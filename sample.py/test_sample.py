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
        self.assertEqual(Fizzbuzz(3), 'Fizz')
        self.assertEqual(Fizzbuzz(6), 'Fizz')
        self.assertEqual(Fizzbuzz(9), 'Fizz')
        self.assertEqual(Fizzbuzz(18), 'Fizz')
        self.assertEqual(Fizzbuzz(21), 'Fizz')
        self.assertEqual(Fizzbuzz(8), 8)
        self.assertEqual(Fizzbuzz(1), 1)
        self.assertEqual(Fizzbuzz(11), 11)
        self.assertEqual(Fizzbuzz(23), 23)
        self.assertEqual(Fizzbuzz(64), 64)
        
        
if __name__ == '__main__':
    unittest.main()
    