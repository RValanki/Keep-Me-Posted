from django.test import TestCase
from django.http import HttpRequest, JsonResponse
from django.urls import reverse
from unittest.mock import patch, MagicMock
from emailing.views import send_email
import json, ssl, smtplib
import os

# Create your tests here.
class TestEmailSent(TestCase):

    @patch('emailing.views.smtplib.SMTP_SSL')
    def test_sending_email(self, MockSMTP_SSL):
        """
        Test if the view correctly handles send_email and returns the expected response.
        """
        # Create a mock instance of SMTP_SSL
        mock_smtp_instance = MagicMock()
        MockSMTP_SSL.return_value = mock_smtp_instance

        # Configure the mock instance to avoid actual email sending
        mock_smtp_instance.login.return_value = None
        mock_smtp_instance.sendmail.return_value = None

        # Make the POST request
        response = self.client.post(
            reverse('send_email'),
            {
                'message': 'hi, please find the meeting minutes below',
                'subject': 'TestMeeting',
                'contacts': 'test@example.com'
            },
            fromat='json'
        )

        # Check the response
        response_content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response_content, {'details': 'Emails sent successfully!'})
        self.assertEqual(response.status_code, 200)


    @patch('emailing.views.ssl.create_default_context')
    @patch('emailing.views.smtplib.SMTP_SSL')
    def test_ssl_secure_email(self, mock_create_default_context, mock_smtp_ssl):
        """
        test_ssl_secure_email function determines if the default_context is atleast called once to determine
        if a secure connection is created
        """
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
    @patch.dict(os.environ, {"SMTP_EMAIL": "test@example.com", "SMTP_API_KEY": "fakeapikey"})
    def test_server_login(self, mock_create_default_context,mock_smtp):
        """
        test server login function determines if the the login method is called with the correct
        credentials
        """
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
        mock_server.login.assert_called_with('test@example.com', 'fakeapikey')

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
    
    @patch('emailing.views.smtplib.SMTP_SSL')
    @patch('emailing.views.ssl.create_default_context')
    def test_login_SMTP_Helo_Error_Exception(self, mock_create_default_context, mock_smtp_ssl):
        """
        test_login_SMTP_Helo_Error test raises an exception for when the Helo command is not supported
        """
        #SMTP Helo Error
        mock_context = MagicMock()
        mock_create_default_context.return_value = mock_context

        # mocking the SMTP Helo command and the server
        mock_server = MagicMock()
        mock_server.login.side_effect = smtplib.SMTPHeloError(500, 'Helo command failed')
        mock_smtp_ssl.return_value = mock_server
        
        mock_server.__enter__.return_value = mock_server
        mock_server.__exit__.return_value = False

        request = HttpRequest()
        request.method = 'POST'
        request.POST['message'] = "Testing message"
        request.POST['subject'] = "Testing Subject"
        request.POST['contacts'] = "at@test.com"

        response = send_email(request)

        #determining if the HELO command is asserted as expected
        self.assertEqual(response.status_code, 500)
        response_content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response_content['error'], "HELO error occurred: (500, 'Helo command failed')")


    @patch('emailing.views.smtplib.SMTP_SSL')
    @patch('emailing.views.ssl.create_default_context')
    def test_login_SMTP_Authentication(self, mock_create_default_context, mock_smtp_ssl):
        """
        test_login_SMTP_Authentication test is used to determine if appropriate exception is raised
        when the authentication fails
        """
        #SMTP authentication Error
        mock_context = MagicMock()
        mock_create_default_context.return_value = mock_context

        # mocking the SMTP authentication command and the server
        mock_server = MagicMock()
        mock_server.login.side_effect = smtplib.SMTPAuthenticationError(535, 'Authentication failed')

        mock_smtp_ssl.return_value = mock_server
        
        mock_server.__enter__.return_value = mock_server
        mock_server.__exit__.return_value = False

        request = HttpRequest()
        request.method = 'POST'
        request.POST['message'] = "Testing message"
        request.POST['subject'] = "Testing Subject"
        request.POST['contacts'] = "at@test.com"

        response = send_email(request)

        #determining if the smtp authentication command is asserted as expected
        self.assertEqual(response.status_code, 535)
        response_content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response_content['error'], "Authentication failed.")


    @patch('emailing.views.smtplib.SMTP_SSL')
    @patch('emailing.views.ssl.create_default_context')
    def test_login_SMTP_not_supported(self, mock_create_default_context, mock_smtp_ssl):
        """
        test_login_SMTP_not_supported is used to determine if exception is raised if 
        a particular login command is not supported
        """
        #SMTP not supported Error

        mock_context = MagicMock()
        mock_create_default_context.return_value = mock_context

        # mocking the SMTPNot supported command and the server
        mock_server = MagicMock()
        mock_server.login.side_effect = smtplib.SMTPNotSupportedError(502, 'SMTP Command not supported')

        mock_smtp_ssl.return_value = mock_server
        
        mock_server.__enter__.return_value = mock_server
        mock_server.__exit__.return_value = False

        request = HttpRequest()
        request.method = 'POST'
        request.POST['message'] = "Testing message"
        request.POST['subject'] = "Testing Subject"
        request.POST['contacts'] = "at@test.com"

        response = send_email(request)

        #determining if the smtp command not supported command is asserted as expected
        self.assertEqual(response.status_code, 502)
        response_content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response_content['error'], "SMTP command not supported.")

    @patch('emailing.views.smtplib.SMTP_SSL')
    @patch('emailing.views.ssl.create_default_context')
    def test_login_SMTP_exception(self, mock_create_default_context, mock_smtp_ssl):
        """
        test_login_SMTP_exception is raised to determine if exception is raised if there is no 
        authenthication method found
        """
        #SMTP exception Error

        mock_context = MagicMock()
        mock_create_default_context.return_value = mock_context

        # mocking the SMTP Exception command and the server
        mock_server = MagicMock()
        mock_server.login.side_effect = smtplib.SMTPException(401, 'No suitable authentication method found.')

        mock_smtp_ssl.return_value = mock_server
        
        mock_server.__enter__.return_value = mock_server
        mock_server.__exit__.return_value = False

        request = HttpRequest()
        request.method = 'POST'
        request.POST['message'] = "Testing message"
        request.POST['subject'] = "Testing Subject"
        request.POST['contacts'] = "at@test.com"

        response = send_email(request)

        #determining if the smtp command for exception is asserted as expected
        self.assertEqual(response.status_code, 401)
        response_content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(response_content['error'], "No suitable authentication method found.")
        

        
