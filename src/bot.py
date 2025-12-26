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

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

# from config import BOT_TOKEN, ADMINS_USERNAMES, VALID_CHATS
# import telebot
# import logging
# from constants import *

# # فعال‌سازی لاگ برای دیباگ
# telebot.logger.setLevel(logging.DEBUG)


# class Testbot:
#     def __init__(self):
#         self.bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")
#         self.setup_handlers()

#     def setup_handlers(self):
#         # فرمان شروع
#         self.bot.message_handler(commands=['start', 'help'])(self.send_welcome)

#         # فقط اگر پیام ریپلای از ادمین تو گروه مجاز بود
#         self.bot.message_handler(func=self.is_valid_admin_reply)(self.handle_admin_reply)

#     # پیام خوش‌آمد
#     def send_welcome(self, message):
#         chat_id = message.chat.id
#         username = message.from_user.username
#         print(f"[+] User {username} in chat {chat_id} used /start")
#         self.bot.reply_to(message, "سلام 👋\nربات تست فعاله ✅")

#     # بررسی اینکه پیام از ادمین مجازه و توی گروه درست هست
#     def is_valid_admin_reply(self, message):
#         return (
#             message.reply_to_message  # باید ریپلای باشه
#             and message.from_user.username in ADMINS_USERNAMES  # باید ادمین باشه
#             and message.chat.id in VALID_CHATS  # باید توی گروه مجاز باشه
#         )

#     # پاسخ به ریپلای ادمین
#     def handle_admin_reply(self, message):
#         replied_text = message.reply_to_message.text or "<بدون متن>"
#         admin_text = message.text or "<بدون متن>"

#         response = (
#             f"✅ <b>Admin Reply Detected</b>\n\n"
#             f"<b>Original message:</b> {replied_text}\n"
#             f"<b>پاسخ ادمین:</b> {admin_text}"
#         )

#         self.bot.reply_to(message, response)
#         print(f"[ADMIN REPLY] {message.from_user.username}: {admin_text}")

#     # اجرای ربات
#     def run(self):
#         print("🤖 Bot is polling... (Ctrl+C to stop)")
#         self.bot.infinity_polling(
#             timeout=10,
#             long_polling_timeout=5,
#             skip_pending=True,
#             # restart_on_change=True,
#         )

#     @bot.message_handler(commands=['start', 'help'])
#     def send_welcome(message):
#         bot.reply_to(message, "سلام! 👋\nاگر پیام‌ها رو لایک یا دیس‌لایک کنی، جواب می‌دم 😉")
    
#     @bot.edited_message_handler(func=lambda m: hasattr(m, "reactions"))
#     def handle_reaction(message):
#         try:
#             reactions = message.reactions
#             username = message.from_user.username or message.from_user.first_name
    
#             if not reactions:
#                 return
    
#             for r in reactions:
#                 emoji = r["emoji"]
#                 count = r["count"]
#                 print(f"📢 {username} reacted with {emoji} ({count})")
    
#                 if emoji == "👍":
#                     bot.send_message(message.chat.id, f"🔥 {username} لایک کرد!")
#                 elif emoji == "👎":
#                     bot.send_message(message.chat.id, f"💢 {username} دیسلایک کرد!")
#                 elif emoji == "❤️":
#                     bot.send_message(message.chat.id, f"❤️ عشقی {username}!")
    
#         except Exception as e:
#             print("⚠️ Error in reaction handler:", e)
    
    
#         print("🤖 Bot is polling... (Ctrl+C to stop)")
#         bot.infinity_polling(timeout=10, long_polling_timeout=5, skip_pending=True)
    


# if __name__ == "__main__":
#     bot = Testbot()
#     bot.run()




# bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")



# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, "سلام به ربات تست خوش آمدید!")

# @bot.message_handler(func=lambda message: message.reply_to_message and message.from_user.username in ADMINS_USERNAMES and message.chat.username in VALID_CHATS)
# def echo_all(message):
#     print("Replying to message:", message.reply_to_message.text)
#     print("Received message:", message.text)
#     replied_text = message.reply_to_message.text
#     current_text = message.text
#     output = f"✅ You replied to: '{replied_text}'\n\nYour message: '{current_text}'"
#     bot.reply_to(message, output )

# print("Bot is polling...")
# bot.infinity_polling()






















































# from config import BOT_TOKEN, ADMINS_USERNAMES, VALID_CHATS
# import telebot
# from telebot import types

# class TestBot:
#     def __init__(self):
#         self.bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")
#         self.setup_handlers()

#     def setup_handlers(self):
#         # فرمان شروع
#         self.bot.message_handler(commands=['start', 'help'])(self.send_welcome)

#         # ریپلای ادمین
#         self.bot.message_handler(func=self.is_valid_admin_reply)(self.handle_admin_reply)

#         # اضافه کردن دکمه‌های لایک/دیسلایک/❤️ به هر پیام
#         self.bot.message_handler(func=lambda m: m.chat.id in VALID_CHATS)(self.add_reaction_buttons)

#         # هندل دکمه‌ها
#         self.bot.callback_query_handler(func=lambda call: True)(self.handle_reaction)

#     # خوش‌آمد گویی
#     def send_welcome(self, message):
#         self.bot.reply_to(message, "سلام 👋 ربات تست فعاله ✅\nپیام‌ها رو لایک یا دیس‌لایک کنید 😉")

#     # بررسی ریپلای ادمین
#     def is_valid_admin_reply(self, message):
#         return (
#             message.reply_to_message
#             and message.from_user.username in ADMINS_USERNAMES
#             and message.chat.id in VALID_CHATS
#         )

#     # پاسخ به ریپلای ادمین
#     def handle_admin_reply(self, message):
#         replied_text = message.reply_to_message.text or "<بدون متن>"
#         admin_text = message.text or "<بدون متن>"
#         response = (
#             f"✅ <b>Admin Reply Detected</b>\n\n"
#             f"<b>Original message:</b> {replied_text}\n"
#             f"<b>پاسخ ادمین:</b> {admin_text}"
#         )
#         self.bot.reply_to(message, response)
#         print(f"[ADMIN REPLY] {message.from_user.username}: {admin_text}")

#     # اضافه کردن دکمه‌های واکنش
#     def add_reaction_buttons(self, message):
#         keyboard = types.InlineKeyboardMarkup()
#         keyboard.add(
#             types.InlineKeyboardButton("👍 لایک", callback_data=f"like:{message.message_id}"),
#             types.InlineKeyboardButton("👎 دیس‌لایک", callback_data=f"dislike:{message.message_id}"),
#             types.InlineKeyboardButton("❤️ عشق", callback_data=f"love:{message.message_id}")
#         )
#         self.bot.send_message(message.chat.id, "واکنش بدهید:", reply_markup=keyboard)

#     # هندل کلیک روی دکمه‌ها
#     def handle_reaction(self, call):
#         try:
#             action, msg_id = call.data.split(":")
#             msg_id = int(msg_id)
#             user = call.from_user.username or call.from_user.first_name

#             if action == "like":
#                 self.bot.answer_callback_query(call.id, f"{user} لایک کرد 👍")
#             elif action == "love":
#                 self.bot.answer_callback_query(call.id, f"{user} عشق کرد ❤️")
#             elif action == "dislike":
#                 self.bot.answer_callback_query(call.id, f"{user} دیس‌لایک کرد 👎")
#                 # پاک کردن پیام مورد نظر
#                 self.bot.delete_message(call.message.chat.id, msg_id)
#                 print(f"[DELETE] {user} دیس‌لایک کرد و پیام {msg_id} پاک شد")

#         except Exception as e:
#             print("⚠️ Error handling reaction:", e)

#     # اجرای ربات
#     def run(self):
#         print("🤖 Bot is polling...")
#         self.bot.infinity_polling(timeout=10, long_polling_timeout=5, skip_pending=True)

# if __name__ == "__main__":
#     TestBot().run()








































































































# import telebot
# import messages
# from config import BOT_TOKEN, ADMINS_USERNAME, VALID_CHATS


# bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")


# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, messages.WELCOME_MESSAGE)

# def is_valid_admin_reply(message):
#     return (
#         message.reply_to_message is not None
#         and message.from_user.username in ADMINS_USERNAME
#         and message.chat.id in VALID_CHATS
#     )

# @bot.message_handler(func=is_valid_admin_reply)
# def echo_all(message):
#     bot.reply_to(message, "پیام شما دریافت شد و در حال پردازش است...")
#     # replied_text = message.reply_to_message.text or "<بدون متن>"
#     # current_text = message.text or "<بدون متن>"
#     # output = messages.ADMIN_REPLY_MESSAGE.format(replied_text=replied_text, current_text=current_text)
#     # bot.reply_to(message, output)

# @bot.message_reaction_handler(func=lambda message: message.new_reaction)
# def handle_reaction(message: telebot.types.Message):
#     reaction = message.new_reaction[-1].emoji  # گرفتن آخرین واکنش
#     if reaction == "👍":
#         bot.reply_to(message, messages.LIKE_MESSAGE.format(username=message.from_user.username or message.from_user.first_name))



# if __name__ == "__main__":
#     print(messages.BOT_RNNING)
#     print("Bot is polling...")
#     bot.infinity_polling(
#         allowed_updates=['message', 'edited_message', 'message_reaction'],
#         restart_on_change=True,
#         timeout=10,
#         long_polling_timeout=5,
#         skip_pending=True
#         )



















# import telebot
# from telebot import types
# from config import BOT_TOKEN, ADMINS_USERNAME, VALID_CHATS

# bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, "سلام! ربات تست فعاله ✅\nپیام‌ها رو لایک یا دیس‌لایک کنید")

# @bot.message_handler(func=lambda m: m.chat.id in VALID_CHATS)
# def add_reaction_buttons(message):
#     keyboard = types.InlineKeyboardMarkup()
#     keyboard.add(
#         types.InlineKeyboardButton("👍 لایک", callback_data=f"like:{message.message_id}"),
#         types.InlineKeyboardButton("👎 دیس‌لایک", callback_data=f"dislike:{message.message_id}")
#     )
#     bot.send_message(message.chat.id, "واکنش بدهید:", reply_markup=keyboard)

# @bot.callback_query_handler(func=lambda call: True)
# def handle_reaction(call):
#     action, msg_id = call.data.split(":")
#     msg_id = int(msg_id)
#     user = call.from_user.username or call.from_user.first_name

#     if action == "like":
#         bot.send_message(call.message.chat.id, f"🔥 {user} لایک کرد!")
#     elif action == "dislike":
#         bot.send_message(call.message.chat.id, f"💢 {user} دیس‌لایک کرد و پیام حذف می‌شود")
#         bot.delete_message(call.message.chat.id, msg_id)

#     bot.answer_callback_query(call.id)

# bot.infinity_polling()







# import telebot
# from telebot import types
# from config import BOT_TOKEN, ADMINS_USERNAME, VALID_CHATS

# bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

# # پیام خوش آمدگویی
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, "سلام! ربات تست فعاله ✅\nمی‌توانید پیام‌ها را لایک یا دیس‌لایک کنید.")

# # افزودن دکمه‌ها به پیام‌های گروه
# @bot.message_handler(func=lambda m: m.chat.id in VALID_CHATS)
# def add_reaction_buttons(message):
#     keyboard = types.InlineKeyboardMarkup()
#     keyboard.add(
#         types.InlineKeyboardButton("👍 لایک", callback_data=f"like:{message.message_id}"),
#         types.InlineKeyboardButton("👎 دیس‌لایک", callback_data=f"dislike:{message.message_id}"),
#         types.InlineKeyboardButton("❤️ عشق", callback_data=f"love:{message.message_id}")
#     )
#     # فقط دکمه‌ها ارسال می‌شوند، متن “واکنش بدهید:” حذف شد
#     bot.send_message(message.chat.id, "💡 روی دکمه‌ها کلیک کنید:", reply_markup=keyboard)

# # هندل دکمه‌ها
# @bot.callback_query_handler(func=lambda call: True)
# def handle_reaction(call):
#     action, msg_id = call.data.split(":")
#     msg_id = int(msg_id)
#     user = call.from_user.username or call.from_user.first_name

#     if action == "like":
#         bot.send_message(call.message.chat.id, f"🔥 {user} لایک کرد!")
#     elif action == "love":
#         bot.send_message(call.message.chat.id, f"❤️ {user} عشق کرد!")
#     elif action == "dislike":
#         bot.send_message(call.message.chat.id, f"💢 {user} دیس‌لایک کرد و پیام حذف می‌شود")
#         try:
#             bot.delete_message(call.message.chat.id, msg_id)
#         except Exception as e:
#             print("⚠️ خطا در حذف پیام:", e)

#     # پاسخ به callback برای حذف ساعت انتظار تلگرام
#     bot.answer_callback_query(call.id)

# bot.infinity_polling()






















































































































































































































































































































































































































































































































































































































































































































































































































