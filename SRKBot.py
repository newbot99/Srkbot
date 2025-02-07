import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Bot Token
BOT_TOKEN = "7788789468:AAH19XSL5Ip2mD2CYqKdeBGWQWsT6O2Pu4"

# Channel Username
CHANNEL_USERNAME = "@zeroflexislive"

# BGMI Video Link
BGMI_VIDEO_LINK = "https://youtube.com/@zeroflexislive?si=F5ARL"

# Logging setup
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s", level=logging.INFO)

# Start Command
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    keyboard = [[InlineKeyboardButton("✅ Join Channel", url="https://t.me/zeroflexislive")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        f"Welcome {user.first_name}!",
        reply_markup=reply_markup
    )

# Help Command
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "**🤖 Bot Commands:**\n\n"
        "/start - Verify & Start the bot\n"
        "/help - Get bot info\n"
        "/bgmi - Watch my latest BGMI video\n\n"
        "👑 *Owner:* @zeroflexislive",
        parse_mode="Markdown"
    )

# BGMI Command
def bgmi(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        f"📌 Watch my latest BGMI video here:\n👉 {https://youtube.com/@zeroflexislive?si=F5ARLBGMI_VIDEO_LINK}"
    )

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("bgmi", bgmi))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
