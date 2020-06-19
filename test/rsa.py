import unittest
from src.rsa_encryption.rsa import RSA

class TestRSA(unittest.TestCase):
 
  def test_object_init(self):
    algo = RSA()
    algo.primary_first = 13
    algo.primary_second = 19
    with self.assertRaises(RuntimeError):
      RSA.with_public_key(2)
    with self.assertRaises(RuntimeError):
      RSA.with_public_key(("2"))
    with self.assertRaises(RuntimeError):
      RSA.with_public_key((17, "3"))
    with self.assertRaises(RuntimeError):
      RSA.with_public_key((-1, 30))
    with self.assertRaises(RuntimeError):
      RSA.with_public_key((10, 5))
    b = RSA.with_public_key(algo.public_key)

  def test_object_init_with_public_key(self):
    algo = RSA()
    algo.primary_first = 13
    algo.primary_second = 19
    with self.assertRaises(RuntimeError):
      RSA.with_public_key(2)
    with self.assertRaises(RuntimeError):
      RSA.with_public_key(("2"))
    with self.assertRaises(RuntimeError):
      RSA.with_public_key((17, "3"))
    with self.assertRaises(RuntimeError):
      RSA.with_public_key((-1, 30))
    with self.assertRaises(RuntimeError):
      RSA.with_public_key((10, 5))
    b = RSA.with_public_key(algo.public_key)

  def test_object_init_with_primary_numbers(self):
    with self.assertRaises(RuntimeError):
      RSA.with_primary_numbers("13", 19)
    with self.assertRaises(RuntimeError):
      RSA.with_primary_numbers(13, "19")
    with self.assertRaises(RuntimeError):
      RSA.with_primary_numbers(3, 2)
    algo = RSA.with_primary_numbers(13, 31)

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
      "?", "-", "+", "1", "2", "3", "4", "5", "6",
      "7", "8", "9", "0"]
    for char in alphabet_extended:
      self.assertEqual(char, algo._decrypt(algo._encrypt(char)))
    algo = RSA()
    algo.primary_first = 11
    algo.primary_second = 43
    for char in alphabet_extended:
      self.assertEqual(char, algo._decrypt(algo._encrypt(char)))

  def test_encrypt_decrypt_msg(self):
    algo = RSA()
    algo.primary_first = 17
    algo.primary_second = 31
    msg = "I am plain text"
    self.assertEqual(msg, algo.decrypt_msg(algo.encrypt_msg(msg)))
    with self.assertRaises(RuntimeError):
      algo.decrypt_msg("234343")
    with self.assertRaises(RuntimeError):
      algo.encrypt_msg(2323)
    with self.assertRaises(RuntimeError):
      algo.decrypt_msg(None)
    with self.assertRaises(RuntimeError):
      algo.encrypt_msg(None)