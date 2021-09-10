from django.urls import path, include

from users.views import CreateUserProfileApiView

urlpatterns = [
    path('create/', CreateUserProfileApiView.as_view(), name='user-create'),
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
]
