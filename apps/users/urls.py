from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserList.as_view(), name='user_list'),
    path('signup/', views.UserSignUp.as_view(), name='user_sign_up'),
    path('signin/', views.UserSignIn.as_view(), name='user_sign_in'),
    path('check-login/', views.UserCheckLogin.as_view(), name='user_check-login')
]
