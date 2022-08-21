import unittest


class MyTestCase(unittest.TestCase):


    def test_something(self):
        #call some method here
        result = 2 + 2
        self.assertEqual(4, result)  # add assertion here

    def test_soma(self):
        result2 = 2 + 0
        self.assertEqual(2, result2)  # add assertion here

    def test_something2(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
