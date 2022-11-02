import serial
import logging
import settings

from logging.config import fileConfig

from messages.telegram import send_message

fileConfig('logs/logging_config.ini')
logger = logging.getLogger()

if __name__ == '__main__':

    # Start database
    from database.database import init_db, Sighting, db_session

    init_db()

    serial_port = serial.Serial(
        settings.SERIAL_PORT,
        baudrate=settings.SERIAL_BAUD_RATE,
        timeout=settings.SERIAL_TIMEOUT
    )

    while True:
        data = serial_port.readline().decode().replace('\r\n', '')
        if data:
            value = int(data)
            if value:
                logger.info("Active")

                # Create an entry in the DB
                last_sighting: Sighting = db_session.query(
                    Sighting
                ).filter_by(
                    message_send=True
                ).order_by(
                    Sighting.id.desc()
                ).first()
                message_send = False
                if not last_sighting or not last_sighting.recently_sighting:
                    message_send = True
                    send_message(settings.TELEGRAM_SIGHTING_MESSAGE)

                db_session.add(Sighting(message_send=message_send))
                db_session.commit()
            else:
                logger.info("Inactive")