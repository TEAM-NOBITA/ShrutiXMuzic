from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from ShrutiMusic import app


# ================= START PANEL =================
def start_panel(_):
    return [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(
                text=_["S_B_2"],
                url=config.SUPPORT_CHAT
            ),
        ]
    ]


# ================= PRIVATE PANEL =================
def private_panel(_):
    return [
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                callback_data="help_page_1"
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_2"],
                url=config.SUPPORT_CHAT
            ),
            InlineKeyboardButton(
                text=_["S_B_6"],
                url=config.SUPPORT_CHANNEL
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true"
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                user_id=config.OWNER_ID
            )
        ],
    ]


# ================= ABOUT PANEL =================
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


# ================= OWNER PANEL =================
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
    
