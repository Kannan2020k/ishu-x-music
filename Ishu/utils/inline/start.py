from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🌹 ᴀᴅᴅ ᴍᴇ ɪɴ yᴏᴜʀ ɢʀᴏᴜᴩ 🌹",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🍂 ʜᴇʟᴩ & ᴄᴏᴍᴍᴀɴᴅꜱ 🍂",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="👀 ꜱᴇᴛᴛɪɴɢꜱ 😁", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🌹 ᴀᴅᴅ ᴍᴇ ɪɴ yᴏᴜʀ ɢʀᴏᴜᴩ 🌹",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🍂 ʜᴇʟᴩ & ᴄᴏᴍᴍᴀɴᴅꜱ 🍂", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🥀", user_id=OWNER
            ),
            InlineKeyboardButton(
                text="🥀❤️‍🔥 ɴᴇᴛᴡᴏʀᴋ  🥀❤️‍🔥", url="https://t.me/poisonupdates"
            )
        ],
        [
            InlineKeyboardButton(
                text="🍂 ꜱᴜᴩᴩᴏʀᴛ ɢʀᴏᴜᴩ 🍂", url="https://t.me/poisonteam1"
            )
        ],
     ]
    return buttons
