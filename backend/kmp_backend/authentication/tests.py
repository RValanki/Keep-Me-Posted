"""
Test cases for the authentication views in the kmp_backend project.

The test cases cover the following scenarios:
1. Valid user login
2. Valid user signup
3. Valid user registration followed by login
4. User registration with invalid data
    4.1. User registration with invalid email
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
from unittest.mock import patch
class AuthTests(TestCase):
    def setUp(self):
        """
        This function is responsible for setting up the test client and creating a user
        """
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123'
        }
        self.user = User.objects.create_user(**self.user_data)
        self.user.set_password(self.user_data['password'])
        self.user.save()
        self.token = Token.objects.create(user=self.user)

    @patch('rest_framework.authtoken.models.Token.objects.get_or_create')
    @patch('django.shortcuts.get_object_or_404')
    def test_valid_user_login(self, mock_get_object_or_404, mock_get_or_create):
        """
        This function is responsible for testing the login endpoint
        The function mocks the get_object_or_404 and Token creation to return the user and token
        The function then sends a POST request to the login endpoint with the user data and
        checks if the response status code is 200 and the token is returned

        :param mock_get_object_or_404: Mock of the get_object_or_404 function
        :param mock_get_or_create: Mock of the Token creation

        """
        # Mock the get_object_or_404 to return our user
        mock_get_object_or_404.return_value = self.user

        # Mock the Token creation
        mock_get_or_create.return_value = (self.token, True)

        url = reverse('login')
        data = {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        self.assertEqual(response.data['token'], self.token.key)
        self.assertEqual(response.data['user']['username'], self.user_data['username'])

    @patch('rest_framework.authtoken.models.Token.objects.create')
    @patch('django.contrib.auth.models.User.objects.create_user')
    def test_valid_user_signup(self, mock_create_user, mock_create_token):
        """
        This function is responsible for testing the signup endpoint
        The function mocks the User and Token creation to return the user and token

        The function then sends a POST request to the signup endpoint with the user data and
        checks if the response status code is 201 and the token is returned

        :param mock_create_user: Mock of the User creation
        :param mock_create_token: Mock of the Token creation

        """
        new_user_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123'
        }

        mock_user = User(**new_user_data)
        mock_create_user.return_value = mock_user
        mock_token = Token(key='dummy-token', user=mock_user)
        mock_create_token.return_value = mock_token

        url = reverse('signup')
        response = self.client.post(url, new_user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)
        self.assertEqual(response.data['token'], mock_token.key)
        self.assertEqual(response.data['user']['username'], new_user_data['username'])


    @patch('rest_framework.authtoken.models.Token.objects.create')
    @patch('django.contrib.auth.models.User.objects.create_user')
    @patch('rest_framework.authtoken.models.Token.objects.get_or_create')
    @patch('django.shortcuts.get_object_or_404')
    def test_signup_and_login(self, mock_get_object_or_404, mock_get_or_create, mock_create_user, mock_create_token):
        """
        This function is responsible for testing the signup and login endpoints

        The function mocks the User and Token creation to return the user and token
        The function then sends a POST request to the signup endpoint with the user data and
        checks if the response status code is 201 and the token is returned
        
        The function then sends a POST request to the login endpoint with the user data and
        checks if the response status code is 200 and the token is returned
        
        This test case is used to test the flow of user registration followed by login
        
        :param mock_get_object_or_404: Mock of the get_object_or_404 function
        :param mock_get_or_create: Mock of the Token creation
        :param mock_create_user: Mock of the User creation
        :param mock_create_token: Mock of the Token creation
        
        """
        new_user_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123'
        }

        # Mock user creation
        mock_user = User(**new_user_data)
        mock_user.set_password(new_user_data['password'])
        mock_create_user.return_value = mock_user

        # Mock token creation
        mock_token = Token(key='dummy-token', user=mock_user)
        mock_create_token.return_value = mock_token

        # Test user registration (signup)
        url = reverse('signup')
        response = self.client.post(url, new_user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)
        self.assertEqual(response.data['token'], mock_token.key)
        self.assertEqual(response.data['user']['username'], new_user_data['username'])

        # Mock get_object_or_404 to return the mock user for login
        mock_get_object_or_404.return_value = mock_user

        # Mock get_or_create for the token to return the mock token
        mock_get_or_create.return_value = (mock_token, True)

        # Test user login
        url = reverse('login')
        login_data = {
            'email': new_user_data['email'],
            'password': new_user_data['password']
        }
        response = self.client.post(url, login_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        self.assertEqual(response.data['token'], mock_token.key)
        self.assertEqual(response.data['user']['username'], new_user_data['username'])

    
    def test_invalid_user_registration(self):
        url = reverse('signup')

        # Test login with invalid emailing format
        data = {
            'username': 'invaliduser',
            'email': 'invalidemail',
            'password': 'invalidpassword123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

        #Test for missing username 
        data = {
            'email': 'invalid@example.com',
            'password': 'invalidpassword123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)

        #Test for missing password 
        data = {
            'username': 'invaliduser2',
            'email': 'invalid2@example.com',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)


    def test_invalid_user_login(self):
        url = reverse('login')
        
        # Test for Incorrect email
        data = {
            'email': 'incorrectemail@example.com',
            'password': 'password123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.data)

        # Test for Incorrect password
        data = {
            'email': 'testuser@gmail.com',
            'password': 'incorrectpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.data)

        # Test for Missing email
        data = {
            'password': 'password123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

        # Test for Missing password
        data = {
            'email': 'testuser@gmail.com'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)
