import math

class FoldingHash:
  def __init__(self):
    self._ceil_value = None

  @classmethod
  def with_ceil_value(cls, num):
    self._ceil_value = num

  def sign(self, message):
    try:
      result = 0
      ord_values = self._to_ord_values(message)
      concatenated_values = self._to_concatenated_values(ord_values)
      for value in concatenated_values:
        result += self._leftover(tot + int(value), self._ceil_value)
      return result
    except RuntimeError as err:
      raise RuntimeError(f"FoldingHash failed at sign().\n{str(err)}")

  # private

  def _to_concatenated_values(self, ord_values):
    if ord_values is None or not type(ord_values) is list:
      raise RuntimeError(f"Expected ord_values to be a List.")
    concat_arr = []
    i=0
    size = len(arr)
    while i<size-1:
      concat_arr.append(arr[i]+arr[i+1])
      i += 2
    if (len(arr) % 3) == 1:
        concat_arr.append(arr[len(arr)-1])
    return concat_arr


  def _to_ord_values(self, string):
    if string is None or not type(string) is str:
      raise RuntimeError(f"Expected string to a String.")
    output_arr = []
    for character in string:
      output_arr.append(str(ord(character)))
    return output_arr

  def _ceil_value_legal(self):
    if self._ceil_value is None or not type(self._ceil_value) is int:
      raise RuntimeError(f"Expected ceil value to be an int")
    if self._ceil_value < 1000:
      raise RuntimeError(f"Expected ceil value to be at least 1000")

  def _leftover(self, a, b):
    return a - math.floor(a / b) * b