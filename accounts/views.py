from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    success_message = "Your account was created successfully."
    template_name = 'registration/sign_up.html'

    def dispatch(self, *args, **kwargs):
        return super(SignUpView, self).dispatch(*args, **kwargs)

