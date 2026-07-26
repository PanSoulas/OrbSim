from orbsim._core import Geographic
from orbsim.core.satellite import Satellite
from datetime import datetime, timedelta
from orbsim.core.propagator import delta_minutes_from_epoch
from orbsim.core.propagator import datetime_to_gst
import math

def geographic_to_ecef(geo: Geographic):
    RE = 6378.137
    lat_rad = math.radians(geo.latitude_degrees)
    alt_km= geo.altitude_km
    lon_rad = math.radians(geo.longitude_degrees)
    x = (RE + alt_km) * math.cos(lat_rad) * math.cos(lon_rad)
    y = (RE + alt_km) * math.cos(lat_rad) * math.sin(lon_rad)
    z = (RE + alt_km) * math.sin(lat_rad) 
    return x, y, z


def elevation_angle(observer: Geographic, satellite_geo: Geographic) -> float:
    obs_x, obs_y, obs_z = geographic_to_ecef(observer)
    sat_x, sat_y, sat_z = geographic_to_ecef(satellite_geo)
    range_vector = (sat_x - obs_x, sat_y - obs_y, sat_z - obs_z)
    zenith_vector = (obs_x, obs_y, obs_z)
    mag_range = math.sqrt(range_vector[0]**2 + range_vector[1]**2 + range_vector[2]**2)
    mag_zenith = math.sqrt(zenith_vector[0]**2 + zenith_vector[1]**2 + zenith_vector[2]**2)
    dot_product = (range_vector[0]*zenith_vector[0] + 
               range_vector[1]*zenith_vector[1] + 
               range_vector[2]*zenith_vector[2])
    elevation = 90 - math.degrees(math.acos(dot_product / (mag_range * mag_zenith)))
    return elevation

def compute_passes(satellite: Satellite, observer: Geographic, start_time: datetime, end_time: datetime, min_elevation_deg: float = 0.0, step_minutes: float = 0.0):
    passes = []
    current_time = start_time
    while current_time < end_time:
        # Propagate satellite to the current time
        delta = delta_minutes_from_epoch(current_time, satellite.tle)
        satellite_position = satellite.ground_position(delta, datetime_to_gst(current_time))

        # Calculate elevation angle
        elevation = elevation_angle(observer, satellite_position)

        if elevation >= min_elevation_deg:
            passes.append((current_time, elevation))

        # Increment time by step_minutes
        current_time += timedelta(minutes=step_minutes)
    return passes
