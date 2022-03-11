import unittest
import views

class TestMatrix(unittest.TestCase):
    def test_Matrix(self):
        actual = views.matrix()
        expected = ("[[1 2 3] [4 5 6] [7 8 9]]","[2 2 2]","[[ 2 4 6] [ 8 10 12] [14 16 18]]","[24 30 36]")
        self.assertEqual(actual, expected)
        print(actual == expected)

class testScipy(unittest.TestCase):
    def test_scipy(self):
        results = views.ricky()
        expected = (210, 16.0)
        self.assertEqual(results, expected)
        print(results == expected)
