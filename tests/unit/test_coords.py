from orbsim._core import eci_to_ecef, ecef_to_geographic, StateVector, ECEFVector

def test_eci_to_ecef():
    # Creates a StateVector, set position_km to some values, call eci_to_ecef with gst=0, assert x/y/z are unchanged
    state_vector = StateVector()
    state_vector.position_km = (1000, 2000, 3000)
    
    # Convert ECI to ECEF
    ecef_coords = eci_to_ecef(state_vector, 0)

    # Assert the conversion is correct
    assert abs(ecef_coords.axis_x_km - 1000) < 0.001
    assert abs(ecef_coords.axis_y_km - 2000) < 0.001
    assert abs(ecef_coords.axis_z_km - 3000) < 0.001

def test_ecef_to_geographic():
    # Creates an ECEFVector, set axis_x_km, axis_y_km, axis_z_km to some values, call ecef_to_geographic, assert lat/lon/alt are as expected
    ecef_vector = ECEFVector()
    ecef_vector.axis_x_km = 6378.137  # Approximate radius of Earth in km
    ecef_vector.axis_y_km = 0
    ecef_vector.axis_z_km = 0

    # Convert ECEF to geographic coordinates
    geo = ecef_to_geographic(ecef_vector)

    # Assert the conversion is correct (latitude should be 0, longitude should be 0, altitude should be approximately 0)
    assert abs(geo.latitude_degrees) < 0.001
    assert abs(geo.longitude_degrees) < 0.001
    assert abs(geo.altitude_km) < 1.0

