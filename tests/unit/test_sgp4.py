from orbsim.core.tle import parse_tle
from orbsim._core import sgp4_propagate
import math

def test_sgp4_propagation():
    title = "ISS (ZARYA)"
    line_1 = "1 25544U 98067A   23166.51782528  .00016717  00000+0  30209-3 0  9992"
    line_2 = "2 25544  51.6416  21.4320 0009623  99.9999  36.0000 15.50000000000000"
    tle_string = f"{title}\n{line_1}\n{line_2}"

    state_vector = sgp4_propagate(parse_tle(tle_string), 0)
    altitude_km = math.sqrt(sum(x**2 for x in state_vector.position_km)) - 6378.137

    assert 400 < altitude_km < 430
    assert len(state_vector.position_km) == 3
    assert len(state_vector.velocity_km_per_sec) == 3
