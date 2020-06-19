import unittest
from src.folding_hash.hash import FoldingHash

class TestFoldingHash(unittest.TestCase):

  def test_object_init(self):
    FoldingHash()

  def test_object_init_with_ceil(self):
    with self.assertRaises(RuntimeError):
      FoldingHash.with_ceil_value(None)
    with self.assertRaises(RuntimeError):
      FoldingHash.with_ceil_value("10000")
    with self.assertRaises(RuntimeError):
      FoldingHash.with_ceil_value(10)
    FoldingHash.with_ceil_value(1000)

  def test_to_ord_values(self):
    hash_func = FoldingHash.with_ceil_value(1000)
    with self.assertRaises(RuntimeError):
      hash_func._to_ord_values(None)
    with self.assertRaises(RuntimeError):
      hash_func._to_ord_values(1)
    hash_func._to_ord_values("")
    hash_func._to_ord_values("2")

  def test_to_concatenated_values(self):
    hash_func = FoldingHash.with_ceil_value(1000)
    with self.assertRaises(RuntimeError):
      hash_func._to_concatenated_values(None)
    with self.assertRaises(RuntimeError):
      hash_func._to_concatenated_values("1, 2")
    with self.assertRaises(RuntimeError):
      hash_func._to_concatenated_values({1, 2})
    hash_func._to_concatenated_values([1, 2])

  def test_sign(self):
    hash_func = FoldingHash.with_ceil_value(1000)
    with self.assertRaises(RuntimeError):
      hash_func.sign(None)
    with self.assertRaises(RuntimeError):
      hash_func.sign(1)
    self.assertEqual(0, hash_func.sign(""))
    hash_func.sign("Please sign here")
    self.assertEqual(hash_func.sign("Please sign here"), hash_func.sign("Please sign here"))