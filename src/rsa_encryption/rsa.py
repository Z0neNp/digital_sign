import math
import random

# TODO
# 1. make more constructors, with private, public keys & primary numbers
# 2. test message encryption decryption, take into account "" and None and not a String

class RSA:
  def __init__(self):
    # Tested
    self._primary_first = None
    self._primary_second = None
    self._private_index = None
    self._public_index = None

  @property
  def n(self):
    # Tested
    self._primary_numbers_valid()
    return self.primary_first * self.primary_second

  @property
  def primary_first(self):
    # Should be a large prime number
    # No test
    return self._primary_first

  @primary_first.setter
  def primary_first(self, num):
    # No test
    self._primary_first = num
  
  @property
  def primary_second(self):
    # Should be a large prime number
    # No test
    return self._primary_second

  @primary_second.setter
  def primary_second(self, num):
    # No test
    self._primary_second = num

  @property
  def private_index(self):
    # Tested
    try:
      if self._private_index is None:
        self._private_index = self._private_index_gen()
      return self._private_index
    except RuntimeError as err:
      err_msg = f"RSA failed at private_index().\n{str(err)}"
      raise RuntimeError(err_msg)
  
  @property
  def private_key(self):
    #  No test
    return (self.private_index, self.reduced_residual_set)

  @property
  def public_index(self):
    # Tested
    try:
      if self._public_index is None:
        self._public_index = self._public_index_gen()
      return self._public_index
    except RuntimeError as err:
      raise RuntimeError(f"RSA failed at public_index().\n#{str(err)}")

  @property
  def public_key(self):
    # No test
    return (self.public_index, self.reduced_residual_set)

  @property
  def reduced_residual_set(self):
    # N = primary_first * primary_second
    # Each element in the reduced_residual_set is relatively prime to N, GCD(element, N) = 1.
    # Tested
    self._primary_numbers_valid()
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
    # Tested
    return chr(self._fast_exponentiation(encrypted, self.private_index, self.n))

  def _encrypt(self, plain):
    # Tested
    return self._fast_exponentiation(plain, self.public_index, self.n)

  def _fast_exponentiation(self, a, b, n):
    # Tested
    if b == 0:
      return 1
    if b % 2 == 0:
      temp = self._fast_exponentiation(a, b / 2, n)
      return self._leftover(temp * temp, n)
    else:
      temp = self._fast_exponentiation(a, b - 1, n)
      return self._leftover(a * temp, n)

  def _gcd(self, a, b):
    # Tested
    if b == 0:
      return a
    else:
      return self._gcd(b, self._leftover(a, b))

  def _primary_numbers_valid(self):
    # Tested
    err_msg = "RSA failed at reduced_residual_set()."
    if self.primary_first is None or self.primary_first < 2:
      raise RuntimeError(err_msg + "\nSet first primary number greater than 1")
    if self.primary_second is None or self.primary_second < 2:
      raise RuntimeError(err_msg + "\nSet second primary number greater than 1")
    if self.primary_first * self.primary_second < 201:
      raise RuntimeError(err_msg + "\nN has to be greater than 200")

  def _private_index_gen(self):
    # Tested
    result = None
    potential_result = 1
    while result is None:
      leftover = self._leftover(
        self.public_index * potential_result,
        self.reduced_residual_set
      )
      if leftover == 1:
        result = potential_result
        break
      potential_result += 1
      if potential_result >= self.reduced_residual_set:
        err_msg = f"There is no legal private index in the range (0,{self.reduced_residual_set})"
        raise RuntimeError(err_msg)
    return result

  def _public_index_gen(self):
    # No test
    result = None
    while result is None:
      potential_result = random.randint(2, self.reduced_residual_set - 1)
      if self._gcd(self.reduced_residual_set, potential_result) == 1:
        result = potential_result
        break
    return result

  def _leftover(self, a, b):
    # Tested
    return a - math.floor(a / b) * b