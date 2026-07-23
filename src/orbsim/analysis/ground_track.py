from orbsim.core import Satellite
from orbsim._core import Geographic
from orbsim.core import delta_minutes_from_epoch
from datetime import datetime
from datetime import timedelta
from orbsim.core import datetime_to_gst

def compute_ground_track(satellite: Satellite, start_time: datetime, end_time: datetime, step_minutes: float):
    delta_start = delta_minutes_from_epoch(start_time, satellite.tle)
    delta_end = delta_minutes_from_epoch(end_time, satellite.tle)

    geographic_list = []
    current_time = start_time
    while delta_start <= delta_end:
        ground = satellite.ground_position(delta_start, datetime_to_gst(current_time))
        geographic_list.append(ground)
        current_time += timedelta(minutes = step_minutes)
        delta_start += step_minutes

    return geographic_list
