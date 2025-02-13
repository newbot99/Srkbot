import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Load environment variables from the .env file
load_dotenv()

# Get the bot token from the .env file
TOKEN = os.getenv("7788789468:AAHI96XSLip2nmD2CYqkE8GWQW5tk029Pu4")

# Check if the token is provided
if not TOKEN:
    print("Error: Bot token is missing. Please check your .env file.")
    exit(1)

# Your details (customize these details)
OWNER_NAME = "ZEROFLEX"  # Replace with your name
CHANNEL_NAME = "ZEROFLEXislive"  # Your channel name
TELEGRAM_CHANNEL = "https://t.me/zeroflexislive1"  # Your Telegram channel link
YOUTUBE_CHANNEL = "https://www.youtube.com/@ZEROFLEXislive"  # Your YouTube channel link

def start(update: Update, context: CallbackContext):
    """Handles the /start command with a welcome message."""
    update.message.reply_text(
        f"🎉 *Welcome to {CHANNEL_NAME} Bot!* 🎉\n\n"
        f"🔥 Stay updated with the latest BGMI content, FPS boosts, and performance fixes!\n"
        f"📢 Join our Telegram community for exclusive updates: [Click Here]({TELEGRAM_CHANNEL})\n"
        f"🎥 Watch our latest YouTube videos: [Click Here]({YOUTUBE_CHANNEL})\n\n"
        f"⚡ Use /help to see all available commands.\n"
        f"Enjoy your stay! 🚀",
        parse_mode="Markdown",
        disable_web_page_preview=True
    )

def help_command(update: Update, context: CallbackContext):
    """Handles the /help command with your channel details."""
    update.message.reply_text(
        f"📌 *Help Menu*\n\n"
        f"🔹 *Owner:* {https://t.me/zeroflexislive1}\n"
        f"🔹 *Channel:* {https://t.me/zeroflexislive1}\n"
        f"🔹 *Telegram Channel:* [Click Here]({TELEGRAM_CHANNEL})\n"
        f"🔹 *YouTube Channel:* [Click Here]({YOUTUBE_CHANNEL})\n\n"
        f"💡 *Commands:*\n"
        f"/start - Start the bot\n"
        f"/help - Show this help message\n"
        f"Just send a message, and I'll echo it back!",
        parse_mode="Markdown",
        disable_web_page_preview=True
    )

def echo(update: Update, context: CallbackContext):
    """Echoes user messages."""
    update.message.reply_text(update.message.text)

def main():
    """Main function to run the bot."""
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
