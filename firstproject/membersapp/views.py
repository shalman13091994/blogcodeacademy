from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class userregisterview(generic.CreateView):
    form_class=UserCreationForm
    template_name='registration/register.html'
    sucess_url=reverse_lazy('login.html')