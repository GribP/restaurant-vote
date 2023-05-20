from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate, login

from utils import auth_login_validator


class AuthAPIView(APIView):
    @staticmethod
    def get(request: Request):
        if not request.user.is_authenticated:
            return Response({'message': 'Please login'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'username': request.user.username})

    @staticmethod
    def post(request: Request):
        errors = auth_login_validator(request.data)

        if len(errors.keys()):
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            return Response({'message': 'Failed to login'}, status=status.HTTP_401_UNAUTHORIZED)
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
