from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import views, status

# Create your views here.
from users.serializer import CreateUserProfileSerializer


class CreateUserProfileApiView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        request_serializer = CreateUserProfileSerializer(data=request.data)
        if request_serializer.is_valid():
            new_user = request_serializer.save()
            if new_user:
                return Response(status=status.HTTP_201_CREATED)

        return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
