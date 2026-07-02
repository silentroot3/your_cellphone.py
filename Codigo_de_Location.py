import phonenumbers
import folium
from phonenumbers import geocoder
#MENU

# print("                                                                                                                  n\")
print(" ██    ██  ██████  ██    ██ ██████       ██████ ███████ ██      ██      ██████  ██   ██  ██████  ███    ██ ███████ ")
print("  ██  ██  ██    ██ ██    ██ ██   ██     ██      ██      ██      ██      ██   ██ ██   ██ ██    ██ ████   ██ ██      ")
print("   ████   ██    ██ ██    ██ ██████      ██      █████   ██      ██      ██████  ███████ ██    ██ ██ ██  ██ █████   ")
print("    ██    ██    ██ ██    ██ ██   ██     ██      ██      ██      ██      ██      ██   ██ ██    ██ ██  ██ ██ ██      ")
print("    ██     ██████   ██████  ██   ██      ██████ ███████ ███████ ███████ ██      ██   ██  ██████  ██   ████ ███████ ")
print("                                                                                                                   ")
print("                                                     bySilentRoot                                                 \n")




number = input("\nIntroduzca el numero:")
# key = input("\nCOLOCA LA KEY:")
# Key = 'E67DI9xfAEJyRGRPxn71RoO9LkdOrdzj'   ##LA KEY ES CONVENIENTE CAMBIARLA 

sanNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(sanNumber, "en")
print(yourLocation)

##Obtiene el servicio del proovedor  
from phonenumbers import carrier 
service = phonenumbers.parse(number, "en")
print(carrier.name_for_number(service, "en"))

# Obtiene el servicio del timezone(zona en donde se registra el numero)
from phonenumbers import timezone
zone = phonenumbers.parse(number, "en")
print(timezone.time_zones_for_number(zone))

# Obtine la Geolocalizacion en base a la key que colocamos,que podemos cambiar con ngrok o otro servicio 

from opencage.geocoder import OpenCageGeocode  ##LIBRERIA
print("\n!!!!!!!LA KEY LA PUEDES CONSEGUIR EN (opencagedata.com)!!!!!!!!\n")
Key = input("\nCOLOCA LA KEY:")   
print("ESTA ES TU KEY:",Key)
# Key = 'E67DI9xfAEJyRGRPxn71RoO9LkdOrdzj'
geocoder = OpenCageGeocode(Key)

query = str(yourLocation)

results = geocoder.geocode(query)

print(results)

lat = results[0]['geometry']['lat']     ##LATITUD

lng = results[0]['geometry']['lng']    ##LONGUITUD

print(lat,lng)  

##El folium se utiliza para colocar la Latitud y Longuitud en un map para posteriormente crear un archivo html

myMap = folium.Map(Location=[lat,lng], zoom_start = 9)


folium.Marker([lat,lng],popup = yourLocation).add_to(myMap)     ##donde se guarda es en myMAP

##guarda el mapa en un archivo HTML

myMap.save("LOCATION_MY_NUMBER.html")

print("\n\n A concluido el proceso...\n\n") 
print("\n\n puede proceder a buscar el archivo html en su equipo, normalmente esta donde se ejecuta el programa :) \n\n")
print("\n\nCabe aclarar que tiene el nombre de LOCATION_MY_NUMBER.HTML\n\n")
print("Busca en esta direccion ↓   :)")
input("PRESIONA CUALQUIER TECLA PARA SALIR...\n")
