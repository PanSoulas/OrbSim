import click
from orbsim.core import Satellite
from orbsim.analysis.ground_track import compute_ground_track
from orbsim.viz.renderer_3d import render_ground_track
from datetime import datetime, timedelta
from orbsim.core.tle import parse_tle
from orbsim.core.tle import fetch_tle

@click.group()
def cli():
    pass

@cli.command()
@click.option('--tle', default = None, help='TLE string or file path')
@click.option('--duration', default=90.0, help='Duration in minutes')
@click.option('--step', default=1.0, help='Step size in minutes')
@click.option('--satellite', default=None, help='Satellite name to fetch from CelesTrak')
def simulate(tle, satellite, duration, step):
    #read TLE from file if path is provided
    if satellite:
        parsed_tle = fetch_tle(satellite)
    elif tle:
        with open(tle, 'r') as f:
            tle_string = f.read()
        parsed_tle = parse_tle(tle_string)
    else:
        raise click.UsageError("Provided neither TLE nor Satellite")
    
    sat = Satellite("unknown", 0, parsed_tle)
    start_time = datetime.utcnow()
    end_time = start_time + timedelta(minutes=duration)
    step_minutes = step
    ground_track = compute_ground_track(sat, start_time, end_time, step_minutes)
    render_ground_track(ground_track)