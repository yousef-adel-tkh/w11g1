import unittest
from funcs import *

class testClass(unittest.TestCase):

    # IsLeap()
    def test_isLeap(self):
        self.assertFalse(isLeap(1991)) # F     -> F
        self.assertTrue(isLeap(1996))  # T F   -> T
        self.assertFalse(isLeap(2100)) # T T F -> F
        self.assertTrue(isLeap(2000))  # T T T -> T

    # pointInTriangle()
    def test_pointInTriangle_InvalidTriangle(self):

        self.assertEqual(pointInTriangle(0,0,0,0), -1)
        self.assertEqual(pointInTriangle(0,1,0,0), -1)
        self.assertEqual(pointInTriangle(1,0,0,0), -1)

    def test_pointInTriangle_Outside(self):
        # x in, y out
        self.assertEqual(pointInTriangle(1,1,0,1.1),  1)
        self.assertEqual(pointInTriangle(1,1,1,-0.1), 1)

        # x out, y in
        self.assertEqual(pointInTriangle(1,1,1.1,0),  1)
        self.assertEqual(pointInTriangle(1,1,1-0.1,1), 1)

        # x out, y out
        self.assertEqual(pointInTriangle(1,1,1.1,1.1),   1)
        self.assertEqual(pointInTriangle(1,1,-0.1,-0.1), 1)

    def test_pointInTriangle_On(self):
        self.assertEqual(pointInTriangle(1,1,0.5,0.5),  2)
    
    def test_pointInTriangle_Inside(self):
        self.assertEqual(pointInTriangle(1,1,0.5,0.4), 0)
        self.assertEqual(pointInTriangle(1,1,0.4,0.5), 0)

    # gradeClassification()
    def test_gradeClassification_Invalid(self):
        self.assertEqual(gradeClassification(101), -1)
        self.assertEqual(gradeClassification(-1),  -1)

    def test_gradeClassification_A(self):
        self.assertEqual(gradeClassification(100), 0)
        self.assertEqual(gradeClassification(70),  0)

    def test_gradeClassification_P(self):
        self.assertEqual(gradeClassification(69), 1)
        self.assertEqual(gradeClassification(40), 1)

    def test_gradeClassification_F(self):
        self.assertEqual(gradeClassification(39), 2)
        self.assertEqual(gradeClassification(0),  2)

    # isPrime()
    def test_isPrime(self):
        self.assertTrue(isPrime(53))
        self.assertFalse(isPrime(9))
        self.assertFalse(isPrime(1))

        with self.assertRaises(TypeError):
            isPrime(21.5)

    # getInvestmentValue()
    def test_getInvestmentValue(self):
        with self.assertRaises(ValueError):
            getInvestmentValue(0,1,1)

        with self.assertRaises(ValueError):
            getInvestmentValue(1,0,1)

        with self.assertRaises(ValueError):
            getInvestmentValue(1,1,0)

        self.assertEqual(getInvestmentValue(1,12,1), 1.13)



