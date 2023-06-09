from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from api.v1.employees.forms import EmployeeForm


class UserAPIView(APIView):
    @staticmethod
    def post(request: Request):
        form = EmployeeForm(request.POST)

        if not form.is_valid():
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        user = User.objects.filter(username=username)

        if len(user):
            return Response({'message': f'{ username } already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username, email, password)
        user.save()
        return Response({"username": username}, status=status.HTTP_201_CREATED)
