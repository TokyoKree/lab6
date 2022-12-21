import unittest
from main import sum
from main import div
from main import sub
from main import mul

class TestCalculator(unittest.TestCase):
  def test_sum(self):
    self.assertEqual(sum(4,7), 11)
  def test_sub(self):
    self.assertEqual(sub(10,5), 5)
  def test_mul(self):
    self.assertEqual(mul(3,7), 21)
  def test_div(self):
    self.assertEqual(div(10,2), 5)
