import logging

from fastapi.security import OAuth2PasswordBearer
import uvicorn

import auth
from messages.telegram import send_message
import settings
from fastapi import FastAPI, Security
from database.database import init_db, Sighting, db_session

logger = logging.getLogger(__name__)
app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=settings.API_KEY)


@app.on_event("startup")
async def startup_event():
    logger.info('Starting bird house')
    # Start database
    init_db()
    logger.info('Bird house started')


@app.get('/ping', dependencies=[Security(auth.api_key_auth)])
async def root():
    return 'Ok'


@app.get('/sighting', dependencies=[Security(auth.api_key_auth)])
async def sighting():

    # Get the last sighting with message send = True and if is not a recently sighting or there wasn't previous
    # sighting send a message
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

    # Save the sighting to the database
    db_session.add(Sighting(message_send=message_send))
    db_session.commit()

    # Response the BirdHouse
    return {
        'received': True,
        'message_send': message_send
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
