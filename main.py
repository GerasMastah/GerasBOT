from __future__ import unicode_literals
##from youtube_dl import YoutubeDL    ##Music
from discord.ext.commands import Bot
##from giphy_client.rest import ApiException
from discord.ext import commands
##from discord import FFmpegPCMAudio
##from discord.utils import get
##from discord.voice_client import VoiceClient
##import random         ##gifs
import asyncio
##import requests           ##gifs
##import youtube_dl           ##Music
##import discord, time    ##Music
##import giphy_client       ##gifs
##import subprocess
##import urllib.request      ##Music
##import re                  ##Music
from music import *
from gifs import *


discord_token = 'TOKEN'

bot = Bot(command_prefix='?')

client = discord.Client()


##Avisa cuando el bot esta listo para usarse despues de iniciarlo.
@bot.event
async def on_ready():
    print("Login as")
    print(bot.user.name)
    print("-------")

@bot.command(aliases=['p', 'play'])
async def _play_song(ctx, search):
    await play_song(ctx, search.replace(' ', '+'))

@bot.command(aliases=['pause', 'pp'])
async def _pause_song(ctx):
    await pause_song(ctx)

@bot.command(aliases=['r', 'resume'])
async def _resume_song(ctx):
    await resume_song(ctx)

@bot.command(aliases=['n', 'next'])
async def _next_song(ctx):
    await next_song()

@bot.command(aliases=['s', 'stop'])
async def _stop(ctx):
    await stop_song(ctx)


@bot.command(aliases=['gif', 'Gif'])
async def _random_gif(ctx, word):
    await random_gif(ctx, word.replace(' ', '+'))
                    
    
@bot.command(aliases=['gfy', 'Gfy'])
async def _gfycat_search(ctx, word):
    await gfycat_search(ctx, word.replace(' ', '+'))


@bot.command(aliases=['ngif', 'nsfw'])
async def _nsfw_gifs(ctx, word):
    await nsfw_gifs(ctx, word.replace(' ', '+'))

    
bot.run(discord_token)
