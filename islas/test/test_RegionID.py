import unittest

from ..RegionID import RegionID

class TestRegionID(unittest.TestCase):
    
    def test_is_equal_object_id(self):
        id_adelaida = RegionID.adelaida
        self.assertTrue(id_adelaida == RegionID.adelaida)

    def test_is_not_equal_object_id(self):
        id_adelaida = RegionID.adelaida
        self.assertFalse(id_adelaida == RegionID.guadalupe)

if __name__ == '__main__':
    unittest.main()
