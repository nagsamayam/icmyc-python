from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('sign-up/', views.SignUpView.as_view(), name='signup'),
]