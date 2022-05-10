import requests

API_URL = 'https://pokeapi.co/api/v2/pokemon?limit=10'

def allPokemons(limit, offset):
    reponse = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}')
    return reponse.json()

def getPokemonsURL(url):
    reponse = requests.get(f'{url}')
    return reponse.json()

def getPokemonsID(id):
    reponse = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
    return reponse.json()

def getPokemonsName(name):
    reponse = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
    return reponse.json()

