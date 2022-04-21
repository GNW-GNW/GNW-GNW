import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input("Enter your number :")

phone = phonenumbers.parse(number)

time = timezone.time_zones_for_number(phone)

Provider_name = carrier.name_for_number(phone, "en")

Region = geocoder.description_for_number(phone, "en")

print(time)
print(Provider_name)
print(Region)