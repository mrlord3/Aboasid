import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZelzalMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZelzalMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["ابو اسد","المطور"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/63773e96ac6a68d9b460e.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪𓏺 𝖠𝖻𝗈 𝖠𝗌𝗂𝖽 .
◉ 𝚄𝚂𝙴𝚁 : ❪ @L_B_J ❫
◉ 𝙸𝙳      : ❪ 6985244785 ❫
◉ 𝙱𝙸𝙾    : ❪ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 : @lNooRxl • ❫""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "• 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 •", url=f"https://t.me/L_B_J"),
            ]
        ]
         ),
     )
  
