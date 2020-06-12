import unittest
from src.rsa_encryption.rsa import RSA

class TestRSA(unittest.TestCase):
  def test_object_init(self):
    RSA()

  def test_gcd(self):
    algo = RSA()
    self.assertEqual(algo._gcd(5, 2), 1)
    self.assertEqual(algo._gcd(5, 3), 1)
    self.assertEqual(algo._gcd(10, 8), 2)
    self.assertEqual(algo._gcd(51, 4), 1)

  def test_public_index(self):
    algo = RSA()
    with self.assertRaises(RuntimeError):
      algo.public_index
    self.primary_first = 2
    with self.assertRaises(RuntimeError):
      algo.public_index
      self.primary_first = 2
    with self.assertRaises(RuntimeError):
      algo.public_index
    algo.primary_first = 13
    algo.primary_second = 19
    public_index = algo.public_index
    self.assertEqual(public_index, algo.public_index)
    self.assertEqual(public_index, algo.public_index)
    self.assertEqual(public_index, algo.public_index)

  def test_private_index(self):
    algo = RSA()
    algo.primary_first = 2
    algo.primary_second = 2
    with self.assertRaises(RuntimeError):
      algo.private_index
    algo = RSA()
    algo.primary_first = 13
    algo.primary_second = 19
    private_index = algo.private_index
    self.assertEqual(private_index, algo.private_index)
    self.assertEqual(private_index, algo.private_index)
    self.assertEqual(private_index, algo.private_index)

  def test_encrypt_decrypt(self):
    algo = RSA()
    algo.primary_first = 13
    algo.primary_second = 19
    alphabet_extended = [
      "a", "b", "c", "d", "e", "f", "g", "h", "i",
      "j", "k", "l", "m", "n", "o", "p", "q", "r",
      "s", "t", "u", "v", "w", "x", "y", "z", "A",
      "B", "C", "D", "E", "F", "G", "H", "I", "K",
      "L", "M", "N", "O", "P", "Q", "R", "S", "T",
      "U", "V", "W", "X", "Y", "Z", " ", ".", "!",
      "?", "-", "+"]
    for char in alphabet_extended:
      self.assertEqual(char, algo._decrypt(algo._encrypt(ord(char))))
    algo = RSA()
    algo.primary_first = 11
    algo.primary_second = 43
    for char in alphabet_extended:
      self.assertEqual(char, algo._decrypt(algo._encrypt(ord(char))))