import phonenumbers
from phone_num import phone_num
from phonenumbers import geocoder,carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium


pep_num = phonenumbers.parse(phone_num)
location = geocoder.description_for_number(pep_num, "en")
print(location)

service_provider = phonenumbers.parse(phone_num)
print(carrier.name_for_number(service_provider,"en"))

key = ""
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
# print(results)

lat= results[5]['geometry']['lat']
lng= results[1]['geometry']['lng']
print(lat,lng)

area_map = folium.Map(location=[lat,lng],zoom_start = 9)
folium.Marker([lat,lng],popup = location).add_to(area_map)
area_map.save("area_map.html")



