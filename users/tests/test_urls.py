from django.urls import resolve, reverse
from django.test import TestCase
from users.views import CreateUserProfileApiView


class CrateUrlApiViewTest(TestCase):

    def test_url_create_user_post_class_view_should_be_equal(self):
        found = reverse('user-create')
        self.assertEqual(resolve(found).func.view_class, CreateUserProfileApiView)

