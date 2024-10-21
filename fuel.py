mile = 1609.344
gallon = 3.785411784

def liters_100km_to_miles_gallon(litres):
    gallons = litres / gallon
    miles = 100 * 1000 / mile
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    km100 = miles * mile / 1000 / 100
    litres = gallon
    return litres / km100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))