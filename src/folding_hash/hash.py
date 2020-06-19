import math

class FoldingHash:
  
  def __init__(self):
    # Tested
    self._ceil_value = None

  @classmethod
  def with_ceil_value(cls, num):
    # Tested
    try:
      result = FoldingHash()
      result._ceil_value = num
      result._ceil_value_legal()
      return result
    except RuntimeError as err:
      raise RuntimeError(f"FoldingHash failed at with_ceil_value().\n{str(err)}")

  def sign(self, message):
    # Tested
    try:
      result = 0
      ord_values = self._to_ord_values(message)
      concatenated_values = self._to_concatenated_values(ord_values)
      for value in concatenated_values:
        result += self._leftover(result + int(value), self._ceil_value)
      return result
    except RuntimeError as err:
      raise RuntimeError(f"FoldingHash failed at sign().\n{str(err)}")

  # private

  def _to_concatenated_values(self, ord_values):
    # Tested
    if ord_values is None or not type(ord_values) is list:
      raise RuntimeError(f"Expected ord_values to be a List.")
    concat_arr = []
    i=0
    size = len(ord_values)
    while i<size-1:
      concat_arr.append(ord_values[i]+ord_values[i+1])
      i += 2
    if (len(ord_values) % 3) == 1:
        concat_arr.append(ord_values[len(ord_values)-1])
    return concat_arr

  def _to_ord_values(self, string):
    # Tested
    if string is None or not type(string) is str:
      raise RuntimeError(f"Expected string to a String.")
    output_arr = []
    for character in string:
      output_arr.append(str(ord(character)))
    return output_arr

  def _ceil_value_legal(self):
    # Tested
    if self._ceil_value is None or not type(self._ceil_value) is int:
      raise RuntimeError(f"Expected ceil value to be an int")
    if self._ceil_value < 1000:
      raise RuntimeError(f"Expected ceil value to be at least 1000")

  def _leftover(self, a, b):
    # Tested
    return a - math.floor(a / b) * b