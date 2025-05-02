import phonenumbers
from phonenumbers import geocoder
from phone import number
import folium
from opencage.geocoder import OpenCageGeocode

key = "bb0be954827d46dfb86cc273b3ea754c"
opencage_geocoder = OpenCageGeocode(key)

# Telefon raqami bo'yicha ma'lumot olish
number = input("Enter the phone number with country code (e.g., +998939351721): ")
if not number.startswith("+"):
    print("Please enter a valid phone number with country code.")
    exit()

check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")  # To'g'ri obyektdan foydalanildi
print(f"Number: {number}")
print(f"Location: {number_location}")

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(f"Service Provider: {carrier.name_for_number(service_provider, 'en')}")

query = str(number_location)
result = opencage_geocoder.geocode(query)  # OpenCageGeocode obyekti to'g'ri ishlatilmoqda

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(f"Latitude: {lat}, Longitude: {lng}")

mylocation = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=number_location).add_to(mylocation)
mylocation.save("location.html")

# Qo'shimcha funksiya: Latitude va Longitude bo'yicha manzilni aniqlash
def get_location_from_coordinates(lat, lng):
    result = opencage_geocoder.reverse_geocode(lat, lng)
    if result:
        location = result[0]['formatted']
        print(f"The location for Latitude: {lat}, Longitude: {lng} is: {location}")
        return location
    else:
        print("Could not find the location for the given coordinates.")
        return None

# Latitude va Longitude kiritish
latitude = float(input("Enter Latitude: "))
longitude = float(input("Enter Longitude: "))
get_location_from_coordinates(latitude, longitude)