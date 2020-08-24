#Developed by MBD
from geopy.distance import geodesic
from functools import partial
from geopy.geocoders import Nominatim

#Definimos las coordenadas de la Ciudad de origen
bsas = (-34.6036844, -58.3815591)
#Variables por default
geolocator = Nominatim(user_agent="test")
geocode = partial(geolocator.geocode, language="es")

#Solicitamos la ciudad destino
d = geocode(input("Ingresa la ciudad destino: "))
#Imprimimos coordenadas de ciudad destino
print(chr(62)*5 + "Coordenadas de la ciudad elegida:",d.latitude, d.longitude)
#Transformamos la ciudad destino a coordenadas para luego calcular la distancia
d = (d.latitude, d.longitude)
location = geolocator.reverse(d)
#Imprimimos la direccion por default de la ciudad elegida
print(chr(62)*5 + "Direccion de la capital:", location.address)
#Imprimimos la distancia hasta la ciudad elegida
print(chr(62)*5 + "Distancia desde Buenos Aires:", geodesic(bsas, d).kilometers, "kms")

#Otras distancias ////////////
santiago = (-33.4488897, -70.6692655)
rio = (-22.9068467, -43.1728965)
asuncion = (-25.2637399, -57.575926)
lima = (-12.0463731, -77.042754)
bogota = (4.7109886, -74.072092)
mont = (-34.9011127, -56.1645314)
print(chr(62)*5 + "Distancias desde Buenos Aires")
print("Hasta Santiago de Chile:", geodesic(bsas, santiago).kilometers, "kms")
print("Hasta Rio de Janeiro:", geodesic(bsas, rio).kilometers, "kms")
print("Hasta Asuncion:", geodesic(bsas, asuncion).kilometers, "kms")
print("Hasta Lima:", geodesic(bsas, lima).kilometers, "kms")
print("Hasta Bogota:", geodesic(bsas, bogota).kilometers, "kms")
print("Hasta Montevideo:", geodesic(bsas, mont).kilometers, "kms")



