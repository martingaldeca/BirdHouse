from unittest import TestCase, mock
from telegram import Bot

import settings
from messages.telegram import send_message


class SendMessageTest(TestCase):
    def test_send_message(self):
        with mock.patch(
            'os.system'
        ) as mock_system, mock.patch.object(
            Bot, 'send_photo'
        ) as mock_send_photo, mock.patch(
            'builtins.open', mock.mock_open(read_data='data')
        ), mock.patch.object(Bot, '_validate_token'):
            message = 'test_message'
            send_message(message)
            self.assertEqual(mock_system.call_count, 1)
            self.assertEqual(
                mock_system.call_args,
                mock.call('fswebcam -r 1280x720 --no-banner ./last_sighting.jpg')
            )
            self.assertEqual(mock_send_photo.call_count, 1)
            self.assertEqual(
                mock_send_photo.call_args,
                mock.call(
                    chat_id=settings.TELEGRAM_CHAT_ID,
                    photo=open('./last_sighting.jpg', 'rb'),
                    caption=message,
                    filename='last_sighting.jpg'
                )
            )
