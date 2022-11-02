import requests
import settings
import serial
import logging
from logging.config import fileConfig
import settings

fileConfig('logs/logging_config.ini')
logger = logging.getLogger()


def send_message(message: str):
    url = (
        f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage?chat_id="
        f"{settings.TELEGRAM_CHAT_ID}&text={message}"
    )
    logger.debug(requests.get(url).json())
