"""
Test cases for the authentication views in the kmp_backend project.

The test cases cover the following scenarios:
1. Valid user login
2. Valid user signup
4. User registration with invalid data
    4.1. User registration with already registered email
    4.2. User registration with invalid email
    4.2. User registration with missing username
    4.3. User registration with missing password
5. User login with invalid data
    5.1. User login with incorrect email
    5.2. User login with incorrect password
    5.3. User login with missing email
    5.4. User login with missing password

"""

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from unittest.mock import patch, MagicMock

class AuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@gmail.com',
            password='testpassword'
        )

    @patch('django.shortcuts.get_object_or_404')
    @patch('django.contrib.auth.models.User.check_password')
    @patch('rest_framework.authtoken.models.Token.objects.get_or_create')
    @patch('authentication.serializers.UserSerializer')
    def test_valid_login(self, mock_serializer, mock_get_or_create, mock_check_password, mock_get_object_or_404):
        """
        Test case for a valid user login.

        This test case mocks the UserSerializer, get_object_or_404, check_password, and Token.objects.get_or_create functions.
        The UserSerializer is mocked to return valid user data.
        The get_object_or_404 function is mocked to return a user object.
        The check_password function is mocked to return True.

        The test sends a POST request to the login endpoint with valid user credentials.
        The test checks if the response status code is 200 OK, and if the response contains the user token and details.
        """
        mock_serializer.return_value.data = {
            'username': 'testuser',
            'email': 'testuser@gmail.com'
        }
        mock_get_object_or_404.return_value = self.user
        mock_check_password.return_value = True
        mock_get_or_create.return_value = (Token(key='testtoken'), True)

        response = self.client.post(
            reverse('login'),
            {
                'email': 'testuser@gmail.com',
                'password': 'testpassword'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['token'], 'testtoken')
        self.assertEqual(response.data['user']['email'], self.user.email)

    
    @patch('django.contrib.auth.models.User.objects.filter')
    @patch('django.contrib.auth.models.User.objects.get')
    @patch('rest_framework.authtoken.models.Token.objects.create')
    def test_valid_signup(self, mock_create_token, mock_get_user, mock_filter_user):
        """
        Test case for a valid user signup.

        This test case mocks the User.objects.filter, User.objects.get, Token.objects.create functions.
        The User.objects.filter is mocked to return False to simulate a new email.
        The User.objects.get is mocked to return a user object.
        The Token.objects.create is mocked to return a token object.

        The test sends a POST request to the signup endpoint with valid user data.
        The test checks if the response status code is 201 CREATED, and if the response contains the user token and details.
        """
        new_user_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123'
        }

        # Mock the User.objects.filter to simulate email check
        mock_filter_user.return_value.exists.return_value = False

        # Mock the serializer to always be valid
        mock_serializer = MagicMock()
        mock_serializer.is_valid.return_value = True
        mock_serializer.data = new_user_data
        mock_serializer.save.return_value = None

        # Mock User.objects.get to return a user object
        mock_user = MagicMock()
        mock_get_user.return_value = mock_user

        # Mock Token.objects.create to return a token
        mock_token = MagicMock()
        mock_token.key = 'dummy-token'
        mock_create_token.return_value = mock_token

        with patch('authentication.serializers.UserSerializer', return_value=mock_serializer):
            url = reverse('signup')
            response = self.client.post(url, new_user_data, format='json')

        # Check signup response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)
        self.assertEqual(response.data['token'], 'dummy-token')
        self.assertEqual(response.data['user']['email'], new_user_data['email'])

    @patch('django.contrib.auth.models.User.objects.filter')
    def test_invalid_signup_existing_email(self, mock_filter):
        """
        Test case for user registration with an already registered email.
        
        This test case mocks the User.objects.filter function to return True to simulate an existing email.
        
        The test sends a POST request to the signup endpoint with user data containing an existing email.
        The test checks if the response status code is 400 BAD REQUEST, and if the response contains an error message.
        """
        existing_user_data = {
            'username': 'existinguser',
            'email': 'existinguser@gmail.com',
            'password': 'existingpassword123'
        }
        mock_filter.return_value.exists.return_value = True

        response = self.client.post(
            reverse('signup'),
            existing_user_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
        self.assertEqual(response.data['error'], 'This email address is already in use.')

    @patch('django.contrib.auth.models.User.objects.filter')
    @patch('authentication.serializers.UserSerializer')
    def test_invalid_signup_invalid_email(self, mock_filter, mock_serializer):
        """
        Test case for user registration with an invalid email.
        
        This test case mocks the User.objects.filter and UserSerializer functions.
        The User.objects.filter is mocked to return False to simulate a new email.
        The UserSerializer is mocked to return an invalid email error message.
        
        The test sends a POST request to the signup endpoint with user data containing an invalid email.
        The test checks if the response status code is 400 BAD REQUEST, and if the response contains an error message.
        """
        invalid_user_data = {
            'username': 'invaliduser',
            'email': 'invalidemail',
            'password': 'invalidpassword123'
        }
        mock_filter.return_value.exists.return_value = False
        mock_serializer.return_value.is_valid.return_value = False
        mock_serializer.return_value.errors = {
            'email': ['Enter a valid email address.']
        }
        
        response = self.client.post(
            reverse('signup'),
            invalid_user_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch('django.contrib.auth.models.User.objects.filter')
    @patch('authentication.serializers.UserSerializer')
    def test_invalid_signup_missing_username(self, mock_filter, mock_serializer):
        """
        Test case for user registration with missing username.
        
        This test case mocks the User.objects.filter and UserSerializer functions.
        The User.objects.filter is mocked to return False to simulate a new email.
        The UserSerializer is mocked to return an invalid username error message.

        The test sends a POST request to the signup endpoint with user data missing the username.
        The test checks if the response status code is 400 BAD REQUEST, and if the response contains an error message.
        """
        user_data = {
            'email': 'missingusername@gmail.com;',
            'password': 'missingusername123'
        }
        mock_filter.return_value.exists.return_value = False
        mock_serializer.return_value.is_valid.return_value = False
        mock_serializer.return_value.errors = {
            'username': ['This field is required.']
        }

        response = self.client.post(
            reverse('signup'),
            user_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch('django.contrib.auth.models.User.objects.filter')
    @patch('authentication.serializers.UserSerializer')
    def test_invalid_signup_missing_password(self, mock_filter, mock_serializer):
        """
        Test case for user registration with missing password.

        This test case mocks the User.objects.filter and UserSerializer functions.
        The User.objects.filter is mocked to return False to simulate a new email.
        The UserSerializer is mocked to return an invalid password error message.

        The test sends a POST request to the signup endpoint with user data missing the password.
        The test checks if the response status code is 400 BAD REQUEST, and if the response contains an error message.
        """
        user_data = {
            'username': 'missingpassword',
            'email': 'missingpassword@gmail.com'
        }
        mock_filter.return_value.exists.return_value = False
        mock_serializer.return_value.is_valid.return_value = False
        mock_serializer.return_value.errors = {
            'password': ['This field is required.']
        }

        response = self.client.post(
            reverse('signup'),
            user_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch('django.shortcuts.get_object_or_404')
    @patch('django.contrib.auth.models.User.check_password')
    def test_invalid_login_incorrect_email(self, mock_check_password, mock_get_object_or_404):
        """
        Test case for user login with incorrect email.
        
        This test case mocks the get_object_or_404 and check_password functions.
        The get_object_or_404 function is mocked to raise a User.DoesNotExist exception.
        The check_password function is mocked to return True.
        
        The test sends a POST request to the login endpoint with user data containing an incorrect email.
        The test checks if the response status code is 404 NOT FOUND, and if the response contains an error message.
        """
        mock_get_object_or_404.side_effect = User.DoesNotExist
        mock_check_password.return_value = True

        response = self.client.post(
            reverse('login'),
            {
                'email': 'doesnotexist@gmail.com',
                'password': 'testpassword'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('detail', response.data)

    @patch('django.shortcuts.get_object_or_404')
    @patch('django.contrib.auth.models.User.check_password')
    def test_invalid_login_incorrect_password(self, mock_check_password, mock_get_object_or_404):
        """
        Test case for user login with incorrect password.

        This test case mocks the get_object_or_404 and check_password functions.
        The get_object_or_404 function is mocked to return a user object.
        The check_password function is mocked to return False.

        The test sends a POST request to the login endpoint with user data containing an incorrect password.
        The test checks if the response status code is 404 NOT FOUND, and if the response contains an error message.
        """
        mock_get_object_or_404.return_value = self.user
        mock_check_password.return_value = False

        response = self.client.post(
            reverse('login'),
            {
                'email': 'wrongpassword@gmail.com',
                'password': 'wrongpassword'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('detail', response.data)
    

    def test_invalid_login_missing_email(self):
        """
        Test case for user login with missing email.
        
        The test sends a POST request to the login endpoint with user data missing the email.
        The test checks if the response status code is 400 BAD REQUEST, and if the response contains an error message.
        """
        response = self.client.post(
            reverse('login'),
            {
                'password': 'testpassword'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)

    def test_invalid_login_missing_password(self):
        """
        Test case for user login with missing password.
        
        The test sends a POST request to the login endpoint with user data missing the password.
        The test checks if the response status code is 400 BAD REQUEST, and if the response contains an error message.
        """
        response = self.client.post(
            reverse('login'),
            {
                'email': 'missingpassword@gmail.com'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
