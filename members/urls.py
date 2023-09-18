from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('signup/', UserRegisterView.as_view(), name='register'),
    path('edit_user/', UserEditView.as_view(), name='EditProfile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html'), name="Password"),
    path('password_success/', views.password_success, name='PasswordSuccess'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='ShowProfilePage'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='EditProfilePage'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='CreateProfilePage'),
]
