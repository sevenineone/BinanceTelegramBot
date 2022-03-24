import json
import urllib.request
import telebot


def get_currency(currency):
    try:
        url = urllib.request.urlopen(
            f"https://api.binance.com/api/v1/klines?symbol={currency.upper()}USDT&interval=1h&limit=1"
        )
        data = json.loads(url.read().decode())
        return f"last hour:\n{currency.upper()} max: {data[0][2].strip('0').strip('.')} $\n" \
               f"{currency.upper()} min: {data[0][3].strip('0').strip('.')} $"
    except  Exception:
        return "No such currency("


bot = telebot.TeleBot('TGBot_token')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Just type a coin)")
    else:
        bot.send_message(message.from_user.id, get_currency(message.text))


bot.polling(none_stop=True, interval=0)
