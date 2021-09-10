from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from users.models import UserProfile
from rest_framework.test import APITestCase, APIClient

from users.serializer import CreateUserProfileSerializer
from users.views import CreateUserProfileApiView


class TestCreateUser(TestCase):

    def setUp(self):
        email = 'b@a.com'
        username = 'username'
        first_name = 'ssss'
        password = '12345'
        other_fields = {
            'is_staff': True,
            'is_superuser': True,
            'is_active': True
        }

        UserProfile.objects.create_superuser(email, username, first_name, password, **other_fields)

    def test_create_user_with_no_email_should_raise_value_error(self):
        user = UserProfile.objects
        email = None
        username = 'username'
        first_name = 'name'
        password = '12345'
        with self.assertRaises(ValueError):
            user.create_user(email, username, first_name, password)

    def test_create_user_with_no_username_should_raise_value_error(self):
        user = UserProfile.objects
        email = 'b@b.com'
        username = None
        first_name = 'name'
        password = '12345'
        with self.assertRaises(ValueError):
            user.create_user(email, username, first_name, password)

    def test_create_user_with_no_first_name_should_value_raise_error(self):
        user = UserProfile.objects
        email = 'b@b.com'
        username = 'username'
        first_name = None
        password = '12345'
        with self.assertRaises(ValueError):
            user.create_user(email, username, first_name, password)

    def test_normalize_the_email_should_return_true(self):
        email = 'b@A.com'
        user = UserProfile.objects.get(email='b@a.com')
        self.assertEqual(user.email, email.lower())

    def test_creating_super_user_testing_other_fields_should_return_True(self):
        user = UserProfile.objects.get(email='b@a.com')
        self.assertEqual(user.is_staff, True)
        self.assertEqual(user.is_superuser, True)
        self.assertEqual(user.is_active, True)

    def test_create_super_user_if_one_of_other_field_is_not_true_should_raise_value_error(self):
        email = 'b@a.com'
        username = 'username'
        first_name = 'ssss'
        password = '12345'
        other_fields = {
            'is_staff': True,
            'is_superuser': True,
            'is_active': True
        }

        user = UserProfile.objects
        for i in other_fields:
            other_fields[i] = False
            print(other_fields)
            with self.assertRaises(ValueError):
                user.create_superuser(email, username, first_name, password, **other_fields)
            other_fields[i] = True

    def test_model_user_profile_to_return_str_email_should_return_true(self):
        user = UserProfile.objects.get(email='b@a.com')

        self.assertEqual(str(user), 'b@a.com')


class PostTest(APITestCase):

    def test_create_user_profile__api_view_should_return_created(self):
        data = {
            'email': 'b@a.com',
            'username': 'username',
            'first_name': 'ssss',
            'password': '12345'
        }
        url = reverse('user-create')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_profile_api_view_should_return_bad_request(self):
        data = {
            'email': None,
            'username': 'username',
            'first_name': 'ssss',
            'password': '12345'
        }
        url = reverse('user-create')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)