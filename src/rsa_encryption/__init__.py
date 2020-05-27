class RSA:
  def __init__(self):
    # pass

  @property
  def primary_first(self):
    # Should be a large prime number
    return self._primary_first
  
  @property
  def primary_second(self):
    # Should be a large prime number
    return self._primary_second

  @property
  def private_key(self):
    # pass

  @property
  def public_key(self):
    # pass

  @property
  def reduced_residual_set(self):
    # N = primary_first * primary_second
    # Each element in the reduced_residual_set is relatively prime to N, GCD(element, N) = 1.
    return (self.primary_first - 1) * (self.primary_second - 1)

