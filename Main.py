"""
Main dashboard file - manage config, hold dash etc
"""
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import dash_html_components as html
import dash_core_components as dcc
import dash

import mapbox as mymap

import pandas as pd

app = dash.Dash(__name__)
mapbox_access_token = "pk.eyJ1Ijoib2RzbyIsImEiOiJjanVvYWMwdTcxcDdhNDRtaTV0ZzNzMWJjIn0.djtTELOE-wtxGt56HPQecg"

stop_data = r"D:\Dougall\OpenDataStories\Posts\OC_Transpo\google_transit\stops_transitway.txt"


#load the data
df = pd.read_csv(stop_data)

#create lists of lon, lat, marker name
long = df['stop_lon'].tolist()
lat = df['stop_lat'].tolist()
mrk = df['stop_name'].tolist()



# data = [
    # go.Scattermapbox(
        # lat=lat,
        # lon=long,
        # mode='markers',
        # marker=go.scattermapbox.Marker(
            # size=9
        # ),
        # text=mrk,
    # )
# ]

# layout = go.Layout(
    # autosize=True,
    # hovermode='closest',
    # mapbox=go.layout.Mapbox(
        # accesstoken=mapbox_access_token,
        # bearing=0,
        # center=go.layout.mapbox.Center(
            # lat=45.39,
            # lon=-75.68
        # ),
        # pitch=0,
        # zoom=10
    # ),
# )

# fig = go.Figure(data=data, layout=layout)
# plot(fig, filename='Multiple Mapbox')
#py.iplot

app.layout = html.Div([
    html.H1('Transitway Stops'),
    html.Div(id='text-content'),
    dcc.Graph(id='map', figure={
        'data': [{
            'lat': lat,
            'lon': long,
			'mode': 'markers',
			'text':mrk,
            'marker': {
                'size': 8,
                'opacity': 0.6
            },
            'type': 'scattermapbox'
        }],
        'layout': {
            'mapbox': {
                'accesstoken': mapbox_access_token,
				'autosize':True,
				'hovermode': 'closest',
				'bearing': 150,
				'pitch': 60,
				'zoom':10,
				'center': { 'lat':45.37,     # 45.39,
							'lon':-75.68
				}
            }

        }
    })
])
	#mymap.mapboxfigure(lat, long, mrk, mapbox_access_token)
	# go.Figure(
		# layout = go.Layout(
			# autosize=True,
			# hovermode='closest',
			# mapbox=go.layout.Mapbox(
				# accesstoken=mapbox_access_token,
				# bearing=0,
				# center=go.layout.mapbox.Center(
					# lat=45.39,
					# lon=-75.68
				# ),
				# pitch=0,
				# zoom=10
			# ),
		# ),
	
	# data = [
		# go.Scattermapbox(
			# lat=lat,
			# lon=long,
			# mode='markers',
			# hoverinfo="text",
			# text=mrk,
			# marker=go.scattermapbox.Marker(
				# size=9
			# ),
			
		# ),
	# ]),
# ])




if __name__ == '__main__':
    app.run_server(debug=True)