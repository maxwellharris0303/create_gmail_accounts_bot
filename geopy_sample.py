from geopy import GoogleV3
import pretty_errors

place = "22lb Baker Street, London"
location = GoogleV3().geocode(place)

print(location.address)
print(location.location)
print(location)