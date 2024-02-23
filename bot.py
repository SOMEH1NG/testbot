from sungram.bot import SungramBot

class MyTelegramBot(SungramBot):
    def __init__(self, token):
        super().__init__(token)

    def handle_start(self, chat_id):
        message = "Welcome to My Telegram Bot! Type /help for assistance."
        self.send_message(chat_id, message)

    def handle_message(self, chat_id, text):
        if text == '/start':
            self.handle_start(chat_id)
        elif text == '/help':
            self.handle_help(chat_id)
        else:
            self.send_message(chat_id, "I don't understand that command.")

bot_token = "6986990228:AAEiBjtqx68pn5-UYeNYnm2LHJ7E-ffBJI8"
telegram_bot = MyTelegramBot(token=bot_token)
telegram_bot.run()
