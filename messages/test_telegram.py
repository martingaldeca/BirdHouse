from unittest import TestCase, mock

from messages.telegram import send_message


class SendMessageTest(TestCase):
    def test_send_message(self):
        test_data_list = [
            [{'ok': True}, True, 1, 0],
            [{'ok': False}, False, 0, 2],
            [{'oki_doki': True}, False, 0, 2],
        ]
        for test_data in test_data_list:
            with self.subTest(
                test_data=test_data
            ), mock.patch(
                'requests.get'
            ) as mock_request, mock.patch(
                'logging.Logger.warning'
            ) as mock_logger_warning, mock.patch(
                'logging.Logger.info'
            ) as mock_logger_info:
                mock_to_use = mock.MagicMock()
                request_data, expected_result, expected_info_count, expected_warning_count = test_data
                mock_to_use.json.return_value = request_data
                mock_request.return_value = mock_to_use
                self.assertEqual(send_message('test_message'), expected_result)
                self.assertEqual(mock_logger_warning.call_count, expected_warning_count)
                self.assertEqual(mock_logger_info.call_count, expected_info_count)
