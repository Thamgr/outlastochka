import datetime
import os
import pickle
import telebot
import time

from const import *


def send_poll_impl(bot_obj, title, options):
    bot_obj.send_poll(chat_id=chat_id,
                      question=title,
                      options=options,
                      is_anonymous=False,
                      allows_multiple_answers=True)

bot=telebot.TeleBot(token)
config = {}
if os.path.isfile(kConfPath):
    with open(kConfPath, 'rb') as file:
        config = pickle.load(file)
else:
    config['last_posted'] = datetime.date.today()

while True:
    today = datetime.date.today()
    while config['last_posted'] - today < datetime.timedelta(days=14):
        config['last_posted'] += datetime.timedelta(days=1)
        for const_data in [kIvanovo2Moscow, kMoscow2Ivanovo]:
            date = config['last_posted'].strftime('%d.%m')
            title = const_data['title'].format(date)
            options = const_data['options']
            send_poll_impl(bot, title, options)
            time.sleep(EPS_TIME)
        with open(kConfPath, 'wb') as file:
            pickle.dump(config, file)
    time.sleep(HOUR)
