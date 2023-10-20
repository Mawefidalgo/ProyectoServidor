
import requests

nombrepok=""
numpok=0


print("Hola buenas esta es una aplicacion sobre pokemons")

var=0

def caractPokemon():
     for pokemon in response2.json()["abilities"]:
          print(pokemon["ability"])
          
def nombresPokemons():
        for pokemon in response1.json()["results"]:
            print(pokemon["name"])

def juegospok():
     for pokemon in response3.json()["game_indices"]:
          print(pokemon["version"])
print("Si quieres ver los nombres de un numero determinado de pokemons pulsa el 1.\n"
       "Si quieres ver las habilidades de un pokemon pulsa 2\n"
       "Si quieres ver los nombres de los juegos pokemon pulsa 3\n"
       "Si quieres abandonar la aplicacion pulsa 4")

var=int(input("Indica el numero:"))


while True:


        if(var==1):
            numpok=input("Escribe el numero de pokemons que quieres ver el nombre: ")
            url1="https://pokeapi.co/api/v2/pokemon?limit="+numpok
            response1= requests.get(url1)
            nombresPokemons()

        elif(var==2):
            nombrepok=input("Escribe el nombre del pokemon: ")

            url2="https://pokeapi.co/api/v2/pokemon/"+nombrepok+"/"
            response2=requests.get(url2)
            caractPokemon()

        elif(var==3):
            url3="https://pokeapi.co/api/v2/pokemon/ditto"
            response3=requests.get(url3)
            juegospok()
        elif(var==4):
             print("Has pulsado salir de la aplicacion\n"
            "Muchas gracias por utilizarla")
             break
        else:
             print("El numero introducido no es valido\n"
                   "Intentalo de nuevo")
             
        input("")
        print("Si quieres ver los nombres de un numero determinado de pokemons pulsa el 1.\n"
        "Si quieres ver las habilidades de un pokemon pulsa 2\n"
        "Si quieres ver los nombres de los juegos pokemon pulsa 3\n"
        "Si quieres abandonar la aplicacion pulsa 4")

        var=int(input("Indica el numero:"))

        