import os
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

load_dotenv()
API_KEY: Final = os.getenv("API_KEY")
BOT_USERNAME: Final = os.getenv("BOT_USERNAME")


TOKEN: Final = API_KEY
BOT_USERNAME: Final = BOT_USERNAME


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ Hey dev, future you (and everyone else) will thank you:
    add some doc comments 🙃
    """

    await update.message.reply_text("Hello. I am squishy")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ Hey dev, future you (and everyone else) will thank you:
    add some doc comments 🙃
    """
    await update.message.reply_text("I am a music bot. Just gimme the title of any song or the most popular line in the song and I will get it for you  ")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ Hey dev, future you (and everyone else) will thank you:
    add some doc comments 🙃
    """
    await update.message.reply_text("This is a custom command")

# Handle responses


def handle_response(text: str) -> str:
    """ Hey dev, future you (and everyone else) will thank you:
    add some doc comments 🙃
    """
    processed: str = text.lower()
    if "hello" in processed:
        return "hey there"
    if "hi" in processed:
        return "Hiii"
    if "hey love" in processed:
        return "hi love, how's your day going"
    if "how are you" in processed:
        return "I'm doing pretty good. How about you"
    if "I'm having a bad day" in processed:
        return "What music can make you feel better"
    if "I'm good" in processed:
        return "that is great"
    if "I'm fine" in processed:
        return "oh okay,cool"
    if "good" in processed:
        return "cool"

    return "i don't understand"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ Hey dev, future you (and everyone else) will thank you:
    add some doc comments 🙃
    """
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User({update.message.chat.id}) in {message_type}:"{text}"')

    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
