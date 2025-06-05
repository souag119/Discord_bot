import discord
from discord.ext import commands
import asyncio
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

CHANNEL_ID = 1271242142374952970

@bot.event
async def on_ready():
    print(f"✅ Bot started as {bot.user}")

@bot.event
async def on_message(message):
    if message.channel.id != CHANNEL_ID:
        return
    if message.author == bot.user:
        return

    if not message.attachments or not "title" in message.content.lower():
        try:
            await message.delete()
            warn = await message.channel.send(f"{message.author.mention} 🚫 لا يسمح بإرسال الرسائل العشوائية.\nأرفق صورة واكتب `title`.")
            await asyncio.sleep(5)
            await warn.delete()
        except:
            pass

    await bot.process_commands(message)

keep_alive()

# توكن البوت
bot.run("MTM2ODY3OTg0NDA5MDc0NDg5Mg.GGwhrd.maFwJdfhR541TDn8OL5E0RSdGYkcSDouY-ORvc")
