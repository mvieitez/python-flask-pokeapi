# Pokedex
### _Pokedex básica con Flask_

### Características
- Lista y busca los pokemones consumiendo los datos desde [PokeApi](https://pokeapi.co). 
- Vea los detalles del pokemon que eliga.

##### GET / &rarr; Lista los primeros 15 pokemones 
![Endpoint /](/screenshots/index.png "Index")

##### GET /pokemon/{id} &rarr; Mustra la información del pokemons con id={id}
![Endpoint /pokemon/{id}](/screenshots/pokemon.png "Pokemon/id")

##### GET /search?pokemon={NombrePokemon} &rarr; Lista los resultados que coinciden con el nombre del pokemon que busca 
![Endpoint /](/screenshots/search.png "Search")
