
# konvertē datu mērvienības
def megabyte_to_megabit(megabyte):
    result = megabyte * 8
    return result

# saskaiti degvielas patēriņu uz 100 km
def fuel_consumption(litres, kilometers):
    koef=100/kilometers
    result = litres * koef
    return result

# konvertē temperatūru
def celsius_to_fahrenheit(celsius):
    result = int(celsius*9/5+32)
    return result

# saliec visus skaitļus pirms dota skaitļa (izmanto for)
def sigma(tail):
    result = 0
    for x in range(tail+1):
        result += x
        
    return result

# nokonvertē svaru uz tuvāko mērvienību - grams, kilograms, tonna (izmanto if)
def weight(grams):
    a = len(str(grams))
    if a <4 and a >=1:
        result = grams
        return str(result) + "g"

    if a >= 4 and a < 7:
        result = int(grams / 1000)
        return str(result) + "kg"
    
    if a >= 7:
        result = int(grams / 1000000)
        return str(result) + "t"


mode = str(input("Choose mode(MG; FC; CF; S; W): "))

if mode == "MG": 
    megabyte = int(input("Enter the amount of megabytes: "))
    print(megabyte_to_megabit(megabyte))

elif mode == "FC": 
    litres = int(input("Enter the amount of fuel: "))
    kilometers = int(input("Enter the amount of km: "))

    print(fuel_consumption(litres, kilometers))

elif mode == "CF": 
    celsius = int(input("Enter the temperature in celsius: "))
    print(celsius_to_fahrenheit(celsius))

elif mode == "S": 
    tail = int(input("Enter the tail: "))
    print(sigma(tail))

elif mode == "W": 
    grams = int(input("Enter tha amount in grams: "))
    print(weight(grams))