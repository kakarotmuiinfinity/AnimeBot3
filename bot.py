import logging
import time
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

# Replace with your bot token (avoid storing it directly in code for production)
BOT_TOKEN = "7712183768:AAFB_5sDCNLNKcMwhvyjLP-nSFqkmSkiXkI"

# Sample user data (replace with actual logic to retrieve from Telegram API)
USER_FULL_NAME = "John Doe"

# Sticker ID and photo link
STICKER_ID = "CAACAgUAAxkBAAIgL2cHg1wOoOZ7uBA5Q8uh8wF2DN1xAAIEAAPBJDExieUdbguzyBAeBA"
PHOTO_URL = "https://te.legra.ph/file/d05ac856c4a8659de29ce.jpg"
BUTTON_LINKS = {
    "Anime Group ✇": "https://t.me/Cartoon_Heaven",
    "Anime Channel ❁": "https://t.me/Cartoon_Carnival"
}


def start(update, context):
    chat_id = update.effective_chat.id

    # Send fire reaction
    context.bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.FIRE)

    # Send sticker with delay
    time.sleep(2)
    context.bot.send_sticker(chat_id=chat_id, sticker_id=STICKER_ID)

    # Delete sticker after 2 seconds
    time.sleep(2)
    message = context.bot.send_message(chat_id=chat_id, text="▣☐☐")
    time.sleep(2)
    context.bot.edit_message_text(chat_id=chat_id, message_id=message.message_id, text="☐▣☐")
    time.sleep(2)
    context.bot.edit_message_text(chat_id=chat_id, message_id=message.message_id, text="☐☐▣")

    # Send welcome message with photo and buttons after final edit delay
    time.sleep(2)
    caption = f"Hᴇʟʟᴏ {USER_FULL_NAME}✨ Mʏsᴇʟғ {context.bot.username} Wᴀɴᴛ ᴛᴏ ᴡᴀᴛᴄʜ Aɴɪᴍᴇ? I ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ Aɴɪᴍᴇ ʏᴏᴜ ᴡᴀɴᴛ!"
    keyboard = [[telegram.InlineKeyboardButton(text, url=link) for text, link in BUTTON_LINKS.items()]]
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    context.bot.send_photo(chat_id=chat_id, photo=PHOTO_URL, caption=caption, reply_markup=reply_markup)


def handle_unknown(update, context):
    logging.warning(f"Unknown command from user: {update.message.text}")


def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )

    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add
