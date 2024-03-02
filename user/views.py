from django.shortcuts import render
from rest_framework import generics,permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from user.models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.authtoken.models import Token

from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated



# Create your views here.


class UserSignUpView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args,**kwargs):
        response = super().create(request,*args,**kwargs)

        user = self.serializer_class(data = request.data).initial_data
        user_instance = CustomUser.objects.get(username=response.data['username'])
    
        if user_instance.role == 'employer':
            # Additional actions for employers
            pass
        elif user_instance.role == 'employee':
            # Additional actions for employees
            pass

        refresh_token = RefreshToken.for_user(user_instance)
        access_token = str(refresh_token.access_token)

        return Response({'access': access_token}, status=status.HTTP_201_CREATED)
        


class UserLoginAPIView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]

    def post(self,request,*args,**kwargs):
        response = super().post(request,*args,**kwargs)
        return response
    

class GetUserInfoView(APIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get(self,request):
        response = request.user
        return Response({"username":response.username,'role':response.role,'is_superuser':response.is_superuser})




class UserLogoutAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        


