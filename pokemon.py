import api

def PokemonCard(list, getPokemon):
    pokemons = []
    all = list
    if getPokemon == 'url':
        for p in all:
            result = api.getPokemonsURL(p['url'])
            pokemons.append({ 
                'id' : result['id'],
                'name' : p['name'], 
                'url' : p['url'] ,
                'img' : result['sprites']['other']['home']['front_default'],
                'types': result['types']})
    elif getPokemon == 'name':
        for p in all:
            result = api.getPokemonsName(p)
            pokemons.append({ 
                'id' : result['id'],
                'name' : result['name'],
                'img' : result['sprites']['other']['home']['front_default'],
                'types' : result['types']})
    return pokemons
