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
        data = response.data
    
        if data['role'] == 'employer':
            # Additional actions for employers
            pass
        elif data['role'] == 'employee':
            # Additional actions for employees
            pass

        return Response({"status":"Successfully created the user."}, status=status.HTTP_201_CREATED)
        


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
        


