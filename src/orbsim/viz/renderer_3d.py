from orbsim._core import Geographic
import plotly.graph_objects as go

def render_ground_track(list_of_geographic_points: list[Geographic]):
    #extract latitudes and longitudes from the list of Geographic points
    latitudes_degrees = [point.latitude_degrees for point in list_of_geographic_points]
    longitudes_degrees = [point.longitude_degrees for point in list_of_geographic_points]

    # Create a 3D scatter plot of the ground track
    fig = go.Figure(data=[go.Scattergeo(
        lon = longitudes_degrees,
        lat = latitudes_degrees,
        mode = 'lines+markers',
        line = dict(width=2, color='blue'),
        marker = dict(size=4, color='red')
    )])
    fig.update_layout(title='Satellite Ground Track', geo=dict(projection_type='orthographic'))
    fig.show()
