import logging
import os
import sys
import time
import spamwatch
import telegram.ext as tg
from pyrogram import Client, errors

from pyrogram import filters, Client
from sample_config import Config
from telethon import TelegramClient

ALAIN = Cilent(
     "Telegra.ph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)
