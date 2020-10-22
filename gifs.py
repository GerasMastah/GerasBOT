import giphy_client
import requests
import random
from giphy_client.rest import ApiException

giphy_token = 'TOKEN'
api_instance = giphy_client.DefaultApi() 
#################Random Gifs#######################

##funcion para realizar busquedas de gifs en giphy
async def search_gifs(query):
    try:
        response = api_instance.gifs_search_get(giphy_token, query, limit=100, rating='r')
        lst = list(response.data)
        gif = random.choices(lst)

        return gif[0].url

    except ApiException as e:
        return "Exception when calling DefaultApi->gifs_search_get: %s\n" % e

##'''Realiza una busqueda en Gfycat utiliando el parametro (word)'''

async def random_gif(ctx, word):
    try:
        gif = await search_gifs(word)

    ##    await ctx.send(random.choice(response))
        await ctx.send('sbs Papuh :v' )
        await ctx.send('Gif URL : ' + gif)

    except IndexError as e:
        await ctx.send('No Encontre tu Porqueria!' )

##'''Realiza una busqueda en Gfycat utiliando el parametro (word)'''


async def gfycat_search(ctx, word):
    try:
        url = 'https://api.gfycat.com/v1/gfycats/search?search_text=' + word
        r = requests.get(url)
        data = r.json()

    ##'''Selecciona un gif al azar utilizando la funcion random'''
        gifs = (len(data["gfycats"])-1)
        rnd = random.randint(0,gifs)
        gif = data["gfycats"][rnd]["max2mbGif"]

    ##'''Envia el gif seleccionado en el chat'''
        await ctx.send('sbs Papuh :v' )
        await ctx.send('Gif URL : ' + gif )

    except ValueError as e:
        await ctx.send('No Encontre tu Porqueria!' )


#################NSFW_GIF#######################

##'''Realiza una busqueda en redgifs utiliando el parametro (word)'''


async def nsfw_gifs(ctx, word):
    try:
        url = 'https://api.redgifs.com/v1/gfycats/search?search_text=' + word + '&count=200&start=150'
        r = requests.get(url)
        data = r.json()
        
        gifs = (len(data["gfycats"])-1)
        rnd = random.randint(0,gifs)
        gif = data["gfycats"][rnd]["max2mbGif"]

        await ctx.send('sbs Papuh :v' )
        await ctx.send('Gif URL : ' + gif )

    except ValueError as e:
        await ctx.send('No Encontre tu Porqueria!' )
