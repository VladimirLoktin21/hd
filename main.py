import os
import random
import discord
from discord.ext import commands
import requests


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'Пока :( {bot.user}!')    

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')    

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

@bot.event
async def on_ready():
    print(f'Бот {bot.user} успешно запущен!')


@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('photos'))
    with open(f'photos/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def my_mem(ctx):
    img_name = random.choice(os.listdir('photos'))
    
    if img_name == '5454be867af9b6db37cf7a83d50d7cb2':
        await ctx.send("Here's my custom meme!")
    else:
        with open(f'photos/{img_name}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
@bot.command()
async def mem(ctx, category=None):
    if category is None:
       
        img_name = random.choice(os.listdir('photos'))
    else:
       
        category_dir = os.path.join('photos', category)
        if os.path.exists(category_dir) and os.path.isdir(category_dir):
            img_name = random.choice(os.listdir(category_dir))
        else:
            await ctx.send(f'Категория "{category}" не существует.')
            return

    with open(os.path.join('photos', category, img_name), 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


bot.run("MTE0NDk2MDA4OTk1OTE5MDY2OA.GDhHYM.biqBl8M-doZgpj6YPFK858D_hHRVIo7pXNuTUI")
