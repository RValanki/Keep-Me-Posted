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
    def test_user_login(self, mock_get_object_or_404, mock_get_or_create):
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
    def test_user_signup(self, mock_create_user, mock_create_token):
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


 
    def test_signup_and_login(self):
        # Test user registration
        url = reverse('signup')
        data = {
            'username': 'signup',
            'email': 'signup@example.com',
            'password': 'signuppassword123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='signup').exists())

        # Test login with registered user
        url = reverse('login')
        data = {
            'email': 'signup@example.com',
            'password': 'signuppassword123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
    
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
