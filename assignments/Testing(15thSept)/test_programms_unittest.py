import unittest
import math
from programms import fact, prime, area


class TestProgramms(unittest.TestCase):

    def test_fact_valid(self):
        self.assertEqual(fact(4), 24)
        with self.assertRaises(ValueError) as e:
            fact(0)
        print("Factorial error message:", str(e.exception))   

    def test_prime_valid(self):
        self.assertTrue(prime(31))
        self.assertTrue(prime(17))
        with self.assertRaises(ValueError) as e:
            prime(0)
        print("Prime error message:", str(e.exception)) 

    def test_area_valid(self):
        assert math.isclose(area(4), math.pi * 16)
        with self.assertRaises(ValueError) as e:
            area(0)
        print("Area error message:", str(e.exception))  

if __name__ == "__main__":
    unittest.main(verbosity=2)
