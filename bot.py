from sungram.bot import SungramBot

bot_token = "6986990228:AAEiBjtqx68pn5-UYeNYnm2LHJ7E-ffBJI8"
telegram_bot = SungramBot(token=bot_token)

def handle_start(update):
    chat_id = update.message.chat.id
    message = "Welcome to My Telegram Bot! Type /help for assistance."
    telegram_bot.send_message(chat_id, message)

def handle_message(update):
    chat_id = update.message.chat.id
    text = update.message.text

    if text == '/start':
        handle_start(update)
    elif text == '/help':
        handle_help(update)
    else:
        telegram_bot.send_message(chat_id, "I don't understand that command.")

def handle_help(update):
    chat_id = update.message.chat.id
    # Implement your /help functionality here
    pass

# Set handlers
telegram_bot.on("message", handle_message)

# Run the bot
telegram_bot.run()
