from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class AuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser',email='testuser@gmail.com', password='password123')
        self.user.save()

    def test_user_registration(self):
        url = reverse('signup')
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_login(self):
        url = reverse('login')
        data = {
            'email': 'testuser@gmail.com',
            'password': 'password123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
 
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
