from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.serializers import Serializer, CharField, EmailField
from rest_framework import serializers


# Create your views here.

class SignUpSerializer(Serializer):
    username = CharField(max_length = 100)
    email = EmailField()
    password = CharField(write_only = True)
    confirm_password = CharField(write_only = True)

    def validate(self,data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data
    
class SignUpView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username = serializer.validated_data['username'],
                email= serializer.validated_data['email'],
                password = serializer.validated_data['password'],
            )
            return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginSerializer(Serializer):
        username = CharField()
        password = CharField(write_only = True)

from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = User.objects.filter(username=username).first()
            if user and user.check_password(password):
                refresh = RefreshToken.for_user(user)
                # Include the username in the token payload
                refresh.payload['username'] = user.username
                return Response({"access_token": str(refresh.access_token)})
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
