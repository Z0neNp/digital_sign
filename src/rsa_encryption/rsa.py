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
    self._n = None
    self._reduced_residual_set = None

  @classmethod
  def with_primary_numbers(cls, first, second):
    try:
      result = RSA()
      result.primary_first = first
      result.primary_second = second
      result._primary_numbers_valid()
      return result
    except RuntimeError as err:
      raise RuntimeError(f"RSA failed at with_primary_numbers().{str(err)}")

  @classmethod
  def with_public_key(cls, key):
    try:
      result = RSA()
      result._key_legal(key)
      return result
    except RuntimeError as err:
      raise RuntimeError(f"RSA failed at with_public_key().{str(err)}")

  @property
  def n(self):
    # Tested
    self._primary_numbers_valid()
    if self._n is None:
      self._n = self.primary_first * self.primary_second
    return self._n

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
    try:
      self._primary_numbers_valid()
      if self._reduced_residual_set is None:
        self._reduced_residual_set = (self.primary_first - 1) * (self.primary_second - 1)
      return self._reduced_residual_set
    except RuntimeError as err:
      raise RuntimeError(f"RSA failed at reduced_residual_set.{str(err)}")

  def decrypt_msg(self, encrypted_msg):
    # Tested
    try:
      if not type(encrypted_msg) is list:
        raise RuntimeError(f"Expected encrypted message to be a List.")
      result = ""
      for encrypted_char in encrypted_msg:
        result = result + self._decrypt(encrypted_char)
      return result
    except RuntimeError as err:
      raise RuntimeError(f"RSA failed at decrypt_msg().\n{str(err)}")

  def encrypt_msg(self, plain_msg):
    # Tested
    try:
      if not type(plain_msg) is str:
        raise RuntimeError("Expected plain message to be a String.")
      result = []
      if len(plain_msg) > 0:
        for char in plain_msg:
          result.append(self._encrypt(char))
      return result
    except RuntimeError as err:
      raise RuntimeError(f"RSA failed at encrypt_msg().\n{str(err)}")

  # private

  def _decrypt(self, encrypted):
    # Tested
    return chr(self._fast_exponentiation(encrypted, self.public_index, self.n))

  def _encrypt(self, plain):
    # Tested
    return self._fast_exponentiation(ord(plain), self.private_index, self.n)

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

  def _key_legal(self, key):
    if not type(key) is tuple:
      raise RuntimeError(f"Expected key to be a Tuple.")
    if not type(key[0]) is int:
      raise RuntimeError(f"Expected key to contain int as the first value.")
    if not type(key[1]) is int:
      raise RuntimeError(f"Expected key to contain int as the second value.")
    if not key[0] > 0 or not key[0] < key[1]:
      raise RuntimeError(f"Expected key's index value to be in range (0, reduced_residual_set") 

  def _primary_numbers_valid(self):
    # Tested
    if self.primary_first is None or not type(self.primary_first) is int:
      raise RuntimeError("Expected first primary number to be an int")
    if self.primary_first < 2:
      raise RuntimeError("Expected first primary number to be greater than 1")
    if self.primary_second is None or not type(self.primary_second) is int:
      raise RuntimeError("Expected second primary number to be an int")
    if self.primary_second < 2:
      raise RuntimeError("Expected second primary number to be greater than 1")
    if self.primary_first * self.primary_second < 201:
      raise RuntimeError("Expected N to be greater than 200")

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
    # Tested
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