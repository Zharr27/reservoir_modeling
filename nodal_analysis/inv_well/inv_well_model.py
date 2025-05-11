class Inverted_well:

  def __init__(self, prod_index, reservoir_press, q = 0):
      self.prod_index = prod_index
      self.reservoir_press = reservoir_press
      self.q = q
      self.Q = q * 31

  def __call__(self):
      return self.reservoir_press - self.q / self.prod_index

well = Inverted_well(1, 300, 20)
#test test test