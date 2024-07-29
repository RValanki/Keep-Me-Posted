from django.test import TestCase
from django.http import HttpRequest, JsonResponse
from unittest.mock import patch, MagicMock
from emailing.views import send_email
import json

# Create your tests here.
class TestEmailSent(TestCase):

    @patch('emailing.views.send_email')
    def test_sending_email(self, mock_send_smtp_email):
        request = HttpRequest()
        request.method = 'POST'
        request.POST = {
            'message': 'Here are the meeting minutes',
            'subject': 'TeamMeeting-20/07/2024',
            'contacts': 'tarayesha508@gmail.com'
        }

        mock_response = JsonResponse({'details':'Emails sent successfully!'})
       
        mock_send_smtp_email.return_value = mock_response

        response = send_email(request)
        response_content = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response_content, {'details':'Emails sent successfully!'})

    #draft testing below for status code response

    # @patch('views.send_email')
    # def test_sent_email_status(self, mock_status_email):
    #     request = HttpRequest()
    #     request.method = 'POST'
    #     request.POST ={
    #         'message': 'hi, please find the meeting minutes below',
    #         'subject' : 'TestMeeting'
    #         'contacts': 'tarayesha508@gmail.com',
           
    #     }
        
    #     mock_response = STATUS CODE 200
    #     mock_status_email.return_value = mock_response

    #     response = send_email(request)

    #     self.assertEqual(response.json(), {'details':'Status code 200?'})

        
