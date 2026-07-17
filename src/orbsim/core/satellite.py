from orbsim._core import sgp4_propagate, eci_to_ecef, ecef_to_geographic
from orbsim._core import TLEElements, StateVector, ECEFVector, Geographic

class Satellite:
    def __init__(self, name, norad_id, tle):
        self.name : str = name
        self.norad_id : int = norad_id
        self.tle : TLEElements = tle

    @classmethod
    def from_tle(cls, name, norad_id, tle_string):
        pass

    def propagate(self, delta_minutes):
        return sgp4_propagate(self.tle, delta_minutes)

    def ground_position(self, delta_minutes, gst) -> Geographic:
        eci_position : StateVector = self.propagate(delta_minutes)
        ecef_position : ECEFVector = eci_to_ecef(eci_position, gst)
        return ecef_to_geographic(ecef_position)

    def ground_track(self, duration_time, step_minutes, gst):
        delta_minutes = 0
        positions = []
        while delta_minutes <= duration_time:
            positions.append(self.ground_position(delta_minutes, gst))
            delta_minutes += step_minutes
        return positions
