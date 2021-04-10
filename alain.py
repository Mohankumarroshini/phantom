import logging
import os
import sys
import time
import spamwatch
import telegram.ext as tg
from pyrogram import Client, errors
from telethon import TelegramClient

ALAIN = TelegramClient(None, API_ID, API_HASH)
