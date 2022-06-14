from numpy import MAY_SHARE_BOUNDS
import geocoder as locate
import folium


geo = locate.ip('me')

myAddress = geo.latlng

my_map = folium.Map(location=myAddress, zoom_start=12 )


folium.CircleMarker(location=myAddress, radius=50, popup="Yorkshire").add_to(my_map)
folium.Marker(location=myAddress, radius=50, popup="Yorkshire").add_to(my_map)

my_map.save('view.html')