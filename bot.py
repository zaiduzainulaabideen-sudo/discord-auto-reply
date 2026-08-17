import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")


@bot.event
async def on_message(message):
    # Don't reply to itself
    if message.author == bot.user:
        return

    msg = message.content.lower().strip()

    # Auto-reply
    if msg in ["hi", "hii", "hello", "hey", "help"]:
        await message.channel.send(
            "Hii! I'm Zaidu Sir's bot 🤖\n"
            "I'm here to help you with anything related to our game, Street Owners.\n"
            "How may I help you?"
        )

    await bot.process_commands(message)


bot.run(os.getenv("DISCORD_TOKEN"))
