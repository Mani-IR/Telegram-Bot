import os


BOT_TOKEN = ""

# فقط یوزرنیم‌هایی که مجازن به پیام‌ها ریپلای بدن
ADMINS_USERNAME = [""]

# لیست آیدی عددی گروه‌هایی که ربات توش فعاله
VALID_CHATS = []



APPROVED_CHATS = [chat.strip().lower() for chat in os.getenv("APPROVED_CHATS", "").split(",")]