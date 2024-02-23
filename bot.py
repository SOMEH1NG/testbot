from sungram.bot import SungramBot

bot_token = "6986990228:AAEiBjtqx68pn5-UYeNYnm2LHJ7E-ffBJI8"
telegram_bot = SungramBot(token=bot_token)

@telegram_bot.on_start
def handle_start(update):
    chat_id = update.message.chat_id
    message = "Welcome to My Telegram Bot! Type /help for assistance."
    telegram_bot.send_message(chat_id, message)

@telegram_bot.on_message(filters.command("help"))
def handle_help(update):
    chat_id = update.message.chat_id
    # Implement your /help functionality here
    pass

@telegram_bot.on_message(filters.text)
def handle_message(update):
    chat_id = update.message.chat_id
    text = update.message.text

    if text == '/start':
        handle_start(update)
    elif text == '/help':
        handle_help(update)
    else:
        telegram_bot.send_message(chat_id, "I don't understand that command.")

telegram_bot.run()
