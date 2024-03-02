from django.urls import path
from .views import UserLoginAPIView,UserLogoutAPIView,UserSignUpView,GetUserInfoView

urlpatterns = [
    path('signup/',UserSignUpView.as_view(),name = 'user_signup'),
    path('login/',UserLoginAPIView.as_view(),name = 'user_login'),
    path('logout/',UserLogoutAPIView.as_view(),name='user_logout'),
    path('userinfo/',GetUserInfoView.as_view(),name='user_info'),
]