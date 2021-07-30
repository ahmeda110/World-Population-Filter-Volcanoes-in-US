import pandas as pd
import json as JSON
import folium
import webbrowser

df = pd.read_csv("Volcanoes.txt")
df = df.loc[: , ['NAME', 'ELEV', 'LAT', 'LON']]
lat, lng, elev, name = (df["LAT"], df["LON"],
  df["ELEV"], df["NAME"])

my_map = folium.Map(location = [lat.mean(), lng.mean()], zoom_start = 4,
  tiles = 'OpenStreetMap')

def marker_color(e):
  lowest, step = (int(min(elev)), int((max(elev) - min(elev)) / 3))
if e in range(lowest, lowest + step):
  return 'green'
elif e in range(lowest + step, lowest + step * 2):
  return 'yellow'
else :
  return 'red'

fgv = folium.FeatureGroup(name = "Volcanoes", control = True)
fgp = folium.FeatureGroup(name = "Population", control = True)

fgp.add_child(folium.GeoJson(data = JSON.load(open('world.json', 'r', encoding = 'utf-8-sig')),
  style_function = lambda i: {
    'fillColor': 'green'
    if i['properties']['POP2005'] < 10000000
    else 'yellow'
    if 10000000 <= i['properties']['POP2005'] < 20000000
    else 'red'
  }))

for lat, lng, el, name in zip(list(lat), list(lng), list(elev), list(name)):
  iframe = folium.IFrame(html = ""
    "
    Volcano name: < br >
    <
    a href = "https://www.google.com/search?q=%%22%s%%22"
    target = "_blank" > % s < /a><br>
    Height: % s m ""
    " % (name, name, el), width=200, height=75)

    fgv.add_child(folium.CircleMarker(location = (lat, lng), radius = 9, fill_color = marker_color(el),
      fill_opacity = 0.5, color = 'grey', popup = folium.Popup(iframe)))

    my_map.add_child(fgp) my_map.add_child(fgv) my_map.add_child(folium.LayerControl()) my_map.save("index.html")

    webbrowser.open(
      "http://localhost:63342/pythonProject1/index.html?_ijt=qeinsdugfgld9k31e9tjsof94h"
    )
