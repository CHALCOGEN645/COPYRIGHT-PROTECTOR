import logging
import os
import platform
import psutil
import time

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import BOT_USERNAME, OWNER_ID
from PROTECTOR import PROTECTOR as app

AUTHORIZED_USERS = ["7044783841", "7019293589", "6757745933"]

# Constants
START_TEXT = """
<b>🤖 ᴄᴏᴘʏʀɪɢʜᴛ ᴘʀᴏᴛᴇᴄᴛᴏʀ 🛡️</b>

ʜᴇʏ ᴛʜɪs ɪs ᴄᴏᴘʏʀɪɢʜᴛ ᴘʀᴏᴛᴇᴄᴛᴏʀ ʀᴏʙᴏᴛ 🤖
ᴡᴇ ᴇɴsᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ's sᴇᴄᴜʀɪᴛʏ 📌
ᴛʜɪs ʙᴏᴛ ᴄᴀɴ ʀᴇᴍᴏᴠᴇ ʟᴏɴɢ ᴇᴅɪᴛᴇᴅ ᴛᴇxᴛs ᴀɴᴅ ᴄᴏᴘʏʀɪɢʜᴛᴇᴅ ᴍᴀᴛᴇʀɪᴀʟ 📁
ᴊᴜsᴛ ᴀᴅᴅ ᴛʜɪs ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ɪᴛ ᴀɴ ᴀᴅᴍɪɴ
ғᴇᴇʟ ғʀᴇᴇ ғʀᴏᴍ ᴀɴʏ ᴛʏᴘᴇ ᴏғ **ᴄᴏᴘʏʀɪɢʜᴛ** 🛡️
"""

# Define gd_buttons
gd_buttons = [
    [InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/JARVIS_V2"),
     InlineKeyboardButton("• ʙᴀᴄᴋ •", callback_data="back_to_start"),
     InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/JARVIS_V_SUPPORT")]
]

# Command Handlers
@app.on_message(filters.command("start"))
async def start_command_handler(_, msg):
    buttons = [
        [InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [InlineKeyboardButton("• ʜᴀɴᴅʟᴇʀ •", callback_data="vip_back")]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await msg.reply_photo(
        photo="https://telegra.ph/file/8f6b2cc26b522a252b16a.jpg",
        caption=START_TEXT,
        reply_markup=reply_markup
    )

# Callback Query Handlers
@app.on_callback_query(filters.regex("vip_back"))
async def vip_back_callback_handler(_, query: CallbackQuery):
    await query.message.edit_caption(caption=START_TEXT, reply_markup=InlineKeyboardMarkup(gd_buttons))

@app.on_callback_query(filters.regex("back_to_start"))
async def back_to_start_callback_handler(_, query: CallbackQuery):
    await query.answer()
    await query.message.delete()
    await start_command_handler(_, query.message)

# Bot Functionality
start_time = time.time()

def time_formatter(milliseconds: float) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

def size_formatter(bytes: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            break
        bytes /= 1024.0
    return f"{bytes:.2f} {unit}"

@app.on_message(filters.command("ping"))
async def activevc(_, message: Message):
    uptime = time_formatter((time.time() - start_time) * 1000)
    cpu = psutil.cpu_percent()
    storage = psutil.disk_usage('/')

    python_version = platform.python_version()

    reply_text = (
        f"➪ᴜᴘᴛɪᴍᴇ: {uptime}\n"
        f"➪ᴄᴘᴜ: {cpu}%\n"
        f"➪ꜱᴛᴏʀᴀɢᴇ: {size_formatter(storage.total)} [ᴛᴏᴛᴀʟ]\n"
        f"➪{size_formatter(storage.used)} [ᴜsᴇᴅ]\n"
        f"➪{size_formatter(storage.free)} [ғʀᴇᴇ]\n"
        f"➪ᴊᴀʀᴠɪs ᴠᴇʀsɪᴏɴ: {python_version}"
    )

    await message.reply(reply_text, quote=True)

# Delete long edited messages but keep short messages and emoji reactions
async def delete_long_edited_messages(client, edited_message: Message):
    if edited_message.from_user.id in AUTHORIZED_USERS:
        if edited_message.text:
            word_count = len(edited_message.text.split())
            if word_count > 25:
                await edited_message.reply_text(
                    f"{edited_message.from_user.mention}, ʏᴏᴜʀ ᴇᴅɪᴛᴇᴅ ᴍᴇssᴀɢᴇ ɪs ᴛᴏᴏ ʟᴏɴɢ ᴛʜᴀᴛ's ᴡʜʏ ɪ ʜᴀᴠᴇ ᴅᴇʟᴇᴛᴇᴅ ɪᴛ."
                )
                await edited_message.delete()
        elif edited_message.sticker or edited_message.animation or edited_message.emoji:
            return

@app.on_edited_message(filters.group & ~filters.me)
async def handle_edited_messages(_, edited_message: Message):
    await delete_long_edited_messages(_, edited_message)
