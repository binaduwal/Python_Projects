import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier

number=input("Enter phone number  and country code:")
phoneNumber=phonenumbers.parse(number)

timeZone=timezone.time_zones_for_number(phoneNumber)
print("TimeZone:",timeZone)

geolocation=geocoder.description_for_number(phoneNumber,"en")
print("Location:",geolocation)

service_provider=carrier.name_for_number(phoneNumber,"en")
print("Service Provider:",service_provider)
