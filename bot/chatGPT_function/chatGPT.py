import discord
import openai
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
bot = commands.Bot(command_prefix='&', intents=intents)

openai.api_key = "YOUR-OPEN-AI-API-GOES HERE"


def run_discord_bot():

    # Discord Bot Token
    token = 'YOUR-BOT-TOKEN-GOES-HERE'

    @bot.command()
    async def gpt(ctx, *args):
        query = " ".join(args)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": query},
                {"role": "user", "content": query},
            ]
        )
        result = ''
        for choice in response.choices:
            result += choice.message.content
        await ctx.send(result)

    bot.run(token)
