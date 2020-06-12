import math
import random

class RSA:
  def __init__(self):
    self._private_index = None
    self._public_index = None

  @property
  def primary_first(self):
    # Should be a large prime number
    return self._primary_first
  
  @property
  def primary_second(self):
    # Should be a large prime number
    return self._primary_second

  @property
  def private_index(self):
    if self._private_index is None:
      self._private_index = self._private_index_gen()
    return self._private_index
  
  @property
  def private_key(self):
    return (self.private_index, self.reduced_residual_set)

  @property
  def public_index(self):
    if self._public_index is None:
      self._public_index = self._public_index_gen()
    return self._public_index

  @property
  def public_key(self):
    return (self.public_index, self.reduced_residual_set)

  @property
  def reduced_residual_set(self):
    # N = primary_first * primary_second
    # Each element in the reduced_residual_set is relatively prime to N, GCD(element, N) = 1.
    return (self.primary_first - 1) * (self.primary_second - 1)

  def decrypt_msg(self, encrypted_msg):
    result = ""
    for char in encrypted_msg:
      result = result + self._decrypt(ord(char))
    return result

  def encrypt_msg(self, plain_msg):
    result = ""
    for char in plain_msg:
      result = result + self._encrypt(ord(char))
    return result

  # private

  def _decrypt(self, encrypted):
    return self._fast_exponentiation(decrypted, self.private_index)

  def _encrypt(self, plain):
    return self._fast_exponentiation(plain, self.public_index)

  def _fast_exponentiation(self, a, b):
    n = self.reduced_residual_set
    if b == 0:
      return 1
    if b % 2 == 0:
      temp = self._fast_exponentiation(a, b / 2, n)
      return self._residue(temp, n) * self._residue(temp, n)
    else:
      temp = self._fast_exponentiation(a, b - 1, n)
      return self._residue(a, n) * self._residue(temp, n)


  def _gcd(self, a, b):
    if b == 0:
      return a
    else:
      return self._gcd(b, a % b)

  def _private_index_gen(self):
    result = None
    potential_result = 1
    while result is None:
      first_leftover = self.public_index % self.reduced_residual_set
      second_leftover = potential_result % self.reduced_residual_set
      if (first_leftover * second_leftover) % self.reduced_residual_set:
        result = potential_result
      potential_result += 1
      if potential_result >= self.reduced_residual_set:
        err_msg = f"There is no legal private index in the range (1,{self.reduced_residual_set})"
        raise RuntimeError(err_msg)
    return result

  def _public_index_gen(self):
    result = None
    while result is None:
      potential_result = random.randint(2, self.reduced_residual_set() - 1)
      if self._gcd(self.reduced_residual_set(), potential_result) == 1:
        result = potential_result
    return result

  def _residue(self, a, b):
    return a - math.floor(a / b) * b