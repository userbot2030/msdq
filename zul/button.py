from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from msdq import BOT_USERNAME

BMANAGE = InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="💁🏻‍♂Perintah Dasar", callback_data="zul_dasar"),
                    InlineKeyboardButton(text="Lanjutan🙋🏻‍♂", callback_data="zul_lanjut"),
                 ],
                 [
                    InlineKeyboardButton(text="🕵🏻Ahli", callback_data="zul_ahli"),
                    InlineKeyboardButton(text="Panduan Pro💆🏻‍♂", callback_data="zul_pro"),
                 ],
                 [
                    InlineKeyboardButton(text="➕ Panduan Lengkap ➕", url=f"http://t.me/{BOT_USERNAME}?start=help"),
                 ],
                 [
                    InlineKeyboardButton(text="🔙 Kembali", callback_data="zul_back"),
                 ]
                ])
BBMANAGE = InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="🔙 Kembali", callback_data="zul_manage"),
                 ]
                ])
BMUSIC = InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="ᴘᴇʀɪɴᴛᴀʜ ᴀᴅᴍɪɴ", callback_data="zul_admin"),
                    InlineKeyboardButton(text="ᴘᴇʀɪɴᴛᴀʜ ʙᴏᴛ", callback_data="zul_bot"),
                 ],
                 [
                    InlineKeyboardButton(text="ᴘᴇʀɪɴᴛᴀʜ ᴘʟᴀʏ", callback_data="zul_play"),
                    InlineKeyboardButton(text="ᴘᴇʀɪɴᴛᴀʜ ᴇxsᴛʀᴀ", callback_data="zul_extra"),
                 ],
                 [
                    InlineKeyboardButton(text="«", callback_data="zul_back"),
                 ]
                ])
BBMUSIC = InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="🔙 Kembali", callback_data="zul_music"),
                 ]
                ])
BJASA = InlineKeyboardMarkup(
              [
                 [
                     InlineKeyboardButton("Admin", url="https://t.me/foundermidnight")
                 ],
                 [
                    InlineKeyboardButton(text="«", callback_data="zul_back"),
                 ]
              ])
    
