from django.test import TestCase
from django.urls import reverse, resolve


class UserViewTest(TestCase):

    def test_user_create_view_should_return_405_response_for_get(self):
        url = reverse('user-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 405)

    def test_user_create_view_should_return_201_response_for_post(self):
        data = {
            'email': 'b@a.com',
            'username': 'username',
            'first_name': 'ssss',
            'password': '12345'
        }
        url = reverse('user-create')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_user_create_view_should_return_400_response_for_post(self):
        data = {
            'email': '',
            'username': 'username',
            'first_name': 'ssss',
            'password': '12345'
        }
        url = reverse('user-create')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 400)
