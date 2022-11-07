import json
import requests

url_Pokeapi_Json = 'https://pokeapi.co/api/v2/'

url_pokemon = url_Pokeapi_Json+"/generation/1/"

data_response = requests.get(url_pokemon)

data = data_response.json()

lista_de_pokemon_generacion=[pokemon['name'] for pokemon in data['pokemon_species'] ] 

print(lista_de_pokemon_generacion)