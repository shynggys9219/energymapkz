from django.shortcuts import render
from .models import *
import folium
import json, os
from energystationsmapkz.settings import BASE_DIR
# Create your views here.
# TO-DO
# Generate map if there were changes otherwise use older map if it exists

def generate_map():
    fuel_types = ['gas', 'wind','coal', 'hydro', 'nuclear', 'pv']

    stations = Station.objects.all()
    with open(f'{BASE_DIR}/main/archive/world-countries.json') as json_data:
        all_countries = json.loads(json_data.read())
    
    for i in all_countries['features']:
        if i['properties']['name'] == "Kazakhstan":
            kaz = i
            break
    with open(f'{BASE_DIR}/main/kz_regions.json') as regions_json:
        kz_regions = json.loads(regions_json.read())

    kz_long_lat = [48.00, 68.00]
    kz_map = folium.Map(location=kz_long_lat,
                    tiles='Stamen Terrain',
                    zoom_start=5, 
                    min_zoom=5)
    folium.GeoJson(kz_regions, name="Kazakhstan").add_to(kz_map)
    folium.LayerControl().add_to(kz_map)
    for station in stations:
        html=f"""
        <h3> {station.station_name}</h3>
        <p>Station details:</p>
        <ul>
            <li>Capacity: {station.station_capacity}</li>
            <li>Fuel: {station.station_fuel} </li>
            <li>Type: {station.station_type} </li>
            <li>Region: {station.station_region} </li>
            <li>Year: {station.station_year} </li>
        </ul>
        </p>
        """
        iframe = folium.IFrame(html=html, width=200, height=300)
        popup = folium.Popup(iframe, max_width=2650)
        icon = folium.CustomIcon(icon_image=f'{BASE_DIR}/main/static/main/{station.station_fuel.lower()}.png', icon_size=(35,35))
        folium.Marker((station.station_location_long, station.station_location_lat),icon=icon, popup=popup).add_to(kz_map)

    kz_map.save(f"{BASE_DIR}/main/templates/main/kz_map_with_energy_stations.html")

def index(request):
    generate_map()
    print(f'{BASE_DIR}/main/archive/')
    return render(request, "main/kz_map_with_energy_stations.html")