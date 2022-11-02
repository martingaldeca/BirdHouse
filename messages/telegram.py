import requests
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
    data = requests.get(url).json()
    send_status = data.get('ok', False)
    if send_status:
        logger.info('Send was ok')
    else:
        logger.warning('Problem with the sending')
        logger.warning(data)

    return send_status
