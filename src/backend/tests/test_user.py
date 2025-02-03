""" Accounts tests """
from datetime import datetime as dt
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from uuid import UUID
from rest_framework.status import (HTTP_201_CREATED, HTTP_204_NO_CONTENT, 
                                   HTTP_403_FORBIDDEN, HTTP_400_BAD_REQUEST)
from rest_framework.test import APITestCase

user_model = get_user_model()


class RegistrationTestCase(APITestCase):

    user_data = {'username': 'user', 'password': 'test_password'}

        # Dev note: doe to some time constraints I will only be adding testing to the user.
        # Testing can be quite extensive and for an exercise, I feel like this is just a quick showcase 
        # rather than a proper test suite.
        # I wish I had more time to properly add a test suite, but I only really had a couple of hours on the weekend for this challenge.

    def test_registration(self):
        
        # Normal user case for registration

        url = reverse('registration')
        response = self.client.post(url, self.user_data, format='json')
        status = response.status_code
        data = response.data

        # Test response status
        self.assertEqual(status, HTTP_201_CREATED, 'Expected a 201 Http Response.')
        
        # Test that the response contains a user id
        user_id = data.get('id', None)
        self.assertTrue(user_id, 'Response should contain the id of the new registered user.')
        
        # Test that the user id is a UUID
        try: 
            UUID(user_id, version=4)
        except:
            self.fail('User id is not a UUID.')
        
        # Verifying DB
        # Dev note: Skipped tests due to time constraints: 
        # - I should verify here if the user was registered with the correct password.
        # - I should also verify here if the user can then login after registration.
        # - I also should verify if the user pk is a uuid4 like expected.
        number_users = user_model.objects.count()
        user = user_model.objects.first()
        self.assertEqual(number_users, 1, 'User not registered properly.')
        self.assertEqual(user.username, self.user_data.get('username'), 
                         'User username is incorrect after registration.')

    def test_soft_password(self):
        
        # Test if when a password is weak, an drf exception is raised.
        
        url = reverse('registration')
        response = self.client.post(url, self.user_data | {'password': '1234'}, format='json')
        status = response.status_code

        self.assertEqual(status, HTTP_403_FORBIDDEN, 'Expected a 403 Http Response.')
        # Dev note: Skipped tests due to time constraints: 
        # - Test for correct message in data 

    def test_duplicate_account(self):
        
        # Test for a user trying to register with an already registered username.

        url = reverse('registration')
        self.client.post(url, self.user_data, format='json')
        response = self.client.post(url, self.user_data, format='json')
        status = response.status_code

        self.assertEqual(status, HTTP_400_BAD_REQUEST, 'Expected a 400 Http Response.')
        # Dev note: Skipped tests due to time constraints: 
        # - Test for correct message in data  


class LoginTestCase(APITestCase):

    user_data = {'username': 'user', 'password': 'test_password'}
    
    def setUp(self):
        self.user = user_model.objects.create_user(**self.user_data)

    def test_login(self):

        # Test login (expected to work)

        first_login = self.user
        
        url = reverse('login')
        self.client.post(url, self.user_data, format='json')
        token_count = Token.objects.count()
        response = self.client.post(url, self.user_data, format='json')
        status = response.status_code
        data = response.data
        
        second_login = user_model.objects.first()

        self.assertEqual(status, HTTP_201_CREATED, 'Expected a 201 Http Response.')
        self.assertIn('token', data, 'Response should contain a token.')
        self.assertIn('id', data, 'Response should contain the user id.')
        self.assertEqual(token_count, 1, 'Expected a token to be created.')
        self.assertIsNone(first_login.last_login, 'Expected first `last_login` to be None.')
        self.assertTrue(isinstance(second_login.last_login, dt), 'Expected second `last_login` to be a non-None timestamp.')

    def test_for_incorrect_username(self):
        
        # Wrong username should product a 403 response.

        url = reverse('login')
        response = self.client.post(url, self.user_data | {'username': 'worng_username'}, format='json')
        status = response.status_code
        
        self.assertEqual(status, HTTP_403_FORBIDDEN, 'Expected a 403 Http Response.')
    

    def test_for_incorrect_password(self):
        
        # Wrong password should product a 403 response.

        url = reverse('login')
        response = self.client.post(url, self.user_data | {'password': 'wrong_pass'}, format='json')
        status = response.status_code
        
        self.assertEqual(status, HTTP_403_FORBIDDEN, 'Expected a 403 Http Response.')


class LogoutTestCase(APITestCase):
    
    user_data = {'username': 'user', 'password': 'test_password'}

    def setUp(self):
        self.user = user_model.objects.create_user(**self.user_data)
        self.token = self.user.token

    def test_authenticated_logs_out(self):
    
        url = reverse('logout')
        response = self.client.post(url, {}, format='json', HTTP_AUTHORIZATION=f'Bearer {self.token}')
        status = response.status_code
        data = response.data

        self.assertEqual(status, HTTP_204_NO_CONTENT, 'Expected a 204 Http Response.')
        self.assertEqual(data, {}, 'Response is supposed to be empty.')
        self.assertEqual(Token.objects.count(), 0, 'Expected token to be None')
