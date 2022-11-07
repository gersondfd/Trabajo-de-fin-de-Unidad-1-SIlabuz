import json
import requests
def pokemon_generacion():
    for i in range(1,9):
        print(f'{i}. Generacion {i}')
    pg=input("\nIngrese un numero de la lista: ")
    url_Pokeapi_Json = 'https://pokeapi.co/api/v2/'
    url_pokemon = url_Pokeapi_Json+"generation/"+pg+"/"
    data_response = requests.get(url_pokemon)
    data = data_response.json()
    print()
    lista_de_pokemon_generacion=[pokemon['name'] for pokemon in data['pokemon_species'] ] 
    print(lista_de_pokemon_generacion)
    seleccionar_menu(evaluar_menu(mostrar_menu()))
    
def pokemon_forma():
    url_Pokeapi_Json = 'https://pokeapi.co/api/v2/'
    url_cat = url_Pokeapi_Json+"pokemon-shape/"
    data_response2= requests.get(url_cat)
    data2 = data_response2.json()
    listaFormas=[pokemon['name'] for pokemon in data2['results'] ] 
    print("\nLista de formas .\n")
    for i in range(0,(len(listaFormas))):
        print(f"{i+1}. {listaFormas[i]}")
    pf=input("\nElige un numero de la lista: ")
    url_pokemon=url_cat+pf+"/"
    data_response = requests.get(url_pokemon)
    data = data_response.json()
    lista_de_pokemon_forma=[pokemon['name'] for pokemon in data['pokemon_species'] ]
    print()
    print(lista_de_pokemon_forma)
    seleccionar_menu(evaluar_menu(mostrar_menu()))

def pokemon_habilidad():

    url_Pokeapi_Json = 'https://pokeapi.co/api/v2/'
    url_parametros = url_Pokeapi_Json+'ability/?offset=0&limit=327'
    url_cat = url_Pokeapi_Json+"ability/"
    data_response2= requests.get(url_parametros)
    data2 = data_response2.json()
    listahabilidades=[pokemon['name'] for pokemon in data2['results'] ] 
    print("\nLista de formas.\n")
    for i in range(0,(len(listahabilidades))):
        print(f"{i+1}. {listahabilidades[i]}")
    ph=input("\nElige un numero de la lista: ")

    if int(ph)>267:
        ph2=int(ph)+9733
        url_pokemon=url_cat+str(ph2)+"/"
        data_response = requests.get(url_pokemon)
        data = data_response.json()
        lista_de_pokemon_habilidad=[pokemon['pokemon']['name'] for pokemon in data['pokemon']]
        print("\nPokeApi aún se encuentra recopilando esta información.")

    else:

        url_pokemon=url_cat+ph+"/"
        data_response = requests.get(url_pokemon)
        data = data_response.json()
        lista_de_pokemon_habilidad=[pokemon['pokemon']['name'] for pokemon in data['pokemon']] 

    print()
    print(lista_de_pokemon_habilidad)
    seleccionar_menu(evaluar_menu(mostrar_menu()))

def pokemon_habitat():
    
    url_Pokeapi_Json = 'https://pokeapi.co/api/v2/'
    url_cat = url_Pokeapi_Json+'pokemon-habitat/'
    data_response2= requests.get(url_cat)
    data2 = data_response2.json()
    listahabitats=[pokemon['name'] for pokemon in data2['results'] ] 
    print("\nLista de habitats.\n")
    for i in range(0,(len(listahabitats))):
        print(f"{i+1}. {listahabitats[i]}")
    ph2=input("\nElige un numero de la lista: ")
    url_pokemon=url_cat+ph2+"/"
    data_response = requests.get(url_pokemon)
    data = data_response.json()
    lista_de_pokemon_habitat=[pokemon['name'] for pokemon in data['pokemon_species']]
    print()
    print(lista_de_pokemon_habitat)
    seleccionar_menu(evaluar_menu(mostrar_menu()))

def pokemon_tipo():

    url_Pokeapi_Json = 'https://pokeapi.co/api/v2/'
    url_cat = url_Pokeapi_Json+'type/'
    data_response2= requests.get(url_cat)
    data2 = data_response2.json()
    listatipos=[pokemon['name'] for pokemon in data2['results'] ] 
    print("\nLista de tipos.\n")
    for i in range(0,(len(listatipos))):
        print(f"{i+1}. {listatipos[i]}")
    pt=input("\nElige un numero de la lista: ")

    if int(pt)>18:
        pt2=int(pt)+9982
        url_pokemon=url_cat+str(pt2)+"/"
        data_response = requests.get(url_pokemon)
        data = data_response.json()
        lista_de_pokemon_tipo=[pokemon['pokemon']['name'] for pokemon in data['pokemon']]
        print("\nPokeApi aún se encuentra recopilando esta información.")
    else:
        url_pokemon=url_cat+pt+"/"
        data_response = requests.get(url_pokemon)
        data = data_response.json()
        lista_de_pokemon_tipo=[pokemon['pokemon']['name'] for pokemon in data['pokemon']]

    print()
    print(lista_de_pokemon_tipo)
    seleccionar_menu(evaluar_menu(mostrar_menu()))

def mostrar_menu():
     return input('\n\nPokeApi\n\nMenú de Opciones\n\n1: Listar pokemons por generación.\n2: Listar pokemons por forma.\n3: Listar pokemons por habilidad.\n4: Listar pokemons por habitat.\n5: Listar pokemons por tipo.\n\nIngrese un número de la lista: ')

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

def seleccionar_menu(a):
    if a==1:
        pokemon_generacion()
    elif a==2:
        pokemon_forma()
    elif a==3:
        pokemon_habilidad()
    elif a==4:
        pokemon_habitat()
    elif a==5:
        pokemon_tipo()
    else:
        print("No disponible")

seleccionar_menu(evaluar_menu(mostrar_menu()))