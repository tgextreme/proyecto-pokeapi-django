from django.shortcuts import render
import requests
from urllib.parse import urlencode
from urllib.parse import quote
from urllib.parse import urlencode
import urllib
import urllib.parse
from urllib.parse import unquote

def urldecode(s):
    return unquote(s)


# Create your views here.
def index(request):
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')
    pokemons = response.json()['results']
    poke2=[]
    i=0
    for pokemon in pokemons:
        print("Antes:", pokemon['url'])
        pokemon['url'] = urllib.parse.quote(pokemon['url'], safe='')
        print("Después:", pokemon['url'])
        poke2.append(pokemon)
        i=i+1


    return render(request, 'index.html', {'pokemons': poke2})
def pokemon_detail(request):
    url = request.GET.get('url', '')
    if url:
        response = requests.get(url)
        data = response.json()
    else:
        data = {}

    return render(request, 'index2.html', {'data': data})