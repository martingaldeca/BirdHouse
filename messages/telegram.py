import os
import logging
from logging.config import fileConfig
import settings
import telegram

fileConfig('logs/logging_config.ini')
logger = logging.getLogger()

bot = telegram.Bot(settings.TELEGRAM_TOKEN)


def send_message(message: str):
    # Make a photo to send it
    os.system('fswebcam -r 1280x720 --no-banner ./last_sighting.jpg')
    with open('./last_sighting.jpg', 'rb') as photo:
        bot.send_photo(
            chat_id=settings.TELEGRAM_CHAT_ID,
            photo=photo,
            caption=message,
            filename='last_sighting.jpg'
        )
