import telebot

bot_token = '6225849129:AAH-5Lnmdq4e6Yb8PpEKLsaZC2xlUWTR3pA'
bot = telebot.TeleBot(token=bot_token)

required_words = ['برمجيات', 'وورد', 'ويندوز']
exempt_users = []
exempt_words = ['شكرا', 'الله', 'جزاكم','شكرًا', 'الله','السلام']

@bot.message_handler(content_types=['text'])
def delete_messages(message):
    user_id = message.from_user.id
    user = bot.get_chat_member(message.chat.id, user_id)
    is_admin = user.status in ['administrator', 'creator']

    if not is_admin and user_id not in exempt_users and not all(word in message.text.lower() for word in required_words):
        if any(word in message.text.lower() for word in exempt_words):
            return  # تجاهل الرسالة

        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, f"@{message.from_user.username} يرجى كتابة رسالة تحتوي على الكلمات المطلوبة: " + ", ".join(required_words))

bot.polling()
