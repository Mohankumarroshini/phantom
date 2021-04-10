import os
from telegraph import upload_file
import pyrogram
TMP_DOWNLOAD_DIRECTORY = "./"
from telethon import events
import os


from PIL import Image
from datetime import datetime
from telegraph import Telegraph, upload_file, exceptions
from pyrogram import filters, Client
from sample_config import Config
from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton,
    CallbackQuery, InlineQuery)

Tgraph = Client(
   "Telegra.ph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Tgraph.on_message(filters.photo)
async def uploadphoto(client, message):
  msg = await message.reply_text("`Tʀʏɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅ`")
  userid = str(message.chat.id)
  img_path = (f"./DOWNLOADS/{userid}.jpg")
  img_path = await client.download_media(message=message, file_name=img_path)
  await msg.edit_text("`Tʀʏɪɴɢ Tᴏ Uᴘʟᴏᴀᴅ.....`")
  try:
    tlink = upload_file(img_path)
  except:
    await msg.edit_text("`Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ...`") 
  else:
    await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
    os.remove(img_path) 

@Tgraph.on_message(filters.animation)
async def uploadgif(client, message):
  if(message.animation.file_size < 5242880):
    msg = await message.reply_text("`Tʀʏɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅ...`")
    userid = str(message.chat.id)
    gif_path = (f"./DOWNLOADS/{userid}.mp4")
    gif_path = await client.download_media(message=message, file_name=gif_path)
    await msg.edit_text("`Tʀʏɪɴɢ Tᴏ Uᴘʟᴏᴀᴅ.....`")
    try:
      tlink = upload_file(gif_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")   
      os.remove(gif_path)   
    except:
      await msg.edit_text("`Sᴏᴍᴇᴛʜɪɴɢ ᴡ3ɴᴛ ᴡʀᴏɴɢ...`") 
  else:
    await message.reply_text("**Sɪᴢᴇ sʜᴏᴜʟᴅ ʙᴇ ʟᴇss ᴛʜᴇɴ 5 ᴍʙ**")

@Tgraph.on_message(filters.video)
async def uploadvid(client, message):
  if(message.video.file_size < 5242880):
    msg = await message.reply_text("`Tʀʏɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅ...`")
    userid = str(message.chat.id)
    vid_path = (f"./DOWNLOADS/{userid}.mp4")
    vid_path = await client.download_media(message=message, file_name=vid_path)
    await msg.edit_text("`Tʀʏɪɴɢ Tᴏ Uᴘʟᴏᴀᴅ.....`")
    try:
      tlink = upload_file(vid_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
      os.remove(vid_path)   
    except:
      await msg.edit_text("`Sᴏᴍᴇᴛʜɪɴɢ ᴡ3ɴᴛ ᴡʀᴏɴɢ...`") 
  else:
    await message.reply_text("**Sɪᴢᴇ sʜᴏᴜʟᴅ ʙᴇ ʟᴇss ᴛʜᴇɴ 5 ᴍʙ**")

@Tgraph.on_message(filters.command(["start"]))
async def home(client, message):
  buttons = [[
        InlineKeyboardButton('Hᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('Cʟᴏsᴇ', callback_data='close')
    ],
    [
        InlineKeyboardButton('Dᴇᴠᴇʟᴏᴘᴇʀ', url='https://t.me/Alain_Champion'),
        InlineKeyboardButton('Uᴘᴅᴀᴛᴇs', url='t.me/PhantomBotz')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await Tgraph.send_message(
        chat_id=message.chat.id,
        text="""<b>Hey there I am here,
        
I'm a Telegraph Uploader that can upload photo video and gif.
        
Simply send me photo, video or gif to upload to telegra.ph
        
Made with ❤️ by @PhantomBotz</b>""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )

@Tgraph.on_message(filters.command(["help"]))
async def help(client, message):
  buttons = [[
        InlineKeyboardButton('Hᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('Cʟᴏsᴇ', callback_data='close')
    ],
]
  reply_markup = InlineKeyboardMarkup(buttons)
  await Tgraph.send_message(
        chat_id=message.chat.id,
        text="""<b>There Is Nothing To Know More,
        
Just Send Me A Video/gif/photo Upto 5 mb.
i'll upload it to telegra.ph and give you the direct link</b>""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )                           
@Tgraph.on_callback_query()
async def button(Tgraph, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(Tgraph, update.message)
      elif "close" in cb_data:
        await update.message.delete() 
      elif "home" in cb_data:
        await update.message.delete()
        await home(Tgraph, update.message)
        
@Tgraph.on_message(filters.command(["tm"]))
async def home(client, message):
      msg = await message.reply_text("`Tʀʏɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅ`")
      userid = str(message.chat.id)
      img_path = (f"./DOWNLOADS/{userid}.jpg")
      img_path = await client.download_media(message=message, file_name=img_path)
      await msg.edit_text("`Tʀʏɪɴɢ Tᴏ Uᴘʟᴏᴀᴅ.....`")
      try:
         tlink = upload_file(img_path)
      except:
         await msg.edit_text("`Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ...`") 
      else:
         await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
      os.remove(img_path) 

Tgraph.run()
