import os
import requests
import json

os.system("clear")

url_pokeapi = 'https://pokeapi.co/api/v2/pokemon/'
lista_pokemon = ['bulbasaur', 'squirtle', 'charmander', 'abra']

def obtener_pokemon(pokemones):
    response = requests.get(url_pokeapi + pokemones)

    data = response.json()
    print(f"Nombre: {data['name']}")
    print(f"Peso: {data['weight']}")

    lista_habilidades = [habilidad['ability']['name'] for habilidad in data['abilities']]

    print(f"Habilidades: {lista_habilidades}")

    dicc_estadistica = {stat['stat']['name']:stat['base_stat'] for stat in data['stats']}

    print(f"Estadisticas: {dicc_estadistica}")

    print("***********" * 2)

for pokemon in lista_pokemon:
    obtener_pokemon(pokemon)
