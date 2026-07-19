import click
from orbsim.core import Satellite
from orbsim.analysis.ground_track import compute_ground_track
from orbsim.viz.renderer_3d import render_ground_track
from datetime import datetime, timedelta
from orbsim.core.tle import parse_tle

@click.group()
def cli():
    pass

@cli.command()
@click.option('--tle', required=True, help='TLE string or file path')
@click.option('--duration', default=90.0, help='Duration in minutes')
@click.option('--step', default=1.0, help='Step size in minutes')
def simulate(tle, duration, step):
    #read TLE from file if path is provided
    if tle.endswith('.txt'):
        with open(tle, 'r') as f:
            tle_lines = f.readlines()
            tle = ''.join(tle_lines)
    satellite = Satellite("unknown", 0, parse_tle(tle))
    start_time = datetime.utcnow()
    end_time = start_time + timedelta(minutes=duration)
    step_minutes = step
    ground_track = compute_ground_track(satellite, start_time, end_time, step_minutes)
    render_ground_track(ground_track)