# Copyright (c) 2025 Nand Yaduwanshi <NoxxOP>
# Location: Supaul, Bihar
#
# All rights reserved.
#
# This code is the intellectual property of Nand Yaduwanshi.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: badboy809075@gmail.com


from .extras import *
from .help import *
from .play import *
from .queue import *
from .settings import *
from .speed import *
from .start import *

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def supp_markup(_=None):
    buttons = [
        [
            InlineKeyboardButton(
                text="📢 sᴜᴘᴘᴏʀᴛ",
                url="https://t.me/YourSupportGroup"  # 🔗 Replace with your real support group
            ),
            InlineKeyboardButton(
                text="⚡ ᴜᴘᴅᴀᴛᴇs",
                url="https://t.me/YourUpdateChannel"  # 🔗 Replace with your real updates channel
            ),
        ]
    ]
    return InlineKeyboardMarkup(buttons)


# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @NoxxOP)
# 🔗 GitHub : https://github.com/NoxxOP/ShrutiMusic
# 📢 Telegram Channel : https://t.me/ShrutiBots
# ===========================================

# ❤️ Love From ShrutiBots

