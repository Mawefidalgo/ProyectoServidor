import json;

# Leemos el archivo JSON
with open("teams.json") as archivo_json:
    teams = json.load(archivo_json)

#Procesar y almacenar en listas de datos

equipos = teams.get('equipos', []) #lista equipos

print("equipos:")
for equipo in equipos:
    print(f"Name: {equipo['name']}, label: {equipo['label']}")