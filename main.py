import discord
import dotenv
import os

token = os.environ['token']
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}!")

@bot.slash_command(guild_ids=[your, guild_ids, here])
async def hello(ctx):
    await ctx.respond("Hello!")

bot.run(token)
