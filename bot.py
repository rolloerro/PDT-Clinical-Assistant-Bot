import telebot
from telebot import types
import os
from dotenv import load_dotenv

# Загрузка токена из .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

PDF_PATH = "assets/pdt_brochure_en.pdf"

def main_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "📖 What is PDT",
        "💊 Radachlorin",
        "✨ Benefits of PDT",
        "🩺 Treatment Steps",
        "🌍 Clinical Applications",
        "📕 Download Brochure",
        "☎️ Contact"
    ]
    for b in buttons:
        keyboard.add(b)
    return keyboard

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Welcome! 👋 I am the PDT Clinical Assistant Bot.\n\n"
        "Please select an option from the menu below ⬇️",
        reply_markup=main_menu()
    )

@bot.message_handler(func=lambda m: True)
def answer(message):
    text = message.text.strip()

    if text == "📖 What is PDT":
        bot.send_message(message.chat.id,
            "📖 *What is Photodynamic Therapy (PDT)*\n\n"
            "PDT is a minimally invasive treatment that uses a photosensitizing agent and light of a specific wavelength. "
            "It selectively targets pathological cells while sparing healthy tissue.\n\n"
            "✅ Non-invasive\n✅ Outpatient procedure\n✅ Minimal systemic toxicity",
            parse_mode="Markdown"
        )

    elif text == "💊 Radachlorin":
        bot.send_message(message.chat.id,
            "💊 *Radachlorin*\n\n"
            "— Next-generation photosensitizer developed in Russia\n"
            "— Activated by specific light wavelengths\n"
            "— Selectively accumulates in pathological tissues\n"
            "— Approved and used clinically\n\n"
            "✔ Compatible with modern PDT equipment\n✔ Allows repeated courses\n✔ High efficacy",
            parse_mode="Markdown"
        )

    elif text == "✨ Benefits of PDT":
        bot.send_message(message.chat.id,
            "✨ *Benefits of PDT*\n\n"
            "• High selectivity\n• Minimal side effects\n• Repeatable sessions\n• Outpatient treatment\n• Compatible with other therapies\n• Rapid recovery",
            parse_mode="Markdown"
        )

    elif text == "🩺 Treatment Steps":
        bot.send_message(message.chat.id,
            "🩺 *Treatment Steps*\n\n"
            "1️⃣ Administer photosensitizer\n"
            "2️⃣ Accumulation in pathological tissue\n"
            "3️⃣ Fluorescence diagnostics\n"
            "4️⃣ Light exposure\n\n"
            "Only pathological cells are destroyed; healthy tissue is preserved.",
            parse_mode="Markdown"
        )

    elif text == "🌍 Clinical Applications":
        bot.send_message(message.chat.id,
            "🌍 *Applications*\n\n"
            "🔹 Oncology\n🔹 Gynecology\n🔹 Urology\n🔹 Dentistry\n🔹 Dermatology\n\n"
            "Used both for therapy and diagnosis.",
            parse_mode="Markdown"
        )

    elif text == "📕 Download Brochure":
        if os.path.exists(PDF_PATH):
            with open(PDF_PATH, "rb") as pdf:
                bot.send_document(message.chat.id, pdf, caption="📕 PDT Brochure (placeholder)")
        else:
            bot.send_message(message.chat.id, f"⚠️ Brochure not found: {PDF_PATH}")

    elif text == "☎️ Contact":
        bot.send_message(message.chat.id, "☎️ For inquiries, contact: @MSL72Rph")

    else:
        bot.send_message(message.chat.id, "⚡ Please select an option from the menu:", reply_markup=main_menu())

print("🤖 PDT Clinical Assistant Bot is running...")
bot.polling(none_stop=True)
