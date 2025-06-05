import discord
from discord.ext import commands
import asyncio
import os
from keep_alive import keep_alive  # فقط إذا كنت تستخدم Replit

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

CHANNEL_ID = 1271242142374952970  # ID الروم الذي تريده

@bot.event
async def on_ready():
    print(f"✅ Bot started as {bot.user}")
    
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("🚨 **تنبيه تلقائي:** تم تشغيل البوت بأمان. الرجاء عدم نشر التوكن.")

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

keep_alive()  # إذا لم تستخدم replit احذف هذا السطر

# تشغيل البوت من متغير البيئة الآمن
bot.run(os.getenv("DISCORD_TOKEN"))
