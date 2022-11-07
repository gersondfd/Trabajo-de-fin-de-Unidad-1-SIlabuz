import json
import requests
def pokemon_generacion():
    url_Pokeapi_Json = 'https://pokeapi.co/api/v2/'
    url_pokemon = url_Pokeapi_Json+"generation/1/"
    data_response = requests.get(url_pokemon)
    data = data_response.json()
    lista_de_pokemon_generacion=[pokemon['name'] for pokemon in data['pokemon_species'] ] 
    print(lista_de_pokemon_generacion)
    
def pokemon_forma():
    url_Pokeapi_Json = 'https://pokeapi.co/api/v2/'
    url_pokemon = url_Pokeapi_Json+"/pokemon-shape/6/"
    data_response = requests.get(url_pokemon)
    data = data_response.json()
    lista_de_pokemon_forma=[pokemon['name'] for pokemon in data['pokemon_species'] ] 
    print(lista_de_pokemon_forma)

def pokemon_habilidad():
    url_Pokeapi_Json = 'https://pokeapi.co/api/v2/'
    url_pokemon = url_Pokeapi_Json+"ability/1/"
    data_response = requests.get(url_pokemon)
    data = data_response.json()
    lista_de_pokemon_habilidad=[pokemon['pokemon']['name'] for pokemon in data['pokemon'] ] 
    print(lista_de_pokemon_habilidad)

def pokemon_habitat():
    url_Pokeapi_Json = 'https://pokeapi.co/api/v2/'
    url_pokemon = url_Pokeapi_Json+"pokemon-habitat/1/"
    data_response = requests.get(url_pokemon)
    data = data_response.json()
    lista_de_pokemon_habitat=[pokemon['name'] for pokemon in data['pokemon_species']]
    print(lista_de_pokemon_habitat)

def pokemon_tipo():
    url_Pokeapi_Json = 'https://pokeapi.co/api/v2/'
    url_pokemon = url_Pokeapi_Json+"type/1/"
    data_response = requests.get(url_pokemon)
    data = data_response.json()
    lista_de_pokemon_tipo=[pokemon['pokemon']['name'] for pokemon in data['pokemon']] 
    print(lista_de_pokemon_tipo)

def evaluar_menu(a):
    try:
    
        b=int(a)
        if 1<=b and b<=5:
            return b
        else:
            print("\nError. Por favor, ingrese un numero de la lista.\n")
            evaluar_menu(mostrar_menu())
    except ValueError:
        print("\nError. Por favor, ingrese un numero de la lista.\n")
        evaluar_menu(mostrar_menu()) 

def mostrar_menu(a):
    a=input('PokeApi\n\nMenú de Opciones\n\n1: Listar pokemons por generación.\n2: Listar pokemons por forma.\n3: Listar pokemons por habilidad.\n4: Listar pokemons por habitat.\n5: Listar pokemons por tipo.\n\nIngrese un número de la lista: ')
evaluar_menu(mostrar_menu())

