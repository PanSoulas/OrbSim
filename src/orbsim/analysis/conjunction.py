from orbsim.core import Satellite
from datetime import datetime, timedelta
from orbsim.core.propagator import delta_minutes_from_epoch
import math

def compute_conjunctions(satellite1: Satellite, satellite2: Satellite, start_time: datetime, end_time: datetime, step_minutes: float = 1.0, threshold_km: float = 10.0):
    conjunctions = []
    while start_time < end_time:
        delta1 = delta_minutes_from_epoch(start_time, satellite1.tle)
        delta2 = delta_minutes_from_epoch(start_time, satellite2.tle)

        pos1 = satellite1.propagate(delta1).position_km
        pos2 = satellite2.propagate(delta2).position_km

        distance_km = math.sqrt(
            (pos1[0] - pos2[0]) ** 2 +
            (pos1[1] - pos2[1]) ** 2 +
            (pos1[2] - pos2[2]) ** 2
        )

        if distance_km <= threshold_km:
            conjunctions.append((start_time, distance_km))

        start_time += timedelta(minutes=step_minutes)

    return conjunctions