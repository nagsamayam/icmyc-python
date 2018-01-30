from django.urls import path
from . import views

urlpatterns = [
    path('contact-us/', views.emailView, name="contact-us"),
    path('success/', views.successView, name="success"),
    path('send-test-mail/', views.sendTestMail, name="send-test-mail")
]