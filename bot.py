import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO,
                    filename = "mylog.log", 
                    format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s", 
                    datefmt='%H:%M:%S')

@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Првиет, {user_name}!'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id = user_id, text=text)


@dp.message()
async def send_translit13(message: Message):
    translit = ({"А":'A', "Б":'B', "В":'V', "Г":'G', "Д":'D', "Е":'E', 'Ё':'E', 'Ж':'ZH', 'З':'Z', 'И':'I', 
                 'Й': 'I', 'К':'K', 'Л':'L', 'М':'M', 'Н':'N', 'О':'O', 'П':'P', 'Р':'R', 'С':'S', 'Т': 'T',
                 'У':'U', 'Ф':'F', 'Х':'KH', 'Ц':'TS', 'Ч':'CH', 'Ш':'SH', 'Щ':'SHCH', 'Ы':'Y', 'Ъ':'IE',
                 'Э':'E', 'Ю':'IU', 'Я':'IA'})
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    logging.info(f'{user_name} {user_id}: {text}')
    transliterated_text = ""

    for char in text:
        if char in translit:  
            transliterated_text += translit[char]  
        elif char.upper() in translit:  
            transliterated_text += translit[char.upper()].lower() 
        else:
            transliterated_text += char  

    await message.answer(text=transliterated_text)

if __name__ == '__main__':
    dp.run_polling(bot)


    
