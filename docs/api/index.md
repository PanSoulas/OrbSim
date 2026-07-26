# API Reference

## orbsim.core

### Satellite
The main class for satellite simulation.

- `Satellite(name, norad_id, tle)` — create a satellite from a `TLEElements` object
- `Satellite.from_tle(name, norad_id, tle_string)` — create a satellite from a raw TLE string
- `propagate(delta_minutes)` — returns a `StateVector` at the given time offset
- `ground_position(delta_minutes, gst)` — returns a `Geographic` position
- `ground_track(duration, step_minutes, gst)` — returns a list of `Geographic` positions

### TLE

- `parse_tle(tle_string)` — parse a 3-line TLE string into a `TLEElements` object
- `fetch_tle(satellite_name)` — fetch a live TLE from CelesTrak by name

### Propagator

- `datetime_to_jd(dt)` — convert a `datetime` to Julian Date
- `datetime_to_gst(dt)` — convert a `datetime` to Greenwich Sidereal Time in radians
- `delta_minutes_from_epoch(dt, tle)` — compute minutes elapsed since TLE epoch

## orbsim.analysis

- `compute_ground_track(satellite, start, end, step_minutes)` — compute a ground track
- `compute_passes(satellite, observer, start, end, min_elevation_deg, step_minutes)` — compute ground station passes
- `compute_conjunctions(sat1, sat2, start, end, step_minutes, threshold_km)` — detect close approaches

## orbsim.viz

- `render_ground_track(positions)` — render a list of `Geographic` positions on a 3D globe

## orbsim._core (C++ extension)

- `TLEElements` — orbital elements struct
- `StateVector` — position and velocity in ECI frame
- `ECEFVector` — position in ECEF frame
- `Geographic` — latitude, longitude, altitude
- `sgp4_propagate(tle, delta_minutes)` — SGP4 propagation
- `eci_to_ecef(state, gst)` — ECI to ECEF conversion
- `ecef_to_geographic(ecef)` — ECEF to geographic conversion