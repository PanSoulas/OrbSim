from orbsim._core import Geographic
from orbsim.core.satellite import Satellite
from datetime import datetime, timedelta
from orbsim.core.propagator import delta_minutes_from_epoch
from orbsim.core.propagator import datetime_to_gst

def elevation_angle(observer: Geographic, satellite_geo: Geographic) -> float:
    # TODO: implement elevation angle calculation
    return 0.0

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
