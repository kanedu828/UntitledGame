import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()

PRODUCTION = os.getenv('PRODUCTION')
if PRODUCTION == 'False':
    TOKEN = os.getenv('TOKEN_DEVELOPMENT')
    client = commands.Bot(command_prefix='-')
else:
    TOKEN = os.getenv('TOKEN')
    client = commands.Bot(command_prefix=';')

client.remove_command('help')

extensions = [

]

def check_if_me(ctx):
    return ctx.message.author.id == 124668192948748288

@client.command()
@commands.check(check_if_me)
async def load(ctx, extension):
    try:
        client.load_extension(extension)
        await ctx.send(f'{extension} successfully loaded')
        print(f'{extension} successfully loaded')
    except Exception as exception:
        await ctx.send(f'{extension} cannot be loaded. [{exception}]')
        print(f'{extension} cannot be loaded. [{exception}]')

@client.command()
@commands.check(check_if_me)
async def unload(ctx, extension):
    try:
        client.unload_extension(extension)
        await ctx.send(f'{extension} successfully unloaded')
        print(f'{extension} successfully unloaded')
    except Exception as exception:
        await ctx.send(f'{extension} cannot be unloaded. [{exception}]')
        print(f'{extension} cannot be unloaded. [{exception}]')

@client.command()
@commands.check(check_if_me)
async def reload(ctx, extension):
    try:
        client.reload_extension(extension)
        await ctx.send(f'{extension} successfully reloaded')
        print(f'{extension} successfully reloaded')
    except Exception as exception:
        await ctx.send(f'{extension} cannot be reloaded. [{exception}]')
        print(f'{extension} cannot be reloaded. [{exception}]')

@client.event
async def on_ready():
    print("Bot is ready")

    game = discord.Game('Hello World!')
    await client.change_presence(activity=game)

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
            print(f'{extension} successfully loaded')
        except Exception as exception:
            print(f'{extension} cannot be loaded. [{exception}]')
    client.run(TOKEN)
