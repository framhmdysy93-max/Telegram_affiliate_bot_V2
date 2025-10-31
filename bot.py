import os
import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# قراءة بيانات الدفع من ملف JSON
with open("wallet_config.json", "r", encoding="utf-8") as f:
    wallet_data = json.load(f)

# إنشاء رابط الدفع باستخدام البيانات
payment_link = f"https://kazaa-wallet.com/pay?to={wallet_data['receiver']}&amount={wallet_data['amount']}&desc={wallet_data['description']}"

# دالة بدء البوت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("ادفع كازا 💸", url=payment_link)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("املا البيانات و اضغط على الزر 👇", reply_markup=reply_markup)

# إعداد البوت وتشغيله
BOT_TOKEN = os.environ.get("BOT_TOKEN")
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("✅ البوت يعمل الآن")
app.run_polling()