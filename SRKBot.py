import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# 🔹 Bot Token (BotFather से लो और यहाँ पेस्ट करो)
BOT_TOKEN = "7788789468:AAHI96XSLip2nmD2CYqkE8GWQW5tk029Pu4"

# 🔹 Channel Username (अपने चैनल का username डालो)
CHANNEL_USERNAME = "@zeroflexislive"

# 🔹 BGMI वीडियो लिंक (अपनी वीडियो लिंक डालो)
BGMI_VIDEO_LINK = "https://youtube.com/@zeroflexislive?si=F5ARLll-VDvzu2Wt"

# 🔹 लॉगिंग सेटअप (टर्मिनल पर एरर या इंफो दिखाने के लिए)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# 🔹 /start Command - चैनल जॉइन करने के लिए बटन देगा
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    keyboard = [[InlineKeyboardButton("✅ Join Channel", url=f"https://t.me/{CHANNEL_USERNAME}")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text(
        f"🔥 Welcome {user.first_name}!

"
        "To use this bot, you must join our channel first! Click the button below to join. ✅",
        reply_markup=reply_markup
    )

# 🔹 /help Command - सभी कमांड्स की जानकारी देगा
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "🤖 *Bot Commands:*
"
        "/start - Verify & Start the bot
"
        "/help - Get bot info
"
        "/bgmi - Watch my latest BGMI video

"
        "👤 *Owner:* @zeroflexislive",  # अपना टेलीग्राम username डालो
        parse_mode="Markdown"
    )

# 🔹 /bgmi Command - BGMI वीडियो लिंक भेजेगा
def bgmi(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"🎮 Watch my latest BGMI video here:\n{BGMI_VIDEO_LINK}")

# 🔹 Main Function - Bot को Start करने के लिए
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Commands को हैंडल करने के लिए Handlers ऐड करें
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("bgmi", bgmi))

    # Bot को चालू करो
    updater.start_polling()
    updater.idle()

# 🔹 Run the Bot
if __name__ == "__main__":
    main()
