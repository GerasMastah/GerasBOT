import urllib.request
import re
import discord, time
import youtube_dl
from youtube_dl import YoutubeDL
from discord import FFmpegPCMAudio
from discord.utils import get
from discord.voice_client import VoiceClient
##############Music Bot#######################
queue = []

##'''Realiza busquedas en YouTube, unicamente con una parametro aceptado.'''
def yt_search(query):


    if query.startswith('https'):


        return query

    else:
    
        query = query.replace(' ', '+')

        ##'''Recibe el parametro (search) y lo agrega al link de busqueda de YT, posteriormente realiza un GET a el link compuesto. 
    ##    Hace un regex al html obtenido y unicamente obtiene el ID del primer video resultado de la busqueda'''
        
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + query)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())


    ##    '''Asigna el URL a una variable para mejor manejo'''
        url = 'https://www.youtube.com/watch?v=' + video_ids[0]
        return url


def get_video_url(url):
    ##    '''Obtiene la informacion del video seleccionado utilizando la (url) y extrae el enlace .mp4 con mayor calidad disponible y lo almacena
    ##    en (url2) '''
    ydl = YoutubeDL()
    r = ydl.extract_info(url, download=False)
    url_mp4 = [r][0]['formats'][(len([r][0]['formats'])-1)]['url']
    ##    print([r][0]['formats'][(len([r][0]['formats'])-1)])

    return url_mp4

    
    

async def play_song(ctx, search):

##'''Identifica en que canal de voz esta el usuario invocador y entra en el mismo chat de voz.
##Reproduciendo el audio del .mp4 en (url2) '''
    channel = ctx.message.author.voice.channel
    global player
    try:
        player = await channel.connect()
    except:
        pass
    SongPlaying = ctx.voice_client.is_playing()
    Paused = ctx.voice_client.is_paused()
    if SongPlaying == False and Paused == False:
        try:
            if search.startswith('https'):
                
                await ctx.send('> **Esta va para mis compas color cecina!** ' + search )
                player.play(discord.FFmpegPCMAudio(get_video_url(yt_search(search))))

            else:
                await ctx.send('> **Para la raza piel de bronce!** ' + yt_search(search) )
        
                player.play(discord.FFmpegPCMAudio(get_video_url(yt_search(search))))
        except DownloadError as e:
            player.play(discord.FFmpegPCMAudio(get_video_url(yt_search(search))))
    
    if SongPlaying == True or Paused == True:

        await ctx.send('> **Cancion agregada a la cola** ')
        queue.append(get_video_url(yt_search(search)))
        print(len(queue))



async def next_song():
    player.stop()
    player.play(discord.FFmpegPCMAudio(queue[0]))
    queue.pop(0)
    print(len(queue))
    

##'''Detiene la reproduccion de Audio'''

async def stop_song():
    player.stop()


##''Pausa el audio''

async def pause_song(ctx):
    """Pauses currently playing song [Format: %pause]"""
    SongPlaying = ctx.voice_client.is_playing()
    Paused = ctx.voice_client.is_paused()
    if Paused != True:
        ctx.voice_client.pause()
        await ctx.send("> **Se detuvo el dese mi guero!**")
    else:
        if SongPlaying == True:
            await ctx.send("> **Ya me frene! irale bien!!**")
        else:
            await ctx.send("> **Avientame algo primero canijo!**")

##''Reanuda el audio pausado''

async def resume_song(ctx):
    """Resumes a paused song [Format: %resume]"""
    Paused = ctx.voice_client.is_paused()
    if Paused == True:
        ctx.voice_client.resume()
        await ctx.send('> **Disfrute la rolita!!**')
    else:
        await ctx.send('> **Indicacion falsa compita!**')
        

