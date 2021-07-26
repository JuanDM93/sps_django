from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.api import serializers as user_serial


class RegisterView(APIView):
    def post(self, request):
        serial = user_serial.RegisterSerializer(data=request.data)

        if serial.is_valid(raise_exception=True):
            serial.save()
            return Response(serial.data)

        return Response(status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serial = user_serial.UserSerializer(request.data)        
        return Response(serial.data)

    def put(self, request):
        user = User.objects.get(id=request.user.id)
        serial = user_serial.UserUpdateSerializer(user, request.data)
        if serial.is_valid(raise_exception=True):
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        

