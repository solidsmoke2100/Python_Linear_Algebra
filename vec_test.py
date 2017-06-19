import unittest
from vec import Vector

class VectorTests(unittest.TestCase):

  def test_construction_from_args(self):
    self.assertEqual("<-6, 27, 4.3, 16, -81.95>", str(Vector(-6,27,4.3,16,-81.95)))

  def test_construction_from_list(self):
    self.assertEqual("<-6, 27, 4.3, 16, -81.95>", str(Vector( [-6,27,4.3,16,-81.95] )))

  def test_construction_from_tuple(self):
    self.assertEqual("<-6, 27, 4.3, 16, -81.95>", str(Vector( (-6,27,4.3,16,-81.95) )))

  def test_construction_from_specified_dim_no_fill(self):
    self.assertEqual("<0, 0, 0, 0, 0>", str(Vector(5)))

  def test_construction_from_specified_dim_and_fill(self):
    self.assertEqual("<1, 1, 1, 1, 1>", str(Vector(5, fill=1)))

  def test_inner_product(self):
    self.assertEqual(-30, Vector(3, fill=2).inner_prod(Vector(3, fill=-5)))

  def test_to_list_conversion(self):
    self.assertEqual( [1,2,3,4,5], Vector(1,2,3,4,5).to_list() )

if __name__ == '__main__':
  unittest.main()