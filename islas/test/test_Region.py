import unittest

from ..RegionID import RegionID
from ..Region import Region

class TestRegion(unittest.TestCase):
    
    def test_region_id_is_equal_object_name(self):
        region = Region(RegionID.adelaida)
        self.assertTrue(region.id == RegionID.adelaida.name)

if __name__ == '__main__':
    unittest.main()