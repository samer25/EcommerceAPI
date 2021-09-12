from django.urls import reverse
from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.test import APIRequestFactory

from users.models import UserProfile
from users.serializer import CreateUserProfileSerializer


class SerializerModelTest(APITestCase):

    def test_create_user_profile_serializer_should_return_equal(self):
        data = {
            'email': 'b@aa.com',
            'username': 'username',
            'first_name': 'asss',
            'password': '12345'
        }
        model_serializer = CreateUserProfileSerializer()
        serializer = model_serializer.create(data)
        self.assertEqual(serializer.email, data['email'])
