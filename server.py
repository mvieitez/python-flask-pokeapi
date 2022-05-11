from flask import Flask, request, redirect, url_for, session, jsonify
from flask import render_template
import api
import pokemon as modelPokemon

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    limit = 15
    offset = 0
    session['page'] = 1
    page = 1
    listPokemons = api.allPokemons(limit,offset)
    totalPage = round(int(listPokemons['count']) / int(limit))
    pokemons = modelPokemon.PokemonCard(listPokemons['results'], getPokemon='url')
    return render_template('content/home.html', title='Inicio', pokemons=pokemons, page=page, totalPage=totalPage)



@app.route('/page', methods=['GET', 'POST'])
def page():
    limit = 15
    offset = 0
    page = session['page']
    if request.method == 'POST':
        if request.form['type'] == 'prev':
            datos =  'prev'
            page = request.form['page']
            page = int(page) - 2
            offset = int(limit) * int(page)
            page = int(page) + 1
        if request.form['type'] == 'next':
            page = request.form['page']
            datos = 'next'
            offset = int(limit) * int(page)
            page = int(page) + 1
    session['page'] = page
    listPokemons = api.allPokemons(limit,offset)
    totalPage = round(int(listPokemons['count']) / int(limit))
    pokemons = modelPokemon.PokemonCard(listPokemons['results'], getPokemon='url')
    return render_template('content/listPokemon.html', pokemons=pokemons, page=page, totalPage=totalPage)

@app.route('/pokemon/<id>', methods=['GET', 'POST'])
def pokemon(id):
    data = api.getPokemonsID(id)
    return render_template('content/pokemon.html', data=data)


@app.route("/search",methods=["GET"])
def search():
    result = []
    results = []
    if request.method == 'GET':
        json = api.allPokemons(1126,0)
        for p in json['results']:
            result.append(p['name'])
        search = request.args.get('pokemon').lower()
        for s in result:
            if s.startswith(search):
                results.append(s)
        pokemons = modelPokemon.PokemonCard(results, getPokemon='name')
    return render_template('content/search.html',pokemons = pokemons, result=results)

if __name__ == '__main__':
    app.secret_key = 'ezMJ5laLz2'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run(port=8083)
