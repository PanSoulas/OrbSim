from orbsim.core.tle import parse_tle
import pytest
    

def test_parse_tle():
    title = "ISS (ZARYA)"
    line_1 = "1 25544U 98067A   23166.51782528  .00016717  00000+0  30209-3 0  9992"
    line_2 = "2 25544  51.6416  21.4320 0009623  99.9999  36.0000 15.50000000000000"
    tle_string = f"{title}\n{line_1}\n{line_2}"
    tle = parse_tle(tle_string)
    assert 0 < tle.eccentricity < 1
    assert tle.mean_motion > 0
    assert tle.inclination > 0

def test_parse_tle_invalid():
    pytest.raises(ValueError, parse_tle, "Invalid string")

