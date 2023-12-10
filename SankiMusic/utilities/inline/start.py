from typing import Union
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from SankiMusic.utilities.config import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=" Commands ",
                url=f"https://t.me/{BOT_USERNAME}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text="⚡ Git Repo ⚡", url=f"https://github.com/MrProgrammer72/GJ516Music"
            )
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ꜱᴜᴘᴇʀ ɢʀᴏᴜᴘ 📈",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅꜱ 🥀", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="Uᴘᴅᴀᴛᴇꜱ 🎊", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="Oᴡɴᴇʀ ⛵", url="https://t.me/ITS_HELLL_BOYYY"
            )
        ]
     ]
    return buttons
