from django.test import TestCase
from users.models import UserProfile


class TestModelUserProfile(TestCase):
    def setUp(self):
        UserProfile.objects.create_user(email='user@normal.com', username='normal-user',
                                        first_name='first name', password='password')

        UserProfile.objects.create_superuser(email='super@user.com', username='superuser',
                                             first_name='first name', password='password')

    def test_model_user_profile_to_create_user_should_return_value_error(self):
        """Returns ValueError if email is not provided"""
        with self.assertRaises(ValueError):
            UserProfile.objects.create_user(email=None, username='username',
                                            first_name='first name', password='password')

        """Returns ValueError if username provided"""
        with self.assertRaises(ValueError):
            UserProfile.objects.create_user(email='value@error.com', username=None,
                                            first_name='first name', password='password')

        """Returns ValueError if first name is not provided"""
        with self.assertRaises(ValueError):
            UserProfile.objects.create_user(email='value@error.com', username='username',
                                            first_name=None, password='password')

    def test_model_user_profile_to_create_user_should_return_true(self):
        self.assertTrue(UserProfile.objects.get(email='user@normal.com'))

    def test_model_user_profile_to_create_user_should_return_email_as_str(self):
        user = UserProfile.objects.get(email='user@normal.com')
        self.assertEqual(str(user), 'user@normal.com')

    def test_model_user_profile_to_create_superuser_should_return_value_error(self):
        """Checking if one of the other fields are False must return ValueError"""
        email = 'is@superuser.com'
        username = 'username'
        first_name = 'ssss'
        password = '12345'
        other_fields = {
            'is_staff': True,
            'is_superuser': True,
            'is_active': True
        }

        for i in other_fields:
            other_fields[i] = False
            with self.assertRaises(ValueError):
                UserProfile.objects.create_superuser(email, username, first_name, password, **other_fields)
            other_fields[i] = True

    def test_model_user_profile_to_create_superuser_should_return_true(self):
        self.assertTrue(UserProfile.objects.get(email='super@user.com'))
