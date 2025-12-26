from config import BOT_TOKEN , ADMINS_USERNAMES, VALID_CHATS
import telebot
import logging
telebot.logger.setLevel(logging.DEBUG)

class Testbot:
    def __init__(self):
        self.bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")
        self.setup_handlers()
        
    def setup_handlers(self):
        self.bot.message_handler(commands=['start', 'help'])(self.send_welcome)
        self.bot.message_handler(func=lambda message: message.reply_to_message and message.from_user.username in ADMINS_USERNAMES and message.chat.username in VALID_CHATS)(self.echo_all)
    
    def send_welcome(self, message):
        self.bot.reply_to(message, "سلام به ربات تست خوش آمدید!")
        
    def is_valid_admin_reply(self, message):
        return (message.reply_to_message and 
                message.from_user.username in ADMINS_USERNAMES and 
                message.chat.username in VALID_CHATS)
        
    def echo_all(self, message):
        self.bot.reply_to(message, f"✅ You replied to: '{message.reply_to_message.text}'\n\nYour message: '{message.text}'","\nhi")
        
    def run(self):
        print("Bot is polling...")
        self.bot.infinity_polling(timeout=10, long_polling_timeout=5, skip_pending=True, logger_level="DEBUG")

        
if __name__ == '__main__':
    test_bot = Testbot()
    print("Bot is polling...")
    test_bot.bot.infinity_polling()

        
        
        
        
