import json

# Leemos el archivo JSON
with open("teams.json") as archivo_json:
    teams = json.load(archivo_json)


#Damos la bienvenida a la aplicacion
print("Bienvenido a la aplicacion de la liga mexicana")
