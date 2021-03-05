import unittest
import fibonacci


class TestCase(unittest.TestCase):
    def test_fibo1(self):
        self.assertEqual(fibonacci.fibo(7),13)
    def test_fibo2(self):
        self.assertEqual(fibonacci.fibo(14),377)
    def test_fact1(self):
        self.assertEqual(fibonacci.fact(6),720)
    def test_fact2(self):
        self.assertEqual(fibonacci.fact(8),40320)


if __name__ == "__main__":
    unittest.main(verbosity=2)
