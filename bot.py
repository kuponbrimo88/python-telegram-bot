from telegram.ext import Updater, CommandHandler

# Token dari BotFather
TOKEN = '7791008102:AAH9KPCm9iSaAzE3OXS5Pgs-AhizyUnoPLc'

# Fungsi untuk membalas perintah start
def start(update, context):
    chat_id = -4790580801  # ID chat yang spesifik
    message = 'Halo! Saya adalah bot Anda.'
    context.bot.send_message(chat_id=chat_id, text=message)

# Fungsi utama untuk menjalankan bot
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Tambahkan handler untuk perintah /start
    dp.add_handler(CommandHandler('start', start))

    # Mulai bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
