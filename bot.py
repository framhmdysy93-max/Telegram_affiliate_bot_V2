  import telebot

TOKEN = 'YOUR_BOT_TOKEN_HERE'  # ← استبدليه بالتوكن الحقيقي من BotFather

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً وسهلاً! 👋 استخدم /products أو /search للبدء.")

@bot.message_handler(commands=['products'])
def show_products(message):
    products = [
        {"name": "سماعات بلوتوث", "link": "https://amzn.to/affiliate1"},
        {"name": "ساعة ذكية", "link": "https://amzn.to/affiliate2"},
        {"name": "حقيبة ظهر", "link": "https://amzn.to/affiliate3"},
    ]
    response = "🛍️ العروض المتاحة:\n\n"
    for p in products:
        response += f"{p['name']}\n👉 {p['link']}\n\n"
    bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['search'])
def search_product(message):
    query = message.text.replace('/search', '').strip().lower()
    if query == "":
        bot.send_message(message.chat.id, "🔍 اكتب اسم المنتج بعد الأمر /search مثل: /search سماعات")
    else:
        if "سماعات" in query:
            bot.send_message(message.chat.id, "🎧 سماعات بلوتوث:\n👉 https://amzn.to/affiliate1")
        elif "ساعة" in query:
            bot.send_message(message.chat.id, "⌚ ساعة ذكية:\n👉 https://amzn.to/affiliate2")
        else:
            bot.send_message(message.chat.id, f"❌ لم يتم العثور على نتائج لـ: {query}")

@bot.message_handler(commands=['deal'])
def daily_deal(message):
    deal = {
        "name": "سماعة JBL أصلية بخصم 30%",
        "link": "https://amzn.to/deal123"
    }
    response = f"🔥 عرض اليوم:\n{deal['name']}\n👉 {deal['link']}"
    bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['help'])
def help_message(message):
    response = (
        "📌 أوامر البوت:\n"
        "/start - ترحيب وتعريف\n"
        "/products - عرض المنتجات\n"
        "/search [كلمة] - البحث\n"
        "/deal - عرض اليوم\n"
        "/help - المساعدة"
    )
    bot.send_message(message.chat.id, response)

bot.polling()
