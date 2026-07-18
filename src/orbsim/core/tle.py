from orbsim._core import TLEElements
import math


def parse_tle(tle_string: str) -> TLEElements:
    lines = tle_string.strip().splitlines()
    if len(lines) != 3:
        raise ValueError("TLE must contain exactly three lines \n")
    
    name = lines[0].strip()
    line1 = lines[1].strip()
    line2 = lines[2].strip()

    tle = TLEElements()
    tle.epoch_jd = float(line1[18:32].strip())
    raw = line1[53:61].strip()
    mantissa = raw[:-2]
    exponent = int(raw[-2:])
    tle.bstar = float("0." + mantissa) * (10 ** exponent)
    tle.eccentricity = float(f"0.{line2[26:33].strip()}")
    
    tle.inclination = float(line2[8:16].strip()) * math.pi / 180.0
    tle.raan = float(line2[17:25].strip()) * math.pi / 180.0
    tle.arg_perigee = float(line2[34:42].strip()) * math.pi / 180.0
    tle.mean_anomaly = float(line2[43:51].strip()) * math.pi / 180.0
    tle.mean_motion = float(line2[52:63].strip()) * 2 * math.pi / 1440.0

    return tle      