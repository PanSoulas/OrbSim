from orbsim._core import TLEElements
from datetime import datetime
import math

def datetime_to_jd(dt: datetime) -> float:
    Julian_date = 367 * dt.year - int(7 * (dt.year + int(dt.month + 9) // 12) // 4) + int(275 * dt.month // 9) + dt.day + 1721013.5 + (dt.hour + dt.minute / 60 + dt.second / 3600) / 24
    return Julian_date

def delta_minutes_from_epoch(date_time: datetime, epoch: TLEElements) -> float:
    return (datetime_to_jd(date_time) - epoch.epoch_jd) * 1440

def datetime_to_gst(dt: datetime) -> float:
    jd = datetime_to_jd(dt)
    gst = 2 * math.pi * (0.7790572732640 + 1.00273781191135448 * (jd - 2451545.0))
    return gst