import discord
from discord.ext import commands
import random
from util.unit_directory import unit_list, Rarity
import util.dbutil as db

class Shop(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name = 'pull')
    async def pull(self, ctx, amount=1):
        message_embed = discord.Embed(title = 'Unit Pull!')
        def random_unit(rarity):
            possible_units = [key for key, value in unit_list.items() if value['rarity'] == rarity]
            pulled_unit_id = random.choice(possible_units)
            return pulled_unit_id
        rarity_odds = random.randint(0, 100)
        if rarity_odds <= 5:
            rarity = Rarity.LEGENDARY
        elif rarity_odds <= 25:
            rarity = Rarity.EPIC
        elif rarity_odds <= 75:
            rarity = Rarity.RARE
        else:
            essence = random.randint(300, 1000)
            await db.update_user_essence(ctx.author.id, essence)
            message_embed.description = f'{ctx.author.mention} pulled {essence} essence!'
            await ctx.send(embed = message_embed)
            return
        random_unit_id = random_unit(rarity)
        unit_name = unit_list[random_unit_id]['unit'].name
        await db.insert_unit(random_unit_id, ctx.author.id, -1)
        message_embed.description = f'{ctx.author.mention} pulled a {rarity} unit! {unit_name}!'
        await ctx.send(embed = message_embed)

def setup(client):
    client.add_cog(Shop(client))
