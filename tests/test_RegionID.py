from ..RegionID import RegionID


def test_is_equal_object_id():
    id_adelaida = RegionID.adelaida
    assert(id_adelaida == RegionID.adelaida)


def test_is_not_equal_object_id():
    id_adelaida = RegionID.adelaida
    assert(id_adelaida != RegionID.guadalupe)
