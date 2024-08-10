from django.test import TestCase
from django.http import HttpRequest, JsonResponse
from unittest.mock import patch, MagicMock
from emailing.views import send_email
import json, ssl

# Create your tests here.
class TestEmailSent(TestCase):

    @patch('emailing.views.send_email')
    def test_sending_email(self, mock_send_smtp_email):
        """
        This function is responsible for testing if an email is sent successfully by determining the json response
        received from the request. 
        The function utilises mocking concept to test this functionality. @Patch is used to create a mock object
        for the function send_email to be tested
        """
        request = HttpRequest()
        request.method = 'POST'
        #creating mock request
        request.POST = {
            'message': 'Here are the meeting minutes',
            'subject': 'TeamMeeting-20/07/2024',
            'contacts': 'tarayesha508@gmail.com'
        }
        #setting the mock_response to what is expected
        mock_response = JsonResponse({'details':'Emails sent successfully!'})
       
        mock_send_smtp_email.return_value = mock_response

        response = send_email(request)
        #extracting the response received from the function
        response_content = json.loads(response.content.decode('utf-8'))
        
        self.assertEqual(response_content, {'details':'Emails sent successfully!'})


    @patch('emailing.views.send_email')
    def test_sent_email_status_code(self, mock_status_email):
        """
        This test case function determines the status code of the 
        request

        Status code 200 confirms that the email has been sent successfully
        """
        request = HttpRequest()
        request.method = 'POST'
        request.POST ={
            'message': 'hi, please find the meeting minutes below',
            'subject' : 'TestMeeting',
            'contacts': 'tarayesha508@gmail.com',
        }
        
        #setting mock status code value
        mock_response = {'status_code': 200}

        mock_status_email.return_value = mock_response

        response = send_email(request)
        #determine if the status code is as expected
        self.assertEqual(response.status_code, 200)


    @patch('emailing.views.ssl.create_default_context')
    @patch('emailing.views.smtplib.SMTP_SSL')
    def test_ssl_secure_email(self, mock_create_default_context, mock_smtp_ssl):

        mock_context = MagicMock()
        mock_create_default_context.return_value = mock_context
        mock_server = MagicMock()
        mock_smtp_ssl.return_value = mock_server

        #mock request created
        request = HttpRequest()
        request.method = 'POST'
        request.POST['message'] = "Testing message"
        request.POST['subject'] = "Testing Subject"
        request.POST['contacts'] = "at@test.com"

        # calling the send_email function to generate response
        response = send_email(request)
        response_content = json.loads(response.content.decode('utf-8'))

        # determining whether the default_context is called at least once
        mock_create_default_context.assert_called_once()

    @patch('emailing.views.smtplib.SMTP_SSL')
    @patch('emailing.views.ssl.create_default_context')
    def test_server_login(self, mock_create_default_context,mock_smtp):
        mock_context = MagicMock()
        mock_create_default_context.return_value = mock_context
        # Mock server.login to verify it is called
        mock_server = MagicMock()
        mock_smtp.return_value = mock_server

        mock_server.__enter__.return_value = mock_server
        mock_server.__exit__.return_value = False

        request = HttpRequest()
        request.method = 'POST'
        request.POST['message'] = "Testing message"
        request.POST['subject'] = "Testing Subject"
        request.POST['contacts'] = "at@test.com"

        
        response = send_email(request)

        # test verify that server login is called with correct credentials
        mock_server.login.assert_called_with('keepmeposted.monash@gmail.com', 'aqsokzlapmzxvuev')

        response_content = json.loads(response.content.decode('utf-8'))

        # confirm and verify response

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content, {'details': 'Emails sent successfully!'})

    
    def test_exception_raised_when_contacts_empty(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST ={
            'message': 'Here you will find a remarkable set of notes.',
            'subject' : 'Meeting Notes'
        }
        with self.assertRaises(ValueError) as context:
            send_email(request)
        self.assertEqual(str(context.exception), "Contacts list is empty.")
        
