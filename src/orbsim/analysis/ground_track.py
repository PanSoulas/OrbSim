from orbsim.core import Satellite
from orbsim._core import Geographic
from orbsim.core import delta_minutes_from_epoch
import datetime

def compute_ground_track(satellite: Satellite, start_time: datetime.datetime, end_time: datetime.datetime, step_minutes: float):
    delta_start = delta_minutes_from_epoch(start_time, satellite.tle)
    delta_end = delta_minutes_from_epoch(end_time, satellite.tle)

    geographic_list = []
    while delta_start <= delta_end:
        ground = satellite.ground_position(delta_start, 0.0)
        geographic_list.append(ground)
        delta_start += step_minutes

    return geographic_list
