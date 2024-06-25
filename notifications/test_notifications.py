import unittest
from unittest.mock import patch, MagicMock
from notifications import send_email_notification, SMTPAuthenticationError, SMTPConnectError, SMTPHeloError, SMTPSenderRefused, SMTPRecipientsRefused, SMTPDataError, SMTPException

class TestSendEmailNotification(unittest.TestCase):

    @patch('notifications.smtplib.SMTP')
    def test_send_email_success(self, mock_smtp):
        mock_server = MagicMock()
        mock_smtp.return_value = mock_server

        send_email_notification("user@example.com", "Test Subject", "Test Message", "smtp.example.com", 587, "username", "password")
        mock_server.sendmail.assert_called_once()

    @patch('notifications.smtplib.SMTP')
    def test_smtp_authentication_error(self, mock_smtp):
        mock_smtp.side_effect = SMTPAuthenticationError(535, b'Authentication failed')

        with self.assertLogs(level='INFO') as log:
            send_email_notification("user@example.com", "Test Subject", "Test Message", "smtp.example.com", 587, "username", "password")
            self.assertIn("INFO:root:Failed to send email to user@example.com. Error: Authentication failed.", log.output)

    @patch('notifications.smtplib.SMTP')
    def test_smtp_connect_error(self, mock_smtp):
        mock_smtp.side_effect = SMTPConnectError(421, b'Unable to connect')

        with self.assertLogs(level='INFO') as log:
            send_email_notification("user@example.com", "Test Subject", "Test Message", "smtp.example.com", 587, "username", "password")
            self.assertIn("INFO:root:Failed to send email to user@example.com. Error: Unable to connect to the SMTP server.", log.output)

    @patch('notifications.smtplib.SMTP')
    def test_smtp_helo_error(self, mock_smtp):
        mock_smtp.side_effect = SMTPHeloError(501, b'Server refused HELO')

        with self.assertLogs(level='INFO') as log:
            send_email_notification("user@example.com", "Test Subject", "Test Message", "smtp.example.com", 587, "username", "password")
            self.assertIn("INFO:root:Failed to send email to user@example.com. Error: The server refused the HELO message.", log.output)

    @patch('notifications.smtplib.SMTP')
    def test_smtp_sender_refused(self, mock_smtp):
        mock_smtp.side_effect = SMTPSenderRefused(550, b'Sender address refused', 'username')

        with self.assertLogs(level='INFO') as log:
            send_email_notification("user@example.com", "Test Subject", "Test Message", "smtp.example.com", 587, "username", "password")
            self.assertIn("INFO:root:Failed to send email to user@example.com. Error: The server refused the sender address.", log.output)

    @patch('notifications.smtplib.SMTP')
    def test_smtp_recipients_refused(self, mock_smtp):
        mock_smtp.side_effect = SMTPRecipientsRefused({'user@example.com': (550, b'Recipient address refused')})

        with self.assertLogs(level='INFO') as log:
            send_email_notification("user@example.com", "Test Subject", "Test Message", "smtp.example.com", 587, "username", "password")
            self.assertIn("INFO:root:Failed to send email to user@example.com. Error: The server refused the recipient address.", log.output)

    @patch('notifications.smtplib.SMTP')
    def test_smtp_data_error(self, mock_smtp):
        mock_smtp.side_effect = SMTPDataError(554, b'Unexpected error code')

        with self.assertLogs(level='INFO') as log:
            send_email_notification("user@example.com", "Test Subject", "Test Message", "smtp.example.com", 587, "username", "password")
            self.assertIn("INFO:root:Failed to send email to user@example.com. Error: The server replied with an unexpected error code.", log.output)

    @patch('notifications.smtplib.SMTP')
    def test_smtp_exception(self, mock_smtp):
        mock_smtp.side_effect = SMTPException("General SMTP error")

        with self.assertLogs(level='INFO') as log:
            send_email_notification("user@example.com", "Test Subject", "Test Message", "smtp.example.com", 587, "username", "password")
            self.assertIn("INFO:root:Failed to send email to user@example.com. SMTP error occurred: General SMTP error", log.output)

if __name__ == '__main__':
    unittest.main()
