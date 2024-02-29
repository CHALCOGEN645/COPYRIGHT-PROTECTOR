from pyrogram import Client, filters
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters
from pyrogram.types import Message
import time
import psutil
import platform
import logging
from config import OWNER_ID, BOT_USERNAME
from config import *
from PROTECTOR import PROTECTOR as app

import pyrogram
from pyrogram.errors import FloodWait

# ----------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------

start_txt = """<b> 🤖 ᴄᴏᴘʏʀɪɢʜᴛ ᴘʀᴏᴛᴇᴄᴛᴏʀ 🛡️ </b>

ʜᴇʏ ᴛʜɪs ɪs ᴄᴏᴘʏʀɪɢʜᴛ ᴘʀᴏᴛᴇᴄᴛᴏʀ ʀᴏʙᴏᴛ🤖!\n ᴡᴇ ᴇɴsᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ sᴇᴄᴜʀɪᴛʏ💻 !\n ᴛʜɪs ʙᴏᴛ ᴄᴀɴ ʀᴇᴍᴏᴠᴇ ʟᴏɴɢ ᴛᴇxᴛ ᴇᴅɪᴛᴇᴅ ᴍsɢs , ᴀɴᴅ ᴄᴏᴘʏʀɪɢʜᴛ ᴍᴀᴛᴇʀɪᴀʟ...!\nᴊᴜsᴛ ᴀᴅᴅ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ᴀᴅᴍɪɴ !!\nғᴇᴇʟ ғʀᴇᴇ ғʀᴏᴍ ᴀɴʏ ᴛʏᴘᴇ ᴏғ ᴄᴏᴘʏʀɪɢʜᴛ... ! 🛡! 🤝🔐 """

@app.on_message(filters.command("rajnishayushilovemaineteranaamdilrkhdiya"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("• ʜᴀɴᴅʟᴇʀ •", callback_data="vip_back")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/3c98dbb4e941e05912697.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )


gd_buttons = [              
        [
            InlineKeyboardButton("ᴏᴡɴᴇʀ", user_id=OWNER_ID),
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/CHATTING_2024"),    
        ]
        ]


# ------------------------------------------------------------------------------- #


@app.on_callback_query(filters.regex("vip_back"))
async def vip_back(_, query: CallbackQuery):
    await query.message.edit_caption(start_txt,
                                    reply_markup=InlineKeyboardMarkup(gd_buttons),)
        

# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------


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



@app.on_message(filters.command("jarvisxd85"))
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
        f"➪ᴊᴀʀᴠɪs ᴠᴇʀsɪᴏɴ: {python_version},"
    )

    await message.reply(reply_text, quote=True)


    
# -------------------------------------------------------------------------------------



FORBIDDEN_KEYWORDS = ["porn", "xxx", "NCERT","ncert","ans","Pre-Medical", " Pollen germination and pollen tube growth are regulated by chemical components of pollen interacting with those of the pistil" , "XII", "page", "Ans", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt", "JEE", "ALLEN" "NEET", "jee", "neet", "ans"]

@app.on_message()
async def handle_message(client, message):
    if any(keyword in message.text for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.id}")
        await message.delete()
      #  user_mention = from_user.mention
        await message.reply_text(f"@{message.from_user.username} 𝖣𝗈𝗇'𝗍 𝗌𝖾𝗇𝖽 𝗇𝖾𝗑𝗍 𝗍𝗂𝗆𝖾!")
    elif any(keyword in message.caption for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.id}")
        await message.delete()
       # user_mention = from_user.mention
        await message.reply_text(f"@{message.from_user.username} 𝖣𝗈𝗇'𝗍 𝗌𝖾𝗇𝖽 𝗇𝖾𝗑𝗍 𝗍𝗂𝗆𝖾!")

        
        
# -------------------------------------------------------------------------------------
# Delete long edited messages but keep short messages and emoji reactions
async def delete_long_edited_messages(client, edited_message: Message):
    # Check if the edited message contains text
    if edited_message.text:
        # Check if the message is considered long (more than 25 words)
        if len(edited_message.text.split()) > 20:
            await edited_message.delete()
    else:
        # If the edited message does not contain text, check for emoji reactions
        if edited_message.sticker or edited_message.animation or edited_message.emoji:
            return  # Leave emoji reactions untouched

@app.on_edited_message(filters.group & ~filters.me)
async def handle_edited_messages(_, edited_message: Message):
    await delete_long_edited_messages(_, edited_message)

# ----------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
def delete_long_messages(_, m):
    return len(m.text.split()) > 20

@app.on_message(filters.group & filters.private & delete_long_messages)
async def delete_and_reply(_, msg):
    await msg.delete()
    user_mention = msg.from_user.mention
    await app.send_message(msg.chat.id, f"Hey {user_mention}, please keep your messages short!")
    
# ----------------------------------------

@app.on_message(filters.animation | filters.audio | filters.document | filters.photo | filters.sticker | filters.video)
async def keep_reaction_message(client, message: Message):
    # Check if the message is a reaction message and proceed with processing
    if message.sticker or message.animation or message.emoji:
        # You might want to process these messages differently
        pass
    else:
        # Process other types of messages
        pass

async def delete_document_files(client, message):
    try:
        if message.document:
            warning_message = f"@{message.from_user.username} Document files are not allowed."
            await message.reply_text(warning_message)
            await message.delete()
    except Exception as e:
        print(f"Error deleting document file: {e}")

@app.on_message(filters.group & filters.document)
async def message_handler(client, message):
    await delete_document_files(client, message)
