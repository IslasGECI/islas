from ..RegionID import RegionID
from ..Region import Region


def test_region_id_is_equal_object_name():
    region = Region(RegionID.adelaida)
    assert(region.id == RegionID.adelaida.name)
