import requests
import logging
from logging.config import fileConfig
import settings
import telegram

fileConfig('logs/logging_config.ini')
logger = logging.getLogger()

bot = telegram.Bot(settings.TELEGRAM_TOKEN)


def send_message(message: str):
    data = bot.send_message(text=message, chat_id=settings.TELEGRAM_CHAT_ID)
    send_status = data.get('ok', False)
    if send_status:
        logger.info('Send was ok')
    else:
        logger.warning('Problem with the sending')
        logger.warning(data)

    return send_status
