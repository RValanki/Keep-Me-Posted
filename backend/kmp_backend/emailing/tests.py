from django.test import TestCase
from django.http import HttpRequest
from views.py import send_email
from unittest.mock import patch, MagicMock

# Create your tests here.
class TestEmailSent(TestCase):
    @patch('views.py.send_email')

    def test_sending_email(self, mock_email_summary, mock_sending_smtp_email):
        request = HttpRequest()
        request.method = 'POST'
        request.POST = {
            'message': 'Here are the meeting minutes',
            'subject': 'TeamMeeting-20/07/2024',
            'contacts': 'tarayesha508@gmail.com'
        }

        mock_email = MagicMock()
        mock_email_value.return_value = mock_email

        response = send_email(request)

        self.assertEqual(response.json(), {'details':'Emails sent succesfully!'})
