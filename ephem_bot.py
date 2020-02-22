<<<<<<< HEAD
"""
Домашнее задание №1
Использование библиотек: ephem
* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.
"""

# Ссылка на моего бота - http://t.me/LP16UberBot

import logging

import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)

PROXY = {
    'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}

PLANET_USAGE = "По названию планеты ищет созвездие, в которое она входит.\nИспользование команды: /planet Планета\nПланета - название планеты на английском, например, Mars."

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def find_constellation(bot, update):
    planet_name_args = update.message.text.split()
    if len(planet_name_args) != 2:
        update.message.reply_text(PLANET_USAGE)
    else:
        planet_name = planet_name_args[1]
        planet_name = planet_name.capitalize()
        planet = getattr(ephem, planet_name)()
        planet.compute()
        update.message.reply_text(ephem.constellation(planet)[1])


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 

def main():
    mybot = Updater("1036004253:AAH6OgKQU0xZH7kDUtURSoaJ2Uvpjvvg8Jc", request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", find_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
=======
"""
Домашнее задание №1
Использование библиотек: ephem
* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.
"""

# Ссылка на моего бота - http://t.me/LP16UberBot

import logging

import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)

PROXY = {
    'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}

PLANET_USAGE = "По названию планеты ищет созвездие, в которое она входит.\nИспользование команды: /planet Планета\nПланета - название планеты на английском, например, Mars."

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def find_constellation(bot, update):
    planet_name_args = update.message.text.split()
    if len(planet_name_args) != 2:
        update.message.reply_text(PLANET_USAGE)
    else:
        planet_name = planet_name_args[1]
        planet_name = planet_name.capitalize()
        planet = getattr(ephem, planet_name)()
        planet.compute()
        update.message.reply_text(ephem.constellation(planet)[1])


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 

def main():
    mybot = Updater("1036004253:AAH6OgKQU0xZH7kDUtURSoaJ2Uvpjvvg8Jc", request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", find_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
>>>>>>> e6dac3a3d91a8aa4e2725bedac2c827724f107aa
    main()