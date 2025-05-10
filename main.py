from pyrogram import Client
from pyrogram.handlers import MessageHandler
import os

app = Client("musicbot",
             api_id=int(os.environ["API_ID"]),
             api_hash=os.environ["API_HASH"],
             bot_token=os.environ["BOT_TOKEN"])

@app.on_message()
async def start(client, message):
    await message.reply("Music bot is online!")

app.run()
