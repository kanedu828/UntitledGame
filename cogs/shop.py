import discord
from discord.ext import commands
import random
from util.unit_directory import unit_list, Rarity

class Shop(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name = 'pull')
    async def pull(self, ctx, amount=1):
        def random_unit(rarity):
            possible_units = [key for key, value in unit_list.items() if value['rarity'] == rarity]
            pulled_unit_id = random.choice(possible_units)
            return pulled_unit_id
        rarity_odds = random.randint(0, 100)
        if rarity_odds <= 10:
            rarity = Rarity.LEGENDARY
        elif rarity_odds <= 30:
            rarity = Rarity.EPIC
        elif rarity_odds <= 100:
            rarity = Rarity.RARE
        unit_name = unit_list[random_unit(rarity)]['unit'].name
        await ctx.send(f"You got a {unit_name}")

def setup(client):
    client.add_cog(Shop(client))
