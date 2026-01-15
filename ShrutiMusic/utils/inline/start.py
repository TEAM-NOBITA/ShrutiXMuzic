from pyrogram.types import InlineKeyboardButton

import config
from ShrutiMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
    
      ],
    
    ]
    return buttons

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def about_panel():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Close",
                    callback_data="close"
                )
            ]
        ]
    )
    
def owner_panel():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Owner",
                    user_id=config.OWNER_ID
                )
            ],
            [
                InlineKeyboardButton(
                    text="Close",
                    callback_data="close"
                )
            ]
        ]
    )
    
